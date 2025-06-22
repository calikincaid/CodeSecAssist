# Receive User Input Source Code 
import argparse
import json
import os
from google import genai

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help = "Source-code file for vulnerability search")
    args = parser.parse_args()
    return args.filename

def get_user_source_code(filename):
    with open(filename) as file:
        source_code = file.read()
    return source_code

def get_prompt_template():
    with open("prompt_template.json") as file:
        template = json.load(file)
    return template["detect_owasp_vulns"]

def build_prompt(prompt_template, source_code):
    prompt_template["source code"] = source_code
    template = json.dumps(prompt_template, indent=4)
    prompt = f"{template}"
    return prompt

def call_LLM(prompt):
    client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content( model = "gemini-2.0-flash", contents = prompt)
    return response.text

def clean_response(response):
    response_lines = response.splitlines()
    response_lines = response_lines[1:-1]
    json_only_response = "\n".join(response_lines)
    cleaned_response = json.loads(json_only_response) 
    return cleaned_response

def print_output(clean_response):
    if clean_response == {}:
        print("The assistant found no vulnerabilies!")
    
    else:
        i = 1
        for vulnerability_detected in clean_response:
            print("----------------------------------------------------------------------------")
            print(f"Vulnerability {i}: {vulnerability_detected['vulnerability']}\n")
            print(f"OWASP Top 10 Category: {vulnerability_detected['owasp_category']}\n")
            print(f"Location: {vulnerability_detected['location']}\n")
            print(f"Description: {vulnerability_detected['description']}\n")
            print(f"Exploit: {vulnerability_detected['exploit']}\n")
            print(f"Remediation: {vulnerability_detected['remediation']}\n")
            print(f"References for Self-Study: {vulnerability_detected['references']}\n")
            print("----------------------------------------------------------------------------")
            i += 1

def main():
    filename = argparser()
    source_code = get_user_source_code(filename)
    prompt_template = get_prompt_template()
    prompt = build_prompt(prompt_template, source_code)
    response = call_LLM(prompt)
    cleaned_response = clean_response(response)
    print_output(cleaned_response)


  

if __name__ == "__main__":
    main()
