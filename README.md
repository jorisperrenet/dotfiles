# Dotfiles

> Special thanks to [LukeSmithxyz/voidrice](https://github.com/LukeSmithxyz/voidrice)
> and [yannickperrenet/dotfiles](https://github.com/yannickperrenet/dotfiles)

## Installation
For an installation script, please refer to my
[iscripts](https://github.com/jorisperrenet/iscripts) repository.

After installing the dotfiles use the respective package managers, see the sections below.

To keep the dotfiles up to date simply run:
```bash
# `dfg` is an alias set in this repository to manage this repository as
# a bare git repository.
dfg pull

# Update submodules and automatically initialize newly added submodules.
dfg submodule update --init
```

The prevent git from listing untracked files run:
```bash
dfg config --global status.showUntrackedFiles no
```

### Vim
 My special thanks go out to the [Ultimate Vim configuration](https://github.com/amix/vimrc) by
 amix.

Use [vim-plug](https://github.com/junegunn/vim-plug) to manage packages, run `:PluginInstall` to
install the plugins (once inside Vim).

### i3-gaps
Disable the menubar of the terminal:
1. *Edit* > *Preferences* > *General*
2. Untick the *Show menubar by default in new terminals*
