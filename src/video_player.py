"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlist = Playlist()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        num_videos = len(self._video_library.get_all_videos())
        print("Here's a list of all available videos:")
        for i in range(num_videos):
            
            print(self._video_library.get_all_videos()[i].title+' '+self._video_library.get_all_videos()[i].video_id
                  +' '+str(self._video_library.get_all_videos()[i].tags))
            
        

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        num_videos = len(self._video_library.get_all_videos())
        Status = []
        ids = []
        for i in range(num_videos):
            ids.append(self._video_library.get_all_videos()[i].video_id)
            Status.append(self._video_library.get_all_videos()[i].play)
        if video_id not in ids:
            print("Cannot play video: Video does not exist")
        elif ('T' in Status) or ('P' in Status):
            
            for i in range(len(Status)):
                if Status[i] == 'T' or Status[i] == 'P':
                    print("Stopping video: "+str(self._video_library.get_all_videos()[i].title))
                    self._video_library.get_all_videos()[i].play='S'
            
        elif "F" in Status:
            i = Status.index("F")
            print("Cannot play video: Video is currently flagged (reason: Not supplied)")    
        else:
            print("Playing video: "+str(self._video_library.get_video(video_id).title))
            self._video_library.get_video(video_id).play='T'  
            

    def stop_video(self):
        """Stops the current video."""
        
        num_videos = len(self._video_library.get_all_videos())
        Status = []
        for i in range(num_videos):
            Status.append(self._video_library.get_all_videos()[i].play)
        if 'T' in Status:
            i = Status.index('T')
            print("Stopping video: "+str(self._video_library.get_all_videos()[i].title))
            self._video_library.get_all_videos()[i].play='S'   
        else:
            print('No video running')    
            
    
            
    def play_random_video(self):
        """Plays a random video from the video library."""
        
        num_videos = len(self._video_library.get_all_videos())
        Status = []
        for i in range(num_videos):
            Status.append(self._video_library.get_all_videos()[i].play)
        if ('T' in Status) or ('P' in Status):
            for i in range(len(Status)):
                if Status[i] == 'T' or Status[i] == 'P':
                    print("Stopping video: "+str(self._video_library.get_all_videos()[i].title))
                    self._video_library.get_all_videos()[i].play='S'
        elif 'F' in Status:
            i = Status.index('F')
            print("No videos available")             
            
        else:
            num = random.randint(0,num_videos-1)
            print('Playing video: '+str(self._video_library.get_all_videos()[num].title))
            self._video_library.get_all_videos()[num].play='T'
            
           
       

    def pause_video(self):
        """Pauses the current video."""

        num_videos = len(self._video_library.get_all_videos())
        Status = []
        for i in range(num_videos):
            Status.append(self._video_library.get_all_videos()[i].play)
        if 'T' in Status:
            i = Status.index('T')
            print("Pausing video: "+str(self._video_library.get_all_videos()[i].title))
            self._video_library.get_all_videos()[i].play='P'   
        elif 'P' in Status:
            i = Status.index('P')
            print("Video already paused: "+str(self._video_library.get_all_videos()[i].title))
        else:
            print("Cannot pause video: No video is currently playing") 
               
        
    def continue_video(self):
        """Resumes playing the current video."""

        num_videos = len(self._video_library.get_all_videos())
        Status = []
        for i in range(num_videos):
            Status.append(self._video_library.get_all_videos()[i].play)
        if 'P' in Status:
            i = Status.index('P')
            print("Continuing video: "+str(self._video_library.get_all_videos()[i].title))
            self._video_library.get_all_videos()[i].play='T' 
        elif 'P' not in Status and 'T' in Status:
            print("Cannot continue video: Video is not paused")    
        else:
            print("Cannot continue video: No video is currently playing")
                   
        
                       
               

    def show_playing(self):
        """Displays video currently playing."""

        num_videos = len(self._video_library.get_all_videos())
        Status = []
        for i in range(num_videos):
            Status.append(self._video_library.get_all_videos()[i].play)
        if 'T' in Status:
            i = Status.index('T')
            print("Currently playing: "+str(self._video_library.get_all_videos()[i].title+" "+self._video_library.get_all_videos()[i].video_id
                  +" "+str(list(self._video_library.get_all_videos()[i].tags))))
        if 'P' in Status:
            i = Status.index('P')
            print("Currently playing: "+str(self._video_library.get_all_videos()[i].title+" "+self._video_library.get_all_videos()[i].video_id
                  +" "+str(list(self._video_library.get_all_videos()[i].tags))+" - PAUSED"))    
        else:
            print("No video is currently playing")  
         
                   
               
               

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        self._playlist.create_playlist(playlist_name)
        

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        
        num_videos = len(self._video_library.get_all_videos())
        
        ids = []
        Status = []
        for i in range(num_videos):
            Status.append(self._video_library.get_all_videos()[i].play)
            ids.append(self._video_library.get_all_videos()[i].video_id)
        
        if video_id not in ids:
            print("Cannot add video to "+playlist_name+": Video does not exist")
        elif 'F' in Status:
            i = Status.index('F')
            print("Cannot add video to "+playlist_name+": Video is currently "
            "flagged (reason: Not supplied)")    
        else:    
            title = str(self._video_library.get_video(video_id).title)
            self._playlist.add_to_playlist(playlist_name, title)
        
        

    def show_all_playlists(self):
        """Display all playlists."""

        
        self._playlist.show_all_playlists()

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        self._playlist.show_playlist(playlist_name)

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        
        num_videos = len(self._video_library.get_all_videos())
        
        ids = []
        for i in range(num_videos):
            ids.append(self._video_library.get_all_videos()[i].video_id)
        
        if video_id not in ids:
            print("Cannot remove video from "+playlist_name+": Video does not exist")
        else:   
            self._playlist.remove_from_playlist(playlist_name, self._video_library.get_video(video_id).title)
   
    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        self._playlist.clear_playlist(playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        self._playlist.delete_playlist(playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        num_videos = len(self._video_library.get_all_videos())
        Present = ['']*(num_videos)
        for i in range(num_videos):
            if search_term in self._video_library.get_all_videos()[i].title.lower():
                Present[i]='p'    
        if 'p' not in Present:
            print("No search results for "+search_term)
        else:
            for i in range(len(Present)):
               if Present[i]=='p':
                  print(str(i)+")"+ str(self._video_library.get_all_videos()[i].title+" "+self._video_library.get_all_videos()[i].video_id
                  +" "+str(list(self._video_library.get_all_videos()[i].tags))))
            
        if 'p' in Present:
            print("Would you like to play any of the above? If yes, "
            "specify the number of the video.")
            print("If your answer is not a valid number, we will assume "
            "it's a no.")
            j = input()
            for i in range(num_videos):
                if j == i:
                    print("Playing video: "+str(self._video_library.get_all_videos()[i].title))
                

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        num_videos = len(self._video_library.get_all_videos())
        Present = ['']*(num_videos)
        for i in range(num_videos):
            if video_tag in self._video_library.get_all_videos()[i].tags:
                Present[i]='p'
        if 'p' not in Present:
            print("No search results for "+video_tag)
        elif Present[i]=='p':
            print(i+")"+ str(self._video_library.get_all_videos()[i].title+" "+self._video_library.get_all_videos()[i].video_id
                  +" "+str(list(self._video_library.get_all_videos()[i].tags))))
            
        if 'p' in Present:
            print("Would you like to play any of the above? If yes, "
            "specify the number of the video.")
            print("If your answer is not a valid number, we will assume "
            "it's a no.")
            j = input()
            for i in range(num_videos):
                if j == i:
                    print("Playing video: "+str(self._video_library.get_all_videos()[i].title))

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        num_videos = len(self._video_library.get_all_videos())
        Status = []
        ids = []
        for i in range(num_videos):
            ids.append(self._video_library.get_all_videos()[i].video_id)
            Status.append(self._video_library.get_all_videos()[i].play)
            
        if video_id not in ids:
            print("Cannot flag video: Video does not exist")
        elif flag_reason=="" and self._video_library.get_video(video_id).play!='F':
            print("Successfully flagged video: "+self._video_library.get_video(video_id).title +
           " (reason: Not supplied)")
            self._video_library.get_video(video_id).play='F'
        elif flag_reason!="" and self._video_library.get_video(video_id).play!='F':
            print("Successfully flagged video: "+self._video_library.get_video(video_id).title +
           " (reason: "+flag_reason+")")
            self._video_library.get_video(video_id).play='F'
        elif self._video_library.get_video(video_id).play=='F':
            print("Successfully flagged video: "+self._video_library.get_video(video_id).title +
           " (reason: "+flag_reason+")")
            print("Cannot flag video: Video is already flagged")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        num_videos = len(self._video_library.get_all_videos())
        Status = []
        ids = []
        for i in range(num_videos):
            ids.append(self._video_library.get_all_videos()[i].video_id)
            Status.append(self._video_library.get_all_videos()[i].play)
            
        if video_id not in ids:
            print("Cannot remove flag from video: Video does not exist")
        elif self._video_library.get_video(video_id).play=='F':
            print("Successfully removed flag from video: "+self._video_library.get_video(video_id).title)
            self._video_library.get_video(video_id).play='S'
        elif self._video_library.get_video(video_id).play!='F':
            print("Cannot remove flag from video: Video is not flagged")
