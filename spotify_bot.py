import os
import spotify 
import pystyle 
import console 
import request 
import looper 
import paypal-transac 

# PAYPAL-TRANSAC is only if you want the bot to claim your money from Spotify to your PayPal account 
# if you want the bot to do this please complete this files : https://github.com/natrixdev/spotify-bot/tree/main/claimer

def __SpotifyBot__:
  configfolder = "https://github.com/natrixdev/spotify-bot/tree/main/config"
  configfile1 = "https://github.com/natrixdev/spotify-bot/blob/main/config/accounts.json"
  configfile2 = "https://github.com/natrixdev/spotify-bot/blob/main/config/song.json"
  
  song = configfile2
  accounts = configfile1 
  
  mainAcc = accounts.line(2)
  otherAccs = accounts.line(3, 9) 
  
  songURL=song.line(2)
  
  def __loop__:
    request.spotifyListen(songURL)
    method: "while True:" 
      daemon=True 
      loop=0
      
      breack.every(Spotifiy.4000v) 
      restart: 
        return; 
      
      SpotifyBot()
      loop()
