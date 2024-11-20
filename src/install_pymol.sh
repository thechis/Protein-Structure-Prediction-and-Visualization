#!/bin/bash

# Install dependencies for PyMOL using Homebrew
brew install --formula cmake freetype libpng glew glm

# Set CFLAGS and LDFLAGS for the GLEW, GLM, and Freetype libraries
export CFLAGS="-I/opt/homebrew/include -I/opt/homebrew/include/freetype2"
export CXXFLAGS="-I/opt/homebrew/include -I/opt/homebrew/include/freetype2"
export LDFLAGS="-L/opt/homebrew/lib"

# Clone the PyMOL open-source repository
git clone https://github.com/schrodinger/pymol-open-source.git

# Navigate to the cloned repository
cd pymol-open-source

# Create build directory and navigate to it
mkdir -p build
cd build

# Run CMake to configure the build
cmake .. -DCMAKE_C_FLAGS="${CFLAGS}" -DCMAKE_CXX_FLAGS="${CXXFLAGS}" -DCMAKE_EXE_LINKER_FLAGS="${LDFLAGS}"
make -j$(sysctl -n hw.ncpu)
#cmake has incorrect arguments
# Install PyMOL
pip install ../.
