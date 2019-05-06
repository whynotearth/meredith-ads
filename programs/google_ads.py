import json
import sys

from lib import File

File = File()

secret_filename = raw_input('''
Enter the path of your secret json key file.
Example : /Users/Desktop/credentials.json

$: ''')

json_file = File.read(secret_filename)
data = json.loads(json_file)["web"]

client_id = data["client_id"]
project_id = data["project_id"]
auth_uri = data["auth_uri"]
token_uri = data["token_uri"]
auth_provider_x509_cert_url = data["auth_provider_x509_cert_url"]
client_secret = data["client_secret"]
