import csv
import io
import json
import requests
import sys
import uuid
from pathlib import Path

meta = '/opt/devel/uva/repos/GDPR-CCPA-violation-checker/utils/aws/meta.json'
pp = '/opt/devel/uva/repos/GDPR-CCPA-violation-checker/utils/aws/plugin_paths.txt'


def tozipname(v):
    dl = v['download_link']
    dl = str(Path(dl).name)
    filename = f'{dl[:dl.find(".")]}.zip'
    return filename


with open(meta, 'r') as f:
    meta_json = json.load(f)

# Hack around with the plugin meta and sort by active_install.
#   - py3.7+ implementation specific.
meta_json = {v['slug']: v for k, v in meta_json.items()}
for k, v in meta_json.items():
    v['zipname'] = tozipname(v)
meta_json = {k: v for k, v in sorted(meta_json.items(), key=lambda item: item[1]['active_installs'], reverse=True)}

with open(pp, 'r') as f:
    paths = {Path(x.strip()).name: x.strip() for x in f}

with open('analysis.csv', 'w') as f:
    f.write('name,slug,homepage,version,active_installs,path\n')
    for slug, plugin_meta in meta_json.items():
        path = paths.get(plugin_meta.get('zipname'), 'TODO')
        name = plugin_meta['name']
        name = f'"{name}"'
        slug = plugin_meta['slug']
        homepage = plugin_meta['homepage']
        version = plugin_meta['version']
        active_installs = plugin_meta['active_installs']
        f.write(f'{name},{slug},{homepage},{version},{active_installs},{path}\n')
