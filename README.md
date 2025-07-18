# python3-cyberfusion-yavb

YAVB is a CLI tool to bump versions and update changelogs.

Supported systems:

* PyProject (Python)
* Debian

It was built by Cyberfusion with two main purposes:

- Automatically bump SemVer version for multiple projects in bulk
- Bump versions for multiple systems simultaneously (e.g. Python packages distributed on PyPI **and** as Debian packages)

# Install

## Debian

Run the following commands to build a Debian package:

    mk-build-deps -i -t 'apt -o Debug::pkgProblemResolver=yes --no-install-recommends -y'
    dpkg-buildpackage -us -uc

## PyPI

Run the following command to install the package from PyPI:

    pip3 install python3-cyberfusion-yavb

# Configure

No configuration is supported.

# Usage

All examples assume that your projects are in the directory `projects/`.

⚠️ Quote glob characters (such as `*`). Otherwise, the shell might expand them.

## Example: increment patch (SemVer) for PyProject

```bash
yavb --system pyproject \
  --bump patch \
  --directory projects/your-project/
```

## Example: increment minor (SemVer) for Debian and PyProject, on Debian

```bash
yavb --system debian --system pyproject \
  --bump minor \
  --directory projects/your-project/ \
  --changelog 'Make this project great again' \
  --name 'John Doe' \
  --email 'john@example.com'
```

## Example: increment minor (SemVer) for Debian, on non-Debian

Changing Debian packaging requires Debian, which you can run inside a Docker container.

Build the Docker container:

```bash
docker build -f Dockerfile.Debian -t yavb-debian .
```

Run the Docker container:

```bash
docker run --rm -t -v $(pwd)/projects/:/projects -w /projects yavb-debian \
  --system debian \
  --bump minor \
  --directory your-project/ \
  --changelog 'Make this project great again' \
  --name 'John Doe' \
  --email 'john@example.com'
```
