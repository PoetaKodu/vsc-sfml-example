-- This is configuration file for build environment generation.
-- 
-- To properly configure build:
--  1) Copy BuildConfig.template.lua to new file and name it BuildConfig.user.lua
--  2) Fill in essential information
-- Use Lua syntax.

userConfig = {

	-- Dependencies configuration:
	deps = {

		-- [Required]
		-- Please provide path to the root of the SFML library.
		sfml = {
			root = "",
			dynamic = true
			-- # Uncomment this if you use pre 2.5.0 version of SFML.
			-- # Remember to add a colon after the line above.
			-- pre250Version = true
		}
	}
}