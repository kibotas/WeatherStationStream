#!/bin/bash

curl --data {"value":"True"} --header Content-Type: application/json 127.0.0.1:5000/show_overlay
