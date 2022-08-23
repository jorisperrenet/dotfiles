""""""""""""""""""""""""""""""
" => Load pathogen paths
""""""""""""""""""""""""""""""
" Use pathogen to manage vim runtimepath to install plugins and runtime
" files in their own private directories.

" Set the path to the vim_configs directory relatively from the current
" directory. The '<sfile>:p:h' gets the folder in which this script is
" located.
let s:vim_configs = expand('<sfile>:p:h')."/.."

" Make the expansion occur in the plugins directory.
call pathogen#infect(s:vim_configs.'/plugins/{}')

" Generate documentation of the plugins by invoking the :Helptags command.
call pathogen#helptags()


""""""""""""""""""""""""""""""
" => vim-plug
""""""""""""""""""""""""""""""
let s:plugins_path=$XDG_CONFIG_HOME.'/nvim/plugins'
call plug#begin(fnameescape(s:plugins_path))

" Additional Plugins
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

" Colors
Plug 'sainnhe/sonokai'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'nvim-treesitter/playground'
Plug 'itchyny/lightline.vim'

" vimwiki
" Plug 'vimwiki/vimwiki'

" Latex writing
Plug 'lervag/vimtex'

" Jumping around
Plug 'easymotion/vim-easymotion'

" Commenting
Plug 'tpope/vim-commentary'

Plug 'lewis6991/gitsigns.nvim'

Plug 'ray-x/lsp_signature.nvim'
Plug 'L3MON4D3/luasnip'
Plug 'saadparwaiz1/cmp_luasnip'
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'neovim/nvim-lspconfig'

Plug 'windwp/nvim-autopairs'

Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-cmdline'

Plug 'mattn/emmet-vim'

" All of your Plugins must be added before the following line
call plug#end()
