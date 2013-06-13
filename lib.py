#!/usr/bin/env python

def args_list(**kwargs):
    for name, value in kwargs.items():
        print name, value

def args_list1(*args):
    for name, value in list_to_dict(args):
        print '{0} -> {1}'.format(name, value)

def list_to_dict(l):
    def extract_argument_name(x):
        argument_name = x.split('=')[0]
        argument_value = x[len(argument_name) + 1:]
        return [argument_name, argument_value]
    return list((x[0], x[1]) for x in map(extract_argument_name, l))
