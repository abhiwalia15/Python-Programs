def make_album(artist_name,album_name,no_of_tracks=''):
  info={'arist':artist_name,'album':album_name}
  if info:
    info['no_of_tracks']=no_of_tracks
  
  return info
print(make_album('arijit','chut',5))
print(make_album('honey singh','gand'))
print(make_album('ragav','loda'))