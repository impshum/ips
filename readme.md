# Get dummy text onto your clipboard as fast as possible. 

#### Just another shortcut I made for myself.

## Dependencies

* Python 2.7
* urllib
* wpyperclip

## Install Dependancies

    pip install -r requirements.txt

## Run

    python ipsum.py

You should have dummy text on your clipboard ready to plaster wherever you need it.

### Change parameters

You can change the parameters to specify the output you're going to get. Say, you need 10 short paragraphs with headings, use loripsum.net/api/10/short/headers. All of the possible parameters are:

    (integer) - The number of paragraphs to generate.
    short, medium, long, verylong - The average length of a paragraph.
    decorate - Add bold, italic and marked text.
    link - Add links.
    ul - Add unordered lists.
    ol - Add numbered lists.
    dl - Add description lists.
    bq - Add blockquotes.
    code - Add code samples.
    headers - Add headers.
    allcaps - Use ALL CAPS.
    prude - Prude version.
    plaintext - Return plain text, no HTML.

All info is here: http://loripsum.net

### Create an alias for speedy retrieval

Create an alias so all you'll have to type is 3 letters to initiate the script. Feel free to edit your alias to your needs or just stick with "ips".

### OSX

```
sudo nano ~/.bash_profile
```
Add this to the bottom and edit the file location.
```
alias ips='python /path/to/folder/ipsum.py'
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
alias ips='python /path/to/folder/ipsum.py'
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
