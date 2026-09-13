import bpy
import bmesh


obj1 = bpy.context.active_object
obj2 = [o for o in bpy.context.selected_objects if o != obj1][0]

bm1 = bmesh.from_edit_mesh(obj1.data)
bm2 = bmesh.from_edit_mesh(obj2.data)

bm1.verts.ensure_lookup_table()
bm2.verts.ensure_lookup_table()

# Selected vertices
v1 = [v for v in bm1.verts if v.select][0]
v2 = [v for v in bm2.verts if v.select][0]

visited = set()

stack = [(v1, v2)]

while stack:

    a, b = stack.pop()

    if a.index in visited:
        continue

    visited.add(a.index)

    # Copy position
    b.co = a.co

    na = [e.other_vert(a) for e in a.link_edges]
    nb = [e.other_vert(b) for e in b.link_edges]

    # Only works if edge ordering matches
    for va, vb in zip(na, nb):
        if va.index not in visited:
            stack.append((va, vb))

bmesh.update_edit_mesh(obj2.data)
