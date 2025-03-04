# sesame_client.DefaultApi

All URIs are relative to *https://api.candyhouse.co/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_result_get**](DefaultApi.md#action_result_get) | **GET** /action-result | Query Execution Result
[**sesame_device_id_get**](DefaultApi.md#sesame_device_id_get) | **GET** /sesame/{device_id} | Get Sesame status
[**sesame_device_id_post**](DefaultApi.md#sesame_device_id_post) | **POST** /sesame/{device_id} | Control Sesame
[**sesames_get**](DefaultApi.md#sesames_get) | **GET** /sesames | Get Sesame list


# **action_result_get**
> QueryExecutionResultResponse action_result_get(task_id)

Query Execution Result

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import sesame_client
from sesame_client.rest import ApiException
from pprint import pprint
configuration = sesame_client.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.candyhouse.co/public
configuration.host = "https://api.candyhouse.co/public"
# Create an instance of the API class
api_instance = sesame_client.DefaultApi(sesame_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Task ID from command result.

try:
    # Query Execution Result
    api_response = api_instance.action_result_get(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->action_result_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | [**str**](.md)| Task ID from command result. | 

### Return type

[**QueryExecutionResultResponse**](QueryExecutionResultResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sesame_device_id_get**
> GetSesameStatusResponse sesame_device_id_get(device_id)

Get Sesame status

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import sesame_client
from sesame_client.rest import ApiException
from pprint import pprint
configuration = sesame_client.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.candyhouse.co/public
configuration.host = "https://api.candyhouse.co/public"
# Create an instance of the API class
api_instance = sesame_client.DefaultApi(sesame_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Sesame unique ID

try:
    # Get Sesame status
    api_response = api_instance.sesame_device_id_get(device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sesame_device_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| Sesame unique ID | 

### Return type

[**GetSesameStatusResponse**](GetSesameStatusResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sesame_device_id_post**
> ControlSesameResponse sesame_device_id_post(device_id, body)

Control Sesame

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import sesame_client
from sesame_client.rest import ApiException
from pprint import pprint
configuration = sesame_client.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.candyhouse.co/public
configuration.host = "https://api.candyhouse.co/public"
# Create an instance of the API class
api_instance = sesame_client.DefaultApi(sesame_client.ApiClient(configuration))
device_id = 'device_id_example' # str | Sesame unique ID
body = sesame_client.ControlSesameRequest() # ControlSesameRequest | Sync command will force the server to update Sesame status. **NOTE**: Frequent use of the sync command will reduce Sesame’s battery life. 

try:
    # Control Sesame
    api_response = api_instance.sesame_device_id_post(device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sesame_device_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| Sesame unique ID | 
 **body** | [**ControlSesameRequest**](ControlSesameRequest.md)| Sync command will force the server to update Sesame status. **NOTE**: Frequent use of the sync command will reduce Sesame’s battery life.  | 

### Return type

[**ControlSesameResponse**](ControlSesameResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sesames_get**
> list[GetSesameResponse] sesames_get()

Get Sesame list

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import sesame_client
from sesame_client.rest import ApiException
from pprint import pprint
configuration = sesame_client.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.candyhouse.co/public
configuration.host = "https://api.candyhouse.co/public"
# Create an instance of the API class
api_instance = sesame_client.DefaultApi(sesame_client.ApiClient(configuration))

try:
    # Get Sesame list
    api_response = api_instance.sesames_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sesames_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GetSesameResponse]**](GetSesameResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

