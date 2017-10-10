#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import uuid


def create_uid():
    return str(uuid.uuid1())


if __name__ == '__main__':
    print(type(create_uid()))
    print(create_uid())
    print(create_uid())
    print(create_uid())
