import yaml
import io

def unknown_tag_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.ScalarNode):
        value = loader.construct_scalar(node)  # Node
    elif isinstance(node, yaml.SequenceNode):
        value = loader.construct_sequence(node)  # List
    elif isinstance(node, yaml.MappingNode):
        value = loader.construct_mapping(node)  # Dict
    else:
        raise TypeError(f"Unknown node type: {type(node)}")

    return {tag_suffix: value}

yaml.add_multi_constructor('!', unknown_tag_constructor)

def yaml_read(path):
    try:
        with io.open(path, "r", encoding="utf8") as yaml_file:
            return yaml.load(yaml_file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        with io.open(path, "w", encoding="utf8") as yaml_file:
            return {}


def from_yaml(file, tag):
    yaml_data = yaml_read(file)
    if tag in yaml_data:
        return yaml_data[tag]
    return None


def yaml_write(path, content):
    with io.open(path, "w", encoding="utf8") as yaml_file:
        yaml.dump(content, yaml_file, indent=2)

