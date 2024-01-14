import requests
import json

# DigitalOcean API Token
api_token = 'dop_v1_78f63d6c24574f55936ab0bcfeb3cd9f1815ba191bfa06faeb60ca15dac69a22'

# Domain and subdomain details
domain_name = 'amer.dev'
subdomain_name = 'media'

# Get your current external IP address
current_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']

# Fetch existing DNS records from DigitalOcean
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

response = requests.get(f'https://api.digitalocean.com/v2/domains/{domain_name}/records', headers=headers)
records = response.json()['domain_records']

# Find the DNS record for 'media.amer.dev'
record_id = None
for record in records:
    if record['name'] == subdomain_name:
        record_id = record['id']
        break

# If the DNS record exists and the IP address has changed, update it
if record_id and record['data'] != current_ip:
    updated_record = {
        'data': current_ip,
    }

    update_response = requests.put(f'https://api.digitalocean.com/v2/domains/{domain_name}/records/{record_id}', headers=headers, json=updated_record)

    if update_response.status_code == 200:
        print(f'DNS record updated successfully to {current_ip}')
    else:
        print(f'Failed to update DNS record: {update_response.text}')
else:
    print('DNS record is up to date or does not exist.')

