#!/bin/bash
#curl sends POST request to URL and to display response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
