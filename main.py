# Receive User Input Source Code 
import argparse
import json
import os
from google import genai


class PromptCrafter:
    def __init__(self, source_path):
        self.path = source_path
        self.template = "prompt_template.json"
        self.source_code = None
        self.prompt = None

    def get_prompt_template(self):
        with open(self.template) as file:
            self.prompt = json.load(file)["detect_owasp_vulns"]

    def set_user_source_code(self):
        with open(self.path) as file:
            self.source_code = file.read() 

    def build_prompt(self):
        self.prompt["source code"] = self.source_code
        self.prompt = json.dumps(self.prompt, indent=4)

    def craft(self):
        self.get_prompt_template()
        self.set_user_source_code()
        self.build_prompt()
        return self.prompt

class QueryLLM:
    def __init__(self, prompt):
        self.prompt = prompt
        self.response = None
        self.cleaned_response = None
        self.response_fields = []

    def call_LLM(self):
        client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))
        reply = client.models.generate_content( model = "gemini-2.0-flash", contents = self.prompt)
        self.response = reply.text

    def clean_response(self):
        response_lines = self.response.splitlines()
        response_lines = response_lines[1:-1]
        json_only_response = "\n".join(response_lines)
        self.cleaned_response = json.loads(json_only_response) 
    
    def print_output(self):
        if self.cleaned_response == {}:
            print("The assistant found no vulnerabilies.")
        
        else:
            i = 1
            for vulnerability_detected in self.cleaned_response:
                print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                print(f"Vulnerability {i}: {vulnerability_detected['vulnerability']}\n")
                print(f"OWASP Top 10 Category: {vulnerability_detected['owasp_category']}\n")
                print(f"Location: {vulnerability_detected['location']}\n")
                print(f"Description: {vulnerability_detected['description']}\n")
                print(f"Exploit: {vulnerability_detected['exploit']}\n")
                print(f"Remediation: {vulnerability_detected['remediation']}\n")
                print(f"References for Self-Study: {vulnerability_detected['references']}\n")
                print("──────────────────────────────────────────────────────────────────────────────────────────────────────────────")
                i += 1

    def query(self):
        self.call_LLM()
        self.clean_response()
        self.print_output()

class CodeSecAssistant:
    def __init__(self):
        self.intro = '''
┏┓   ┓  ┏┓     ┏┓  •       
┃ ┏┓┏┫┏┓┗┓┏┓┏  ┣┫┏┏┓┏╋┏┓┏┓╋
┗┛┗┛┗┻┗ ┗┛┗ ┗  ┛┗┛┛┗┛┗┗┻┛┗┗

*** Note: This LLM vulnerability scanner should only be used for educational purposes ***
*** There may be instances of false-negatives, false-positives, or under developed true-positives ***
'''
    def run_CLI(self):
        # ARG PARSER TAKES COMMAND LINE ARGUMENT FOR SOURCECODE FILENAME
        parser = argparse.ArgumentParser()
        parser.add_argument("filename", help = "Source-code file for vulnerability search")
        args = parser.parse_args()

        print(self.intro)

        # PROMPT CRAFTER CREATES THE PROMPT FROM SOURCE CODE + TEMPLATE AND JSONIFIES IT
        crafter = PromptCrafter(args.filename)
        prompt = crafter.craft()
        querier = QueryLLM(prompt)
        querier.query()

################ Main ################
def main():
    app = CodeSecAssistant()
    app.run_CLI()

  

if __name__ == "__main__":
    main()
