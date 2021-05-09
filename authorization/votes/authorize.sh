#!/bin/sh

touch file
echo "">file
face_recognition ../voting/known_people/ ../voting/unknown_people/ >file
find unknown_people/* -delete

output=$(python ./votes/check.py)

echo "">out

echo $output >out
