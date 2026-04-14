from google.adk.agents import llm_agent
from google.adk.tools import AgentTool
from google.adk.tools import google_search
from google.adk.tools import url_context


def build_root_agent() -> llm_agent.LlmAgent:
  sous_agent_google_search_agent = llm_agent.LlmAgent(
      name='Sous_agent_google_search_agent',
      model='gemini-3-flash-preview',
      description='Agent specialized in performing Google searches.',
      instruction='Use the GoogleSearchTool to find information on the web.',
      tools=[google_search],
  )

  sous_agent_url_context_agent = llm_agent.LlmAgent(
      name='Sous_agent_url_context_agent',
      model='gemini-3-flash-preview',
      description='Agent specialized in fetching content from URLs.',
      instruction='Use the UrlContextTool to retrieve content from provided URLs.',
      tools=[url_context],
  )

  sousagent = llm_agent.LlmAgent(
      name='sousagent',
      model='gemini-3-flash-preview',
      description='Run the code',
      instruction=(
          'Run the TestObjet :\nnew Thread(testObjectRef).start();\n'
          'et récupérer les images résultantes et/ou la vidéo et/ou le modèle '
          'avec setGenerate(GENERATE_IMAGES, ...)'
      ),
      tools=[
          AgentTool(agent=sous_agent_google_search_agent),
          AgentTool(agent=sous_agent_url_context_agent),
      ],
  )

  agent_scene_empty3_google_search_agent = llm_agent.LlmAgent(
      name='Agent_scene_Empty3_google_search_agent',
      model='gemini-3-flash-preview',
      description='Agent specialized in performing Google searches.',
      instruction='Use the GoogleSearchTool to find information on the web.',
      tools=[google_search],
  )

  agent_scene_empty3_url_context_agent = llm_agent.LlmAgent(
      name='Agent_scene_Empty3_url_context_agent',
      model='gemini-3-flash-preview',
      description='Agent specialized in fetching content from URLs.',
      instruction='Use the UrlContextTool to retrieve content from provided URLs.',
      tools=[url_context],
  )

  return llm_agent.LlmAgent(
      name='Agent_scene_Empty3',
      model='gemini-3-flash-preview',
      description=(
          'Codage en java, en kotlin à partir de la bibliothèque '
          'one.empty3:empty3-library-mp'
      ),
      sub_agents=[sousagent],
      instruction=(
          'Créer un object one.empty3.library.Scene et y ajouter des objets de '
          'type one.empty3.library.Representable et classes dérivées.\n'
          "Si l'utilisateur demande une vidéo, intégrer le document Scene scene "
          'dans la classe TestObjet ou plutôt TestObjetSub en surchargeant les '
          "méthodes void ginit() qui permet d'initialiser l'état des objets pour "
          "l'ensemble du film, et la méthode void finit() qui permet de mettre à "
          'jour les objets à chaque image de la vidéo.\n'
          'Si une image est demandée, écrire le code avec '
          'one.empty3.library.ZBufferImpl et Scene et Camera.\n'
          'Utiliser de préférence les classes one.empty3.libs.Image et '
          'one.empty3.libs.Color aux classes java.awt.Color et BufferedImage. '
          "Par exemple image.saveFile() de préférence à ImageIO.write() pour "
          "les manipulations de textures, de couleurs, et d'images\n"
          'On utilise un changement d\'axes Representable.setOrig(Point3D) pour '
          'le déplacement des objets et pour la rotation '
          'Representable.setVectX(Point3D), Representable.setVectY(Point3D), '
          'Representable.setVectZ(Point3D)\n'
          'On utilise la méthode setGenerate(int generateBinOption) comme: '
          'setGenerate(getGenerate()|newOption).\n\n'
          'Remarks\n'
          '1. Degenerate Camera Matrix (The "Up" Vector Problem)\n'
          'The primary reason for blank images in this library when looking '
          'straight along the Z-axis is a zeroed camera matrix. In '
          'GreenCubeAnimation.java, you initialize the camera as:\n'
          'Camera camera = new Camera(new Point3D(0d, 0d, 5d), Point3D.O0);\n'
          'When a camera is created without an explicit "up" vector, the '
          'library attempts to calculate a default one. However, if the camera '
          'is looking exactly along the Z-axis (from z=5 to z=0), the '
          'mathematical cross-product used for this calculation involves the '
          'global Z-axis. This results in a zero vector (0,0,0), which causes '
          'the entire projection matrix to fail.\n'
          'Fix: Provide an explicit "up" vector (usually Point3D.Y) to the '
          'camera constructor:\n'
          'Camera camera = new Camera(new Point3D(0d, 0d, 5d), Point3D.O0, '
          'Point3D.Y);\n'
          '3. Use latest version of the library i.e. '
          'one.empty3:empty3-library-mp:2026.4.12-25\n'
          '4. Use subclass one.empty3.Color.newCol(redFloat, greenFloat, '
          'blueFloat) instead of new java.awt.Color(redFloat, greenFloat, '
          'blueFloat)\n'
          '5. Use subclass one.empty3.libs.Image.saveFile(File file) instead of '
          'ImageIO.write(Image image, String format, File file) and access to '
          'image bitmap with Image.getBi()\n'
          '6. Use model STL or OBJ when needed. Class for OBJ is E3Model. Use '
          'in-code obj text or a .obj file.\n'
          '7. Use .0 or d suffix for double value instead of Integer literal'
      ),
      tools=[
          AgentTool(agent=agent_scene_empty3_google_search_agent),
          AgentTool(agent=agent_scene_empty3_url_context_agent),
      ],
  )


root_agent = build_root_agent()
