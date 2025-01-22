# API Testing Specification

## Get Request Test
Tags: get, api

* Send GET request to "https://httpbin.org/get" with parameters:
   |param|value|
   |-----|-----|
   |name |test |
   |id   |123  |
* Verify response status code is "200"
* Verify response contains correct parameters

## Post Request Test
Tags: post, api

* Send POST request to "https://httpbin.org/post" with JSON body:
   |key      |value    |
   |---------|---------||
   |username |testuser |
   |password |test123  |
* Verify response status code is "200"
* Verify response body contains submitted data