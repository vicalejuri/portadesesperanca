import distutils.core

distutils.core.setup(
    name="portadesperanca",
    packages = ["portadesesperanca"],
    requires = ['pexpect (>= 2.4)'],
    )