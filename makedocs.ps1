# change to the myproject docs folder
Set-Location -Path ".\myproject\docs"

# activate the virtual environment
..\..\.venv\Scripts\activate

Remove-Item -Path ".\_*\" -Recurse -Force
Remove-Item -Path "*.rst" -Recurse -Force
Copy-Item -Path "index_template" "index.rst"

./make clean
./make html

# get back to the main myproject-project folder
Set-Location -Path "..\..\"
