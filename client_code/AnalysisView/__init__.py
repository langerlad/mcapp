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
    #self.repeating_panel_alternatives.items = anvil.server.call('get_alternatives', self.item)
    self.get_alternatives()
    self.repeating_panel_criteria.items = anvil.server.call('get_criteria', self.item)
    
  def get_alternatives(self):
    #self.item is a row from the projects table
    self.alternatives = self.item
    self.rows = anvil.server.call('get_alternatives', self.alternatives)
    print("Alternatives rows:", self.rows)
    self.repeating_panel_alternatives.items = self.rows
  
  def link_add_alternative_row_click(self, **event_args):
    """This method is called when the link is clicked"""
    # přidá novou řádku do tabulky
    anvil.server.call('add_row_to_alternatives', self.item)
    self.repeating_panel_alternatives.items = anvil.server.call('get_alternatives', self.item)

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
    if confirm(f"Are you sure you want to delete {self.item['name']}?"):
      self.parent.raise_event('x-delete-analysis', analysis=self.item)

  def clone_analysis_btn_click(self, **event_args):
    """This method is called when the "Clone" button is clicked"""
    self.parent.raise_event('x-clone-analysis', clone=self.item)

  def show_analysis_btn_click(self, **event_args):
    """This method is called when the "Show analysis" button is clicked"""
    self.show_analysis_btn.visible = False
    self.hide_analysis_btn.visible = True
    self.column_panel_analysis_detail.visible = True

  def hide_analysis_btn_click(self, **event_args):
    """This method is called when the "Hide analysis" button is clicked"""
    self.hide_analysis_btn.visible = False
    self.show_analysis_btn.visible = True
    self.column_panel_analysis_detail.visible = False

    
