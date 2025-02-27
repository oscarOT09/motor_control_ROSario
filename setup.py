import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'motor_control_ROSario'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),
            glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oscar_ot09',
    maintainer_email='oscar_ot09@outlook.es',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dc_motor_ROSario = motor_control_ROSario.dc_motor_ROSario:main',
            'set_point_ROSario = motor_control_ROSario.set_point_ROSario:main',
            'control_pid_ROSario = motor_control_ROSario.control_pid_ROSario:main'
        ],
    },
)
