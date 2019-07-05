# Japanese Number Learner
In Japanese, numbers can be hard on the ears to parse. One second you may be listening to something or 
someone and a number is mentioned, then next thing you know, your brain got hung up on trying to parse 
the number while the person continued to speak. This small program uses Google's text to speech api to 
play the audio for a random number to you (in a range you set). 

## Getting Started
You'll need python 3 for this project. It was developed on python 3.7.2. 

For third part modules, playsound will need to be installed as well as google cloud text to speech. 

```pip install --upgrade google-cloud-texttospeech```

```pip install playsound```

Follow the 5 simple instructions here, https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries, 
to set up a Google Cloud Platform(GCP) Project. You will need a google cloud account. I believe you get $300 
free credits on sign up (at least this was the case earlier in 2019.) Either way, it shouldn't matter. The 
pricing is shown here, https://cloud.google.com/text-to-speech/pricing, and there is a free tier that I assume is 
used automatically. I don't see any one user going over that amount through the use of this project. 

## Installing
To install this repo, either clone the repo or download as a zip file. 

## Notes
I wrote this for Windows and am unsure if it would be completely compatible with Mac and Linux. I believe mp3 files
should be able to be played with playsound on Mac but I have my doubts about Linux.  The signal code in app.py could 
prove troublesome on other systems as well. 

If anyone uses this program and wants me to change anything or fix any bugs then please let me know. I encountered some
500 server errors when interacting with google api at one point and I tried my best to handle any errors that could 
arise as a result. Not enough testing was done there since I didn't encounter the error enough times. 

For exiting the program just use ctrl + C then hit enter and a prompt will show asking the you to input y or n to close.
