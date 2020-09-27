# Dependencyless client api for [Numverify](https://numverify.com)
## Installation
```
python setup.py install
```
## Usage
```
from numverify_api_client import Client

client = Client('YOUR_API_ACCESS_KEY_HERE')
try:
    print(client.get_info('79991111111'))
except Exception as e:
    print(e)
```
### Outputs:
#### Success:
```
{
    'valid': True, 
    'number': '79991111111', 
    'local_format': '9991111111', 
    'international_format': '+79991111111', 
    'country_prefix': '+7', 
    'country_code': 'RU', 
    'country_name': 'Russian Federation', 
    'location': 'Moscow and Moscow Oblast', 
    'carrier': 'LLC Skartel (YOTA)', 
    'line_type': 'mobile'
}
```
#### Failure:
```
Error: You have not supplied a valid API Access Key. [Technical Support: support@apilayer.com], Code: 101
```