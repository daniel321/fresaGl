# fresaGl

Editor que permite visualizar los movimientos de una maquina cnc a partir del codigo 'g'
y proporciona herramientas para la deteccion de errores, su correccion y posterior ejecucion
utilizando el programa 'match3'

![piece creation](/images/1.png)

# instalacion

**Instalar la version 2.7 de python de: https://www.python.org/downloads/**

**Instalar librerias:**
pip install PyGame
pip install WxPython
pip install PyOpenGl
pip install OpenGLContext
instalar PyOpenGlAccelerate https://pypi.python.org/pypi/PyOpenGL-accelerate

**instalar mach3:**
https://www.machsupport.com/software/mach3/


**Configurar los paths del programa (“paths.cfg”):**
mach3Path =  path donde se encuentra el ejecutable del programa Mach3
mach3ProfilePath = path de la carpeta del perfil utilizado en el mach3.
textEditorPath = editor de texto a ser usado para modificar el código G

**Configurar la relación  de tamaños entre las ventanas del programa (“windowsPercentage.cfg”):**
height3dWindow: Altura de la ventana 3d & la ventana de código, se trata de un
porcentaje de la altura total.
heightActionWindow: Altura de la ventana de acción, se trata de un porcentaje de la altura total.
width3dWindow: Ancho de la ventana 3d, se trata de un porcentaje de la altura total.
widthCodeWindow: Ancho de la ventana de código, se trata de un porcentaje de la altura total.

correr ejecutando "fresa.bat"
