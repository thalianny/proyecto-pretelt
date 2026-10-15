from pathlib import Path
import webbrowser

from modelo.ropa_modelo import obtener_prendas

def mostrar_catalogo():

    vista = Path(__file__).resolve().parent.parent
    plantilla = vista / "vista" / "Index.html"
    salida = vista / "vista" / "catalogo_ropa.html"
    prendas = obtener_prendas()
    tarjetas = "\n".join(
        f"<li>{prenda['Producto']} - {prenda['Marca']} - {prenda['Precio']}</li>"
        for prenda in prendas
    )
    contenido = plantilla.read_text(encoding="utf-8")
    contenido = contenido.replace("<!--PRENDAS-->", tarjetas)
    salida.write_text(contenido, encoding="utf-8")
    
    print(f"Mi catálogo de ropa generado con MVC: {salida}")
    navegador_abierto = webbrowser.open_new_tab(salida.as_uri())
    print(f"Navegador Abierto: {navegador_abierto}")