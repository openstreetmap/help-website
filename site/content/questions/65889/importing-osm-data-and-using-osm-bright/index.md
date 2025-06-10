+++
type = "question"
title = "Importing OSM data and using OSM-Bright"
description = '''I noticed that the recommended command to import data into the postgresql database from the tutorial here  https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ is  osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C ...'''
date = "2018-09-13T22:25:00Z"
lastmod = "2018-09-18T16:30:00Z"
weight = 65889
keywords = [ "import", "style", "postgresql", "stylesheet" ]
aliases = [ "/questions/65889" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Importing OSM data and using OSM-Bright](/questions/65889/importing-osm-data-and-using-osm-bright)

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
<span id="post-65889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65889-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed that the recommended command to import data into the postgresql database from the tutorial here</p>
<p><a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/"><code>https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</code></a></p>
<p>is</p>
<p><code>osm2pgsql -d gis --create --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/azerbaijan-latest.osm.pbf</code></p>
<p>which lists the openstreetmap-carto style file. The recommended import command for OSM-Bright from</p>
<p><a href="https://github.com/mapbox/osm-bright"><code>https://github.com/mapbox/osm-bright</code></a></p>
<p>is</p>
<p><code>osm2pgsql -c -G -U postgres_user -d postgis_database data.osm.pbf</code></p>
<p>My question is do I need to re-import the raw OSM data into the postgresql database everytime I want to change map styles and specify it during data import? The first tutorial specifies a style in the import command while the OSM-Bright tutorial does not. Thanks for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '18, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/7594614ba848fdde8ac9feb3d91253f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coderunner&#39;s gravatar image" />
<p><span>coderunner</span><br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coderunner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65889" class="comments-container">
&#10;</div>
<div id="comment-tools-65889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65889-form-container" class="comment-form-container">
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

<span id="65953"></span>

<div id="answer-container-65953" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65953-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="coderunner has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer: Yes. There is no need to reimport data.</p>
<p>A style file for osm2pgsql specifies aspects of how osm2pgsql converts OSM data into PostgreSQL tables, how much data is transferred from OSM xml into Postgres database. For example if a style does not display some kind of objects (powerlines, sidewalks etc) there is no much sense in keeping them in the rendering database. By constructing custom style you can filter what objects to include. More on this can be found here: <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql#Import_style">https://wiki.openstreetmap.org/wiki/Osm2pgsql#Import_style</a></p>
<p>Now to compatibility of openstreetmap-carto.style for OSM-Bright. Though default style that comes with osm2pgsql imports more data comparing to openstreetmap-carto (you can take diff of these two styles to see what objects are filtered) OSM-Bright does not use these data. So you can safely use the OSM-Bright style on the same database you made for openstreetmap-carto style. You can look at layers that are used by OSM-bright in this file <a href="https://github.com/mapbox/osm-bright/blob/master/osm-bright/osm-bright.osm2pgsql.mml">https://github.com/mapbox/osm-bright/blob/master/osm-bright/osm-bright.osm2pgsql.mml</a> - look for SQL statements. This is how data is queried from Postgres to Mapnik for rendering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '18, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/2d2131962e32cfde012ed80c5d09db37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="getmaps_io&#39;s gravatar image" />
<p><span>getmaps_io</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="getmaps_io has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-65953" class="comments-container">
<span id="65968"></span>
<div id="comment-65968" class="comment">
<div id="post-65968-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Makes sense, thank you for the explanation of what's going on under the hood. That was very helpful.</p>
</div>
<div id="comment-65968-info" class="comment-info">
<span class="comment-age">(18 Sep '18, 16:30)</span> <span class="comment-user userinfo">coderunner</span>
</div>
</div>
</div>
<div id="comment-tools-65953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65953-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65890"></span>

<div id="answer-container-65890" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65890-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Probably yes. Rendering database is a special purpose database derivative and this can be very different for different styles.</p>
<p>One can make some mappings, but it needs some knowledge about SQL.</p>
<p>Quite simple solution (if you have enough of disc space) is to have more databases and just switch them - this is my rough script for this purpose (gis is default database, gis2 is the second one):</p>
<pre><code>#!/bin/bash
sudo service postgresql restart
sudo -u postgres -H -- psql -c &quot;alter database gis rename to temp;&quot;
sudo -u postgres -H -- psql -c &quot;alter database gis2 rename to gis;&quot;
sudo -u postgres -H -- psql -c &quot;alter database temp rename to gis2;&quot;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '18, 22:43</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '18, 03:29</strong> </span></p>
</div>
</div>
<div id="comments-container-65890" class="comments-container">
<span id="65967"></span>
<div id="comment-65967" class="comment">
<div id="post-65967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is a good idea. Thank you.</p>
</div>
<div id="comment-65967-info" class="comment-info">
<span class="comment-age">(18 Sep '18, 16:30)</span> <span class="comment-user userinfo">coderunner</span>
</div>
</div>
</div>
<div id="comment-tools-65890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65890-form-container" class="comment-form-container">
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

