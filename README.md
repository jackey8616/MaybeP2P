# MaybeP2P [![PyPI version](https://badge.fury.io/py/MaybeP2P.svg)](https://badge.fury.io/py/MaybeP2P) [![Build Status](https://travis-ci.org/jackey8616/MaybeP2P.svg?branch=master)](https://travis-ci.org/jackey8616/MaybeP2P) [![codecov](https://codecov.io/gh/jackey8616/MaybeP2P/branch/master/graph/badge.svg)](https://codecov.io/gh/jackey8616/MaybeP2P) [![Maintainability](https://api.codeclimate.com/v1/badges/1a8dceae8859199d3d54/maintainability)](https://codeclimate.com/github/jackey8616/MaybeP2P/maintainability)  
This is a very simple P2P framework for implement peer-to-peer system into Applications in Python.   
  
## Notice  
Right now this framework does not support any NAT hole paunching.  
Also, only support a very basic P2P communication protocol, you need to wrote your route rule by youself.  
  
## Feature

  1. Easy implementation of protocols.  
  2. Support TCP server.  
  
## Installation & Useage
`pip install MaybeP2P`

```
>>> p = Peer()
>>> p.start()
...
>>> p.exit()
Ctrl+D
```
## Other  
Feel free to RP to help me imporve.  
