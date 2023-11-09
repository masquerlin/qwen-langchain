import yaml
def read_config(config_path):
    """"读取配置"""
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def update_config(config,config_path):
    """"更新配置"""
    with open(config_path, 'w') as yaml_file:
        yaml.dump(config, yaml_file)
    return None
