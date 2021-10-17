from setuptools import setup

setup(
    name="parameter-utils",
    version="0.0.1",
    packages=["putils", "putils.commands"],
    include_package_data=True,
    install_requires=["click", "boto3", "moto"],
    tests_requires=["pytest"],
    entry_points="""
        [console_scripts]
        putils=putils.cli:cli
    """,
)
