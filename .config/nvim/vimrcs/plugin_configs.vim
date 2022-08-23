" VIMTEX
" This is necessary for VimTeX to load properly. The "indent" is optional.
" Note that most plugin managers will do this automatically.
filetype plugin indent on

" This enables Vim's and neovim's syntax-related features. Without this, some
" VimTeX features will not work (see ":help vimtex-requirements" for more
" info).
syntax enable

" Viewer options: One may configure the viewer either by specifying a built-in
" viewer method:
let g:vimtex_view_method = 'zathura'

" VimTeX uses latexmk as the default compiler backend. If you use it, which is
" strongly recommended, you probably don't need to configure anything. If you
" want another compiler backend, you can change it as follows. The list of
" supported backends and further explanation is provided in the documentation,
" see ":help vimtex-compiler".

let g:vimtex_compiler_method = 'latexmk'
" let g:vimtex_compiler_method = 'xelatex'

" Most VimTeX mappings rely on localleader and this can be changed with the
" following line. The default is usually fine and is the symbol "\".
let maplocalleader = " "







""""""""""""""""""""""""""""""
" => Colorscheme and Fonts
""""""""""""""""""""""""""""""
set termguicolors


let g:sonokai_style = 'andromeda'
let g:sonokai_enable_italic = 1
let g:sonokai_disable_italic_comment = 1
let g:sonokai_transparent_background = 1

colorscheme sonokai

lua <<EOF
require'nvim-treesitter.configs'.setup {
  ensure_installed = "maintained",
  highlight = {
    enable = true,
  }
}
EOF



" OMG, without this the signcolumn is displayed as DarkGreen
" ... so ugly
highlight SignColumn ctermfg=none ctermbg=none


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => lightline
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:lightline = {
      \ 'colorscheme': 'wombat',
      \ 'active': {
      \   'left': [ ['mode', 'paste'],
      \             ['readonly', 'relativepath'],
      \             ['modified', 'fugitive'] ],
      \   'right': [ [ 'lineinfo' ],
      \              ['percent'],
      \              ['fileencoding', 'filetype'] ]
      \ },
      \ 'component': {
      \   'readonly': '%{&filetype=="help"?"":&readonly?"🔒":""}',
      \   'modified': '%{&filetype=="help"?"":&modified?"+":&modifiable?"":"-"}',
      \   'fugitive': '%{exists("*fugitive#head")?fugitive#head():""}'
      \ },
      \ 'component_visible_condition': {
      \   'readonly': '(&filetype!="help"&& &readonly)',
      \   'modified': '(&filetype!="help"&&(&modified||!&modifiable))',
      \   'fugitive': '(exists("*fugitive#head") && ""!=fugitive#head())'
      \ },
      \ 'separator': { 'left': ' ', 'right': ' ' },
      \ 'subseparator': { 'left': '|', 'right': ' ' }
      \ }

let g:lightline.tab = {
	\ 'active': [ 'tabnum', 'filename', 'modified' ],
	\ 'inactive': [ 'tabnum', 'filename', 'modified' ] }


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => lsp signature
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lua <<EOF
 cfg = {
  debug = false, -- set to true to enable debug logging
  log_path = vim.fn.stdpath("cache") .. "/lsp_signature.log", -- log dir when debug is on
  -- default is  ~/.cache/nvim/lsp_signature.log
  verbose = false, -- show debug line number

  bind = true, -- This is mandatory, otherwise border config won't get registered.
               -- If you want to hook lspsaga or other signature handler, pls set to false
  doc_lines = 100, -- will show two lines of comment/doc(if there are more than two lines in doc, will be truncated);
                 -- set to 0 if you DO NOT want any API comments be shown
                 -- This setting only take effect in insert mode, it does not affect signature help in normal
                 -- mode, 10 by default

  floating_window = true, -- show hint in a floating window, set to false for virtual text only mode

  floating_window_above_cur_line = true, -- try to place the floating above the current line when possible Note:
  -- will set to true when fully tested, set to false will use whichever side has more space
  -- this setting will be helpful if you do not want the PUM and floating win overlap

  floating_window_off_x = 20, -- adjust float windows x position.
  floating_window_off_y = 20, -- adjust float windows y position.


  fix_pos = false,  -- set to true, the floating window will not auto-close until finish all parameters
  hint_enable = true, -- virtual hint enable
  hint_prefix = "🐼 ",  -- Panda for parameter
  hint_scheme = "String",
  hi_parameter = "LspSignatureActiveParameter", -- how your parameter will be highlight
  max_height = 5, -- max height of signature floating_window, if content is more than max_height, you can scroll down
                   -- to view the hiding contents
  max_width = 80, -- max_width of signature floating_window, line will be wrapped if exceed max_width
  handler_opts = {
    border = "rounded"   -- double, rounded, single, shadow, none
  },

  always_trigger = false, -- sometime show signature on new line or in middle of parameter can be confusing, set it to false for #58

  auto_close_after = nil, -- autoclose signature float win after x sec, disabled if nil.
  extra_trigger_chars = {"(", ","}, -- Array of extra characters that will trigger signature completion, e.g., {"(", ","}
  zindex = 200, -- by default it will be on top of all floating windows, set to <= 50 send it to bottom

  padding = '', -- character to pad on left and right of signature can be ' ', or '|'  etc

  transparency = nil, -- disabled by default, allow floating win transparent value 1~100
  shadow_blend = 36, -- if you using shadow as border use this set the opacity
  shadow_guibg = 'Black', -- if you using shadow as border use this set the color e.g. 'Green' or '#121315'
  timer_interval = 200, -- default timer check interval set to lower value if you want to reduce latency
  toggle_key = '<C-Space>' -- toggle signature on and off in insert mode,  e.g. toggle_key = '<M-x>'
}

-- recommended:
require'lsp_signature'.setup(cfg)
EOF


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => autopairs
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
lua <<EOF
    local npairs = require('nvim-autopairs')
    npairs.setup{}

    -- put this to setup function and press <a-e> to use fast_wrap
    npairs.setup({
        fast_wrap = {},
    })

    -- change default fast_wrap
    npairs.setup({
        fast_wrap = {
          map = '<C-p>',
          chars = { '{', '[', '(', '"', "'" },
          pattern = string.gsub([[ [%'%"%)%>%]%)%}%,] ]], '%s+', ''),
          offset = 0, -- Offset from pattern match
          end_key = 'l',
          keys = 'qwertyuiopzxcvbnmasdfghjk',
          check_comma = true,
          highlight = 'Search',
          highlight_grey='Comment'
        },
    })


    local disable_filetype = { "TelescopePrompt" }
    local disable_in_macro = false  -- disable when recording or executing a macro
    local disable_in_visualblock = false -- disable when insert after visual block mode
    local ignored_next_char = string.gsub([[ [%w%%%'%[%"%.] ]],"%s+", "")
    local enable_moveright = true
    local enable_afterquote = true  -- add bracket pairs after quote
    local enable_check_bracket_line = true  --- check bracket in same line
    local check_ts = false
    local map_bs = true  -- map the <BS> key
    local map_c_h = false  -- Map the <C-h> key to delete a pair
    local map_c_w = false -- map <c-w> to delete a pair if possible

    -- If you want insert `(` after select function or method item
    local cmp_autopairs = require('nvim-autopairs.completion.cmp')
    local cmp = require('cmp')
    cmp.event:on( 'confirm_done', cmp_autopairs.on_confirm_done({  map_char = { tex = '' } }))


    -- add a lisp filetype (wrap my-function), FYI: Hardcoded = { "clojure", "clojurescript", "fennel", "janet" }
    cmp_autopairs.lisp[#cmp_autopairs.lisp+1] = "racket"
EOF


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => lspconfig
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set completeopt+=menuone

lua <<EOF
    local lspconfig = require('lspconfig')

    -- Enable some language servers with the additional completion capabilities offered by nvim-cmp
    local servers = { 'clangd', 'rust_analyzer', 'tsserver', 'pylsp' }
    for _, lsp in ipairs(servers) do
      lspconfig[lsp].setup {
        -- on_attach = my_custom_on_attach,
        capabilities = capabilities,
      }
    end

    -- luasnip setup
    local luasnip = require 'luasnip'

    -- nvim-cmp setup
    local cmp = require 'cmp'
    cmp.setup {
      snippet = {
        expand = function(args)
          require('luasnip').lsp_expand(args.body)
        end,
      },
      mapping = {
        ['<C-p>'] = cmp.mapping.select_prev_item(),
        ['<C-n>'] = cmp.mapping.select_next_item(),
        ['<C-d>'] = cmp.mapping.scroll_docs(-4),
        ['<C-f>'] = cmp.mapping.scroll_docs(4),
        ['<C-e>'] = cmp.mapping.complete(),
        ['<C-Space>'] = cmp.mapping.close(),
        ['<CR>'] = cmp.mapping.confirm {
          behavior = cmp.ConfirmBehavior.Replace,
          select = true,
        },
        ['<Tab>'] = function(fallback)
          if cmp.visible() then
            cmp.select_next_item()
          elseif luasnip.expand_or_jumpable() then
            luasnip.expand_or_jump()
          else
            fallback()
          end
        end,
        ['<S-Tab>'] = function(fallback)
          if cmp.visible() then
            cmp.select_prev_item()
          elseif luasnip.jumpable(-1) then
            luasnip.jump(-1)
          else
            fallback()
          end
        end,
      },
      sources = {
        { name = 'nvim_lsp' },
        { name = 'luasnip' },
      },
    }
EOF
