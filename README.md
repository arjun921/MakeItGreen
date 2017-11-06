# MakeItGreen
Simple PyPi Package that adds contributions to your GitHub repository

### How to use?

```
$ pip install makeitgreen
$ mig
Enter path where you want to clone and make Misc Changes every time you run MakeItGreen:
/Users/arjun921/working_directory/ #Change path to your own system path!
Enter link to private repo for writing to remote:
https://github.com/arjun921/migPrivate #Change link to your own repository!
```
##### Start All Over again

 ```
$ mig --setup Y
 ```

BEWARE: This will delete your current repository folder from local system and remove all configuration from memory.



#### Troubleshooting/FAQ

##### Mig not found

If running `$ mig` does nothing or if `no module named mig found` is shown, follow instructions below:

```
$ pip uninstall makeitgreen
$ sudo pip install makeitgreen
```



##### GDBM No such File or directory 

If you come across the following error:

```
_gdbm.error: [Errono 2] No such file or Directory
```

then probably you're not having access to the folder where shelve is being stored. Run

```
$ sudo mig
```



##### mig —setup fails

```
$ sudo mig --setup Y
```



##### -bash: $: command not found

Run all commands without the `$` sign🙄🙄🙄

