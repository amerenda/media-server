# How to setup hama agent
cd /mnt/data/apps/plex/config/Library/'Application Support'/'Plex Media Server'/Plug-ins/
git clone https://github.com/ZeroQI/Hama.bundle.git
chmod 775 -R Hama.bundle
cd ..
mkdir -p Scanners/Series
cd Scanners/Series
wget -O 'Absolute Series Scanner.py' https://raw.githubusercontent.com/ZeroQI/Absolute-Series-Scanner/master/Scanners/Series/Absolute%20Series%20Scanner.py
cd ../..
chown -R plex:plex Scanners
chmod 775 -R Scanners

cd 'Plug-in Support/Data'
mkdir -p com.plexapp.agents.hama/DataItems/AniDB
mkdir -p com.plexapp.agents.hama/DataItems/Plex
mkdir -p com.plexapp.agents.hama/DataItems/OMDB
mkdir -p com.plexapp.agents.hama/DataItems/TMDB
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/blank
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/_cache/fanart/original
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/episodes
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/fanart/original
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/fanart/vignette
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/graphical
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/posters
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/seasons
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/seasonswide
mkdir -p com.plexapp.agents.hama/DataItems/TVDB/text
mkdir -p com.plexapp.agents.hama/DataItems/FanartTV
chmod 775 -R com.plexapp.agents.hama


## On Sonarr
Create /anime path
When downloading anime, ensure it uses this path and the anime profile

## On plex
Add Library
TV Shows
set path to /anime
Advanced
Agent
HamaTV
