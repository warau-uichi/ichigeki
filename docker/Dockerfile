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
COPY --chown=devuser:devuser pyproject.toml ./
# COPY --chown=devuser:devuser uv.lock ./
RUN uv venv --python python3.11 .venv && \
    uv pip install .[dev]
ENV PATH="/app/.venv/bin:${PATH}"

# 8. Copy Remaining Project Code (Optional)
# For development, the rest of the code is typically mounted.
# If building an image for deployment, you would uncomment the following:
# COPY --chown=devuser:devuser . .

# Default command (can be overridden in docker-compose.yml or docker run)
# CMD ["python", "src/main.py"]
