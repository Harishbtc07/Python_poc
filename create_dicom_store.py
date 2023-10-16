import os
import json
from googleapiclient import discovery

def create_dicom_store(config_file):
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

        # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to your JSON key file.
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

        api_version = "v1"
        service_name = "healthcare"
        
        # Returns an authorized API client by discovering the Healthcare API
        client = discovery.build(service_name, api_version)

        dicom_store_parent = f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"

        request = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .create(parent=dicom_store_parent, body={}, dicomStoreId=dicom_store_id)
        )

        response = request.execute()
        print(f"Created DICOM store: {dicom_store_id}")
        return response
    except Exception as e:
        print(f"Error creating DICOM store: {str(e)}")

if __name__ == "__main__":
    create_dicom_store("config.json")
