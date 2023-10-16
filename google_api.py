# Import necessary modules
from google.oauth2 import service_account
import googleapiclient.discovery
import json

# Path to the service account key JSON file
key_path = 'C:\\Users\\Harish\\Downloads\\mimetic-obelisk-399608-c948a0e0f1a0.json'

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

# Define the FHIR resource (Patient resource in this example)
patient_resource = {
    "resourceType": "Patient",
    "id": "12345",
    "name": [{"family": "Doe", "given": ["John"]}],
}

# Convert the resource to JSON format
patient_resource_json = json.dumps(patient_resource)

# Define the parent dataset
parent = 'projects/your-project-id/locations/your-location/datasets/your-dataset-id'

# Define the FHIR store name
fhir_store = ''

# Store the FHIR resource
response = healthcare_service.projects().locations().datasets().fhirStores().fhir().create(
    parent=parent,
    fhirStore=fhir_store,
    body=patient_resource_json,
).execute()

print("Resource created: {}".format(response['name']))
