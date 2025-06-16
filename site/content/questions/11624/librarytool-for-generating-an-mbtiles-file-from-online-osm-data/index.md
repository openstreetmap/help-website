+++
type = "question"
title = "library/tool for generating an MBTiles file from online osm data"
description = '''Hi all, I am aware of TileMill, however, I need a library or tool that can take osm data (from a URL, rather than a local file source) and return an MBTiles file. I would like to create my own application where the user can view an area on the map (I plan on using OpenLayers + data from OpenStreetMa...'''
date = "2012-03-30T06:24:00Z"
lastmod = "2021-08-19T19:48:00Z"
weight = 11624
keywords = [ "generate_tiles", "tilemill", "api", "library", "mbtiles" ]
aliases = [ "/questions/11624" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [library/tool for generating an MBTiles file from online osm data](/questions/11624/librarytool-for-generating-an-mbtiles-file-from-online-osm-data)

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
<span id="post-11624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11624-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am aware of TileMill, however, I need a library or tool that can take osm data (from a URL, rather than a local file source) and return an MBTiles file. I would like to create my own application where the user can view an area on the map (I plan on using OpenLayers + data from OpenStreetMap) and upon selection of an area, the application can call this tool/library and an MBTiles file can be generated and saved locally. I would then use this MBTiles file to display a map to the user when he/she is off-line.</p>
<p>Does such a tool/library exist? Can TileMill offer this functionality via an API?</p>
<p>Thank you,</p>
<p>-f.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_tiles" rel="tag" title="see questions tagged &#39;generate_tiles&#39;">generate_tiles</span> <span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-library" rel="tag" title="see questions tagged &#39;library&#39;">library</span> <span class="post-tag tag-link-mbtiles" rel="tag" title="see questions tagged &#39;mbtiles&#39;">mbtiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '12, 06:24</strong></p>
<img src="https://secure.gravatar.com/avatar/78b0f3c5ce5eaccf8d0e1cd7011d70dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fabasi&#39;s gravatar image" />
<p><span>fabasi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fabasi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Mar '12, 06:25</strong> </span></p>
</div>
</div>
<div id="comments-container-11624" class="comments-container">
&#10;</div>
<div id="comment-tools-11624" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11624-form-container" class="comment-form-container">
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

<span id="11625"></span>

<div id="answer-container-11625" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11625-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like you will either have to download the files first and then use <a href="https://github.com/mapbox/mbutil">mbutil</a> to make an MBTiles file, or you will have to modify that utility to read from the web instead of from a file.</p>
<p>Be aware that while it is ok to use <em>data</em> from OpenStreetMap for your purpose, it is not acceptable that you use the OSM-provided tile server; you will have to set up your own tile server for that. See <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile Usage Policy.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '12, 07:17</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11625" class="comments-container">
<span id="11626"></span>
<div id="comment-11626" class="comment">
<div id="post-11626-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer; that makes sense. I would be happy to setup my own tiles server, if that is what is needed. So in that case, would I download all the data from osm (periodically?), and host that on my own server? What is required to setup a tiles server? I think that an "enhanced" tiles server which generates MBTiles files is essentially what I am trying to build for the project described above.</p>
<p>Cheers,</p>
<p>-f.</p>
</div>
<div id="comment-11626-info" class="comment-info">
<span class="comment-age">(30 Mar '12, 07:50)</span> <span class="comment-user userinfo">fabasi</span>
</div>
</div>
<span id="34782"></span>
<div id="comment-34782" class="comment">
<div id="post-34782-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, planet.osm if 29GB (400GB uncompressed XML) so if possible start from a smaller part; see <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts</a></p>
</div>
<div id="comment-34782-info" class="comment-info">
<span class="comment-age">(09 Jul '14, 22:41)</span> <span class="comment-user userinfo">sesam</span>
</div>
</div>
</div>
<div id="comment-tools-11625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11625-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81373"></span>

<div id="answer-container-81373" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81373-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81373-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81373-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can create MBTiles from any .osm.pbf file using this tool - <a href="https://github.com/systemed/tilemaker">https://github.com/systemed/tilemaker</a></p>
<ol>
<li><p>Download .osm.pbf file from <a href="https://download.geofabrik.de/">Geofabric</a>. To download for a custom area, you can use <a href="https://protomaps.com/extracts">Protomaps</a> or <a href="https://extract.bbbike.org/">BBBike Extract</a></p></li>
<li><p>Download <a href="https://github.com/systemed/tilemaker/releases">tilemaker</a></p></li>
<li><p>Execute the following command</p></li>
</ol>
<p><code>tilemaker --input netherlands.osm.pbf --output netherlands.mbtiles --process resources/process-openmaptiles.lua --config resources/config-openmaptiles.json</code></p>
<p>You can read more about it in this blog post - <a href="https://blog.kleunen.nl/blog/tilemaker-generate-map">https://blog.kleunen.nl/blog/tilemaker-generate-map</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '21, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/79e65eed0a4d543a7229550d59f0e309?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="protos29&#39;s gravatar image" />
<p><span>protos29</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="protos29 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81373" class="comments-container">
&#10;</div>
<div id="comment-tools-81373" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81373-form-container" class="comment-form-container">
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

