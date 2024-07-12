from ._anvil_designer import EntrypointTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..AnalysisEdit import AnalysisEdit



class Entrypoint(EntrypointTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    
    # Set an event handlers on the RepeatingPanel (our 'analysis_panel')
    self.analyses_panelnel.set_event_handler('x-delete-analysis', self.delete_analysis)
    self.analyses_panel.set_event_handler('x-clone-analysis', self.clone_analysis)
                    
    self.refresh_analyses()
    

  def add_analysis_btn_click(self, **event_args):
    """This method is called when the "Add Analysis" button is clicked"""
    # Initialise an empty dictionary to store the user inputs
    new_analysis = {}
    # Open an alert displaying the 'AnalysisEdit' Form    
    save_clicked = alert(
      content=AnalysisEdit(item=new_analysis),
      title="Add Analysis",
      large=True,
      buttons=[("Save", True), ("Cancel", False)],
    )
    if save_clicked:
      anvil.server.call('add_analysis', new_analysis)
      self.refresh_analyses()

  def refresh_analyses(self):
    self.analyses_panel.items = anvil.server.call('get_analyses')

  def delete_analysis(self, analysis, **event_args):
    # Delete the analysis
    anvil.server.call('delete_analysis', analysis)
    self.refresh_analyses()

  def clone_analysis(self, clone, **event_args):
    # Pass clone as dictionary
    anvil.server.call('clone_analysis', dict(clone))
    self.refresh_analyses()