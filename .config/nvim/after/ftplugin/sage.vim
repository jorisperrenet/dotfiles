" au FileType python syn keyword pythonDecorator True None False self

setlocal cindent
setlocal cinkeys-=0#
setlocal indentkeys-=0#

" `\<` and `\>` denote word boundaries in Vim regular expressions so
" that `if` in `elif` does not match `if`.
" NOTE: These patterns do not understand the language, just "dumb" matching!
let b:match_words = '\<if\>:\<elif\>:\<else\>,'
    \ . '\<try\>:\<except\>:\<finally\>,'
    \ . '\<for\>:\<break\>'
