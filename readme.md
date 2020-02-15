# plink

plink is a command line python script that replaces patent numbers with links to patents.

`python plink 5678456` returns a link to this patent in the USPTO database.

Calling `python plink` without arguments replaces the patent number in your clipboard with a link.

## Options

plink can optionally link instead to Google patents, or replace all patent numbers in Excel or Google sheet documents.

### Link to Google patents

Use option -g:

`python plink -g`


### TODO: Link patent numbers in an Excel spread sheet or Google sheets document

`python plink path/to/spreadsheet`

`python plink https://docs.google.com/spreadsheets/`