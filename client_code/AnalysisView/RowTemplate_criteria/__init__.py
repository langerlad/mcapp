from ._anvil_designer import RowTemplate_criteriaTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate_criteria(RowTemplate_criteriaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def row_delete_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def link_delete_row_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def row_delete_btn_click(self, **event_args):
  """This method is called when the button is clicked"""
  anvil.server.call('delete_alternative', self.item)
  self.parent.raise_event('x-refresh-alternatives')
