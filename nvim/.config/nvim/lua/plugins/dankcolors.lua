return {
	{
		"RRethy/base16-nvim",
		priority = 1000,
		config = function()
			require('base16-colorscheme').setup({
				base00 = '#121315',
				base01 = '#121315',
				base02 = '#888d93',
				base03 = '#888d93',
				base04 = '#e0e6ee',
				base05 = '#f8fbff',
				base06 = '#f8fbff',
				base07 = '#f8fbff',
				base08 = '#ff9fbb',
				base09 = '#ff9fbb',
				base0A = '#cce1f9',
				base0B = '#a5ffb1',
				base0C = '#e6f1ff',
				base0D = '#cce1f9',
				base0E = '#d9eaff',
				base0F = '#d9eaff',
			})

			vim.api.nvim_set_hl(0, 'Visual', {
				bg = '#888d93',
				fg = '#f8fbff',
				bold = true
			})
			vim.api.nvim_set_hl(0, 'Statusline', {
				bg = '#cce1f9',
				fg = '#121315',
			})
			vim.api.nvim_set_hl(0, 'LineNr', { fg = '#888d93' })
			vim.api.nvim_set_hl(0, 'CursorLineNr', { fg = '#e6f1ff', bold = true })

			vim.api.nvim_set_hl(0, 'Statement', {
				fg = '#d9eaff',
				bold = true
			})
			vim.api.nvim_set_hl(0, 'Keyword', { link = 'Statement' })
			vim.api.nvim_set_hl(0, 'Repeat', { link = 'Statement' })
			vim.api.nvim_set_hl(0, 'Conditional', { link = 'Statement' })

			vim.api.nvim_set_hl(0, 'Function', {
				fg = '#cce1f9',
				bold = true
			})
			vim.api.nvim_set_hl(0, 'Macro', {
				fg = '#cce1f9',
				italic = true
			})
			vim.api.nvim_set_hl(0, '@function.macro', { link = 'Macro' })

			vim.api.nvim_set_hl(0, 'Type', {
				fg = '#e6f1ff',
				bold = true,
				italic = true
			})
			vim.api.nvim_set_hl(0, 'Structure', { link = 'Type' })

			vim.api.nvim_set_hl(0, 'String', {
				fg = '#a5ffb1',
				italic = true
			})

			vim.api.nvim_set_hl(0, 'Operator', { fg = '#e0e6ee' })
			vim.api.nvim_set_hl(0, 'Delimiter', { fg = '#e0e6ee' })
			vim.api.nvim_set_hl(0, '@punctuation.bracket', { link = 'Delimiter' })
			vim.api.nvim_set_hl(0, '@punctuation.delimiter', { link = 'Delimiter' })

			vim.api.nvim_set_hl(0, 'Comment', {
				fg = '#888d93',
				italic = true
			})

			local current_file_path = vim.fn.stdpath("config") .. "/lua/plugins/dankcolors.lua"
			if not _G._matugen_theme_watcher then
				local uv = vim.uv or vim.loop
				_G._matugen_theme_watcher = uv.new_fs_event()
				_G._matugen_theme_watcher:start(current_file_path, {}, vim.schedule_wrap(function()
					local new_spec = dofile(current_file_path)
					if new_spec and new_spec[1] and new_spec[1].config then
						new_spec[1].config()
						print("Theme reload")
					end
				end))
			end
		end
	}
}
