# Tamil Phonetic Typing [with Screen reader support]
This application allows users to directly type in Tamil using Tamil phonetic equivalent.

Ex: ammA or ammaa for அம்மா

There are numerous tools and application that are available to make it happen. 
This application was created mainly to aid Visually Challenged friends to directly type in tamil and allow the screenreaders like [NVDA](https://www.nvaccess.org/) to read as they type.

This is a simple prototype to start with. Phonetic typing was bigger problem with screenreaders so we had to create this to handle the issue.


## Usage
Run the exe file and it will be running in the background.
```
ctrl+1 - To activate Phonetic Tamil typing
ctrl+0 - To stop Phonetic Tamil typing and return to default settings
ctrl+q - To quit the application
```

## Generate exe
```
$ pyinstaller --onefile -w .\src\tamil_phonetic_typing_with_screenreader_support.py
```

## NOTE - This application is tested only for windows. Keyboard module behaves differently with Mac.
