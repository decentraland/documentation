# Use Alpine Linux as base image for smaller size
FROM alpine:3.17

# Set Hugo version
ENV HUGO_VERSION=0.108.0
ENV HUGO_BINARY=hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz

# Install dependencies
RUN apk add --no-cache \
    curl \
    git \
    ca-certificates \
    libc6-compat \
    libstdc++

# Download and install Hugo
RUN curl -L https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY} | tar -xz && \
    mv hugo /usr/local/bin/hugo && \
    chmod +x /usr/local/bin/hugo

# Verify Hugo installation
RUN hugo version

# Set working directory
WORKDIR /src

# Copy package files first for better caching
COPY config.toml ./

# Copy the entire project
COPY . .

# Expose port 1313 for Hugo server
EXPOSE 1313

# Default command to serve the site
CMD ["hugo", "server", "--config", "config.toml", "--bind", "0.0.0.0", "--port", "1313", "--disableFastRender"] 