# CS3300 Intro To SWE Semester Project
*Welcome to my SU25 Intro to Software Engineering project!* The goal for this project is to create a vulnerability assessment assistant tool to evaluate a user's source code for commonly exploited software vulnerabilities.

## Details
- Python CLI and GUI tool

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