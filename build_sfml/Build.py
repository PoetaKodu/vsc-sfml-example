####################################
# Notes:
# - Put this file in your root SFML repository folder.
# - Configure variables below.
####################################

####################################
# User configuration:
####################################
build_config = {
	"install_path": "",
	"build_folder": "build",
	"platforms": [ "x86", "x64" ], # Available options: "x86", "x64"
	"configs": [ "Debug", "Release", "RelWithDebInfo", "MinSizeRel" ],
	"folders_to_relocate": [ "lib", "bin" ], # include/ folder will be always relocated

	"compilation": {
		"cmake_generator": "MinGW Makefiles",

		# Build command is executed with working directory set to build_config["folder"]
		"build_command": 	"cmake --build .",
		"install_command": 	"cmake --build . --target install"

		# Consider:
		# "build_command": 		"mingw32-make -j<num_cores>",
		# "install_command": 	"mingw32-make install"
	}
}

####################################
# Script content. Do not edit.
####################################

# Imports:
from pathlib import Path
import shutil
import os

# Functions:

#####################################################
def build_and_install(platform, cfg):

	# Prepare variables:
	cmake_generator = build_config["compilation"]["cmake_generator"]
	build_command 	= build_config["compilation"]["build_command"]
	install_command = build_config["compilation"]["install_command"]

	# Remove previous build folder:
	shutil.rmtree(build_config["build_folder"], ignore_errors = True)
	# Make empty build folder:
	Path(build_config["build_folder"]).mkdir(parents = True, exist_ok = True)
	# Change working directory to build folder:
	os.chdir(build_config["build_folder"])

	# Setup build command:
	cmd = f"cmake .. -G\"{cmake_generator}\" -DCMAKE_BUILD_TYPE={cfg}"

	if platform == "x86":
		cmd += " -DCMAKE_CXX_FLAGS=-m32 -DCMAKE_C_FLAGS=-m32"

	cmd += " -DCMAKE_INSTALL_PREFIX:PATH={0}/{1}/{2}".format(build_config["install_path"], platform, cfg)

	# Print debug messages:
	print("Building:")
	print("- Configuration: " + cfg)
	print("- Platform: " + platform)
	print(f"- Command: {cmd}")

	# Execute build command:
	os.system(cmd)
	os.system(build_command)
	os.system(install_command)
	os.chdir("..")
	
	# Print debug separator message:
	print("=================================================")
#####################################################

#####################################################
def build_and_install_for_platform(platform):
	for cfg in build_config["configs"]:
		build_and_install(platform, cfg)
#####################################################

#####################################################
def relocate(folder, platform, config):
	"""Relocates folder from this hierarchy (example):

	/x86/Debug/lib
	
	... to this:
	
	/lib/x86/Debug	
	"""

	# Store as shortcut:
	install_path = build_config["install_path"]

	target_path	=f"{install_path}/{folder}/{platform}/{config}"
	src_path	=f"{install_path}/{platform}/{config}/{folder}"

	# Copy to target folder:
	shutil.copytree(src_path, target_path)
#####################################################

#####################################################
def relocate_folder_for_platform(folder, platform):
	for cfg in build_config["configs"]:
		relocate(folder, platform, cfg)
#####################################################

#####################################################
def relocate_for_platform(platform):
	for folder in build_config["folders_to_relocate"]:
		relocate_folder_for_platform(folder, platform)
#####################################################



#####################################################
if __name__ == "__main__":

	if build_config["install_path"] == "":
		print("You have to properly configure \"build_config[\"install_path\"]\" variable!")
		quit()

	# Store as shortcut:
	install_path = build_config["install_path"]

	print("=================================================")
	print("================== Build started ================")
	print("=================================================")
	print("")

	copied_include_folder = False

	# Build and install for every platform:
	for platform in build_config["platforms"]:
		build_and_install_for_platform(platform)

	# Relocate for every platform
	for platform in build_config["platforms"]:

		relocate_for_platform(platform)

		# Relocate include directory (once):
		if not copied_include_folder:
			copied_include_folder = True
			shutil.copytree(f"{install_path}/{platform}/Debug/include", f"{install_path}/include")
		

		# Remove unnecessary files: 
		shutil.rmtree(f"{install_path}/{platform}")
#####################################################