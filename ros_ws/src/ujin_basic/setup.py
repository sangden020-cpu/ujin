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
            "qos_test_pub = ujin_basic.qos_test_pub:main",
            "qos_test_sub = ujin_basic.qos_test_sub:main",
            "user_int_pub = ujin_basic.user_int_pub:main",
            "service_server = ujin_basic.service_server:main",
            "service_thread_server = ujin_basic.service_thread_server:main",
            "service_client = ujin_basic.service_client:main",
            "my_param=ujin_basic.my_param:main",
            "param_async=ujin_basic.param_async:main",
            "param.launch = ujin_basic.param_launch:main",
            "action_server = ujin_basic.action_server:main",
            "action_client = ujin_basic.action_client:main",
            "action_thread_server = ujin_basic.action_thread_server:main",
            "mv_turtle_ns = ujin_basic.mv_turtle_ns:main",
            "m = ujin_basic.m:main"


        ],
    },
)
