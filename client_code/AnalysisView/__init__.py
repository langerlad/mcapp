from ._anvil_designer import AnalysisViewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..AnalysisEdit import AnalysisEdit


class AnalysisView(AnalysisViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def edit_analysis_btn_click(self, **event_args):
    """This method is called when the "Edit" button is clicked"""
    # Create a copy of the existing analysis from the Data Table
    analysis_copy = dict(self.item)
    # Open an alert displaying the 'AnalysisEdit' Form
    # set the `self.item` property of the AnalysisEdit Form to a copy of the analysis to be updated
    save_clicked = alert(
      content=AnalysisEdit(item=analysis_copy),
      title="Update Analysis",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    # Update the analysis if the user clicks save
    if save_clicked:
      anvil.server.call('update_analysis', self.item, analysis_copy)
      # Now refresh the page
      self.refresh_data_bindings()

  def delete_analysis_btn_click(self, **event_args):
    """This method is called when the "Delete" button is clicked"""
    # Check that the user does want to delete the selected analysis
    # If yes, raise the 'x-delete-analysis' event on the parent 
    # (which is the analysis_panel on Homepage)
    if confirm(f"Are you sure you want to delete {self.item['title']}?"):
      self.parent.raise_event('x-delete-analysis', analysis=self.item)
