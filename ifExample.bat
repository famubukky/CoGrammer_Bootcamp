:: Check if folder named new_folder exist
:: if new_folder exist, create a folder called if_folder
:: if if_folder exist, create a folder called HyperionDev 
:: if if_folder doesnt exist, create a folder called new-projects
if  exist "new_folder" (
    mkdir if_folder
)
if exist "if_folder" (
    mkdir HyperionDev
)else (
    mkdir new-projects
)

