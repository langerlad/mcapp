from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_analysis_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("You clicked the button")
