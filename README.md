# swagger-client
WEM Application API Documentation

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install wem-saas
```
(you may need to run `pip` with root permission: `sudo pip install wem-saas`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
appointment_id = 'appointment_id_example' # str | 

try:
    # Deletar apontamento
    api_response = api_instance.appointmentDelete(appointment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->appointmentDelete: %s\n" % e)


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
appointment_id = 56 # int | 
body = NULL # object |  (optional)

try:
    # Editar apontamento
    api_response = api_instance.appointmentPatch(appointment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->appointmentPatch: %s\n" % e)


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Criar apontamento
    api_response = api_instance.appointmentPost(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->appointmentPost: %s\n" % e)


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Buscar apontamentos
    api_response = api_instance.appointmentQuery(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->appointmentQuery: %s\n" % e)


# create an instance of the API class
api_instance = swagger_client.ApontamentosApi(swagger_client.ApiClient(configuration))
appointment_id = 'appointment_id_example' # str | 
body = NULL # object |  (optional)

try:
    # Aprovar apontamento
    api_response = api_instance.exchange_api_v2_appointment_status_appointment_id_patch(appointment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApontamentosApi->exchange_api_v2_appointment_status_appointment_id_patch: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://wem-qa.wnology.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApontamentosApi* | [**appointmentDelete**](docs/ApontamentosApi.md#appointmentDelete) | **DELETE** /exchange/api/v2/appointment/{appointment_id} | Deletar apontamento
*ApontamentosApi* | [**appointmentPatch**](docs/ApontamentosApi.md#appointmentPatch) | **PATCH** /exchange/api/v2/appointment/{appointment_id} | Editar apontamento
*ApontamentosApi* | [**appointmentPost**](docs/ApontamentosApi.md#appointmentPost) | **POST** /exchange/api/v2/appointment | Criar apontamento
*ApontamentosApi* | [**appointmentQuery**](docs/ApontamentosApi.md#appointmentQuery) | **POST** /exchange/api/v2/appointment/query | Buscar apontamentos
*ApontamentosApi* | [**exchange_api_v2_appointment_status_appointment_id_patch**](docs/ApontamentosApi.md#exchange_api_v2_appointment_status_appointment_id_patch) | **PATCH** /exchange/api/v2/appointment/status/{appointment_id} | Aprovar apontamento
*ConversoDeFatoresDeEmissoApi* | [**emissionsConversionFactorPatch**](docs/ConversoDeFatoresDeEmissoApi.md#emissionsConversionFactorPatch) | **PATCH** /exchange/api/v1/emissions/conversion-factor | Editar fatores de emissão
*ConversoDeFatoresDeEmissoApi* | [**emissionsConversionFactorDeleteAll**](docs/ConversoDeFatoresDeEmissoApi.md#emissionsConversionFactorDeleteAll) | **DELETE** /exchange/api/v1/emissions/conversion-factor/plants/{plant_id} | Remover todos os fatores
*ConversoDeFatoresDeEmissoApi* | [**emissionsConversionFactorGet**](docs/ConversoDeFatoresDeEmissoApi.md#emissionsConversionFactorGet) | **GET** /exchange/api/v1/emissions/conversion-factor/plants/{plant_id} | Buscar fatores de emissão
*MetasApi* | [**goalsDeleteAll**](docs/MetasApi.md#goalsDeleteAll) | **DELETE** /exchange/api/v1/goals/plants/{plant_id} | Remover metas
*MetasApi* | [**goalsPut**](docs/MetasApi.md#goalsPut) | **PUT** /exchange/api/v1/goals/plants/{plant_id} | Editar metas
*MetasApi* | [**goalsGet**](docs/MetasApi.md#goalsGet) | **POST** /exchange/api/v2/appointments/targets | Buscar metas
*RelatrioApi* | [**reportCardsGet**](docs/RelatrioApi.md#reportCardsGet) | **GET** /exchange/api/v2/report/emissions/cards | Cards
*RelatrioApi* | [**reportChartsGet**](docs/RelatrioApi.md#reportChartsGet) | **GET** /exchange/api/v2/report/emissions/chart | Chart

## Documentation For Models


## Documentation For Authorization


## bearerAuth



## Author


