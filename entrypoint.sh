#!/bin/bash

if [ "$ENVIRONMENT" == "PRD"]
then
    echo "\$ENVIRONMENT is Production"
    uvicorn --host ${SERVICE_HOST} --port ${SERVICE_PORT} main:app
else
    echo "\$ENVIRONMENT is Development"
    uvicorn --reload --host ${SERVICE_HOST} --port ${SERVICE_PORT} main:app
fi
