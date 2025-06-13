"""Update the fortnite game data with the latest on fortnite-api.com"""
import ast
import os
import black
import fortnite_api

client = fortnite_api.client.SyncClient()
with client:
    pois = client.fetch_map()

file = os.path.abspath(os.path.join(__file__, "..", "..", "fortnite.py"))
with open(file, 'r') as f:
    tree = ast.parse(f.read())

assigns = [s for s in tree.body if isinstance(s, ast.Assign)]
for const in assigns:
    target = const.targets[0]
    if not isinstance(target, ast.Name):
        continue
    name = target.id
    value = const.value
    if name == 'BR_NAMED_LOCATIONS':
        new_value = [p.name for p in pois.pois if p.id.startswith('Athena.Location.POI.Generic')]
        const.value = ast.List(elts=[ast.Constant(s) for s in new_value], ctx=ast.Load())

with open(file, 'w') as f:
    f.write(black.format_file_contents(ast.unparse(tree), fast=True, mode=black.FileMode(line_length=88)))
