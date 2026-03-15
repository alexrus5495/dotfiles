# Tmux Cheat Sheet

## Config

~/.tmux.conf

## Keybinds

Leader key - \<C-space\>

- C _h_ _j_ _k_ _l_ - move around

- " - horizontal split

- % - vertical split

- c - close pane

## Session control

### Create new session

tmux new -s [name]

### Attach session

tmux attach -t [name]

### Kill session

tmux kill-session -t [name]

### Rename session

leader $

## Window management

- c - create new

- , - rename

- n - next

- p - previous

- 0...9 - go to

- & - close

- w - select from list

## Pane control

- " - split horizontal

- % - split vertical

- { or } - move

- ! - turn into new window

- q - show pane numbers

- z - zoom

- x - close

- j k - split up/down

- h l - rotate

## Copying and scrolling

- [ - enter copy mode

- q - quit copy mode

- PgUp/PgDn - scroll

- Space - begin selection

- Enter - copy selection

- ] - paste
