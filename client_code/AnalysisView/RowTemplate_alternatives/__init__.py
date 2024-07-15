from ._anvil_designer import RowTemplate_alternativesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...EditableLink import EditableLink


class RowTemplate_alternatives(RowTemplate_alternativesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.editable_link_1.add_event_handler('x-change-text', self.change_text)
    print("Initializing RowTemplate_alternatives with item:", self.item)
    self.editable_link_1.link_1.text = self.item['name']
    

  def change_text(self, text, **event_args):
    anvil.server.call('change_cell_value_alternatives', self.item, text)
    #self.editable_link_1.link_1.text = self.item['name'] , změna funguje
    self.editable_link_1.link_1.text = self.item

  def link_delete_row_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('delete_alternative', self.item)
    self.parent.raise_event('x-refresh-alternatives')

