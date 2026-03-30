#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='linker_hand_l20d_ros2_sdk',
            executable='linker_hand_l20d',
            name='linker_hand_l20d',
            output='screen',
            parameters=[{
                'hand_type': 'left', # 配置Linker Hand灵巧手类型 left | right 字母为小写
                'hand_joint': "L20D", # L20D 字母为大写
                'is_touch': False, # 配置Linker Hand灵巧手是否有压力传感器 True | False
            }],
        ),
    ])