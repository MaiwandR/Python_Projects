#! python3

#Program that copies to clipboard for easy emails

TEXT = {
    'agree':
    """Thanks for getting back to me. I totally agree so we should go ahead with that.

    Yours sincerely,
    Maiwand Raheem""",
    'solved': 
    """Thank you I just checked and the issue was solved. Thanks again for the help.
     
      Yours sincerely,
       Maiwand Raheem """

}

import sys
import pyperclip

if len(sys.argv) < 2:
    print("Usage: py CopyPaste.py [Keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for' + keyphrase)

