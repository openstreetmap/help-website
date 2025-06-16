+++
type = "question"
title = "[closed] How to Convert .OSM.PBF or .OSM.BZ2 to Geo .Tiff via Command Line"
description = '''How do I convert .osm.pbf or .osm.bz2 http://download.geofabrik.de/africa-latest.osm.bz2. to Geo .tiff via commandline? I want is end results to convert files to .mbtiles. If I have Geo .tiff I can convert using Gdal to .mbtiles easily. This is the response I got from the guys at geofabrik.de.  This...'''
date = "2015-07-30T03:43:00Z"
lastmod = "2015-07-30T03:43:00Z"
weight = 44529
keywords = [ "openstreetmap", "tilemill", ".osm", "gdal", "mbtiles" ]
aliases = [ "/questions/44529" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to Convert .OSM.PBF or .OSM.BZ2 to Geo .Tiff via Command Line](/questions/44529/how-to-convert-osmpbf-or-osmbz2-to-geo-tiff-via-command-line)

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
<span id="post-44529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44529-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I convert .osm.pbf or .osm.bz2 <a href="http://download.geofabrik.de/africa-latest.osm.bz2.">http://download.geofabrik.de/africa-latest.osm.bz2.</a> to Geo .tiff via commandline? I want is end results to convert files to .mbtiles. If I have Geo .tiff I can convert using Gdal to .mbtiles easily. This is the response I got from the guys at geofabrik.de.</p>
<pre><code> This is not so easy. You will want to have different zoom levels
 generated, so it is better to go osm-&gt;mbtiles directly without GDAL and
 GeoTiff. However, osm-&gt;mbtiles requires map rendering and style
 information. If it is for a small area, you can probably use Maperitive
 for this (unsure if it has a command line). Otherwise you will need to
 import OSM data into a PostGIS database, and then you can use e.g.
 Tilemill to batch-process</code></pre>
<p>(Credits Frederik Ramm)</p>
<p>Can someone translate this? How do I import OSM data into PostGIS database. Reference: <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql">https://wiki.openstreetmap.org/wiki/Osm2pgsql</a></p>
<pre><code>osm2pgsql -s -U postgres -d nameofdatabase /file/path/toosm/fileorpbf/name.osm</code></pre>
<p>Will this work for .OSM.PBF?</p>
<p>How do I use a Tilemill to do a batch process? What is the commandline arguments?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-gdal" rel="tag" title="see questions tagged &#39;gdal&#39;">gdal</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jul '15, 03:43</strong></p>
<img src="https://secure.gravatar.com/avatar/614e3e56882743b78234c816965f4040?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chathu&#39;s gravatar image" />
<p><span>Chathu</span><br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chathu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>30 Jul '15, 09:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span></p>
</div>
</div>
<div id="comments-container-44529" class="comments-container">
&#10;</div>
<div id="comment-tools-44529" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44529-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question with just 1 dot extra." by Hendrikklaas 30 Jul '15, 09:40

</div>

</div>

</div>

