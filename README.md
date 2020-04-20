# Nicotine+

[![N|Solid](files/icons/96x96/nicotine-plus.png)](https://github.com/Nicotine-Plus/nicotine-plus/)

> :warning: Python 3 port is at early alpha stage. Don't expect things to work flawlessly.

Nicotine+ is a graphical client for the SoulSeek peer-to-peer system. It is an attempt to keep Nicotine working with the latest libraries, kill bugs, keep current with the SoulSeek protocol, and add some new features that users want and/or need.

# Installation

## Docker
This method should work with any modern Linux distribution in both Xorg and Wayland environments. Nicotine will be run with your current user.

```shell script
$ docker-compose up nicotine
```

If you want to install dev requirements to resulting image:

```shell script
$ docker-compose up nicotine-dev
```

To run Nicotine pre-configured with dummy account add the following lines to `docker-compose.yml`:

```yaml
volumes:
- docker/config:$HOME/.config/nicotine/config
```

You could also mount your home directory as a persistent storage if needed:
```yaml
volumes:
- $HOME/.config/nicotine/config:$HOME/.config/nicotine/config
```

## Standalone

Prerequesites for local building are the following:

* Python 3.6+
* poetry package manager installed

To install Poetry for current user run the following commands:

```shell script
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
$ export PATH="$HOME/.poetry/bin:$PATH"
```

Then proceed with instructions for your distribution:

### Debian/Ubuntu or other .deb-based distribution
```shell script
$ make prepare-deb
$ make install
$ poetry run nicotine
```

### Arch Linux
```shell script
$ make prepare-arch
$ make install
$ poetry run nicotine
```

### macOS

You must have a `brew` package manager installed. Currently macOS build is only possible with Python 3.8 due to the way `brew` installs `pygobject`.

```shell script
$ make prepare-macos
$ make install-macos
$ poetry run nicotine
```

# License

Nicotine+ released under the terms of the [GNU Public License v3](https://www.gnu.org/licenses/gpl-3.0-standalone.html) or later.

# Getting Involved
Please come and join us in the `#nicotine+` channel on Freenode!

If you'd like to contribute, you have a couple of options to get started. You can open an issue ticket on GitHub, discuss in `#nicotine+`, or post to the project [mailing list](nicotine-team@lists.launchpad.net). Developers are also encouraged to join the [Launchpad Team](https://launchpad.net/~nicotine-team) or subscribe to the mailing list so that they are automatically notified of failed commits.

There is a current list of things [TODO](doc/TODO.md). If you'd like to translate Nicotine+ into another language it has not been already, see [TRANSLATIONS](doc/TRANSLATIONS.md).

You want to contact someone? See: [MAINTAINERS](AUTHORS.md)

# Precompiled Packages
If you have no need to modify the Nicotine+ source, you are strongly recommended to use precompiled packages for your distribution. This will save you time.

## Ubuntu PPA (Unstable)
The project builds [daily unstable snapshots](https://code.launchpad.net/~nicotine-team/+recipe/nicotine+-daily) in a separate [unstable PPA](https://code.launchpad.net/~nicotine-team/+archive/ubuntu/unstable). To use it, run the following:

```console
$ sudo add-apt-repository ppa:nicotine-team/unstable
$ sudo apt update
$ sudo apt install nicotine
```

## Ubuntu PPA (Stable)
To use [stable packages](https://launchpad.net/~nicotine-team/+archive/ubuntu/stable), run the following:

```console
$ sudo add-apt-repository ppa:nicotine-team/stable
$ sudo apt update
$ sudo apt install nicotine
```

## Other Distributions
Package maintainers, please insert instructions for users to install pre-compiled packages from your respective repositories here. For packaging instructions please see [PACKAGING](doc/PACKAGING.md). For downstream packages patches [DISTRO_PATCHES](doc/DISTRO_PATCHES.md).

# Versioning scheme

Nicotine+ uses a versioning scheme similar to what gnome does:

* Stable releases have an even minor version number, ex: 1.**4**.x, 1.**6**.x, ...

* Unstable releases have an odd minor version number, ex: 1.**3**.x, 1.**5**.x, ...

# Run it from git

To run it from git master see: [RUNFROMGIT](doc/RUNFROMGIT.md)

A Debian/Ubuntu repository containing the latest git master-based packages is also available: [GITDEB](doc/GITDEB.md)
