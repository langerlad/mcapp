from ._anvil_designer import AnalysisDetailTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AnalysisDetail(AnalysisDetailTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_alternatives.items = anvil.server.call('get_alternatives')
    self.repeating_panel_criteria.items = anvil.server.call('get_criteria')