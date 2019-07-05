# vsc-sfml-example
An example SFML project in C++11 with Premake5 build system, created with VS Code.

## Required things

1. Premake5 (also added to `PATH` environment variable)
2. C++ Compiler (GCC and MSVC configurations are ready to use)
3. SFML 2.0+ (with source) or prebuilt version with binaries.  
**I strongly recommend to build SFML from source code with provided Python ([download](https://www.python.org/downloads/)) script: [Build.py](build_sfml/Build.py).**  
In case you really want to use your prebuilt SFML, **make sure that folder structure is designed this way:**  
`SFML root`  
	`- include`  
	**`- bin`**  
		`--- x64`  
			`------ Debug`  
		`--- (other platforms)`  
			`------ (other configurations)`  
	**`- lib`**  
		`--- x64`  
		`------ Debug`  
		`--- (other platforms)`  
			`------ (other configurations)`  
**You need binaries for platforms and configurations you want to target during compilation.**
Provided [**SFML build script**](build_sfml/Build.py) compiles and organises all platforms and configurations automatically.
1. [**CMake**](https://cmake.org/download/) (only if building SFML from source)

## Configuration

1. Configure `.vscode` folder (see: [**Configuration.md**](.vscode-template/Configuration.md))
2. Configure [**BuildConfig.template.lua**](BuildConfig.template.lua)

## Compilation

After configuration is done, you can easily build this project with [**prepared VS Code tasks**](.vscode-example/tasks.json):
1. Run command box with `Ctrl + Shift + P`
2. Enter `Run build task` and run the command
3. Select Build or Rebuild task, platform and configuration
4. Run your application from `bin/` folder.

## Notes

- You can configure SFML project in [**Project.lua**](Project.lua) file.
- You can configure entire workspace in [**premake5.lua**](premake5.lua) file.
- Remember to put **proper** SFML binaries to the application binary folder, if linking dynamically.  
**[Build.py](`build_sfml/Build.py`) script is not currently capable of building static SFML libraries.**
- Make sure that following files exist and contains your personal configuration before you build:
  - `.vscode/c_cpp_properties.json`
  - `.vscode/tasks.json`
  - `BuildConfig.user.lua`