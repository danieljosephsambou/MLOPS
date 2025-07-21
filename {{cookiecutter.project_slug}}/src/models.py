from sklearn.ensemble import RandomForestClassifier

def get_model(config):
    return RandomForestClassifier(
        n_estimators=config["n_estimators"],
        max_depth=config["max_depth"]
    )
