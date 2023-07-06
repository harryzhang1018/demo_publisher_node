from setuptools import setup

package_name = 'lib_demo_publisher'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Harry',
    maintainer_email='hzhang699@wisc.edu',
    description='Thiss node publishing the demo videos that has been generated already',
    license='BSD 3-Clause License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'video_pub = lib_demo_publisher.video_pub:main',
        ],
    },
)
