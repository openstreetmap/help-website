+++
type = "question"
title = "Rendering failed with command 4"
description = '''Hi, I am trying to set OSM map server as per steps given in link below: https://seshagiriprabhu.wordpress.com/2013/07/21/building-an-openstreetmap-tile-server-on-ubuntu-12-04-lts/ But I am getting following following errors: While running renderd in debugging mode: renderd[6593]: An error occurred w...'''
date = "2019-08-22T06:15:00Z"
lastmod = "2019-09-04T07:44:00Z"
weight = 70461
keywords = [ "rendering" ]
aliases = [ "/questions/70461" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Rendering failed with command 4](/questions/70461/rendering-failed-with-command-4)

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
<span id="post-70461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70461-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am trying to set OSM map server as per steps given in link below:</p>
<p><a href="https://seshagiriprabhu.wordpress.com/2013/07/21/building-an-openstreetmap-tile-server-on-ubuntu-12-04-lts/">https://seshagiriprabhu.wordpress.com/2013/07/21/building-an-openstreetmap-tile-server-on-ubuntu-12-04-lts/</a></p>
<p>But I am getting following following errors:</p>
<p>While running renderd in debugging mode:</p>
<p>renderd[6593]: An error occurred while loading the map layer 'default': Shape Plugin: shapefile '/etc/mapnik-osm-carto-data/data/simplified-land-polygons-complete-3857/simplified_land_polygons.shp' does not exist encountered during parsing of layer 'world' in Layer at line 76 of '/etc/mapnik-osm-carto-data/osm.xml'</p>
<p>While giving pre-render command sudo render_list -a -s /var/run/renderd/renderd.sock</p>
<p>ubuntu@ip-172-31-23-126:~$ sudo render_list -a -s /var/run/renderd/renderd.sock debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile Rendering client Starting 1 rendering threads Rendering all tiles from zoom 0 to zoom 20 Rendering all tiles for zoom 0 from (0, 0) to (0, 0) Rendering all tiles for zoom 1 from (0, 0) to (1, 1) Rendering all tiles for zoom 2 from (0, 0) to (3, 3) Rendering all tiles for zoom 3 from (0, 0) to (7, 7) Rendering all tiles for zoom 4 from (0, 0) to (15, 15) Rendering all tiles for zoom 5 from (0, 0) to (31, 31) Rendering all tiles for zoom 6 from (0, 0) to (63, 63) rendering failed with command 4, pausing. rendering failed with command 4, pausing.</p>
<p>Can somebody help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '19, 06:15</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70461" class="comments-container">
<span id="70477"></span>
<div id="comment-70477" class="comment">
<div id="post-70477-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any guide that dates from 2013 and Ubuntu 12 is likely to be out of data in a number of areas, not least the Natural Earth data zip files have changed slightly in the last 6 years. I haven't tested the PPA that that used for a while (and not on Ubuntu 12 for ages) so cant guarantee that it will still work.</p>
<p>Is there a reason why you're using Ubuntu 12?</p>
</div>
<div id="comment-70477-info" class="comment-info">
<span class="comment-age">(22 Aug '19, 17:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70478"></span>
<div id="comment-70478" class="comment">
<div id="post-70478-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using Ubuntu 14.04 LTS</p>
</div>
<div id="comment-70478-info" class="comment-info">
<span class="comment-age">(22 Aug '19, 17:49)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="70480"></span>
<div id="comment-70480" class="comment">
<div id="post-70480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's still from <a href="https://www.theguardian.com/world/2014/dec/26/top-10-news-stories-2014-guardian">2014</a> - is there anything stopping you using a later version?</p>
</div>
<div id="comment-70480-info" class="comment-info">
<span class="comment-age">(22 Aug '19, 17:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70461-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="70476"></span>

<div id="answer-container-70476" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70476-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello</p>
<p>Check the <strong>/etc/mapnik-osm-carto-data/data/simplified-land-polygons-complete-3857/</strong> directory and see what files/subdirectories are inside. Renderd is complying about missing shape file, so probably you didn't download it or you have got that file in different place. If the <strong>simplified-land-polygons-complete-3857</strong> isn't there, then take look into the <strong>/etc/mapnik-osm-carto-data/data/</strong> .</p>
<p>You could also try the <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> which should work without any major problems.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '19, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/7b5775bcca69a6b6603f02a8255ef2f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="januzi&#39;s gravatar image" />
<p><span>januzi</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="januzi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70476" class="comments-container">
<span id="70492"></span>
<div id="comment-70492" class="comment">
<div id="post-70492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded land-polygons-split-3857.zip and simplified-land-polygons-complete-3857.zip from below link:</p>
<p><a href="https://osmdata.openstreetmap.de/download/simplified-land-polygons-complete-3857.zip">https://osmdata.openstreetmap.de/download/simplified-land-polygons-complete-3857.zip</a> <a href="https://osmdata.openstreetmap.de/download/land-polygons-split-3857.zip">https://osmdata.openstreetmap.de/download/land-polygons-split-3857.zip</a></p>
<p>Now errors for these two files is gone and a new error is shown while I run renderd in debug mode.</p>
<p>renderd[3641]: An error occurred while loading the map layer 'default': Shape Plugin: shapefile '/etc/mapnik-osm-carto-data/data/ne_110m_admin_0_boundary_lines_land/ne_110m_admin_0_boundary_lines_land.shp' does not exist encountered during parsing of layer 'necountries' in Layer at line 123 of '/etc/mapnik-osm-carto-data/osm.xml'</p>
</div>
<div id="comment-70492-info" class="comment-info">
<span class="comment-age">(23 Aug '19, 11:22)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="70493"></span>
<div id="comment-70493" class="comment">
<div id="post-70493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://github.com/nvkelso/natural-earth-vector/blob/master/110m_cultural/ne_110m_admin_0_boundary_lines_land.shp">https://github.com/nvkelso/natural-earth-vector/blob/master/110m_cultural/ne_110m_admin_0_boundary_lines_land.shp</a></p>
<p>This one will probably work. Download it and put into the /etc/mapnik-osm-carto-data/data/ne_110m_admin_0_boundary_lines_land/.</p>
<p>If there are more errors about missing shapes, then type the last part of the error (like ne_110m_admin_0_boundary_lines_land.shp) into the google and download those shapes as well.</p>
</div>
<div id="comment-70493-info" class="comment-info">
<span class="comment-age">(23 Aug '19, 11:32)</span> <span class="comment-user userinfo">januzi</span>
</div>
</div>
<span id="70495"></span>
<div id="comment-70495" class="comment">
<div id="post-70495-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No. its giving me an error for /etc/mapnik-osm-carto-data/data/ne_10m_populated_places/ne_10m_populated_places_fixed.shp. Above link downloads a different file.</p>
</div>
<div id="comment-70495-info" class="comment-info">
<span class="comment-age">(23 Aug '19, 13:32)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="70496"></span>
<div id="comment-70496" class="comment">
<div id="post-70496-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As I've mentioned before, type the missing file name into the google and get the file: <a href="http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_populated_places.zip">http://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_populated_places.zip</a></p>
</div>
<div id="comment-70496-info" class="comment-info">
<span class="comment-age">(23 Aug '19, 13:48)</span> <span class="comment-user userinfo">januzi</span>
</div>
</div>
<span id="70497"></span>
<div id="comment-70497" class="comment">
<div id="post-70497-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One other thing to mention - whatever map style you get after getting this data to load, it won't look like <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a> does now, as that currently use Natural Earth data. The style might look like OSM's "standard style" looked about 6 years ago.</p>
</div>
<div id="comment-70497-info" class="comment-info">
<span class="comment-age">(23 Aug '19, 16:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="70608"></span>
<div id="comment-70608" class="comment not_top_scorer">
<div id="post-70608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>I have followed steps given in <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a> link</p>
<p>I am getting following errors not for running renderd service</p>
<p>Mapnik LOG&gt; 2019-09-03 07:31:07: warning: unable to find face-name 'unifont Medium' in FontSet 'fontset-2' renderd[7426]: An error occurred while loading the map layer 'ajt': Postgis Plugin: FATAL: role "root" does not exist Connection string: ' dbname=gis connect_timeout=4' encountered during parsing of layer 'landcover-low-zoom' in Layer at line 819 of '/home/renderaccount/src/openstreetmap-carto/mapnik.xml' renderd[7426]: An error occurred while loading the map layer 'ajt': Postgis Plugin: FATAL: role "root" does not exist Connection string: ' dbname=gis connect_timeout=4' encountered during parsing of layer 'landcover-low-zoom' in Layer at line 819 of '/home/renderaccount/src/openstreetmap-carto/mapnik.xml' renderd[7426]: An error occurred while loading the map layer 'ajt': Postgis Plugin: FATAL: role "root" does not exist Connection string: ' dbname=gis connect_timeout=4'</p>
</div>
<div id="comment-70608-info" class="comment-info">
<span class="comment-age">(03 Sep '19, 08:33)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="70611"></span>
<div id="comment-70611" class="comment not_top_scorer">
<div id="post-70611-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In the project.mml scroll down to the line where you have set dbname. Add the lines: user: "youruser" port: "5432" password: "yourpassword" host: "localhost" (where youruser and yourpassword are from the user that was added to the postgress in the "Installing postgresql / postgis" paragraph). Regenerate style.xml and try again.</p>
<p>You might also need to use (in the psql console): ALTER USER youruser with password 'yourpassword';</p>
</div>
<div id="comment-70611-info" class="comment-info">
<span class="comment-age">(03 Sep '19, 10:31)</span> <span class="comment-user userinfo">januzi</span>
</div>
</div>
<span id="70612"></span>
<div id="comment-70612" class="comment not_top_scorer">
<div id="post-70612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tried this. Now getting below error. Password is correctly put in project.mml file. Then I recreated mapnik.xml file.</p>
<p>renderd[26191]: An error occurred while loading the map layer 'ajt': Postgis Plugin: FATAL: password authentication failed for user "renderaccount" FATAL: password authentication failed for user "renderaccount" Connection string: 'host=localhost port=5432 dbname=gis user=renderaccount connect_timeout=4' encountered during parsing of layer 'landcover-low-zoom' in Layer at line 819 of '/home/ubuntu/src/openstreetmap-carto/mapnik.xml' renderd[26191]: An error occurred while loading the map layer 'ajt': Postgis Plugin: FATAL: password authentication failed for user "renderaccount" FATAL: password authentication failed for user "renderaccount" Connection string: 'host=localhost port=5432 dbname=gis user=renderaccount connect_timeout=4' encountered during parsing of layer 'landcover-low-zoom' in Layer at line 819 of '/home/ubuntu/src/openstreetmap-carto/mapnik.xml' renderd[26191]: An error occurred while loading the map layer 'ajt': Postgis Plugin: FATAL: password authentication failed for user "renderaccount"</p>
</div>
<div id="comment-70612-info" class="comment-info">
<span class="comment-age">(03 Sep '19, 13:01)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="70614"></span>
<div id="comment-70614" class="comment not_top_scorer">
<div id="post-70614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Try to log in into postgres from console: 1. psql -h localhost -U renderaccount 2. psql -h localhost -U renderaccount -W</p>
<p>First command skips password, the second one asks for it. If you can't login with the renderaccount using those two commands, then login into postgres as root and run "alter user" command. After setting the password for renderaccount try again with the second command. This time you should be able to "get inside".</p>
</div>
<div id="comment-70614-info" class="comment-info">
<span class="comment-age">(03 Sep '19, 14:29)</span> <span class="comment-user userinfo">januzi</span>
</div>
</div>
<span id="70618"></span>
<div id="comment-70618" class="comment not_top_scorer">
<div id="post-70618-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>using alter user command, I could login to postgresql. Getting below error now for the command - sudo renderd -f -c /usr/local/etc/renderd.conf</p>
<p>renderd[14559]: config renderd: num_threads=4 renderd[14559]: config renderd: num_slaves=0 renderd[14559]: config renderd: tile_dir=/var/lib/mod_tile renderd[14559]: config renderd: stats_file=/var/run/renderd/renderd.stats renderd[14559]: config mapnik: plugins_dir=/usr/lib/mapnik/3.0/input renderd[14559]: config mapnik: font_dir=/usr/share/fonts/truetype renderd[14559]: config mapnik: font_dir_recurse=1 renderd[14559]: config renderd(0): Active renderd[14559]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock renderd[14559]: config renderd(0): num_threads=4 renderd[14559]: config renderd(0): tile_dir=/var/lib/mod_tile renderd[14559]: config renderd(0): stats_file=/var/run/renderd/renderd.stats renderd[14559]: config map 0: name(ajt) file(/home/ubuntu/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(localhost) renderd[14559]: Initialising unix server socket on /var/run/renderd/renderd.sock socket bind failed for: /var/run/renderd/renderd.sock</p>
</div>
<div id="comment-70618-info" class="comment-info">
<span class="comment-age">(04 Sep '19, 06:56)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="70619"></span>
<div id="comment-70619" class="comment not_top_scorer">
<div id="post-70619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>Now everything is working fine! thank you so much for the help.</p>
<p>Now I have two more things to do:</p>
<ol>
<li>Prerender the tiles</li>
<li>Currently I have downloaded India Map. Now I want to append one more country map data to my existing tiles and again prerender</li>
</ol>
</div>
<div id="comment-70619-info" class="comment-info">
<span class="comment-age">(04 Sep '19, 07:10)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="70621"></span>
<div id="comment-70621" class="comment not_top_scorer">
<div id="post-70621-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am trying to append GCC states data using below command, but getting error.</p>
<p>Command - sudo -u renderaccount osm2pgsql -d gis --append --slim -G --hstore ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 4096 --number-processes 6 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/gcc-states-latest.osm.pbf</p>
<p>Error -</p>
<p>Using built-in tag processing pipeline Using projection SRS 3857 (Spherical Mercator) Setting up table: planet_osm_point Setting up table: planet_osm_line Setting up table: planet_osm_polygon Setting up table: planet_osm_roads</p>
<p>Reading in file: /home/ubuntu/data/gcc-states-latest.osm.pbf Using PBF parser. Processing: Node(120k 4.8k/s) Way(0k 0.00k/s) Relation(0 0.00/s)DB writer thread failed due to ERROR: COPY planet_osm_point(osm_id,"access","addr:housename","addr:housenumber","admin_level","aerialway","aeroway","amenity","barrier","boundary","building","highway","historic","junction","landuse","layer","leisure","lock","man_made","military","name","natural","oneway","place","power","railway","ref","religion","shop","tourism","water","waterway",tags,way) FROM STDIN failed: ERROR: column "tags" of relation "planet_osm_point" does not exist</p>
</div>
<div id="comment-70621-info" class="comment-info">
<span class="comment-age">(04 Sep '19, 07:44)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
</div>
<div id="comment-tools-70476" class="comment-tools">
<span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-70476-form-container" class="comment-form-container">
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

