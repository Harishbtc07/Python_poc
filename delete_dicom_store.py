import json
from google.oauth2 import service_account
import googleapiclient.discovery

def delete_dicom_store(config_file):
    try:
        with open(config_file, 'r') as config_file:
            config_data = json.load(config_file)

        project_id = config_data.get("project_id")
        location = config_data.get("location")
        dataset_id = config_data.get("dataset_id")
        dicom_store_id = config_data.get("dicom_store_id")
        key_path = config_data.get("key_path")

        if not all([project_id, location, dataset_id, dicom_store_id, key_path]):
            print("Missing configuration values in the JSON file.")
            return

        # Create credentials
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

        # Define the parent resource for the DICOM store
        parent = f'projects/{project_id}/locations/{location}/datasets/{dataset_id}'

        try:
            # Delete the DICOM store
            healthcare_service.projects().locations().datasets().dicomStores().delete(
                name=f'{parent}/dicomStores/{dicom_store_id}'
            ).execute()

            print(f'Deleted DICOM store: {dicom_store_id}')
        except Exception as e:
            print(f'Error deleting DICOM store: {str(e)}')
    except Exception as e:
        print(f'Error reading config file: {str(e)}')

if __name__ == "__main__":
    delete_dicom_store("config.json")
