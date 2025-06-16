+++
type = "question"
title = "Size of files"
description = '''Hello - this is for an iPad3 with GPS. I want to use the iPad as a navigator. Download a mapset, go to a city, and navigate without using a wireless network. Totally autonomous. Let&#x27;s use Rome, Italy a an example. There are third party applications that use OSM datasets. I&#x27;m OK with that. There are ...'''
date = "2012-04-15T06:00:00Z"
lastmod = "2012-04-17T07:55:00Z"
weight = 12026
keywords = [ "download", "times", "file", "size" ]
aliases = [ "/questions/12026" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Size of files](/questions/12026/size-of-files)

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
<span id="post-12026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12026-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello - this is for an iPad3 with GPS. I want to use the iPad as a navigator. Download a mapset, go to a city, and navigate without using a wireless network. Totally autonomous. Let's use Rome, Italy a an example. There are third party applications that use OSM datasets. I'm OK with that. There are three questions: (1) What is the size of OSM files needed for street-level detail for a city like Rome, (2) would downloading this dataset impact the operation of OSM, and (3) is there a time of day that is most appropriate for downloading a file like this?<br />
</p>
<p>thanks,</p>
<p>Bob</p>
<p>Bainbridge Island, WA (US) --- Close to Seattle</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-times" rel="tag" title="see questions tagged &#39;times&#39;">times</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '12, 06:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef75dbb6fabb67987158f3d5607c636?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BainbridgeBob&#39;s gravatar image" />
<p><span>BainbridgeBob</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BainbridgeBob has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-12026" class="comments-container">
&#10;</div>
<div id="comment-tools-12026" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12026-form-container" class="comment-form-container">
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

<span id="12027"></span>

<div id="answer-container-12027" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12027-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are different ways of downloading OSM data. One way is using ready-made "map tiles" like you see them in your browser. The other is downloading the raw data and using a suitable vector rendering software on the device. Existing applications on the iPad use either of these methods (see <a href="https://wiki.openstreetmap.org/wiki/IPad">Wiki</a> for a list of applications) but those downloading tiles are not well liked for reasons given below.</p>
<p><strong>Question 1:</strong></p>
<p>If you are talking tile data, this depends on what you mean by "street-level detail" and what area exactly you want. Let's assume you mean zoom level 17:</p>
<p><img src="http://a.tile.openstreetmap.org/17/70083/48709.png" alt="zoom level 17" /></p>
<p>Let's assume you want the area inside the motorway circle in this tile:</p>
<p><img src="http://a.tile.openstreetmap.org/10/547/380.png" alt="zoom level 10" /></p>
<p>The tile above is a zoom level 10 tile. You want approximately half of a zoom level 10 tile. Since each zoom level means 4 times the number of tiles, you can calculate like this: 0.5 tiles on z10 is 2 tiles on z11, 8 on z12, 32 on z13, 128 on z14, 512 on z15, 2048 on z16, 8192 on z17. Since you will probably want <em>all</em> these zoom levels, you're looking at roughly 10k tiles altogehter. Now the size of the PNG files varies depending on how much is on them, but for this area, I guess you'll end up with an average of about 8 KB per tile, so you're looking at a data volume of about 80 MB.</p>
<p>The <a href="http://tools.geofabrik.de/map/?type=Geofabrik&amp;lon=12.46295&amp;lat=41.89141&amp;zoom=12&amp;grid=1">map on the Geofabrik web site</a> is a good tool for getting familiar with tiles and zoom levels because you can display a tile coordinate grid on top of the map there.</p>
<p>If you are talking vector data, then - depending on how densely the area is mapped - the same area should take about 20 MB in our raw "osm.pbf" format but you will not be able to simply download it; you will have to download a larger file (there are ready-made files for various countries or continents) and then cut out the region of interest from that file. You will then be responsible for rendering the data yourself which will <em>usually</em> encompass converting from .osm.pbf to something usable for map drawing. Existing vector drawing software like e.g. Navit does exactly that.</p>
<p>For raw data download sources, see <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">the Planet.osm wiki page</a>.</p>
<p><strong>Questions 2 and 3:</strong></p>
<p>If you are talking tiles, then downloading this data set would violate OSM's <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">Tile Usage Policy</a>. While our tile server usually is less busy when it is night in Europe:</p>
<p><img src="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/mod_tile_response-day.png" alt="tilesever munin graph" /></p>
<p>we would still ask people who need that amount of tiles to either produce them themselves (by downloading the raw data and setting up a rendering engine) or get them from another source. Teh aforementioned policy has links to alternative sources.</p>
<p>If you are talking vector data, then it does not matter when you download it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '12, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Apr '12, 19:51</strong> </span></p>
</div>
</div>
<div id="comments-container-12027" class="comments-container">
<span id="12067"></span>
<div id="comment-12067" class="comment">
<div id="post-12067-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Frederik, you start your answer assuming what he wants to download is tiles. He asks for a <em>map</em>: why not propose him the vectorial map, that he'd use with an appropriate viewer? That's what Lambertus is doing weekly outputting Garmin versions of the whole world, region by region, so I presume there must be a way to just get the map, without the transformation into Garmin? (Indeed most probably there exist iPad apps that do manage it all, it's just I'm no iPad expert...) Hervé</p>
</div>
<div id="comment-12067-info" class="comment-info">
<span class="comment-age">(16 Apr '12, 19:37)</span> <span class="comment-user userinfo">Herve5</span>
</div>
</div>
<span id="12068"></span>
<div id="comment-12068" class="comment">
<div id="post-12068-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Indeed. Thank you Herve5, I will modify my answer accordingly.</p>
</div>
<div id="comment-12068-info" class="comment-info">
<span class="comment-age">(16 Apr '12, 19:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="12075"></span>
<div id="comment-12075" class="comment">
<div id="post-12075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Note that, at least for Navit, you <em>can</em> download vector data for just an area you choose (no need to download planet.osm). That's what <a href="http://maps.navit-project.org/">http://maps.navit-project.org/</a> is for.</p>
</div>
<div id="comment-12075-info" class="comment-info">
<span class="comment-age">(17 Apr '12, 07:55)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-12027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12027-form-container" class="comment-form-container">
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

