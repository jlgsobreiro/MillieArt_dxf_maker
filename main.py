import ezdxf
from ezdxf import path, zoom
from ezdxf.addons import text2path
from ezdxf.tools import fonts

caminho = 'C:\\Users\\JLGS\\Desktop\\Trabalhos\\DXFs\\'
caminho_fontes = 'C:\\Windows\\Fonts\\'

# Create a new DXF document.
doc = ezdxf.new('R2007', setup=True)
doc.styles.new('Monotype', dxfattribs={'font': 'monotype-corsiva.ttf'})
# Create new table entries (layers, linetypes, text styles, ...).

doc.layers.new('TEXTLAYER', dxfattribs={'color': 2})
doc.header['$INSUNITS'] = 4

# DXF entities (LINE, TEXT, ...) reside in a layout (modelspace, 
# paperspace layout or block definition).  
msp = doc.modelspace()

# Add entities to a layout by factory methods: layout.add_...()
# Retangulo
centro = [-20, 7.5]
msp.add_line((centro[0]+1.5, centro[1]+0), (centro[0]+38.5, centro[1]+0), dxfattribs={'color': 7})
msp.add_arc((centro[0]+38.5, centro[1]+-1.5), 1.5, 0, 90, True, )
msp.add_line((centro[0]+40, centro[1]+-1.5), (centro[0]+40, centro[1]+-13.5), )
msp.add_arc((centro[0]+38.5, centro[1]+-13.5), 1.5, 270, 360, True, )
msp.add_line((centro[0]+38.5, centro[1]+-15), (centro[0]+1.5, centro[1]+-15), )
msp.add_arc((centro[0]+1.5, centro[1]+-13.5), 1.5, 180, 270, True, )
msp.add_line((centro[0]+0, centro[1]+-13.5), (centro[0]+0, centro[1]+-1.5), )
msp.add_arc((centro[0]+1.5, centro[1]+-1.5), 1.5, 90, 180, True, )

# Buracos
msp.add_arc((centro[0]+37, centro[1]+-3), 1, 0, 360, True, )
msp.add_arc((centro[0]+37, centro[1]+-12), 1, 0, 360, True, )
msp.add_arc((centro[0]+3, centro[1]+-12), 1, 0, 360, True, )
msp.add_arc((centro[0]+3, centro[1]+-3), 1, 0, 360, True, )

# Texto
ff = fonts.FontFace(family="Carbonium")
paths = text2path.make_paths_from_str("MillieArt", ff, 10, 'CENTER', 30)
path.render_splines_and_polylines(msp, paths)
# Save DXF document.
zoom.extents(msp)
doc.saveas(caminho + 'test.dxf')
