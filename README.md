# Siege Server Changer
A Python program to easily change data centers/servers for Rainbow Six: Siege.

## Getting Started
Head on over to the [Releases tab](https://github.com/Gunsmithy/SiegeServerChanger/releases) and download the latest siege_server_changer-vX.X.X.zip file and extract it somewhere convenient on your PC.  

All you need to do to is simply run the included `siege_server_changer.exe` and it will prompt you for the rest!  

You will be prompted for an account UUID which can be found in the URL after searching yourself on [R6Tab.com](https://r6tab.com/)

Right now there is no local storage of account UUIDs or names, so the easiest thing to do is have it automatically detect and change the server for all accounts on your PC.

## Command-Line usage
Command-line use is now supported! Simply include one or both of the below parameters to skip the user prompt.

* --account ACCOUNT - The account UUID for which you want to change servers. Assumed to be all accounts found locally if not provided.
* --server SERVER - The server/data-centre you wish to use. Assumed to be default/ping-based if not provided.

You can use this with a Stream Deck "Open" action for example by pointing to `siege_server_changer.exe` and including the parameters after it in the text box.  

Example of what you would include in the App/File box of the Open action:  
`C:\Users\User\Downloads\siege_server_changer-v0.2\siege_server_changer.exe --account="3cb45a4a-9208-48ac-8690-27dcbf1b6604" --server="eastus"`

## Future Releases
Future releases will likely include:
* Local storage of account UUIDs/querying R6Tab for names.
* A GUI instead of command prompt when not opting to use parameters/shortcuts

## Enjoy!
Feel free to create a [Github Issue or Feature Request](https://github.com/Gunsmithy/SiegeServerChanger/issues) if you have any problems using this or if there's something you'd like added!  
