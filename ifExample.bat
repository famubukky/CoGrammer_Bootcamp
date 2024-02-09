:: line of code that shows if folder named new_folder exist
if  exist "new_folder" (
    mkdir if_folder
)
if exist "if_folder" (
    mkdir hyperionDev
)else (
    mkdir new-projects
)

