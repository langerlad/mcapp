import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.

@anvil.server.callable
def add_analysis(analysis_dict):
  app_tables.analyses.add_row(
    created=datetime.now(),
    **analysis_dict
  )

@anvil.server.callable
def get_analyses():
  # Get a list of analyses from the Data Table, sorted by 'created' column, in descending order
  return app_tables.analyses.search(
    tables.order_by("created", ascending=False)
  )

@anvil.server.callable
def update_analysis(analysis, analysis_dict):
  # check that the analysis given is really a row in the ‘analyses’ table
  if app_tables.analyses.has_row(analysis):
    analysis_dict['updated'] = datetime.now()
    analysis.update(**analysis_dict)
  else:
    raise Exception("Analysis does not exist")

@anvil.server.callable
def delete_analysis(analysis):
  # check that the analysis being deleted exists in the Data Table
  if app_tables.analyses.has_row(analysis):
    analysis.delete()
  else:
    raise Exception("Analysis does not exist")

@anvil.server.callable
def clone_analysis(analysis):
  # Get the original analysis row
  original_analysis = app_tables.analyses.get(analysis)
  if original_analysis is None:
    raise Exception("Analysis not found")

  # Create a new analysis row with the same data
  new_analysis = original_analysis.to_dict()
  new_analysis['created'] = datetime.now()  # Update the created time for the new analysis
  # del new_analysis['id']  # Remove the id field, as it will be auto-generated

  new_analysis_row = app_tables.analyses.add_row(**new_analysis)
  return new_analysis_row