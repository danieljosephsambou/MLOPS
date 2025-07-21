import yaml

def load_config(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    config = load_config("configs/config.yaml")
    print("Configuration chargée :", config)
