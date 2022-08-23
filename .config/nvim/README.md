# Vim Dotfiles
Here you will find an up-to-date version of my vim-dotfiles.

In case things are not running as expected inside Nvim, run `:checkhealth`.

# Included Plugins
The following plugins will automatically be setup when cloning this repo
* [Pathogen](https://github.com/tpope/vim-pathogen): Manage vim runtimepath. Install plugins and runtime files in their own private directories.
* [peaksea](https://github.com/vim-scripts/peaksea): color scheme.
This will install the following plugins for you
* [lightline](https://github.com/itchyny/lightline.vim): a light and configurable statusline/tabline plugin for Vim. I use it to style my statusline and tabline as well as determine what should be displayed on them.


## Custom mappings inside the vimrcs (exluding the plugins)
General
* `<leader>w` save file
* `:W` sudo save file
* `<leader>e` open and edit test_configs.vim
* `<leader><cr>` disable highlight
* `<leader>q` quickly opens a new buffer for scribble

* `<leader>pp` toggle paste mode on and off
* `<leader>cf` copy file content to clipboard
* `<leader>g` generates a tag file in the currently active virtual environment
* `<C-\>` opens the definition (using ctags) in vertical split
* `<leader>c` to toggle cursorline

Window movement, tab management and buffers
* `<C-j>` to go down a window, similarly for left, up and right
* `<leader>te` to open a new tab with the current buffer's path. Great when editing files in the same directory
* `<leader>cd` switch CWD to the directory of the open buffer
* `<leader>l` go to the previous buffer
* `<leader>h` go to the next buffer

Text alteration
* `<leader>ss` toggle and untoggle spell checking
* `<leader>sn` go to next misspelled word
* `<leader>sp` go to previous misspelled word
* `<leader>sa` add misspelled word to dictionary
* `<leader>sf` fix misspelled word by listing suggestions

Visual mode
* Pressing `*` or `#` searches for the current selection
* `<leader>y` yanks the selection to clipboard

Normal mode
* `<leader>j` go to any word on screen (uses easymotion)


What I did

# have init.vim
# have vimrcs/... (where ... is the thing that you source in init.vim)


# to get pathogen
curl -LSso autoload/pathogen.vim https://tpo.pe/pathogen.vim
# to get vim-plug
curl -fLo autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
### Now autoload is where it should be, plugins is initiated when :PlugInstall
### is executed (vim-plug).

### add plugin nvim-treesitter and run (e.g. :TSInstall python)
sudo npm i -g pyright
