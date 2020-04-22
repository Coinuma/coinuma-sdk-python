# Coinuma API SDK for Python
Welcome to the Coinuma API! Through our cryptocurrency exchange we offer a wide selection 
of currencies for you to trade. For a complete API request and response reference please check 
out our [API documentation](https://coinuma.com/developers/docs). If you need additional help in using 
the API, please visit the [Coinuma website](https://coinuma.com) and reach our support center. 
Happy trading!
## Requirements
Python 3.5+

## Installation

```sh
pip3 install coinuma-sdk
```

## Getting started
To import the package:
    
```python
import coinuma_sdk 
```

### Public client
```python
import coinuma_sdk 
public = coinuma_sdk.api.Public()
```

### Private client
```python
import coinuma_sdk 
private = coinuma_sdk.api.Private("YOUR_PUBLIC_KEY", "YOUR_PRIVATE_KEY")
```
