# MakeItGreen
Simple PyPi Package that adds contributions to your GitHub repository

### How to use?

Use Sudo to set path to executable systemwide

`pip install makeitgreen` 

`mig`

#### When it shows

`Enter path where you want to clone and make Misc Changes every time you run MakeItGreen:`

Enter the path to folder where you want the repo to be cloned. Repo will be cloned by repository name under the path specified. 

`Enter link to private repo for writing to remote:`

Enter the link to a private repository you have write access to.

### Start All Over again

To setup MakeItGreen from the beginning, 

 `mig --setup Y`

BEWARE: This will delete your current repository folder from local system and remove all configuration from memory.

### Troubleshooting

If running `mig` does nothing or if `no module named mig found` is shown, follow instructions below:

`pip uninstall makeitgreen`

`sudo pip install makeitgreen`





