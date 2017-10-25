# MakeItGreen
Simple PyPi Package that adds contributions to your GitHub repository

## How to use?

Use Sudo to set path to executable systemwide

`$ pip install makeitgreen` 

`$ mig`

## When it shows

`Enter path where you want to clone and make Misc Changes every time you run MakeItGreen:`

Enter the path to folder where you want the repo to be cloned. Repo will be cloned by repository name under the path specified. 

`Enter link to private repo for writing to remote:`

Enter the link to a private repository you have write access to.

## Start All Over again

To setup MakeItGreen from the beginning, 

 `$ mig --setup Y`

BEWARE: This will delete your current repository folder from local system and remove all configuration from memory.

## Troubleshooting

##### Mig not found

If running `$ mig` does nothing or if `no module named mig found` is shown, follow instructions below:

`$ pip uninstall makeitgreen`

`$ sudo pip install makeitgreen`

##### GDBM No such File or directory 

If you come across the following error:

`_gdbm.error: [Errono 2] No such file or Directory`

Then probably you're not having access to the folder where shelve is being stored. Use

`$ sudo mig`

##### mig —setup fails

Run `$ sudo mig --setup Y`

##### -bash: $: command not found

Run all commands without the `$` sign🙄🙄🙄

