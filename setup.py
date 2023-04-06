from setuptools import setup

package_name = 'f64tomulti'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='atticus',
    maintainer_email='atticusrussell@gmail.com',
    description='Converts Float64 to 1d Float64Multi',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'f64_to_multiarray = f64tomulti.f64_to_multiarray:main',
        ],
    },
)