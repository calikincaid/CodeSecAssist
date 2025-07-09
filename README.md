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
>    - Place API in env variables `export GEMINI_API_KEY={your-api-key}`

## Initial Tool Setup

>**OPTIONAL:** Create a virtual enviroment to isolate dependencies
>    - To create the virtual enviornment - `python3 -m venv venv` 
>    - To activate the environment - Linux: `source venv/bin/activate` | Windows: `venv\Scripts\activate`
>    - Deactivate the environment when done using - `deactivate` *system agnostic*

### Step 1:
First, you will need to install all required python dependencies `pip install -r requirements.txt`
- If you are using a python virtual environment activate it before you install the required dependences

