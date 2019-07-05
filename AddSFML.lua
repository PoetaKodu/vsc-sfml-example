addSFML = function(sfmlRootDir, sfmlLibDir, modules, dynamic, debug, pre250Version)

	-- By default, use >= 2.5.0 version.
	pre250Version = pre250Version or false

	local libSuffix = ""
	if not dynamic then
		libSuffix = "-s"
	end
	if debug then
		libSuffix = libSuffix .. "-d"
	end

	-- SFML/include
	includedirs { path.join(sfmlRootDir, "include") }
	libdirs { sfmlLibDir }
	
	-- SFML/lib
	local uses = {
		graphics 	= false,
		window 		= false,
		audio 		= false,
		network 	= false,
		system 		= false
	}
		

	if modules.graphics ~= nil and modules.graphics == true then
		links { "sfml-graphics" .. libSuffix }
		uses.graphics = true
	end
	if modules.window ~= nil and modules.window == true then
		links { "sfml-window" .. libSuffix }
		uses.window = true
	end
	if modules.audio ~= nil and modules.audio == true then
		links { "sfml-audio" .. libSuffix }
		uses.audio = true
	end
	if modules.network ~= nil and modules.network == true then
		links { "sfml-network" .. libSuffix }
		uses.network = true
	end
	if modules.system ~= nil and modules.system == true then
		links { "sfml-system" .. libSuffix }
		uses.system = true
	end
	

	-- Link dependencies:
	if uses.graphics then
		if pre250Version then
			links { "jpeg" }
		end
		links {
			"opengl32",
			"freetype"
		}
	end

	if uses.window then
		links { "opengl32" }
	end

	if uses.audio then
		links {
			"openal32",
			"flac",
			"vorbisenc",
			"vorbisfile",
			"vorbis",
			"ogg"
		}
	end

	-- Link window dependencies
	if os.host() == "windows" then
		if uses.network then
			links { "ws2_32" }
		end
		if uses.system or uses.window then
			links { "winmm" }
		end
		if uses.window then
			links { "gdi32" }
		end
	end
	
end