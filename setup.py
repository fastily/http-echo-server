import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="http-echo-server",
    version="0.0.1",
    author="Fastily",
    author_email="fastily@users.noreply.github.com",
    description="Simple http echo server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastily/http-echo-server",
    project_urls={
        "Bug Tracker": "https://github.com/fastily/http-echo-server/issues",
    },
    include_package_data=True,
    packages=setuptools.find_packages(include=["http_echo_server"]),
    install_requires=['Flask', 'gunicorn'],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)
