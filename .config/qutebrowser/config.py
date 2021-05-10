# Change some settings here since the autoconfig must only be changed
# through typing `:set` in the browser and for keybinding/aliases that
# is not recommended. (Saving in the browser is done by typing `sf`).

# Loading autoconfig.yml
config.load_autoconfig()

# Bindings
c.bindings.default = {
    'normal': {
        # General
        '.': 'repeat-command',
        '/': 'set-cmd-text /',
        ':': 'set-cmd-text :',
        ' ': 'set-cmd-text :',
        '?': 'set-cmd-text ?',
        # Select Tabs
        '1': 'tab-focus 1',
        '2': 'tab-focus 2',
        '3': 'tab-focus 3',
        '4': 'tab-focus 4',
        '5': 'tab-focus 5',
        '6': 'tab-focus 6',
        '7': 'tab-focus 7',
        '8': 'tab-focus 8',
        '9': 'tab-focus 9',
        '0': 'tab-focus -1',
        # Zoom
        '<Ctrl-Shift-+>': 'zoom-in',
        '<Ctrl-->': 'zoom-out',
        '<Ctrl-=>': 'zoom',  # reset zoom
        # Hints
        'f': 'hint',  # opens hint in same tab
        'F': 'hint all tab',  # opens in background tab
        'I': 'hint inputs --first',  # type in the first input
        ';o': 'hint all',
        ';O': 'hint all tab-fg',
        ';b': 'hint all tab-bg',
        ';w': 'hint all window',
        ';h': 'hint all hover',
        ';r': 'hint all right-click',
        ';d': 'hint links download',
        ';<Ctrl-d>': 'hint all delete',
        ';y': 'hint links yank',
        ';Y': 'hint links yank-primary',
        ';i': 'hint inputs',
        ';I': 'hint images',
        ';<Ctrl-i>': 'hint images tab',
        # Enter Modes
        'i': 'mode-enter insert',
        'v': 'mode-enter caret',
        'V': 'mode-enter caret ;; toggle-selection --line',
        'z': 'mode-enter passthrough',
        # Open
        'o': 'set-cmd-text -s :open',
        'O': 'set-cmd-text -s :open -t',
        'b': 'set-cmd-text -s :open -b',
        'w': 'set-cmd-text -s :open -w',
        'W': 'set-cmd-text -s :open -w',
        'ao': 'set-cmd-text :open -r {url:pretty}',
        'aO': 'set-cmd-text :open -r -t {url:pretty}',
        'ab': 'set-cmd-text :open -r -b {url:pretty}',
        'aw': 'set-cmd-text :open -r -w {url:pretty}',
        'aW': 'set-cmd-text :open -r -p {url:pretty}',
        'go': 'open',
        'gO': 'open -t',
        'T': 'open -t',
        'gb': 'open -b',
        'gw': 'open -w',
        'gW': 'open -p',  # private
        'po': 'open -- {clipboard}',
        'pO': 'open -t -- {clipboard}',
        'pb': 'open -b -- {clipboard}',
        'pw': 'open -w -- {clipboard}',
        'pp': 'open -p -- {clipboard}',
        'Po': 'open -- {primary}',
        'PO': 'open -t -- {primary}',
        'Pb': 'open -b -- {primary}',
        'Pw': 'open -w -- {primary}',
        'Pp': 'open -p -- {primary}',
        # Close
        'c': 'tab-close',
        'Cp': 'tab-close -p',
        'Cn': 'tab-close -n',
        'Co': 'tab-close -o',
        'Cf': 'tab-close -f',
        'C<Ctrl-w>': 'close',
        'Cet': 'tab-only',
        'Cef': 'tab-only --force',
        'Cep': 'tab-only --prev',
        'Cen': 'tab-only --next',
        'C<Ctrl-Shift-W>': 'window-only',
        # Undo
        'u': 'undo',
        # Reload and Go back/forwards
        'r': 'reload',
        'R': 'reload -f',
        'J': 'back',
        'K': 'forward',
        '<Ctrl-h>t': 'back -t',
        '<Ctrl-h>b': 'back -b',
        '<Ctrl-h>w': 'back -w',
        '<Ctrl-h>W': 'back -p',
        '<Ctrl-l>t': 'forward -t',
        '<Ctrl-l>b': 'forward -b',
        '<Ctrl-l>w': 'forward -w',
        '<Ctrl-l>W': 'forward -p',
        '<back>': 'back',
        '<forward>': 'forward',
        # Cookies enable etc
        'tuc': 'config-cycle -p -u {url} content.cookies.accept all no-3rdparty never ;; reload',
        'tui': 'config-cycle -p -u {url} content.images ;; reload',
        'tup': 'config-cycle -p -u {url} content.plugins ;; reload',
        'tus': 'config-cycle -p -u {url} content.javascript.enabled ;; reload',
        # Yank
        'yd': 'yank domain',
        'yp': 'yank pretty-url',
        'yt': 'yank title',
        'yy': 'yank',
        'Yd': 'yank domain -s',
        'Yp': 'yank pretty-url -s',
        'Yt': 'yank title -s',
        'Yy': 'yank -s',
        # Other tab shortcuts
        'H': 'tab-prev',
        'L': 'tab-next',
        'S': 'set-cmd-text -s :tab-focus',
        'tf': 'tab-focus',
        'tm': 'tab-move',
        'tcb': 'tab-clone -b',
        'tcw': 'tab-clone -w',
        'tp': 'tab-pin',
        'tg': 'tab-give',
        'tj': 'tab-move +',
        'tk': 'tab-move -',
        # Normal shortcuts
        #   new
        '<Ctrl-m>': 'tab-mute',
        '<Ctrl-Alt-p>': 'print',
        '<Ctrl-Tab>': 'tab-focus last',
        '<Ctrl-Shift-F>': 'fullscreen',
        #   original
        '<Ctrl-t>': 'open -t',
        '<Ctrl-w>': 'tab-close',
        '<Ctrl-n>': 'open -w',
        '<Ctrl-Shift-n>': 'open -p',
        '<F11>': 'fullscreen',
        # Searching and Selection
        'n': 'search-next',
        'N': 'search-prev',
        '<Ctrl-Return>': 'selection-follow -t',
        '<Return>': 'follow-selected',
        # Scrolling
        'h': 'scroll left',
        'j': 'scroll down',
        'k': 'scroll up',
        'l': 'scroll right',
        '<Ctrl-D>': 'scroll-page 0 0.5',
        '<Ctrl-U>': 'scroll-page 0 -0.5',
        '<Ctrl-F>': 'scroll-page 0 1',
        '<Ctrl-B>': 'scroll-page 0 -1',
        'gg': 'scroll-to-perc 0',
        'G': 'scroll-to-perc',
        # Other vim-related shortcuts
        'q': 'macro-record',
        '@': 'macro-run',
        '`': 'set-mark',
        "'": 'jump-mark',
        '<Escape>': 'clear-keychain ;; search ;; fullscreen --leave',
        'ZQ': 'quit',
        'ZZ': 'quit --save',
        # Downloads
        'dd': 'download',
        'dc': 'download-clear',
        'ds': 'download-cancel',
        'dD': 'download-delete',  # Delete the download from the disk
        'do': 'download-open',
        'dv': 'download-open alacritty -e nvim {}',
        'dz': 'download-open zathura {}',
        'dr': 'download-retry',
        # History, bookmarks, etc.
        'sh': 'history -t',
        'sB': 'open -t qute://bookmarks',
        'Ba': 'bookmark-add',
        'Bd': 'bookmark-del',
        'Bo': 'set-cmd-text -s :bookmark-load',
        'BO': 'set-cmd-text -s :bookmark-load -t',
        'Bb': 'set-cmd-text -s :bookmark-load -b',
        'Bw': 'set-cmd-text -s :bookmark-load -w',
        'BW': 'set-cmd-text -s :bookmark-load -p',
        'ea': 'quickmark-add',
        'ed': 'quickmark-del',
        'es': 'quickmark-save',
        'eo': 'set-cmd-text -s :quickmark-load',
        'eO': 'set-cmd-text -s :quickmark-load -t',
        'eb': 'set-cmd-text -s :quickmark-load -b',
        'ew': 'set-cmd-text -s :quickmark-load -w',
        'eW': 'set-cmd-text -s :quickmark-load -p',
        # Navigate (next page)
        '<Ctrl-X>': 'navigate decrement',
        '[[': 'navigate prev',
        ']]': 'navigate next',
        '{{': 'navigate prev -t',
        '}}': 'navigate next -t',
        # Devtools (Inspector)
        ',i': 'devtools',
        ',h': 'devtools left',
        ',j': 'devtools bottom',
        ',k': 'devtools top',
        ',l': 'devtools right',
        ',w': 'devtools window',
        # Other
        'sf': 'save',
        'ss': 'view-source',
        'sv': 'set',
        '<Ctrl-V>': 'hint inputs --first ;; insert-text {clipboard}',
        '<Ctrl-Shift-E>': 'config-edit',
    },
    'hint': {
        '<Ctrl-B>': 'hint all tab-bg',
        '<Ctrl-F>': 'hint links',
        '<Ctrl-R>': 'hint --rapid links tab-bg',
        '<Return>': 'hint-follow',
        '<Escape>': 'mode-leave',
    },
    'caret': {
        # movements
        '$': 'move-to-end-of-line',
        '0': 'move-to-start-of-line',
        'gg': 'move-to-start-of-document',
        'G': 'move-to-end-of-document',
        'H': 'scroll left',
        'J': 'scroll down',
        'K': 'scroll up',
        'L': 'scroll right',
        'h': 'move-to-prev-char',
        'j': 'move-to-next-line',
        'k': 'move-to-prev-line',
        'l': 'move-to-next-char',
        '{': 'move-to-end-of-prev-block',
        '}': 'move-to-end-of-next-block',
        '[': 'move-to-start-of-prev-block',
        ']': 'move-to-start-of-next-block',
        'b': 'move-to-prev-word',
        'e': 'move-to-end-of-word',
        'w': 'move-to-next-word',
        # other mode
        'V': 'selection-toggle --line',
        'c': 'mode-enter normal',
        '<Escape>': 'mode-leave',
        # selection
        'o': 'reverse-selection',
        'v': 'toggle-selection',
        '<Shift-Space>': 'drop-selection',
        '<Space>': 'toggle-selection',
        # yank
        '<Return>': 'yank selection',
        '<Shift-Return>': 'yank selection --sel',
        'y': 'yank selection',
        'Y': 'yank selection -s',
    },
    'command': {
        '<Ctrl-B>':         'rl-backward-word',
        '<Ctrl-W>':         'rl-forward-word',
        '<Ctrl-E>':         'rl-end-of-word',
        '<Ctrl-Shift-B>':   'rl-unix-word-rubout',
        '<Ctrl-Shift-W>':   'rl-kill-word',
        '<Ctrl-Shift-K>':   'rl-kill-line',
        '<Ctrl-U>':         'rl-unix-line-discard',
        '<Ctrl-Backspace>': 'rl-backward-kill-word',
        '<Ctrl-0>':         'rl-beginning-of-line',
        '<Ctrl-$>':         'rl-end-of-line',
        '<Ctrl-H>':         'rl-backward-char',
        '<Ctrl-L>':         'rl-forward-char',
        '<Ctrl-?>':         'rl-delete-char',
        '<Backspace>':      'rl-backward-delete-char',
        '<Ctrl-Y>':         'rl-yank',
        '<Ctrl-C>':         'completion-item-yank',
        '<Ctrl-Shift-C>':   'completion-item-yank --sel',
        '<Tab>':            'completion-item-focus next',
        '<Shift-Tab>':      'completion-item-focus prev',
        '<Ctrl-J>':         'completion-item-focus next',
        '<Ctrl-K>':         'completion-item-focus prev',
        '<Down>':           'completion-item-focus --history next',
        '<Up>':             'completion-item-focus --history prev',
        '<Ctrl-N>':         'command-history-next',
        '<Ctrl-P>':         'command-history-prev',
        '<Return>':         'command-accept',
        '<Shift-Return>':   'command-accept --rapid',
        '<Escape>':         'mode-leave',
    },
    'insert': {
        '<Ctrl-W>':       'tab-close',
        '<Ctrl-P>':       'insert-text {primary}',
        '<Ctrl-M>':       'tab-mute',
        '<Ctrl-Tab>':     'tab-focus last',
        '<Ctrl-T>':       'open -t',
        '<Ctrl-N>':       'open -w',
        '<Ctrl-Shift-N>': 'open -p',
        '<Ctrl-Shift-F>': 'fullscreen',
        '<F11>':          'fullscreen',
        '<Escape>':       'mode-leave',
    },
    'passthrough': {
        '<Escape>': 'mode-leave',
    },
    'prompt': {
        '<Ctrl-B>':         'rl-backward-word',
        '<Ctrl-W>':         'rl-forward-word',
        '<Ctrl-E>':         'rl-end-of-word',
        '<Ctrl-Shift-B>':   'rl-unix-word-rubout',
        '<Ctrl-Shift-W>':   'rl-kill-word',
        '<Ctrl-Shift-K>':   'rl-kill-line',
        '<Ctrl-U>':         'rl-unix-line-discard',
        '<Ctrl-Backspace>': 'rl-backward-kill-word',
        '<Ctrl-0>':         'rl-beginning-of-line',
        '<Ctrl-4>':         'rl-end-of-line',
        '<Ctrl-H>':         'rl-backward-char',
        '<Ctrl-L>':         'rl-forward-char',
        '<Ctrl-?>':         'rl-delete-char',
        '<Backspace>':      'rl-backward-delete-char',
        # '<Ctrl-Y>':         'rl-yank',
        '<Ctrl-Shift-Y>':   'prompt-yank --sel',
        '<Ctrl-Y>':         'prompt-yank',
        '<Ctrl-P>':         'prompt-open-download --pdfjs',
        '<Ctrl-X>':         'prompt-open-download',
        '<Return>':         'prompt-accept',
        '<Tab>':            'prompt-item-focus next',
        '<Shift-Tab>':      'prompt-item-focus prev',
        '<Ctrl-K>':         'prompt-item-focus next',
        '<Ctrl-J>':         'prompt-item-focus prev',
        '<Down>':           'prompt-item-focus next',
        '<Up>':             'prompt-item-focus prev',
        '<Escape>':         'mode-leave',
    },
    'yesno': {
        '<Ctrl-Y>': 'prompt-yank',
        '<Ctrl-Shift-Y>': 'prompt-yank --sel',
        '<Return>': 'prompt-accept',
        'N': 'prompt-accept --save no',
        'Y': 'prompt-accept --save yes',
        'n': 'prompt-accept no',
        'y': 'prompt-accept yes',
        '<Escape>': 'mode-leave',
    }
}

c.aliases = {
        'w':  'session-save',
        'wq': 'quit --save',
        # 'light': 'set content.user_stylesheets user_light.css',
        # 'dark':  'set content.user_stylesheets user_dark.css',
}


#########################
# Completion menu
#########################
c.completion.cmd_history_max_items = -1  # unlimited
c.completion.delay = 0  # Delay after pressing key
# The height of the completion, in px or as percentage of the window.
c.completion.height = '40%'
c.completion.quick = True

c.completion.show = 'always'
c.completion.timestamp_format = '%Y-%m-%d %H:%M'


#########################
# Content, Downloads, Editor and Filesection
#########################
c.confirm_quit = ['downloads']
c.content.fullscreen.window = True
c.content.javascript.can_open_tabs_automatically = True
c.content.proxy = 'none'
# c.content.user_stylesheets = ['user_dark.css']  # This is a list, so you can add more

c.downloads.location.directory = '/home/joris/downloads/'
c.downloads.location.prompt = True
c.downloads.location.remember = True
c.downloads.location.suggestion = 'path'
c.downloads.position = 'bottom'
c.downloads.remove_finished = -1  # milliseconds

c.editor.command = ['alacritty', '-e', 'nvim', '{file}']


#########################
# Fonts, Hints, Input and Keyhints
#########################
c.fonts.default_family = 'Dejavu Sans'
c.fonts.default_size = '10pt'
c.fonts.statusbar = '9pt Dejavu Sans'

c.hints.chars = "asdfghjkl"

c.input.insert_mode.auto_load = True
c.input.insert_mode.leave_on_load = True

c.keyhint.delay = 0  # default 500 milliseconds


#########################
# Messages, Opening tabs, Prompts, Scrollbar and Searching
#########################
c.messages.timeout = 6000  # milliseconds

c.new_instance_open_target = 'tab-silent'
c.new_instance_open_target_window = 'last-focused'

c.prompt.filebrowser = True
c.prompt.radius = 8

c.scrolling.bar = 'always'
c.scrolling.smooth = False

c.search.ignore_case = 'smart'
c.search.wrap = True

#########################
# Sessions, spellcheck and statusbar
#########################
c.session.lazy_restore = True
c.spellcheck.languages = ['en-US', 'en-GB', 'de-DE', 'nl-NL']
c.statusbar.padding = {
        'bottom': 1,
        'left': 1,
        'right': 3,
        'top': 1,
}
c.statusbar.position = 'bottom'
c.statusbar.show = 'always'
c.statusbar.widgets = ['url', 'keypress', 'progress', 'tabs', 'history', 'scroll']


#########################
# Tabs
#########################
c.tabs.background = True
c.tabs.close_mouse_button = 'right'  # close tabs with right button
c.tabs.favicons.scale = 0.9
c.tabs.favicons.show = 'always'
c.tabs.indicator.padding = {
        'bottom': 1,
        'left': 2,
        'right': 4,
        'top': 2,
}
c.tabs.indicator.width = 4
c.tabs.last_close = 'default-page'
c.tabs.max_width = -1
c.tabs.min_width = -1
c.tabs.mode_on_change = 'normal'
c.tabs.mousewheel_switching = True
c.tabs.new_position.related = 'next'
c.tabs.new_position.stacking = True
c.tabs.new_position.unrelated = 'last'
c.tabs.padding = {
    "left": 0,
    "right": 8,
    "top": 0,
    "bottom": 0,
}
c.tabs.pinned.frozen = True
c.tabs.pinned.shrink = True
c.tabs.position = 'top'  # left is also quite nice
c.tabs.select_on_remove = 'last-used'
c.tabs.show = 'always'
c.tabs.show_switching_delay = 500  # milliseconds
c.tabs.tabs_are_windows = False
c.tabs.title.alignment = 'center'
c.tabs.title.format = '{audio}{private}{index}: {current_title}'
c.tabs.tooltips = True
c.tabs.undo_stack_size = 100
c.tabs.wrap = True


#########################
# URL, Window, Zoom
#########################
c.url.auto_search = 'naive'
c.url.default_page = 'https://www.google.com/'
c.url.open_base_url = False
c.url.searchengines = {'DEFAULT': "https://www.google.com/search?q={}"}
c.url.start_pages = 'https://www.google.com/'

c.window.hide_decoration = False
c.window.title_format = "{private}{perc}{current_title}{title_sep}qutebrowser"


#########################
# Colors
#########################

## Colors of completion (when hitting Tab after typing `:`)
# Category (top where the word Commands is)
c.colors.completion.category.bg            = ('qlineargradient(x1:0, y1:0, x2:0, y2:1,'
                                                              'stop:0 #666666,'
                                                              'stop:1 #000000)')
c.colors.completion.category.fg            = '#ffffff'
c.colors.completion.category.border.bottom = '#000000'
c.colors.completion.category.border.top    = '#666666'
# Even/odd row background colors
c.colors.completion.even.bg      = '#333333'
c.colors.completion.odd.bg       = '#444444'
# On the right is a scrollbar, bg and fg color
c.colors.completion.scrollbar.bg = '#333333'
c.colors.completion.scrollbar.fg = '#bbbbbb'
# Text color of all the columns
c.colors.completion.fg           = ['#ffffff', '#ffffff', '#ffffff']
# Selected row colors
c.colors.completion.item.selected.bg            = '#a6caf0'
c.colors.completion.item.selected.fg            = '#000000'
c.colors.completion.item.selected.border.bottom = '#333333'
c.colors.completion.item.selected.border.top    = '#333333'
# Color of matched part in and out of selected item
c.colors.completion.item.selected.match.fg = '#dd00dd'
c.colors.completion.match.fg               = '#33ff33'

## Colors of context menu (right-click)
c.colors.contextmenu.disabled.bg = '#ffffff'  # none
c.colors.contextmenu.disabled.fg = '#aaaaaa'
# c.colors.contextmenu.menu.bg     = '#ffffff'  # default is better
c.colors.contextmenu.menu.fg     = '#000000'
c.colors.contextmenu.selected.bg = '#aaaaaa'
c.colors.contextmenu.selected.fg = '#000000'

## Colors of donwloads
c.colors.downloads.bar.bg        = '#000000'
c.colors.downloads.error.bg      = '#ff0000'
c.colors.downloads.error.fg      = '#ffffff'
c.colors.downloads.start.bg      = '#0000aa'
c.colors.downloads.start.fg      = '#ffffff'
c.colors.downloads.stop.bg       = '#00aa00'
c.colors.downloads.stop.fg       = '#ffffff'
c.colors.downloads.system.bg     = 'rgb'
c.colors.downloads.system.fg     = 'rgb'

## Colors of hints (when typing `f`)
c.colors.hints.bg = ('qlineargradient(x1:0, y1:0, x2:0, y2:1,'
                                     'stop:0 rgba(255, 247, 133, 0.8),'
                                     'stop:1 rgba(255, 197, 66, 0.8))')
c.colors.hints.fg = '#000000'
c.colors.hints.match.fg = '#00cc00'

## Colors of keyhints (little menu that opens if you hit for example `h`)
c.colors.keyhint.bg = 'rgba(0, 0, 0, 0.7)'
c.colors.keyhint.fg = '#ffffff'
c.colors.keyhint.suffix.fg = c.colors.completion.match.fg

## Colors of messages (I like the default but here are the options)
# c.colors.messages.error.bg       = 'red'
# c.colors.messages.error.border   = '#bb0000'
# c.colors.messages.error.fg       = 'white'
# c.colors.messages.info.bg        = 'black'
# c.colors.messages.info.border    = '#333333'
# c.colors.messages.info.fg        = 'white'
# c.colors.messages.warning.bg     = 'darkorange'
# c.colors.messages.warning.border = '#d47300'
# c.colors.messages.warning.fg     = 'black'

## Colors of prompts (again, I prefer the default)
# c.colors.prompts.border      = '1px solid gray'
# c.colors.prompts.fg          = 'white'
# c.colors.prompts.selected.bg = 'grey'

## Colors of the statusbar in different modes (bottom bar)
# (based on the vim colors)
c.colors.statusbar.caret.bg             = '#f2c68a'  # selection mode
c.colors.statusbar.caret.fg             = '#444444'
c.colors.statusbar.caret.selection.bg   = '#ff66ff'  # when you select in selection mode
c.colors.statusbar.caret.selection.fg   = '#444444'
c.colors.statusbar.insert.bg            = '#95e454'  # insert mode
c.colors.statusbar.insert.fg            = '#444444'
c.colors.statusbar.command.bg           = '#242424'  # command mode
c.colors.statusbar.command.fg           = '#ffffff'
c.colors.statusbar.command.private.bg   = '#000000'  # incognito mode
c.colors.statusbar.command.private.bg   = '#ffffff'
c.colors.statusbar.normal.bg            = '#242424'  # normal mode
c.colors.statusbar.normal.fg            = '#ffffff'
c.colors.statusbar.passthrough.bg       = '#e5786d'  # passthrough mode for sending keys to webpages
c.colors.statusbar.passthrough.fg       = '#444444'
c.colors.statusbar.private.bg           = '#000000'  # incognito mode
c.colors.statusbar.private.fg           = '#ffffff'
c.colors.statusbar.progress.bg          = '#ffffff'  # little progress bar bottom right
# url in statusbar (most are default)
c.colors.statusbar.url.error.fg         = 'orange'
c.colors.statusbar.url.fg               = 'white'
c.colors.statusbar.url.hover.fg         = 'aqua'
c.colors.statusbar.url.success.http.fg  = 'white'
c.colors.statusbar.url.success.https.fg = 'lime'
c.colors.statusbar.url.warn.fg          = 'yellow'

## Colors of different tabs (top bar) (most are default)
c.colors.tabs.bar.bg                    = '#555555'
c.colors.tabs.even.bg                   = 'darkgrey'
c.colors.tabs.even.fg                   = 'white'
c.colors.tabs.odd.bg                    = 'grey'
c.colors.tabs.odd.fg                    = 'white'
c.colors.tabs.selected.even.bg          = 'black'
c.colors.tabs.selected.even.fg          = 'white'
c.colors.tabs.selected.odd.bg           = 'black'
c.colors.tabs.selected.odd.fg           = 'white'
c.colors.tabs.pinned.even.bg            = 'darkseagreen'
c.colors.tabs.pinned.even.fg            = 'white'
c.colors.tabs.pinned.odd.bg             = 'seagreen'
c.colors.tabs.pinned.odd.fg             = 'white'
c.colors.tabs.pinned.selected.even.bg   = 'black'
c.colors.tabs.pinned.selected.even.fg   = 'white'
c.colors.tabs.pinned.selected.odd.bg    = 'black'
c.colors.tabs.pinned.selected.odd.fg    = 'white'
c.colors.tabs.indicator.error           = '#ff0000'
c.colors.tabs.indicator.start           = '#0000aa'
c.colors.tabs.indicator.stop            = '#00aa00'
c.colors.tabs.indicator.system          = 'rgb'

## Dark mode
c.colors.webpage.darkmode.algorithm      = 'lightness-hsl'
c.colors.webpage.darkmode.contrast       = -0.025
# c.colors.webpage.darkmode.enabled        = True
c.colors.webpage.darkmode.enabled        = False
c.colors.webpage.darkmode.grayscale.all  = False
c.colors.webpage.darkmode.grayscale.images = 0.0
c.colors.webpage.darkmode.policy.images  = 'smart'
c.colors.webpage.darkmode.policy.page    = 'smart'
c.colors.webpage.darkmode.threshold.text = 150
c.colors.webpage.darkmode.threshold.background = 205
