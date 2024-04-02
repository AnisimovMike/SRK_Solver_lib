from setuptools import setup


setup(
    name='SRK_Solver_lib',                    # package name
    version='0.1',                            # version
    description='Solving stochastic differential equations using the Runge Kutta method',      # short description
    url='https://github.com/AnisimovMike/SRK_Solver_lib',                                      # package URL
    install_requires=['pandas>=2.2.1'],                    # list of packages this package depends on.
    packages=['SRK_Solver_lib'],              # List of module names that installing this package will provide.
)
