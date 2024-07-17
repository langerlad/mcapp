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
    
    # Initialize EditableLink values
    self.editable_link_name.link_1.text = self.item['name']
    self.editable_link_unit.link_1.text = self.item['unit']
    self.editable_link_priority.link_1.text = str(self.item['priority'])  # Ensure it's a string for display

    # Add event handlers for EditableLink
    self.editable_link_name.add_event_handler('x-change-text', self.change_text_name)
    self.editable_link_unit.add_event_handler('x-change-text', self.change_text_unit)
    self.editable_link_priority.add_event_handler('x-change-text', self.change_text_priority)
    
  
  def change_text_name(self, text, **event_args):
    anvil.server.call('change_cell_value_criteria', self.item, 'name', text)
    self.editable_link_name.link_1.text = text

  def change_text_unit(self, text, **event_args):
    anvil.server.call('change_cell_value_criteria', self.item, 'unit', text)

  def change_text_priority(self, text, **event_args):
    try:
      # Convert the text to a number before sending to the server
      priority_value = float(text)
      anvil.server.call('change_cell_value_criteria', self.item, 'priority', priority_value)
      self.editable_link_priority.link_1.text = text
    except ValueError:
      alert("Priority must be a number")

  def link_delete_row_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.server.call('delete_criterium', self.item)
    self.parent.raise_event('x-refresh-criteria')

  def link_max_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
  
