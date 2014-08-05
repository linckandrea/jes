# JES- Jython Environment for Students
# Copyright (C) 2002  Jason Ergle, Claire Bailey, David Raines, Joshua Sklare
# See JESCopyright.txt for full licensing information

import java.awt as awt

BEGINNER_MODE = 'Normal'
EXPERT_MODE = 'Expert'

LOW_FONT = 8
MID_FONT = 32
HIGH_FONT = 72


FONT_MODE_LOW = [LOW_FONT, MID_FONT, HIGH_FONT]
FONT_MODE_MID = [MID_FONT, LOW_FONT, HIGH_FONT]
FONT_MODE_HIGH = [HIGH_FONT, MID_FONT, LOW_FONT]

USER_MODES = [BEGINNER_MODE, EXPERT_MODE]
USER_MODES_2 = [EXPERT_MODE, BEGINNER_MODE]

TAB = '  '
APPLICATION_TITLE = 'JES - Jython Environment for Students - %s'
INITIAL_WINDOW_SIZE = (1000, 600)
KEYWORD_COLOR = awt.Color(50, 50, 150)
ENVIRONMENT_WORD_COLOR = awt.Color(150, 50, 150)
COMMENT_COLOR = awt.Color(50, 120, 50)
STRING_COLOR = awt.Color(150, 90, 90)
LPAREN_COLOR = awt.Color(150, 0, 0)
RPAREN_COLOR = awt.Color(150, 0, 0)
LOAD_BUTTON_DIFF_COLOR = awt.Color(200, 50, 50)
LOAD_BUTTON_SAME_COLOR = awt.Color(50, 200, 50)
FONT_SIZE = 12

COMMAND_FROM_CONSOLE = '<input>'
STACK_MSG = ' in file %s, on line %d, in function %s\n'
NAME_OF_EXC_MSG = 'The error "%s" had occurred\n'
LINE_NUM_MSG = 'Please check line %d of %s\n'

JESPROGRAM_ERROR_LOADING_FILE = '\nThere was an error loading the file.  ' \
                                + 'It may not be present.  FILENAME: '
JESPROGRAM_NO_FILE = '\nNo file has been selected.\n' + \
                     'You must open a saved file, or save the opened file,\n' +\
                     'before clicking LOAD\n'

EDITOR_LOAD_WARNING = "WARNING: Current code has not been loaded.\n"
HELP_START_PAGE = 'http://coweb.cc.gatech.edu/mediaComp-teach/25'

# The EXCEPTION_MESSAGES array contains a list of user-friendly exceptions
# messages.  Messages can also contain values that will be replaced by JES
# before displaying the message.  These values can be any attribute of the
# exception type that is being raised.
# For example, the RuntimeError exception has an attribute called 'lineno'; if
# the RuntimeError message contained '%(lineno)s', then that text would be
# replaced with the actual value of the lineno attribute.
# Example message:  "Runtime error occurred on line '%(lineno)s'"
EXCEPTION_MESSAGES = {
    'AssertionError': 'An "assert" statement has failed.',
    'AttributeError': 'You are trying to access a part of the object that doesn\'t exist.',
    'EOFError': 'The build-in read function failed because the end  of the file has been reached. This happens when you leave a statement or function unfinished or do not match up all of your parentheses.',
    'FloatingPointError': 'A floating point operation has failed.',
    'IOError': 'I tried to read a file, and couldn\'t.  Are you sure that file exists? If it does exist, did you specify the correct directory/folder?',
    'ImportError': 'An import statement failed to find the module that was defined. You need to find the correct name of the module you want to use.',
    'IndexError': 'The index you\'re using goes beyond the size of that data (too low or high). For instance, maybe you tried to access OurArray[10] and OurArray only has 5 elements in it.',
    'IndentationError': 'A line of code contains bad indentation. Make sure all of your lines match up inside your functions.',
    'KeyError': 'Attempt to access a key that is not in a dictionary.',
    'KeyboardInterrupt': 'The user pressed the interrupt key.',
    'NameError': 'A local or global name could not be found. You need to define the function or variable before you try to use it in any way.',
    'NotImplementedError': 'A method that was called must be implemented in a sub-class. You need to define this method yourself before you use it, jython or JES will not do it for you.',
    'OSError': 'An error occurred while making an operating system call. Please tell a TA what you were doing when this happened, so we may correct it.',
    'OverflowError': 'An arithmetic result is outside the range of acceptable values. This means that the answer is either too large or too small to be represented.',
    'RuntimeError': "An unexpected error happened.",
    'StackOverflowError': 'You have overrun the stack. This means that way too many functions were called before they ever had a chance to return.',
    'SyntaxError': "Your code contains at least one syntax error, meaning it is not legal Jython.",
    'SystemError': 'An internal system error has occurred.  Please tell a TA what you were doing when this happened so that we may correct it. ',
    'SystemExit': 'A call to the sys.exit() function has been made. Normally this would exit JES entirely, but we want to make sure you don\'t exit accidentally and lose your work. If you want to exit JES, use the Exit option in the File menu.',
    'TypeError': 'An attempt was made to call a function with a parameter of an invalid type. This means that you did something such as trying to pass a string to a method that is expecting an integer.',
    'UnboundLocalError': 'A local name was used before it was created. You need to define the method or variable before you try to use it.',
    'UnicodeError': 'An error occurred while encoding or decoding Unicode characters.',
    'ValueError': 'An error occurred attempting to pass an argument to a function.',
    'WindowsError': 'An error occurred while making a Windows system call. Please let your TA know what you were doing when this happened, so we can fix it.',
    'ZeroDivisionError': 'You have attempted to divide a number by zero. In mathematics (and in computing), this gives an undefined result. JES cannot deal with this and you should never be attempting to do it.',
    'ThreadDeath': 'The code has been stopped due to you hitting the stop button.',
    'TokenError': 'There is something wrong with the text of the file you had me try to load.\nYou may have not have as many closing parentheses as opening parentheses, left the ending quote off of a string, or tried to use a Jython keyword (if, def, etc...) as a function.'}

STOP_MESSAGE = '[The program was stopped by the stop button.]'

# Error messages that we can't actually catch:

#   'MemoryError'          : 'The system does not have enough memory to allocate an object.',

GENERIC_EXCEPTION_MESSAGE = 'A Python %s happened while running your program, so it stopped.'
TAB_ERROR_MESSAGE = "There was a spacing error in the program.\nIt might be from a previous line, but I think the error is in line "

