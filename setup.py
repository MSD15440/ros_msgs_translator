from setuptools import setup

package_name = 'ros_msgs_translator'

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
    description='Converts ros messages, like Float64 to 1d Float64Multi',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ros_msgs_translator = ros_msgs_translator.ros_msgs_translator:main',
        ],
    },
)
