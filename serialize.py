#!/usr/bin/env python
# -*- coding: utf-8 -*-

# main mechanism of serialisation
import yaml
from entity import Entity


# thin wrappers around yaml methods
def dump(obj, **kwargs):
    return yaml.dump(obj, Dumper = yaml.SafeDumper,
                     default_flow_style=False, allow_unicode=True,
                     **kwargs)


# thin wrappers around yaml methods
def load(stream):
    return yaml.load(stream, Loader=yaml.SafeLoader)


class SerializableEntity(Entity, yaml.YAMLObject):

    """Entity that can be serialized
    via default means of serialization"""

    yaml_loader = yaml.SafeLoader
    yaml_dumper = yaml.SafeDumper

    def __init__(self, **kwargs):
        Entity.__init__(self, **kwargs)
        yaml.YAMLObject.__init__(self)
