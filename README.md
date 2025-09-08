# Azure_WebAPP_Databricks_Agentic_AI

The modular AI system is designed to efficiently route and answer user queries using a combination of FAQ, semantic search, and AI models via a customized model deployed in Databricks and serviced via a dedicated endpoint; all while maintaining strong evaluation, logging, and governance practices.

The azure WebApp is using Flask with html template to be uploaded. 

To test it locally via "http://127.0.0.1:5000/", follow the below steps:

1. Open Anaconda promp to avoid Admin permissions 

remove myenv ... rmdir /s /q myenv

2. Create virtual env: 
(base) C:\Users\xxxxx>conda create --prefix "C:\Users\xxxxx\Documents\V1\myenv" python=3.11

3. cd to the new venv:
cd C:\Users\xxxxx\Documents\V1\myenv

4. activate venv
(base) conda activate "C:\Users\xxxxx\Documents\V1\myenv"

5. pip install -r requirements.txt

6. git init              #This command creates a new subdirectory named .git that contains all the necessary files for the repository. 

7. git add .             #This command stages all the changes in the current directory for the next commit.

7. git commit -m "Prepare for deployment"


8. deploy 1:              #choose az resource 
az webapp up --name OpenAI-Conversation --resource-group rg-dxxxxxxxxxxxxxxxx-01 --runtime "PYTHON|3.11" --location "Canada Central" --sku F1


8. deploy 2:              # ci/cd
git push azure master
