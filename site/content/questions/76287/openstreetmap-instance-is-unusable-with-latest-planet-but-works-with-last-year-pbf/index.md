+++
type = "question"
title = "OpenStreetMap instance is unusable with latest planet, but works with last year PBF"
description = '''I&#x27;m running a custom OpenStreetMap instance on my server, with both the standard openstreetmap-carto style and a custom style. The current version up and running in production uses a planet file from 2019-09-12. I now want to update the data from the latest planet file on my dev server. I have a scr...'''
date = "2020-08-25T12:42:00Z"
lastmod = "2020-08-29T18:42:00Z"
weight = 76287
keywords = [ "openstreetmap-carto", "slow", "renderd", "osm2pgsql", "mapnik" ]
aliases = [ "/questions/76287" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap instance is unusable with latest planet, but works with last year PBF](/questions/76287/openstreetmap-instance-is-unusable-with-latest-planet-but-works-with-last-year-pbf)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76287-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm running a custom OpenStreetMap instance on my server, with both the standard openstreetmap-carto style and a custom style. The current version up and running in production uses a planet file from 2019-09-12.</p>
<p>I now want to update the data from the latest planet file on my dev server.</p>
<p>I have a script that will:</p>
<ul>
<li>download the latest file</li>
<li>tune the database for the import</li>
<li>drop and recreate the database</li>
<li>import the PBF</li>
<li>create the indexes</li>
<li>tune the database for production use</li>
</ul>
<p>The server is a quad-core i7-6700 with 64 GB of RAM, a 1 To SSD (storing the database) and 8 TB of hard drives (storing the tiles).</p>
<p>Here's the script code:</p>
<pre><code># Define some values:
PBF=~/data/planet-latest.osm.pbf
THREADS=8
CORES=4
&#10;# Download latest PBF:
wget https://planet.openstreetmap.org/pbf/planet-latest.osm.pbf -O $PBF
&#10;# Drop the databse:
sudo -u postgres dropdb osm
&#10;# Recreate the databse:
sudo mkdir -p /ssd/db/osm
sudo chown postgres /ssd/db/osm
sudo -u postgres psql -c &quot;CREATE TABLESPACE osm_tablespace LOCATION &#39;/ssd/db/osm&#39;;&quot;
sudo -u postgres createdb -E UTF8 -O myusername -D osm_tablespace osm
&#10;# Setup PostGIS:
sudo -u postgres psql osm -c &quot;CREATE EXTENSION postgis;&quot;
sudo -u postgres psql osm -c &quot;CREATE EXTENSION hstore;&quot;
sudo -u postgres psql osm -c &quot;ALTER TABLE geography_columns OWNER TO myusername;&quot;
sudo -u postgres psql osm -c &quot;ALTER TABLE geometry_columns OWNER TO myusername;&quot;
sudo -u postgres psql osm -c &quot;ALTER TABLE raster_columns OWNER TO myusername;&quot;
sudo -u postgres psql osm -c &quot;ALTER TABLE raster_overviews OWNER TO myusername;&quot;
sudo -u postgres psql osm -c &quot;ALTER TABLE spatial_ref_sys OWNER TO myusername;&quot;
&#10;# Fine tune for import
if [ ! -f /etc/postgresql/10/main/postgresql.conf.bak ]; then
    sudo cp /etc/postgresql/10/main/postgresql.conf /etc/postgresql/10/main/postgresql.conf.bak
fi
&#10;sudo rm /etc/postgresql/10/main/postgresql.conf
sudo cp /etc/postgresql/10/main/postgresql.conf.bak /etc/postgresql/10/main/postgresql.conf
&#10;sudo tee -a /etc/postgresql/10/main/postgresql.conf &lt;&lt; EOF
synchronous_commit = off        # /!\ Use these for OSM import only
fsync = off                     # /!\ Use these for OSM import only
random_page_cost = 1.1
wal_buffers = 16MB
effective_cache_size = 48GB
maintenance_work_mem = 8GB
shared_buffers = 16GB
work_mem = 4GB
autovacuum = on
effective_io_concurrency = 200
max_connections = 300
checkpoint_completion_target = 0.7
default_statistics_target = 100
min_wal_size = 1GB
max_wal_size = 4GB
max_worker_processes = $THREADS
max_parallel_workers_per_gather = $CORES
max_parallel_workers = $THREADS
EOF
&#10;sudo service postgresql restart
&#10;# Import the PBF:
mkdir -p /ssd/flat-nodes
&#10;osm2pgsql \
    -d osm \
    --create --slim --multi-geometry --hstore --drop \
    --cache 20000 \
    --number-processes 1 \
    --tag-transform-script ~/src/map-styles/openstreetmap-carto/openstreetmap-carto.lua \
    --style ~/src/map-styles/openstreetmap-carto/openstreetmap-carto.style \
    --flat-nodes /ssd/flat-nodes/osm.cache \
    &quot;$PBF&quot;
&#10;# Create the indexes:
cd ~/src/map-styles/openstreetmap-carto
psql -d osm -f indexes.sql
&#10;# Fine tune for production:
sudo rm /etc/postgresql/10/main/postgresql.conf
sudo cp /etc/postgresql/10/main/postgresql.conf.bak /etc/postgresql/10/main/postgresql.conf
&#10;sudo tee -a /etc/postgresql/10/main/postgresql.conf &lt;&lt; EOF
#synchronous_commit = off        # /!\ Use these for OSM import only
#fsync = off                     # /!\ Use these for OSM import only
random_page_cost = 1.1
wal_buffers = 16MB
effective_cache_size = 48GB
maintenance_work_mem = 8GB
shared_buffers = 16GB
work_mem = 1GB
autovacuum = on
effective_io_concurrency = 200
max_connections = 300
checkpoint_completion_target = 0.7
default_statistics_target = 100
min_wal_size = 1GB
max_wal_size = 4GB
max_worker_processes = $THREADS
max_parallel_workers_per_gather = $CORES
max_parallel_workers = $THREADS
EOF</code></pre>
<p>I have already successfully used that script in the past. But if I run it now, my map becomes super slow (with both openstreetmap-carto style and mine), like if it was missing all the indexes. Running the script on the 2019-09-12 PBF results in a perfectly usable map.</p>
<p>What could be wrong? Did the OSM database schema change since last year? Do I need to delete the flat-nodes files before importing again?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap-carto" rel="tag" title="see questions tagged &#39;openstreetmap-carto&#39;">openstreetmap-carto</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '20, 12:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a711e0129f307399a857a6f9b4bfd0e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timautin&#39;s gravatar image" />
<p><span>timautin</span><br />
<span class="score" title="151 reputation points">151</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timautin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76287" class="comments-container">
<span id="76288"></span>
<div id="comment-76288" class="comment">
<div id="post-76288-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you clarify what exactly is super slow. The script runs and completes within the expected time, and then the map tiles are slow? (Yes you should have deleted the node cache file but it would only slow down the import, not the tile serving.) Are you using renderd or tirex or ...? Did you clean old tiles from your tile cache or are they still there? Is there a planet-import-complete file in your tile directory?</p>
</div>
<div id="comment-76288-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 12:48)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="76289"></span>
<div id="comment-76289" class="comment">
<div id="post-76289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your comment. By slow I mean that generating my test tile takes 1-2 mn when it should takes 6-8 seconds. The import ran fine (in 24h). I'm using renderd and mapnik, and yes I deleted the old tiles. I have no planet-import-complete in my mod_tile directory, what is that file? I don't think I ever had one, is this new? EDIT: creating the file and restarting Apache + renderd does not change anything.</p>
</div>
<div id="comment-76289-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 12:54)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="76291"></span>
<div id="comment-76291" class="comment">
<div id="post-76291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The planet-import-complete file is not required, i was just asking to better understand your setup.</p>
</div>
<div id="comment-76291-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 13:06)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76287-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="76351"></span>

<div id="answer-container-76351" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76351-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-76351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As Jochen Topo suggested in comments, I simply ran out of disk space during the import. Making some room fixed the problem.</p>
<p>It's a 960GB SSD, on which I only had 128 GB of data. So 832 GB of free disk space is no longer enough to create a planet OSM DB. Looks like we'll pretty soon need 2 TB SSDs.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Aug '20, 18:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a711e0129f307399a857a6f9b4bfd0e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timautin&#39;s gravatar image" />
<p><span>timautin</span><br />
<span class="score" title="151 reputation points">151</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timautin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76351" class="comments-container">
&#10;</div>
<div id="comment-tools-76351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76351-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76290"></span>

<div id="answer-container-76290" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76290-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you are seeing is the normal effect of having deleted your tile cache. Tiles on z0-8 can easily take minutes - tiles in very dense areas might take longer than 10 minutes even with fast disks (remember, it always computes 8x8 tiles at once). The fact that it was faster before was not due to your indexes, but due to the cache which you have deleted.</p>
<p>Try rendering a tile on zoom 18, that should be relatively quick. Then use the appropriate render_list commands to pre-render your area of interest for zoom 0-12 (if the area is not the whole planet, perhaps look at <a href="https://github.com/alx77/render_list_geo.pl).">https://github.com/alx77/render_list_geo.pl).</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '20, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-76290" class="comments-container">
<span id="76292"></span>
<div id="comment-76292" class="comment">
<div id="post-76292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry I should have added more details: my test tile is a zoom 13 tile, that I use to check that everything works properly after each update. Usually my process is: delete the tile cache, recreate the DB (+ indexes), check that my test tile (13/4231/3002) is still generated in 6-8 secs, and then re-generate the cache. EDIT: an explain analyse shows that the indexes are correctly used. EDIT 2: I have no /ssd/flat-nodes/osm.cache file, is that normal? I don't have one either on the (working) production server.</p>
</div>
<div id="comment-76292-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 13:08)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="76295"></span>
<div id="comment-76295" class="comment">
<div id="post-76295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I'm missing the planet_osm_polygon_way_idx index, that's very likely the problem (I'm creating it, il will take a while). Isn't it supposed to be created by osm2pgsql?</p>
</div>
<div id="comment-76295-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 14:46)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
<span id="76296"></span>
<div id="comment-76296" class="comment">
<div id="post-76296-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh yes, not having that index will certainly slow down rendering a lot! And yes, it should be generated by osm2pgsql. Make sure you have the geometry indexes on the other tables as well.</p>
</div>
<div id="comment-76296-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 15:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="76297"></span>
<div id="comment-76297" class="comment">
<div id="post-76297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which version of osm2pgsql are you using?</p>
</div>
<div id="comment-76297-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 15:50)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="76299"></span>
<div id="comment-76299" class="comment">
<div id="post-76299-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Older versions of osm2pgsql have a bug where no error is shown if index creation failes. So maybe you ran out of disk space or so and the index wasn't created, but no error was shown. The newest version of osm2pgsql doesn't have this bug any more.</p>
</div>
<div id="comment-76299-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 16:48)</span> <span class="comment-user userinfo">Jochen Topf</span>
</div>
</div>
<span id="76302"></span>
<div id="comment-76302" class="comment not_top_scorer">
<div id="post-76302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks guys. Back after a few more investigations: creating the index myself does not solve the problem, and the created index is 25GB vs 37GB on the prod server. I'm thus restarting the whole import process with the osm2pgsql output saved in a file this time (by the way, don't osm2pgsql has a way to output its log to a file?), because on the previous import I didn't notice anything wrong and didn't keep the output. The drive had 755GB available, which I thought was enough, isn't it? I'll make some room before restarting the import. I'm using osm2pgsql v 0.96.0</p>
</div>
<div id="comment-76302-info" class="comment-info">
<span class="comment-age">(25 Aug '20, 18:20)</span> <span class="comment-user userinfo">timautin</span>
</div>
</div>
</div>
<div id="comment-tools-76290" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-76290-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

