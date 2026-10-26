main() {
    HUGO_VERSION=0.151.0

    export TZ=Americas/Los Angeles

    # Install Hugo (extended: image processing to WebP in layouts/partials/profile-image.html needs it)
    echo "Installing Hugo extended v${HUGO_VERSION}..."
    curl -LJO "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
    tar -xf "hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"
    cp hugo /opt/buildhome
    rm license README.md "hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz"

    # Verify installed versions
    echo "Verifying installations..."
    echo Go: echo "$(go version)"
    echo Hugo: "${HUGO_VERSION}"
    echo Node.js: "$(node --version)"

    # Clone themes repository
    echo "Clone Blowfish..."
    git submodule update --init --recursive
    git config core.quotepath false

    # Building the website
    echo "Building the Site..."
    hugo --gc --minify
}
#set -euo pipefail
main "$@"