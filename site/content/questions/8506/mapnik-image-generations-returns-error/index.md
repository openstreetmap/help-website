+++
type = "question"
title = "mapnik image generations returns error"
description = '''I installed postgresql, gis and mapnik conform this tutorial: http://www.hyperionreactor.net/blog/how-build-your-own-osm-server-part-1-postgis-and-mapnik . But i took a different step and instead of downloading the whole world, i downloaded just my country. Now, when i run generate_xml.py and genera...'''
date = "2011-10-19T13:49:00Z"
lastmod = "2011-10-24T07:17:00Z"
weight = 8506
keywords = [ "osm", "mapnik" ]
aliases = [ "/questions/8506" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [mapnik image generations returns error](/questions/8506/mapnik-image-generations-returns-error)

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
<span id="post-8506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8506-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed postgresql, gis and mapnik conform this tutorial: <a href="http://www.hyperionreactor.net/blog/how-build-your-own-osm-server-part-1-postgis-and-mapnik">http://www.hyperionreactor.net/blog/how-build-your-own-osm-server-part-1-postgis-and-mapnik</a> . But i took a different step and instead of downloading the whole world, i downloaded just my country. Now, when i run <a href="http://generate_xml.py">generate_xml.py</a> and <a href="http://generate_image.py">generate_image.py</a>(or tiles) i recieve the following error</p>
<pre><code>./generate_xml.py --dbname gis --user prodeng  --accept-none --password apass --symbols ./symbols/ --world_boundaries ./world_boundaries/
Include files written successfully! Pass the osm.xml file as an argument if you want to serialize a new version or test reading the XML
alexandru@alex-lap:~/.osm/bin/mapnik$ ./generate_image.py 
PostGIS: SRID warning, using srid=-1
Traceback (most recent call last):
  File &quot;./generate_image.py&quot;, line 42, in &lt;module&gt;
    mapnik.load_map(m,mapfile)
RuntimeError: PSQL error:
ERROR:  relation &quot;planet_osm_polygon&quot; does not exist
LINE 4:        from planet_osm_polygon
                    ^
Full sql was: &#39;select * from 
      (select way,aeroway,amenity,landuse,leisure,man_made,military,&quot;natural&quot;,power,tourism,name,highway,
       case when religion in (&#39;christian&#39;,&#39;jewish&#39;) then religion else &#39;INT-generic&#39;::text end as religion
       from planet_osm_polygon
       where landuse is not null
          or leisure is not null
          or aeroway in (&#39;apron&#39;,&#39;aerodrome&#39;)
          or amenity in (&#39;parking&#39;,&#39;university&#39;,&#39;college&#39;,&#39;school&#39;,&#39;hospital&#39;,&#39;kindergarten&#39;,&#39;grave_yard&#39;)
          or military in (&#39;barracks&#39;,&#39;danger_area&#39;)
          or &quot;natural&quot; in (&#39;field&#39;,&#39;beach&#39;,&#39;desert&#39;,&#39;heath&#39;,&#39;mud&#39;,&#39;wood&#39;,&#39;sand&#39;,&#39;scrub&#39;)
          or power in (&#39;station&#39;,&#39;sub_station&#39;,&#39;generator&#39;)
          or tourism in (&#39;attraction&#39;,&#39;camp_site&#39;,&#39;caravan_site&#39;,&#39;picnic_site&#39;,&#39;zoo&#39;)
          or highway in (&#39;services&#39;,&#39;rest_area&#39;)
       order by z_order,way_area desc
      ) as leisure
       limit 0&#39;
 (encountered during parsing of layer &#39;landcover&#39;)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '11, 13:49</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8506" class="comments-container">
&#10;</div>
<div id="comment-tools-8506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8506-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="8552"></span>

<div id="answer-container-8552" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8552-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alexz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ok, then it is osm2pgsql not importing your data. The tutorial says</p>
<h1 id="cd-mntbinosm2pgsql">cd /mnt/bin/osm2pgsql</h1>
<h1 id="osm2pgsql--s-default.style---slim--d-gis--c-4096-mntplanetplanet-latest.osm.bz2">./osm2pgsql -S default.style --slim -d gis -C 4096 /mnt/planet/planet-latest.osm.bz2</h1>
<p>How big is the file you import? It may take 1-2 hours per 100mb of compressed data. The -C 4096 expectes more than 4GB of RAM on your machine.</p>
<p>In my toolchain, I use osm2pgsql --create --database osmdb --username osmuser --prefix planet --slim --cache 1024 -S default.style --hstore D:/Karten/osm/Geofabrik/duesseldorf.osm.bz2</p>
<p>osmdb, osmuser and planet to be modified for your needs.</p>
<p>Could you protocol the output of osm2pgsql?</p>
<p>HTH, ajoessen</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '11, 07:09</strong></p>
<img src="https://secure.gravatar.com/avatar/baddeab22266e1533be4ba4c9f3deb49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajoessen&#39;s gravatar image" />
<p><span>ajoessen</span><br />
<span class="score" title="168 reputation points">168</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajoessen has one accepted answer">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '11, 07:10</strong> </span></p>
</div>
</div>
<div id="comments-container-8552" class="comments-container">
<span id="8555"></span>
<div id="comment-8555" class="comment not_top_scorer">
<div id="post-8555-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot sir. But i receive errors with that command.</p>
<pre><code>$./osm2pgsql -S default.style --slim -d gis -C 2048 /home/alexandru/.osm/moldova.osm.bz2 --password --user &#39;prodeng&#39;
osm2pgsql SVN version 0.80.0 (32bit id space)
Password:
Using projection SRS 900913 (Spherical Mercator)
Setting up table: planet_osm_point
NOTICE:  table &quot;planet_osm_point&quot; does not exist, skipping
NOTICE:  table &quot;planet_osm_point_tmp&quot; does not exist, skipping
Setting up table: planet_osm_line</code></pre>
</div>
<div id="comment-8555-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 08:29)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8556"></span>
<div id="comment-8556" class="comment not_top_scorer">
<div id="post-8556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>some more similar messages, then:</p>
<pre><code>NOTICE:  table &quot;planet_osm_rels&quot; does not exist, skipping
NOTICE:  CREATE TABLE / PRIMARY KEY will create implicit index &quot;planet_osm_rels_pkey&quot; for table &quot;planet_osm_rels&quot;
Reading in file: /home/alexandru/.osm/moldova.osm.bz2
Segmentation fault</code></pre>
</div>
<div id="comment-8556-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 08:30)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8558"></span>
<div id="comment-8558" class="comment">
<div id="post-8558-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ah, thats the point it stops. According to <a href="https://wiki.openstreetmap.org/wiki/Mapnik#PostgreSQL.2FPostGIS">https://wiki.openstreetmap.org/wiki/Mapnik#PostgreSQL.2FPostGIS</a> the _int.sql installed previous is interfering.</p>
</div>
<div id="comment-8558-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 08:42)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8559"></span>
<div id="comment-8559" class="comment not_top_scorer">
<div id="post-8559-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@ajoessen</span>, yes, i just fixed that by deleting my gis db and recreating it accordingly, with this fix : <a href="https://wiki.openstreetmap.org/wiki/Talk:Openptmap/Installation">https://wiki.openstreetmap.org/wiki/Talk:Openptmap/Installation</a> .<br />
<br />
But i still have errors. Please help me to sort it out. Check my previous comments, i've edited them.</p>
</div>
<div id="comment-8559-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 08:56)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8560"></span>
<div id="comment-8560" class="comment">
<div id="post-8560-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The NOTICE: are ok. But the Segmentation fault not. Maybe the file was corrupted while downloading? Can you expand it to moldova.osm without error?</p>
</div>
<div id="comment-8560-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 08:59)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8562"></span>
<div id="comment-8562" class="comment not_top_scorer">
<div id="post-8562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, extraction worked fine. I changed my cache space to -C 1024 and it seems to work now. Strange how 2048 didn't worked because i have 3 gb on my pc.</p>
</div>
<div id="comment-8562-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 09:09)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8563"></span>
<div id="comment-8563" class="comment not_top_scorer">
<div id="post-8563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The operating System still needs some memory ;-) Mine (Windows XP) ist satisfied with 500kB.</p>
</div>
<div id="comment-8563-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 09:11)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8564"></span>
<div id="comment-8564" class="comment not_top_scorer">
<div id="post-8564-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So,import finished with</p>
<pre><code>Stopped table:planet_osm_ways in 67s
Osm2pgsql took 1115s overall</code></pre>
<p><br />
But i still don't succeed in generating tiles...<br />
</p>
<pre><code>./generate_xml.py --dbname gis --user=prodeng --accept-none
Include files written successfully! Pass the osm.xml file as an argument if you want to serialize a new version or test reading the XML
alexandru@alex-lap:~/.osm/bin/mapnik$ ./generate_tiles.py
render_tiles( (-180.0, -90.0, 180.0, 90.0) /home/alexandru/svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml /home/alexandru/osm/tiles/ 0 5 World )</code></pre>
</div>
<div id="comment-8564-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 09:35)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8565"></span>
<div id="comment-8565" class="comment not_top_scorer">
<div id="post-8565-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Continue</p>
<pre><code>RuntimeError: Could not load map file &#39;/home/alexandru/svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml&#39;: File does not exist</code></pre>
</div>
<div id="comment-8565-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 09:39)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8566"></span>
<div id="comment-8566" class="comment">
<div id="post-8566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>slowly getting ahead ;-) I usually make a copy of <a href="http://generate_tiles.py">generate_tiles.py</a> and change the parameters within that file, found at the end. render_tiles may suppress the error messgaes. You can try <a href="http://generate_image.py">generate_image.py</a> to produce a single picture for testing the installation.</p>
</div>
<div id="comment-8566-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 09:46)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8567"></span>
<div id="comment-8567" class="comment not_top_scorer">
<div id="post-8567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OH HEY! <a href="http://generate_image.py">generate_image.py</a> works! I needed to supply a pass for db user prodeng at <a href="http://generate_xml.py">generate_xml.py</a> for it to work.<br />
Unfortunately <a href="http://generate_tiles.py">generate_tiles.py</a> doesn't work yet. :(</p>
</div>
<div id="comment-8567-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 09:48)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8568"></span>
<div id="comment-8568" class="comment not_top_scorer">
<div id="post-8568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds good. In the <a href="http://generate_tiles.py">generate_tiles.py</a>, change the NUM_THREADS = 4 to NUM_THREADS = 1 for a try.</p>
</div>
<div id="comment-8568-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 09:53)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8570"></span>
<div id="comment-8570" class="comment not_top_scorer">
<div id="post-8570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nope, that doesn't change anything. Are you sure this may be the cause for now? it says file not found though.</p>
<p>EDIT: where is the xml generated anyway?</p>
<p>Btw, is potlatch and gis db somehow connected? Because i've stumbled on an interesting change. Please visit this topic for relevancy: <a href="/questions/8561/potlatch2-loads-but-then-crashes-on-my-osm-server">https://help.openstreetmap.org/questions/8561/potlatch2-loads-but-then-crashes-on-my-osm-server</a></p>
</div>
<div id="comment-8570-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 10:02)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8573"></span>
<div id="comment-8573" class="comment">
<div id="post-8573-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>generate_xml creates a few xml.inc in the inc directory. For rendering, you want to use osm_local.xml? Normally, osm.xml in the same directory as <a href="http://generate_tile.py">generate_tile.py</a> is used. You can edit that in the <a href="http://generate_tile.py">generate_tile.py</a>:</p>
<p>if <strong>name</strong> == "<strong>main</strong>": home = 'D:/' try: mapfile = "osm.xml" except KeyError: mapfile = home + "/<a href="http://svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml">svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml"</a> try: tile_dir = 'D:/Tiles/myMapnik/'</p>
</div>
<div id="comment-8573-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 10:18)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8574"></span>
<div id="comment-8574" class="comment not_top_scorer">
<div id="post-8574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why should i change that, i don't get it. Btw, my text is different:</p>
<p><code>if </code><strong><code>name</code></strong><code> == "</code><strong><code>main</code></strong><code>": home = os.environ['HOME'] try: mapfile = os.environ['MAPNIK_MAP_FILE'] except KeyError: mapfile = home + "/</code><a href="http://svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml"><code>svn.openstreetmap.org/applications/rendering/mapnik/osm-local.xml"</code></a><code> try: tile_dir = os.environ['MAPNIK_TILE_DIR'] except KeyError: tile_dir = home + "/osm/tiles/" if not tile_dir.endswith('/'): tile_dir = tile_dir + '/'</code></p>
<p><code> </code></p>
<p><code>What should i change it to? BTW, </code><code>echo $MAPNIK_MAP_FILE </code><code> returns nothing. Is it ok?</code></p>
</div>
<div id="comment-8574-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 10:31)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8575"></span>
<div id="comment-8575" class="comment">
<div id="post-8575-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Change the mapfile = to the local place and file osm.xml you want to use for rendering. The osm-local.xml does not seem to exist in the right place.</p>
</div>
<div id="comment-8575-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 10:37)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8577"></span>
<div id="comment-8577" class="comment not_top_scorer">
<div id="post-8577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Cool. It works now. THough i get a lot of "unknown: empty tile" messages. Hope it's ok.</p>
<p>Btw, where are these tiles going to be used? Can i see them in JOSM? Will i get something more if i'll use then for my osm server (assuming it doesn't).</p>
</div>
<div id="comment-8577-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 10:55)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8578"></span>
<div id="comment-8578" class="comment not_top_scorer">
<div id="post-8578-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What do you expect when you import only moldava and render the hole world from -180° to +180°? Most of the tiles must be empty! To see them, you can set up a html-page with openlayers. My wiki-Page is only in German, but perhaps useful for you:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/User:Ajoessen/Osmviewer_und_GPXviewer">https://wiki.openstreetmap.org/wiki/User:Ajoessen/Osmviewer_und_GPXviewer</a></p>
<p>You have to change the path for the tiles from <a href="http://osm.org">http://osm.org</a> to your local file system, or setup an apache server to use <a href="http://localhost">http://localhost</a> For your potlatch2 problem, I cant help you. I only use josm, but with the original osm servers.</p>
</div>
<div id="comment-8578-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 11:05)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8579"></span>
<div id="comment-8579" class="comment not_top_scorer">
<div id="post-8579-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So then you download the xml from <a href="http://osm.org">osm.org</a>, make changes and then... what? upload the changes to your osm db / gis db / <a href="http://osm.org">osm.org</a> ? Just curious :)</p>
</div>
<div id="comment-8579-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 11:43)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8580"></span>
<div id="comment-8580" class="comment not_top_scorer">
<div id="post-8580-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The Postgis database is only useful for rendering with mapnik. Osm2pgsql does a bit preprocessing to change route and multipolygon relations to geometry types that mapnik can understand.</p>
<p>A database for editing must have a different database scheme, dealing with changesets and version history of nodes, ways and relations. Rails Port is the software and database behind that.</p>
<p>I make my edits with josm on the <a href="http://osm.org">osm.org</a> servers, and take a copy of my local area every month from Geofabrik to render my area. Downloading all the tiles from <a href="http://osm.org">osm.org</a> is causing too much traffic on the tile servers.</p>
</div>
<div id="comment-8580-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 12:05)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8581"></span>
<div id="comment-8581" class="comment not_top_scorer">
<div id="post-8581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried reading it a couple of times but still not sure if i understand. As far as i know, you can download the map data from <a href="http://osm.org">osm.org</a> and then begin to edit it. THen you submit and upload the changes with your <a href="http://oms.org">oms.org</a> account. If you need to see the map changed you go to <a href="http://osm.org">osm.org</a> so how does Geofabrik fits in all this? (i don't know what's geofabrik).</p>
</div>
<div id="comment-8581-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 13:10)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8582"></span>
<div id="comment-8582" class="comment not_top_scorer">
<div id="post-8582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Geofabrik by Frederik Ramm <a href="http://download.geofabrik.de/osm/">http://download.geofabrik.de/osm/</a> offers the regional extracts (as cloudemade does, but also smaller extracts for my country).</p>
<p>To see my changes, i visit <a href="http://openstreetmap.org">openstreetmap.org</a>, yes. But I use my own database to make transparent overlays for cycle and hiking routes, bus services, height contour data and borders. These I only use locally in the same way you use the little blue-white "+" on the right of <a href="http://osm.org">osm.org</a>. And I can take them on my mobile device without Internet access.</p>
</div>
<div id="comment-8582-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 13:18)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
<span id="8606"></span>
<div id="comment-8606" class="comment not_top_scorer">
<div id="post-8606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, but that facebook stuff is not my world. You can contact me over my osm profile: <a href="https://www.openstreetmap.org/user/ajoessen">https://www.openstreetmap.org/user/ajoessen</a></p>
</div>
<div id="comment-8606-info" class="comment-info">
<span class="comment-age">(24 Oct '11, 07:17)</span> <span class="comment-user userinfo">ajoessen</span>
</div>
</div>
</div>
<div id="comment-tools-8552" class="comment-tools">
<span class="comments-showing"> showing 5 of 23 </span> <a href="#" class="show-all-comments-link">show 18 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-8552-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8509"></span>

<div id="answer-container-8509" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8509-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please give us access to your xml file produced at the step 1 to inspect it.</p>
<p>Have you imported the data with the same options (dbname, user) than in your given command?</p>
<p>The best way is to look at your DB with a client to see if the table is already there. Can you do this?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '11, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8509" class="comments-container">
<span id="8510"></span>
<div id="comment-8510" class="comment">
<div id="post-8510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1.Which xml file? Where is it located? What does it represent? I'm new to osm and still trying to figure out how everything works.</p>
</div>
<div id="comment-8510-info" class="comment-info">
<span class="comment-age">(19 Oct '11, 17:10)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8511"></span>
<div id="comment-8511" class="comment">
<div id="post-8511-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>2.Different user? No, i don't think so. I used user prodeng. I hope this following table gives some clarity...<br />
</p>
<pre><code>Database | user | etc|etc|
     gis           | prodeng       | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
     openstreetmap | openstreetmap | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
     osm           | openstreetmap | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
     osm_test      | openstreetmap | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
     postgres      | postgres      | UTF8     | en_US.UTF-8 | en_US.UTF-8 |</code></pre>
</div>
<div id="comment-8511-info" class="comment-info">
<span class="comment-age">(19 Oct '11, 17:11)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8512"></span>
<div id="comment-8512" class="comment">
<div id="post-8512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>3.What table are we looking for?<br />
<img src="/upfiles/Screenshot_1.png" alt="alt text" /></p>
</div>
<div id="comment-8512-info" class="comment-info">
<span class="comment-age">(19 Oct '11, 17:12)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8519"></span>
<div id="comment-8519" class="comment">
<div id="post-8519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li><p>I was talking about the osm.xml that is outputed by <a href="http://generate_xml.py">generate_xml.py</a>.</p></li>
<li><p>On the bottom of your screenshot, there is a node "Tables", check that you have the table "planet_osm_polygon" below</p></li>
<li><p>Can you precise the country you have downloaded?</p></li>
</ol>
</div>
<div id="comment-8519-info" class="comment-info">
<span class="comment-age">(20 Oct '11, 08:42)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="8535"></span>
<div id="comment-8535" class="comment">
<div id="post-8535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li>THat file has a lot of text! I don't think i can copy paste it here.<br />
</li>
<li>At the bottom of my screenshot are 2 table and they are both visible. But in the pg_catalog, with 42 table, there is no such thing as planet_osm_polygon.<br />
</li>
<li>Moldova.</li>
</ol>
</div>
<div id="comment-8535-info" class="comment-info">
<span class="comment-age">(20 Oct '11, 14:55)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
<span id="8536"></span>
<div id="comment-8536" class="comment not_top_scorer">
<div id="post-8536-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li>Use <a href="http://pastebin.com">pastebin.com</a>.</li>
</ol>
</div>
<div id="comment-8536-info" class="comment-info">
<span class="comment-age">(20 Oct '11, 14:58)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="8571"></span>
<div id="comment-8571" class="comment not_top_scorer">
<div id="post-8571-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>here we go. This is osm.xml from my mapnik folder. <a href="http://pastebin.com/1eyEvD8V">http://pastebin.com/1eyEvD8V</a></p>
<p>Btw, i can't generate tiles though i can generate the image.</p>
</div>
<div id="comment-8571-info" class="comment-info">
<span class="comment-age">(21 Oct '11, 10:11)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8509" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-8509-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8530"></span>

<div id="answer-container-8530" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8530-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tables-Section usually holds 9 Entrys: the two shown, and planet_osm_line/nodes/point/polygon/rels/roads and ways. Maybe you should add --prefix planet_osm when importing with osm2pgsql, or look for error messages at this step.</p>
<p>In the tutorial, look at the section Setup PostGIS for OSM</p>
<h1 id="sudo--u-postgres--i">sudo -u postgres -i</h1>
<h1 id="createuser-prodeng">createuser prodeng</h1>
<h1 id="createdb--e-utf8--o-prodeng-gis">createdb -E UTF8 -O prodeng gis</h1>
<h1 id="createlang-plpgsql-gis">createlang plpgsql gis</h1>
<h1 id="exit">exit</h1>
<h1 id="psql--f-usrsharepostgresql8.4contribpostgis.sql--d-gis">psql -f /usr/share/postgresql/8.4/contrib/postgis.sql -d gis</h1>
<h1 id="echo-alter-table-geometry_columns-owner-to-prodeng-alter-table-spatial_ref_sys-owner-to-prodeng-psql--d-gis">echo "ALTER TABLE geometry_columns OWNER TO prodeng; ALTER TABLE spatial_ref_sys OWNER TO prodeng;" | psql -d gis</h1>
<h1 id="psql--f-usrsharepostgresql8.4contrib_int.sql--d-gis">psql -f /usr/share/postgresql/8.4/contrib/_int.sql -d gis</h1>
<h1 id="psql--f-mntbinosm2pgsql900913.sql--d-gis">psql -f /mnt/bin/osm2pgsql/900913.sql -d gis</h1>
<p>are the sql-files in the place where you call them? Otherwise the database is not ready for import.</p>
<p>HTH, ajoessen</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '11, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/baddeab22266e1533be4ba4c9f3deb49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ajoessen&#39;s gravatar image" />
<p><span>ajoessen</span><br />
<span class="score" title="168 reputation points">168</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ajoessen has one accepted answer">9%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Oct '11, 14:10</strong> </span></p>
</div>
</div>
<div id="comments-container-8530" class="comments-container">
<span id="8537"></span>
<div id="comment-8537" class="comment">
<div id="post-8537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, i think everything was done by the tutorial. The files where in place, too.</p>
</div>
<div id="comment-8537-info" class="comment-info">
<span class="comment-age">(20 Oct '11, 14:59)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-8530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8530-form-container" class="comment-form-container">
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

