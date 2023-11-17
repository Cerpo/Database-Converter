import wx
import wx.grid as grid
import pandas as pd
from src.config import cfg
from src.utils import datasource
from src.utils import csv


def get_table_names():
    engine = datasource.create_engine()
    sql = 'SHOW TABLES;'
    sql_query = pd.read_sql_query(sql, engine)
    engine.dispose()
    return sql_query[sql_query.columns[0]].tolist()


def save_selected_tables(selected_tables):
    engine = datasource.create_engine()
    for table in selected_tables:
        sql = 'select * from ' + cfg.get_value('datasource', 'database') + '.' + table
        sql_query = pd.read_sql_query(sql, engine)
        csv.save(sql_query, table, True)
    engine.dispose()


class MyGrid(grid.Grid):
    def __init__(self, parent):
        grid.Grid.__init__(self, parent, -1, pos=(41, 20), size=(217, 150))
        self.table_names = get_table_names()

        self.CreateGrid(self.table_names.__len__(), 2)
        self.RowLabelSize = 0
        self.ColLabelSize = 20

        self.SetColLabelValue(0, "S")
        self.SetColLabelValue(1, "Table Name")

        attr = grid.GridCellAttr()
        attr.SetEditor(grid.GridCellBoolEditor())
        attr.SetRenderer(grid.GridCellBoolRenderer())
        self.SetColAttr(0, attr)
        self.SetColSize(0, 20)
        self.SetColSize(1, 180)
        self.DisableDragGridSize()

        self.Bind(grid.EVT_GRID_CELL_LEFT_CLICK, self.onMouse)
        self.Bind(grid.EVT_GRID_SELECT_CELL, self.onCellSelected)
        self.Bind(grid.EVT_GRID_EDITOR_CREATED, self.onEditorCreated)

        for x, item in enumerate(self.table_names):
            self.SetCellValue(x, 1, item)
            self.SetReadOnly(x, 1, True)

    def onMouse(self, evt):
        if evt.Col == 0:
            wx.CallLater(100, self.toggle_check_box)
        evt.Skip()

    def toggle_check_box(self):
        self.cb.Value = not self.cb.Value

    def onCellSelected(self, evt):
        if evt.Col == 0:
            wx.CallAfter(self.EnableCellEditControl)
        evt.Skip()

    def onEditorCreated(self, evt):
        if evt.Col == 0:
            self.cb = evt.Control
            self.cb.WindowStyle |= wx.WANTS_CHARS
        evt.Skip()


class SaveButton(wx.Button):
    def __init__(self, parent, my_grid):
        wx.Button.__init__(self, parent, -1, label="Save", pos=(90, 180), size=(100, 30))
        self.SetBackgroundColour('WHITE')
        self.my_grid = my_grid
        self.Bind(wx.EVT_BUTTON, self.onClick)

    def onClick(self, evt):
        selected_table_names = []
        for x in range(self.my_grid.table_names.__len__()):
            if bool(self.my_grid.GetCellValue(x, 0)):
                selected_table_names.append(self.my_grid.GetCellValue(x, 1))
        save_selected_tables(selected_table_names)


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, -1, title=title, size=(300, 260))

        self.panel = wx.Panel(self)

        my_grid = MyGrid(self.panel)
        my_grid.SetFocus()
        SaveButton(self.panel, my_grid)

        self.CentreOnScreen()


class DBConverterApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Database Converter")
        self.frame.Show()
        return True


DBConverterApp(0).MainLoop()
