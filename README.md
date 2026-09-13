# Topology-Transform
This project presents a character creation workflow for generating game-ready animated creatures by combining AI-generated models with existing production-ready game assets. The workflow utilizes Meshy AI, Wrap by FaceForm, Blender, Adobe Substance 3D Painter, and Unreal Engine to transform high-polygon creature concepts into optimized, animation-ready characters while preserving compatibility with existing skeletal rigs.

The process begins by selecting a suitable game-ready base mesh that already contains an optimized topology, UV layout, and skeletal rig. In this workflow, a Tyrannosaurus Rex (T-Rex) model extracted from Jurassic World Evolution 2 is used as the foundation. A high-polygon dinosaur is then generated using AI tools such as Meshy AI, with the generated creature chosen to closely match the anatomical structure of the base mesh.

Both meshes are imported into Wrap by FaceForm, where correspondence landmarks are established to transfer the topology of the base mesh onto the AI-generated character. This allows the generated dinosaur to inherit the optimized topology and rig compatibility of the original game asset while retaining its unique visual appearance. To further improve mesh conformity, a custom Blender Python script transfers vertex positions while preserving the original topology, UV mapping, and mesh connectivity.

The optimized mesh is then imported into Adobe Substance 3D Painter, where high-resolution details from the original AI-generated creature are baked onto the low-polygon mesh using Normal, Ambient Occlusion, Curvature, and World Space Normal maps. AI-generated textures are applied to recreate the appearance of the original character while maintaining a game-ready asset suitable for real-time rendering.

Because the workflow preserves the original skeletal rig and UV layout, the resulting creature remains animation-ready and can be imported directly into Unreal Engine without requiring additional rigging or UV unwrapping.

Key Features

• AI-generated to game-ready creature conversion workflow
• Topology transfer using Wrap by FaceForm
• Preservation of original skeletal rig compatibility
• UV layout preservation during mesh transformation
• Custom Blender Python-based vertex transfer workflow
• High-poly to low-poly detail baking and optimization
• AI-assisted texture generation and application
• Reusable workflow for multiple creature variants
• Animation-ready character generation
• Unreal Engine compatible real-time assets
