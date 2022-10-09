from nredarwin.webservice import DarwinLdbSession
darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx", api_key="e40bbb5b-3f96-4396-b8fd-f139a81bd86d")
board = darwin_sesh.get_station_board('GRT')
print(board)