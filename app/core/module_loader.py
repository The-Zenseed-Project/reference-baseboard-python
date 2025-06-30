import os
import yaml

def load_module_manifest(path: str = "modules.yaml") -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f).get('modules', {})

_MODULE_MANIFEST = load_module_manifest()

def get_module_versions() -> dict:
    return { name: info.get('version') for name, info in _MODULE_MANIFEST.items() }
