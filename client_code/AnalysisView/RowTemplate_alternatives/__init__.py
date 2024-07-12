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
    #self.editable_link_1.add_event_handler('x-change-text', self.change_text)

  #def change_text(self, text, **event_args):
    #anvil.server.call('change_cell_value_alternatives', self.item, text)