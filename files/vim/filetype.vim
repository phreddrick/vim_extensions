" my filetype file
if exists("did_load_filetypes")
    finish
endif

autocmd BufNewFile,BufRead *.packer setlocal filetype=json

autocmd BufNewFile,BufRead *.yml setlocal filetype=yaml
autocmd BufNewFile,BufRead *.yaml setlocal filetype=yaml

autocmd BufNewFile,BufRead *.sh setlocal filetype=sh
autocmd BufNewFile,BufRead *.bash setlocal filetype=sh
