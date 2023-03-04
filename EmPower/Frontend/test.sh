#!/bin/bash

# set the folder name to search in
folder_name="Teacher_UI"

# set the keyword to search for
search_keyword="../Images/"

# set the replacement string
replace_string="../EmPower/Frontend/Images"

# iterate through the files in the folder
for file in "$folder_name"/*.ui; do
  # check if the file exists and is a regular file
  if [[ -f "$file" ]]; then
    # replace the keyword with the replacement string in every line of the file
    sed -i "s|$search_keyword|$replace_string|g" "$file"
    
  fi
done

