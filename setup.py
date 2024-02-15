import setuptools

setuptools.setup(
    name="pyrob",
    version="0.0.1",
    author="r0b4dams",
    description="pyrob package manager",
    entry_points={"console_scripts": ["pyrob=cli:main"]},
    python_requires=">=3.10",
    setup_requires=["setuptools"],
    package_dir={"": "cli"},
    packages=setuptools.find_packages("cli"),
)
