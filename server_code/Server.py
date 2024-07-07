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
    raise Exception("Analysis not found")

@anvil.server.callable
def delete_analysis(analysis):
  # check that the analysis being deleted exists in the Data Table
  if app_tables.analyses.has_row(analysis):
    analysis.delete()
  else:
    raise Exception("Analysis not found")

@anvil.server.callable
def clone_analysis(clone):
  if clone is None:
    raise Exception("Analysis not found")  
  clone['created'] = datetime.now()
  clone['updated'] = None
  app_tables.analyses.add_row(**clone)
  