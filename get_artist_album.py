def make_album(artist_name,album_name):
  info={'artisst':artist_name,'albumm':album_name}
  return info
  
while True:
  
  print('\nEnter the name of the artist and the album')
  print('Enter q to exit')
   
  artist=input('artist_name: ') 
  if artist=='q':
    break
  
  album=input('album_name: ')
  if album=='q':
    break
  
  print(make_album(artist,album))
  