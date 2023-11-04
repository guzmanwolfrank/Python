# Wolf Chart 

This program allows you to show stock prices using the yfinance module.

My motivation was to create a light, quick loading stock and futures quote application.  
I wanted to create something that would load quickly and without sign on authentication.  Deleting the need for signon authorization 
worked to cut load times.  

## Challenges
A challenge I overcame was coding for a new framework.  I had never used tkinter before this and the mortgage calculator project. 
Tkinter has unique code patterns and functions within the Python language.  

Some challenges I am currently facing are conversion to candlestick chart output.  I am currently getting an error message for a bug in the 'stock' variable. 

I am also looking to upload the project as a .EXE program for easy download and launch on desktop or windows os tablets and laptops. 


## Deployment
First, download Python. 

Then to deploy this project, run the following after dowloading source code or copying file as wolfchart.py

```bash
  python wolfchart.py 
```

Once the program is running, simply type in the stock symbol for the stock desired or the futures abbreviation and equal sign followed by F. 

For example,


```bash
 Nasdaq 100 Emini Futures = NQ=F 
 SP 500 Emini Futures = ES=F 
 Tesla = TSLA 
 Apple = AAPL
```

![entry](https://github.com/guzmanwolfrank/Python/assets/29739578/83fd99a2-2ede-45f6-afce-ec214d2324fe)

# 

![showchart](https://github.com/guzmanwolfrank/Python/assets/29739578/3d814cdc-7fc8-4510-99a4-29fd0b3f47c4)


## Tech Stack

yfinance==0.2.18 <br/>
matplotlib==3.7.1 <br/>
tkinter==8.6 <br/>
python==3.11.3 <br/>




## License

[MIT](https://choosealicense.com/licenses/mit/)





