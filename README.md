# Models As a Service Python CLI

[MaaS](https://maas.apps.prod.rhoai.rh-aiservices-bu.com/) Sign up for an API key here. 

## Requirements
* Python3, PIP


## Installation

1. Make a virtualenv

```bash
python3 -m venv venv
```
2. Activate it

```bash
source venv/bin/activate
```

3. Install requirements
   
```bash
pip install -r requirements.txt
```

4. Copy and configure your `.env`
```bash
cp .env.sample .env
```
and update the correct values from [API Keys](https://maas.apps.prod.rhoai.rh-aiservices-bu.com/admin/applications) and [API Endpoints](https://maas.apps.prod.rhoai.rh-aiservices-bu.com/docs)


## Usage
Show Help
```bash
python prompt.py -h
```

Run a Prompt
```bash
python prompt.py "This is the best machine learning prompt ever written" 
```