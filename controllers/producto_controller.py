from flask import Blueprint, render_template, request, redirect, url_for
from models.producto import Producto, db

producto_bp = Blueprint('producto', __name__)

#READ - Listar productos

@producto_bp.route('/')
def index():
    productos = Producto.query.all()
    return render_template('productos/index.html', productos=productos)

#CREATE - Agregar nuevo producto
@producto_bp.route('/crear', methods=['GET'])
def crear():
    return render_template('productos/crear.html')

#GUARDAR - Guardar nuevo producto
@producto_bp.route('/crear', methods=['POST'])
def guardar():
    nuevo = Producto(
        nombre=request.form['nombre'],
        precio= float(request.form['precio']),
        stock = int(request.form['stock'])
    )
    
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for('producto.index'))

#UPDATE - Editar producto
@producto_bp.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    producto = Producto.query.get_or_404(id)
    return render_template('productos/editar.html', producto=producto)

@producto_bp.route('/editar/<int:id>', methods=['POST'])
def actualizar(id):
    producto = Producto.query.get_or_404(id)

    producto.nombre=request.form['nombre']
    producto.precio= float(request.form['precio'])
    producto.stock = int(request.form['stock'])

    db.session.commit()
    return redirect(url_for('producto.index'))

#DELETE - Eliminar producto

@producto_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('producto.index'))