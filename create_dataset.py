import json
from google.oauth2 import service_account
import googleapiclient.discovery

def create_healthcare_dataset(project_id, location, dataset_id, key_path):
    # Create credentials, and are used to authenticate with the Google Cloud platform.
    credentials = service_account.Credentials.from_service_account_file(
        key_path,
        scopes=['https://www.googleapis.com/auth/cloud-platform'],
    )

    # Create a client for the Healthcare API
    healthcare_service = googleapiclient.discovery.build(
        'healthcare',
        'v1',
        credentials=credentials,    
        cache_discovery=False,
    )

    # Define the parent resource for the dataset
    parent = f'projects/{project_id}/locations/{location}'
    # # # Define the dataset request body
    # # dataset_body = {
    # #     'datasetId': dataset_id,
    # }

    try:
        # Create the dataset
        response = healthcare_service.projects().locations().datasets().create(
            parent=parent,
            datasetId = dataset_id,
        ).execute()

        print(f'Dataset created: {response["name"]}')
    except Exception as e:
        print(f'Error creating dataset: {str(e)}')

def load_config(config_file):
    try:
        with open(config_file, 'r') as config_file:
            config_data = json.load(config_file)
            return config_data
    except Exception as e:
        print(f'Error loading config file: {str(e)}')
        return None

if __name__ == "__main__":
    config = load_config("config.json")
    if config:
        create_healthcare_dataset(config["project_id"], config["location"], config["dataset_id"], config["key_path"])