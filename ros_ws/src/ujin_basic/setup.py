from setuptools import find_packages, setup

from setuptools import find_packages, setup

package_name = 'ujin_basic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/hello.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aa',
    maintainer_email='sangden020@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "simple_pub = ujin_basic.simple_pub:main",
            "class_pub = ujin_basic.class_pub:main",
            "class_sub = ujin_basic.class_sub:main",
            "header_pub = ujin_basic.header_pub:main",
            "mtsub = ujin_basic.mtsub:main",
            "tpub = ujin_basic.tpub:main",
            "mpub = ujin_basic.mpub:main",
            "msub = ujin_basic.msub:main",
            "m2sub = ujin_basic.m2sub:main",
            "mv_turtle = ujin_basic.mv_turtle:main",
        ],
    },
)
