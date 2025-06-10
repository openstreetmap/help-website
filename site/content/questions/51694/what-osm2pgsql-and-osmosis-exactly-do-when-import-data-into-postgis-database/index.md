+++
type = "question"
title = "What osm2pgsql and osmosis exactly do when import data into postgis database?"
description = '''I have set up the rails port on ubuntu14.04, and then I build my local tile server under the instruction of &quot;Manually building a tile server (14.04)&quot;. And I have changed the OSM map to my local tile server. The nominatim is still use the http://nominatim.openstreetmap.org/ I have dowmloaded the beij...'''
date = "2016-08-24T10:31:00Z"
lastmod = "2016-08-24T10:31:00Z"
weight = 51694
keywords = [ "osm2pgsql", "osmosis" ]
aliases = [ "/questions/51694" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What osm2pgsql and osmosis exactly do when import data into postgis database?](/questions/51694/what-osm2pgsql-and-osmosis-exactly-do-when-import-data-into-postgis-database)

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
<span id="post-51694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51694-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have set up the rails port on ubuntu14.04, and then I build my local tile server under the instruction of "<a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">Manually building a tile server (14.04)</a>". And I have changed the OSM map to my local tile server. The nominatim is still use the <a href="http://nominatim.openstreetmap.org/">http://nominatim.openstreetmap.org/</a></p>
<p>I have dowmloaded the beijing_china.osm.pbf data file from the <a href="https://mapzen.com/data/metro-extracts/metro/beijing_china/">Metro Extracts</a>, then i use osm2pgsql to import data into the tile server database,such as "<strong>osm2pgsql --slim -d gis -C 1600 --number-processes 3 /usr/local/share/maps/planet/beijing_china.osm.pbf</strong>", and i use osmosis to import data into the rails port database,such as "<strong>./osmosis-latest/bin/osmosis --read-pbf /home/osm/planet/beijing_china.osm.pbf --write-apidb host="localhost" database="openstreetmap" user="osm" password="buaanlp" validateSchemaVersion="no"</strong>". What confuse me is that the table structure in this two database is quite different, then how could it use the same data file to import data?</p>
<p>The table structure in the rails port database and in the tile server database can be showed as blow.</p>
<p>rails port database</p>
<p><img src="http://help.openstreetmap.org/upfiles/osmdb.png" alt="alt text" /></p>
<p>tile server database</p>
<p><img src="http://help.openstreetmap.org/upfiles/R2K9W%60PLHG7280%5D80%7D0E2E6.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '16, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</img>
</div>
</div>
<div id="comments-container-51694" class="comments-container">
&#10;</div>
<div id="comment-tools-51694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51694-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

