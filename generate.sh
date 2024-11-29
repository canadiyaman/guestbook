#!/bin/bash

BASE_URL="http://127.0.0.1:8000/api"
USER_ENDPOINT="$BASE_URL/users/"
ENTRY_ENDPOINT="$BASE_URL/entries"


for i in {1..500}
do
  USER_NAME="User_$RANDOM"
  SUBJECT="Subject_$RANDOM"
  MESSAGE="Message body for $SUBJECT"

  curl -X POST "$ENTRY_ENDPOINT" \
  -H "Content-Type: application/json" \
  -d "{\"user_name\": \"$USER_NAME\", \"subject\": \"$SUBJECT\", \"message\": \"$MESSAGE\"}"

  echo "User: $NAME (ID: $USER_NAME) - Entry: $SUBJECT created."
done