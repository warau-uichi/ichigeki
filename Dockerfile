# 1. Base Image
FROM python:3.11-slim

# 2. Environment Variables
ENV PYTHONUNBUFFERED=1

# 3. System Dependencies for Pyxel
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    # xvfb is often needed for headless environments for GUI apps
    # xvfb \
    && rm -rf /var/lib/apt/lists/*

# 4. Install uv
# Using RUN for pip install uv as curl method might have issues with PATH setup in non-interactive Docker build
# If the curl method is preferred and works in the target CI, it can be used.
# For now, using pip to ensure uv is available for subsequent RUN commands directly.
RUN pip install uv

# 5. Create Non-Root User
ARG USERNAME=devuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && rm -rf /var/lib/apt/lists/*

# Switch to non-root user
USER $USERNAME

# 6. Set Working Directory
WORKDIR /app

# 7. Copy Project Files & Install Dependencies
# Copy pyproject.toml first to leverage Docker layer caching for dependencies
COPY --chown=devuser:devuser pyproject.toml ./
# If a uv.lock file is generated and used, it should be copied too:
# COPY --chown=devuser:devuser uv.lock ./

# Create virtual environment, install dependencies, and ensure the venv is in PATH
# Using the full path to the `uv` installed by pip for the devuser
# The `uv` installed via pip for root might not be in PATH for devuser immediately.
# A more robust way is to ensure uv is in a system-wide accessible PATH or re-login,
# but for Dockerfile, specifying the path can be more direct if needed.
# However, `uv` installed via `pip install uv` for root should be in PATH.
# If not, one might need to adjust PATH or use `python -m uv ...`
RUN uv venv --python python3.11 .venv && \
    uv pip install .[dev]
# Add .venv/bin to PATH for subsequent commands in the Dockerfile and for the CMD/ENTRYPOINT
ENV PATH="/app/.venv/bin:${PATH}"

# 8. Copy Remaining Project Code (Optional)
# For development, the rest of the code is typically mounted.
# If building an image for deployment, you would uncomment the following:
# COPY --chown=devuser:devuser . .

# Default command (can be overridden in docker-compose.yml or docker run)
# For a development server, this might be `python src/main.py` or similar
# CMD ["python", "src/main.py"]
