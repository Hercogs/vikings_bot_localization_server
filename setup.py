from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'vikings_bot_localization_server'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "config"), glob("config/*")),
        (os.path.join("share", package_name, "rviz"), glob("rviz/*")),
        (os.path.join("share", package_name, "launch"), glob("launch/*")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hercogs',
    maintainer_email='jecuks96@gmail.coms',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
