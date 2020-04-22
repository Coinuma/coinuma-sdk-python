# Coinuma API SDK for Python

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
