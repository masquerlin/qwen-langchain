import yaml
def read_config():
    """"读取配置"""
    with open("./config.yaml") as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def update_config(config):
    """"更新配置"""
    with open("./config.yaml", 'w') as yaml_file:
        yaml.dump(config, yaml_file)
    return None