
from PySide2.QtWidgets import QMainWindow , QFileDialog, QMessageBox , QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot 
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow  import Ui_MainWindow
from particulas import Particula
from Lista import Lista


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.lista = Lista()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.inicio_pushButton.clicked.connect(self.click_agregar)
        self.ui.FINAL_pushButton.clicked.connect(self.click_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
        self.ui.orden_dist.clicked.connect(self.orden_d)
        self.ui.orden_id.clicked.connect(self.orden_id)
        self.ui.orden_vel.clicked.connect(self.orden_vel)

        self.ui.Dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2 , 1.2)
        else:
            self.ui.graphicsView.scale(0.8 , 0.8)    

    @Slot()
    def dibujar(self):
        pen = QPen()
        pen.setWidth(3)

        for Particula in self.lista:
            r = Particula.red
            b = Particula.blue
            g = Particula.green
            color = QColor(r,b,g)
            pen.setColor(color)
            self.scene.addEllipse(Particula.origen_x,Particula.origen_y,3,3,pen)
            self.scene.addEllipse(Particula.destino_x,Particula.destino_y,3,3,pen)
            self.scene.addLine(3+Particula.origen_x,3+Particula.origen_y,Particula.destino_x,Particula.destino_y,pen)
            

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def orden_d(self):
        self.lista.ordenar_distancia()
        self.mostrar_tabla()

    @Slot()
    def orden_id(self):
        self.lista.ordenar_id()
        self.mostrar_tabla()
        
    @Slot()
    def orden_vel(self):
        self.lista.ordenar_velocidad()
        self.mostrar_tabla()


    @Slot()
    def buscar_id(self):
        id = self.ui.Buscar_lineEdit.text()
        encontrado = False
        for Particula in self.lista:
            if id == (str(Particula.id)):

                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(1)

                id_widget = QTableWidgetItem (str(Particula.id))
                origen_x_widget = QTableWidgetItem (str(Particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(Particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(Particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(Particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
                red_widget = QTableWidgetItem(str(Particula.red))
                blue_widget = QTableWidgetItem(str(Particula.blue))
                green_widget = QTableWidgetItem(str(Particula.green))
                distancia_widget = QTableWidgetItem(str(Particula.distancia))

                self.ui.tableWidget.setItem(0,0,id_widget)
                self.ui.tableWidget.setItem(0,1,origen_x_widget)
                self.ui.tableWidget.setItem(0,2,origen_y_widget)
                self.ui.tableWidget.setItem(0,3,destino_x_widget)
                self.ui.tableWidget.setItem(0,4,destino_y_widget)
                self.ui.tableWidget.setItem(0,5,velocidad_widget)
                self.ui.tableWidget.setItem(0,6,red_widget)
                self.ui.tableWidget.setItem(0,7,blue_widget)
                self.ui.tableWidget.setItem(0,8,green_widget)
                self.ui.tableWidget.setItem(0,9,distancia_widget)

                encontrado = True
                return 
        if not encontrado:
               QMessageBox.warning(
               self,
               "ATENCION",
               f'LA PARTICULA"{id}"NO FUE ENCONTADA'
               )



    @Slot()
    def mostrar_tabla(self):
        self.ui.tableWidget.setColumnCount(10)
        headers = ["id","origen_x", "origen_y","destino_x","destino_y","velocidad","red","green","blue","distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget.setRowCount(len(self.lista))

        row = 0
        for Particula in self.lista:
            id_widget = QTableWidgetItem (str(Particula.id))
            origen_x_widget = QTableWidgetItem (str(Particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(Particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(Particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(Particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
            red_widget = QTableWidgetItem(str(Particula.red))
            blue_widget = QTableWidgetItem(str(Particula.blue))
            green_widget = QTableWidgetItem(str(Particula.green))
            distancia_widget = QTableWidgetItem(str(Particula.distancia))

            self.ui.tableWidget.setItem(row,0,id_widget)
            self.ui.tableWidget.setItem(row,1,origen_x_widget)
            self.ui.tableWidget.setItem(row,2,origen_y_widget)
            self.ui.tableWidget.setItem(row,3,destino_x_widget)
            self.ui.tableWidget.setItem(row,4,destino_y_widget)
            self.ui.tableWidget.setItem(row,5,velocidad_widget)
            self.ui.tableWidget.setItem(row,6,red_widget)
            self.ui.tableWidget.setItem(row,7,blue_widget)
            self.ui.tableWidget.setItem(row,8,green_widget)
            self.ui.tableWidget.setItem(row,9,distancia_widget)

            row += 1
            

    @Slot()
    def action_abrir_archivo(self):
      
       ubicacion = QFileDialog.getOpenFileName(
        self,
        'Abrir archivo',
        '.',
        'JSON (*.json)'
       )[0]
       if self.lista.abrir(ubicacion):
          QMessageBox.information(
            self,
            "EXITO",
            "SE ABRIO CON EXITO EL ARCHIVO" + ubicacion
        )
       else:
            QMessageBox.critical(
                self,
                "ERORR",
                "ERROR AL ABRIR EL ARCHIVO" + ubicacion
        )
       
        
        

    @Slot()
    def action_guardar_archivo(self):
      ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar',
            '.',
            'JSON (*.json)'
        )[0]
      print(ubicacion)
      if self.lista.guardar(ubicacion):
        QMessageBox.information(
            self,
            "EXITO",
            "SE PUDO CREAR EL ARCHIVO" + ubicacion,
        )

      else :
        QMessageBox.critical(
            self,
            "ERROR",
            "NO SE PUDO CREAR EL ARCHIVO" + ubicacion
        )


    @Slot()
    def click_mostrar(self):
        self.ui.salida.insertPlainText(str(self.lista))


    @Slot()
    def click_agregar(self):
        id = self.ui.ID_spinBox.value()
        origen_x = self.ui.ORIGEN_X_spinBox.value()
        origen_y = self.ui.ORIGEN_Y_spinBox.value()

        destino_x = self.ui.x_spinBox.value()
        destino_y = self.ui.y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        verde = self.ui.verde_spinBox.value()
        azul = self.ui.azul_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.agregar_inicio(particula)

    
    @Slot()
    def click_final(self):
        id = self.ui.ID_spinBox.value()
        origen_x = self.ui.ORIGEN_X_spinBox.value()
        origen_y = self.ui.ORIGEN_Y_spinBox.value()

        destino_x = self.ui.x_spinBox.value()
        destino_y = self.ui.y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        verde = self.ui.verde_spinBox.value()
        azul = self.ui.azul_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.agregar_final(particula)

    

        
