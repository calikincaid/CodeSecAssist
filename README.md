# CS3300 Intro To SWE Semester Project
<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203.9%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Licence-MIT-green?style=for-the-badge"/>
</p>

*Welcome to my SU25 Intro to Software Engineering project!* The goal for this project is to create a vulnerability assessment assistant tool to evaluate a user's source code for commonly exploited software vulnerabilities.

## Details
CodeSecAssistant is a vulnerability scanner that focuses on identifying security vulnerabilities in user-submitted code snippets or user-selected source code files. In the future, the option to parse full codebases will also be implemented. CodeSecAssistant utilizes LLM API services for security vulnerability detection based on prompts in a template file that tailors the LLM analysis to focus on the selected prompt's instructions. It is not intended to be a replacement for professional code analysis and shouldn't be deployed in professional settings or be used on proprietary code bases. CodeSecAssistant includes a GUI option and a rudimentary CLI option to support scripting capability.

## Requirements

### LLM APIs
**Note:** Putting API key(s) in your env is required for functionality

>**Gemini**
>    - Create Google AI Studio account 
>    - Generate and copy API key in Google AI Studio
>    - Set env - Linux: `export ASSIST_API_KEY={your-api-key}` | Windows: `$env:ASSIST_API_KEY="{your-api-key}"`

>**OpenAI**
>    - Create OpenAI account 
>    - Generate and copy API key in OpenAI dashboard
>    - Set env - Linux: `export ASSIST_API_KEY={your-api-key}` | Windows: `$env:ASSIST_API_KEY="{your-api-key}"`

## Initial Tool Setup

>**OPTIONAL:** Create a virtual enviroment to isolate dependencies
>    - To create the virtual enviornment - `python3 -m venv venv` 
>    - To activate the environment - Linux: `source venv/bin/activate` | Windows: `venv\Scripts\activate`
>    - Deactivate the environment when done using - `deactivate` *system agnostic*

You will need to install all required python dependencies `pip install -r requirements.txt`
- If you are using a python virtual environment, activate it before you install the required dependences

## Usage
### GUI Version
1. Run `python app.py` to open the GUI version of the app
2. Either:
    - Copy and paste source code into entry box labeled "Upload Source Code", then click "Submit" button
    - Click "Browse" button, and select file through GUI file explorer popout
3. Select "LLM Model" from drop down options in settings
4. Configure other desired settings from settings panel
5. Click "Start Analysis" button to generate response

### CLI Version
Run `python main.py [-l LLM] [filename]`
- `-l LLM` option is not required. defaults to Gemini

## Disclaimer
- This LLM vulnerability scanner should only be ethically used for educational purposes and not be used in professional settings or with propiertary codebases.
- There may be instances of false-negatives, false-positives, under developed true-positive, or other erroneous outputs.
- API usage cost is dependent on the LLM service and specific model chosen.