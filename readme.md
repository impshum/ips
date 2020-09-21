## IPS

**Get dummy text onto your clipboard as fast as possible.**

## Dependencies

* Python 3
* Requests
* pyperclip

## Install Dependancies

    pip install -r requirements.txt

## Run

Get 1 paragraph

    python ips.py

Get 10 paragraphs

    python ips.py 10

You should have dummy text on your clipboard ready to plaster wherever you need it.

### Change parameters

All info is here: http://loripsum.net

### Create an alias for speedy retrieval

Create an alias so all you'll have to type is 3 letters to initiate the script. Feel free to edit your alias to your needs or just stick with "ips".

### OSX

```
sudo nano ~/.bash_profile
```
Add this to the bottom and edit the file location.
```
alias ips='python /path/to/folder/ips.py'
```
And refresh
```
source ~/.bash_profile
```
Then run it.
```
ips
```

### Linux

```
sudo nano ~/.bashrc
```
Add this to the bottom.
```
alias ips='python /path/to/folder/ips.py'
```
And refresh
```
source ~/.bashrc
```
Then run it.
```
ips
```

### Windows

I have no idea.

---

##### Enjoy!
