#!/bin/bash
# Run a Pyxel application inside the Docker container and display on host

# Check if file path is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <path_to_pyxel_file> [additional_pyxel_args]"
    echo "Example: $0 src/main.py"
    exit 1
fi

PYXEL_FILE="$1"
shift  # Remove the first argument (file path)

# Run the Pyxel application with X11 forwarding to host
docker exec -it ichigekeen-dev-container bash -c "python -m pyxel run $PYXEL_FILE $*"
