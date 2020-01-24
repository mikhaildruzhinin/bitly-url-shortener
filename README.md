# Bitly url shortener

This script has two main features. It can shorten links with [Bitly.com](https://bitly.com) and also it can provide you with the statistics for your short links.

### How to install

This script will not execute unless you have a Bitly token. You can get a token in your profile settings on [Bitly.com](https://bitly.com). For more information, please read section Authorization of [Bitly API Documentation](https://dev.bitly.com/v4_documentation.html).

After you get the token, create a file with the name `.env` in the same directory with the script. Paste your token in the file:
```
BITLY_TOKEN = token
```
where token is your Bitly token.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Launch


```
python3 main.py url
```
where url is the link you want the script to use.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
