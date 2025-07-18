-- AstroCommunity: import any community modules here
-- We import this file in `lazy_setup.lua` before the `plugins/` folder.
-- This guarantees that the specs are processed before any user plugins.

---@type LazySpec
return {
  "AstroNvim/astrocommunity",
  { import = "astrocommunity.pack.lua" },

  "AstroNvim/astrocommunity",
  { import = "astrocommunity.colorscheme.onedarkpro-nvim" },

  "AstroNvim/astrocommunity",
  { import = "astrocommunity.pack.python" },

  "AstroNvim/astrocommunity",
  { import = "astrocommunity.pack.typescript" },

  "AstroNvim/astrocommunity",
  { import = "astrocommunity.pack.astro" },

  "AstroNvim/astrocommunity",
  { import = "astrocommunity.pack.tailwindcss" },

  "AstroNvim/astrocommunity",
  { import = "astrocommunity.pack.cpp" },
  -- ... import any community contributed plugins here
}
