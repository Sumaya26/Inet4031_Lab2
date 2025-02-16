#!/bin/bash

user_list=("User1" "User2" "User3")

for user in "${user_list[@]}"; do
    echo "$user"
done

