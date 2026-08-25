from setuptools import find_packages, setup

package_name = 'my_first_ros2_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='My first ROS2 Python package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = my_first_ros2_pkg.simple_publisher:main',
            'simple_subscriber = my_first_ros2_pkg.simple_subscriber:main',
            'turtle_controller = my_first_ros2_pkg.turtle_controller:main',
            'turtle_square_controller = my_first_ros2_pkg.turtle_square_controller:main',
        ],
    },
)
