USAGE
  unimatrix [-a] [-b] [-c COLOR] [-f] [-g COLOR] [-h] [-l CHARACTER_LIST] [-n]
            [-o] [-s SPEED] [-u CUSTOM_CHARACTERS]

OPTIONAL ARGUMENTS
  -a                   Asynchronous scroll. Lines will move at varied speeds.

  -b                   Use only bold characters

  -c COLOR             One of: green (default), red, blue, white, yellow, cyan,
                       magenta, black

  -f                   Enable "flashers," characters that continuously change.

  -g COLOR             Background color (See -c). Defaults to keeping
                       terminal's current background.

  -h                   Show this help message and exit

  -l CHARACTER_LIST    Select character set(s) using a string over letter
                       codes (see CHARACTER SETS below.)

  -n                   Do not use bold characters (overrides -b)

  -o                   Disable on-screen status

  -s SPEED             Integer up to 100. 0 uses a one-second delay before
                       refreshing, 100 uses none. Use negative numbers for
                       even lower speeds. Default=85

  -t TIME              Exit the process after TIME seconds

  -u CUSTOM_CHARACTERS Your own string of characters to display. Enclose in
                       single quotes ('') to escape special characters. For
                       example: -u '#$('

  -w                   Single-wave mode: Does a single burst of green rain,
                       exits. You can put in a .bashrc file to run when your
                       terminal launches. Works well with speed at 95.

LONG ARGUMENTS
  -a --asynchronous
  -b --all-bold
  -c --color=COLOR
  -f --flashers
  -g --bg-color=COLOR
  -h --help
  -l --character-list=CHARACTER_LIST
  -s --speed=SPEED
  -n --no-bold
  -o --status-off
  -t --time
  -u --custom_characters=CUSTOM_CHARACTERS
  -w --single_wave

CHARACTER SETS
  When using '-l' or '--character_list=' option, follow it with one or more of
  the following letters:

  a   Lowercase alphabet
  A   Uppercase alphabet
  c   Lowercase Russian Cyrillic alphabet
  C   Uppercase Russian Cyrillic alphabet
  e   A few common emoji ( ☺☻✌♡♥❤⚘❀❃❁✼☀✌♫♪☃❄❅❆☕☂★ )
  g   Lowercase Greek alphabet
  G   Uppercase Greek alphabet
  k   Japanese katakana (half-width)
  m   Default 'Matrix' set, equal to 'knnssss'
  n   Numbers 0-9
  o   'Old' style non-unicode set, like cmatrix. Equal to 'AaSn'
  p   Klingon pIqaD (requires 'Horta' family font)*
  P   Klingon pIqaD (requires 'Klingon-pIqaD' or 'Code2000' family font)*
  r   Lowercase Roman numerals ( mcclllxxxxvvvvviiiiii )
  R   Uppercase Roman numerals ( MCCLLLXXXXVVVVVIIIIII )
  s   A subset of symbols actually used in the Matrix films ( -=*_+|:<>" )
  S   All common keyboard symbols ( `-=~!z#$%^&*()_+[]{}|\;':",./<>?" )
  u   Custom characters selected using -u switch

  For example: '-l naAS' or '--character_list=naAS' will give something similar
  to the output of the original cmatrix program in its default mode.
  '-l ACG' will use all the upper-case character sets. Use the same
  letter multiple times to increase the frequency of the character set. For
  example, the default setting is equal to '-l knnssss'.

  * With most modern Linux terminals (gnome-terminal, konsole, lxterminal,
    xfce4-terminal, mate-terminal) simply having the font installed system-wide
    is enough. The terminal will fall back to it for the Klingon, meaning that
    you don't have to select it in your terminal settings. 'Horta' seems not to
    work in Konsole. Fonts may need to be set manually as fallbacks in
    .Xresources for older terminals, such as urxvt and xterm.

KEYBOARD CONTROL
  SPACE, CTRL-c or q   exit
  - or LEFT            decrease speed by 1
  + or RIGHT           increase speed by 1
  [ or DOWN            decrease speed by 10
  ] or UP              increase speed by 10
  a                    toggle asynchronous scrolling
  b                    cycle through bold character options
                           (bold off-->bold on-->all bold)
  f                    toggle flashing characters
  o                    toggle on-screen status
  1 to 9               set color: (1) Green   (2) Red   (3) Blue     (4) White
                                  (5) Yellow  (6) Cyan  (7) Magenta  (8) Black
                                  (9) Terminal default
  ! to (               set background color (same colors as above, but pressing
                           shift + number)

EXAMPLES
  Mimic default output of cmatrix (no unicode characters, works in TTY):
    $ unimatrix -n -s 96 -l o

  Use the letters from the name of your favorite operating system in bold blue:
    $ unimatrix -B -u Linux -c blue

  Use default character set, plus dollar symbol (note single quotes around
      special character):
    $ unimatrix -l knnssssu -u '$'

  No bold characters, slowly, using emojis, numbers and a few symbols:
    $ unimatrix -n -l ens -s 50