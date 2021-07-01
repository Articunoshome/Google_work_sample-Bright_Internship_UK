"""A video playlist class."""



class Playlist:
    """A class used to represent a Playlist."""
    
    def __init__(self):
        
        self._dict={}
        
    def create_playlist(self, name):
        
        string = " "
        string = name.upper()
        if string not in self._dict.keys():
             self._dict[string.upper()]=[]
             print("Successfully created new playlist: "+name)
        else:
            print("Cannot create playlist: A playlist with the same name already "
            "exists")
        
    def add_to_playlist(self, name, title ):
        
        string = " "
        string = name.upper()
        if len(self._dict)==0:
           print("Cannot add video to "+name+": Playlist does not exist")
        else:
             for i in self._dict.keys():
                if i == string:
                   if title not in self._dict.get(i):
                     self._dict[i].append(title)
                     print("Added video to "+name+": "+title)
                   else:
                     print("Cannot add video to "+name+": Video already added")
                elif string not in self._dict.keys():
                   print("Cannot add video to "+name+": Playlist does not exist")
        
    def show_all_playlists(self):
        
        if len(self._dict.keys())==0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for i in self._dict.keys():
                print(i)
           
    def show_playlist(self, name):
        
        string = " "
        string = name.upper()
        if len(self._dict.keys())==0:
            print("Cannot show playlist another_playlist: Playlist does not exist")
        else:
            for i in self._dict.keys(): 
               if i == string:
                  if len(self._dict.get(i))==0:
                     print("No videos here yet")
                  else:
                     print("Showing playlist: "+name)
                     for j in self._dict.get(i):
                          print(j)
                 
    def remove_from_playlist(self, name, title):
        string = " "
        string = name.upper()
        for i in self._dict.keys():
            if i == string:
              for j in self._dict.get(i):
                  if title in self._dict.get(i):
                       self._dict.get(i).remove(j)
                       print("Removed video from "+name+":"+title)
                  elif title not in self._dict.get(i):
                      print("Cannot remove video from "+name+": Video is not in playlist")
            elif string not in self._dict.keys():
                print("Cannot remove video from "+name+": Playlist does not exist")
        
        
    def clear_playlist(self, name):
        string = " "
        string = name.upper()
        for i in self._dict.keys():
            if i == string:
                  self._dict.get(i).clear()
                  print("Successfully removed all videos from "+name)
                  
    def delete_playlist(self, name):
        string = " "
        string = name.upper()
        for i in list(self._dict):
            if i == string:
                del self._dict[i]
                print("Deleted playlist: "+name)
            elif string not in list(self._dict):
                print("Cannot delete playlist "+name+": Playlist does not exist")