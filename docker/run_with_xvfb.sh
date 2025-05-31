#!/bin/sh
# Start Xvfb in the background
Xvfb :99 -screen 0 1024x768x24 -ac &
# Export the display
export DISPLAY=:99
# Execute the command passed to this script
exec "$@"
