+++
type = "question"
title = "Saving map edits to local server"
description = '''Hello I have installed a tile server on my local Ubuntu 12.04 server.  I&#x27;ve used this  http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/ I have slippymap working, it shows only my country, so it is ok. Then I&#x27;ve installed nominatim, it is also ok. Then the Rails Port, that in...'''
date = "2013-02-18T15:43:00Z"
lastmod = "2017-11-24T11:07:00Z"
weight = 20021
keywords = [ "potlatch2", "rendering", "openstreetmap" ]
aliases = [ "/questions/20021" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Saving map edits to local server](/questions/20021/saving-map-edits-to-local-server)

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
<span id="post-20021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20021-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello I have installed a tile server on my local Ubuntu 12.04 server. I've used this <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> I have slippymap working, it shows only my country, so it is ok. Then I've installed nominatim, it is also ok. Then the Rails Port, that includes Potlatch2 inside. Rails port works fine, i've registered potlatch and now I can make changes to the map, put an object for exaple. When I press "Save" - Potlatch says 'Saved'. And I see my changes when I load Potlatch again. But I don't see any changes on my slippymap. So the tiles are the same. How can I detect where the problem is? To what db does potlatch write? When re-rendering should happen? Thanks in advance=)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '13, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a6680dec59d30edf579e1efadbbdf300?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex_Z&#39;s gravatar image" />
<p><span>Alex_Z</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex_Z has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20021" class="comments-container">
<span id="20108"></span>
<div id="comment-20108" class="comment">
<div id="post-20108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have one more idea. There is a place in Rails port install, that I don't understand quite well.</p>
<blockquote>
<p>Populating</p>
<p>To populate a PostgreSQL database using Osmosis from a planet file, do this: osmosis --read-xml-0.6 file="planet.osm.bz2" --write-apidb-0.6 populateCurrentTables=yes host="localhost" database="openstreetmap" user="openstreetmap" password="openstreetmap" validateSchemaVersion=no</p>
<p>Later updates to the database (sometimes referred to as the apidb) will need to use a change format (.osc).</p>
<p>You will need the latest Osmosis to have the right database scheme.</p>
<p>Troubleshooting database population<br />
Running causes the error "Unable to create streaming resultset"</p>
<p>Run osmosis on the database "openstreetmap", e.g. use the command osmosis --rx file="planet.osm" --wd database="openstreetmap" user="openstreetmap" password="openstreetmap" Running causes the error "The database schema version of $1 does not match the expected version of $2"</p>
<p>Assuming that you are using osmosis with the 0.6 db, you can just add validateSchemaVersion=no to the --write-apidb params. Configuring Database to Write</p>
<p>If you intend to write to your database, you will need to reset the auto-increment sequences first (within postgres).</p>
<p>Note: Do this sequence twice, once for openstreetmap, once for osm.</p>
</blockquote>
<p>I did not run this, as the idea is not clear for me. Can it be the root of my problem?</p>
</div>
<div id="comment-20108-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 11:57)</span> <span class="comment-user userinfo">Alex_Z</span>
</div>
</div>
<span id="20161"></span>
<div id="comment-20161" class="comment">
<div id="post-20161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I've made this steps</p>
<p>1.sudo ./osmosis -q --replicate-apidb authFile=~osmosis/authFile.conf allowIncorrectSchemaVersion=true validateSchemaVersion=no --wr workingDirectory=/var/www/replication</p>
<p>2. ./osmosis --read-replication-interval workingDirectory=~/.osmosis/ --simplify-change --write-xml-change ~/.osmosis/changes.osc.gz</p>
<p>I can see my changes in xml format inside this file</p>
<ol>
<li>osm2pgsql --append --slim changes.osc.gz</li>
</ol>
<p>But I'm getting an error</p>
<p>:~/OSMOSIS/osmosis-0.41/bin$ osm2pgsql --append --slim .osmosis/changes.osc.gz osm2pgsql SVN version 0.81.0 (64bit id space)</p>
<p>Using projection SRS 900913 (Spherical Mercator) Setting up table: planet_osm_point NOTICE: table "planet_osm_point_tmp" does not exist, skipping Setting up table: planet_osm_line NOTICE: table "planet_osm_line_tmp" does not exist, skipping Setting up table: planet_osm_polygon NOTICE: table "planet_osm_polygon_tmp" does not exist, skipping Setting up table: planet_osm_roads NOTICE: table "planet_osm_roads_tmp" does not exist, skipping Allocating memory for dense node cache Allocating dense node cache in one big chunk Allocating memory for sparse node cache Sharing dense sparse Node-cache: cache=800MB, maxblocks=102401*8192, allocation method=11 Mid: pgsql, scale=100 cache=800 Setting up table: planet_osm_nodes PREPARE insert_node (int8, int4, int4, text[]) AS INSERT INTO planet_osm_nodes VALUES ($1,$2,$3,$4); PREPARE get_node (int8) AS SELECT lat,lon,tags FROM planet_osm_nodes WHERE id = $1 LIMIT 1; PREPARE delete_node (int8) AS DELETE FROM planet_osm_nodes WHERE id = $1; failed: ERROR: relation "planet_osm_nodes" does not exist LINE 1: ...rt_node (int8, int4, int4, text[]) AS INSERT INTO planet_osm... ^</p>
<p>Error occurred, cleaning up</p>
<p>There is really no table "planet_osm_nodes" in "gis" schema. Should it be there?</p>
</div>
<div id="comment-20161-info" class="comment-info">
<span class="comment-age">(22 Feb '13, 16:13)</span> <span class="comment-user userinfo">Alex_Z</span>
</div>
</div>
</div>
<div id="comment-tools-20021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20021-form-container" class="comment-form-container">
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

<span id="20125"></span>

<div id="answer-container-20125" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20125-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you have two databases or database schemas (one for editing and one for rendering) then you need to setup a tool chain to propagate the changes from the edit-db to the render-db.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '13, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a1156d45a55699715b80fc3cadd0c8d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmehl&#39;s gravatar image" />
<p><span>mmehl</span><br />
<span class="score" title="565 reputation points">565</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmehl has 3 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-20125" class="comments-container">
<span id="20126"></span>
<div id="comment-20126" class="comment">
<div id="post-20126-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>See (as a starting point):</p>
<ul>
<li><a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--replicate-apidb_.28--repa.29">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--replicate-apidb_.28--repa.29</a></li>
<li><a href="https://wiki.openstreetmap.org/wiki/Minutely_Mapnik">https://wiki.openstreetmap.org/wiki/Minutely_Mapnik</a></li>
</ul>
</div>
<div id="comment-20126-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 18:23)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="20128"></span>
<div id="comment-20128" class="comment">
<div id="post-20128-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, links seem to be useful. But can I use just one schema both for rendering and editing?</p>
</div>
<div id="comment-20128-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 18:45)</span> <span class="comment-user userinfo">Alex_Z</span>
</div>
</div>
<span id="20135"></span>
<div id="comment-20135" class="comment">
<div id="post-20135-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nobody has created a tool (yet) to render directly from the apidb schema. The two schemes are very different, as they have different requirements.</p>
</div>
<div id="comment-20135-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 20:45)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-20125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20125-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20024"></span>

<div id="answer-container-20024" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20024-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Check that renderd is running on your machine (probably should add it to startup scripts) and configured correctly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '13, 16:14</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-20024" class="comments-container">
<span id="20025"></span>
<div id="comment-20025" class="comment">
<div id="post-20025-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>renederd feels good, the problem is not here (</p>
</div>
<div id="comment-20025-info" class="comment-info">
<span class="comment-age">(18 Feb '13, 16:19)</span> <span class="comment-user userinfo">Alex_Z</span>
</div>
</div>
<span id="60763"></span>
<div id="comment-60763" class="comment">
<div id="post-60763-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am sorry to ask you question here.But could you tell me how did you sovle that problem,I really need your help. Thanks very much.</p>
</div>
<div id="comment-60763-info" class="comment-info">
<span class="comment-age">(24 Nov '17, 11:07)</span> <span class="comment-user userinfo">gleide</span>
</div>
</div>
</div>
<div id="comment-tools-20024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20024-form-container" class="comment-form-container">
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

