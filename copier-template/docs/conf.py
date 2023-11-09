from pathlib import Path

from swh.docs.sphinx.conf import *  # NoQA


def ensure_readme(app, config):
    srcpath = Path(app.srcdir)

    for extension in ("rst", "md"):
        fname = f"README.{extension}"
        readme_file = srcpath / ".." / fname
        symlink = srcpath / fname
        if readme_file.exists() and not symlink.exists():
            symlink.symlink_to(readme_file)
            break


def setup(app):
    app.connect("config-inited", ensure_readme)
