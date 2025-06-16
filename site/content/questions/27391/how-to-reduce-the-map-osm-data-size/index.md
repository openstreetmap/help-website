+++
type = "question"
title = "how to reduce the map OSM data size"
description = '''Right now we are using Bing Map Web Services API for Map/geocoding/reverse geocoing at our application. Our application is installed on premise and so we are evaluating some on premise replacement. Based on current research, OpenStreetMap should be a good candidate for this purpose, however I found ...'''
date = "2013-10-21T18:44:00Z"
lastmod = "2020-08-17T15:24:00Z"
weight = 27391
keywords = [ "planet_osm" ]
aliases = [ "/questions/27391" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [how to reduce the map OSM data size](/questions/27391/how-to-reduce-the-map-osm-data-size)

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
<span id="post-27391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27391-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Right now we are using Bing Map Web Services API for Map/geocoding/reverse geocoing at our application. Our application is installed on premise and so we are evaluating some on premise replacement. Based on current research, OpenStreetMap should be a good candidate for this purpose, however I found out this from <a href="https://wiki.openstreetmap.org/wiki/Downloading_data">OpenStreetMap dowloading data</a></p>
<blockquote>
<p>The entire planet is a huge amount of data. Common tools like Osmosis or various import tools for database imports and converters usually need several days to process it, even on fast computers.</p>
<p>This is almost 27 GB compressed or 370 GB uncompressed XML.</p>
</blockquote>
<p>The file size is quite huge for an on premise installation and plus long time to load data into database.</p>
<p>We don't need all layers of the data, just wonder if there is any simple approach we would strip the data to just show the road Map.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Oct '13, 18:44</strong></p>
<img src="https://secure.gravatar.com/avatar/5ffe5210d371a39b69484258062a94f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="windfly&#39;s gravatar image" />
<p><span>windfly</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="windfly has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27391" class="comments-container">
&#10;</div>
<div id="comment-tools-27391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27391-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="27406"></span>

<div id="answer-container-27406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27406-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-27406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The exact space required will vary with what are you import and how you import it. I wouldn't regard the decompressed XML size as too relevant because a) virtually no one decompress the XML for the planet to disk and b) you should use the .pbf formatted data, not the .osm.bz2 formatted data because PBF is a much faster format to process, and smaller too.</p>
<p>I've also updated the wiki page with more accurate speeds.</p>
<p>If you want to render tiles on-demand with the standard setup you need an osm2pgsql database. I <a href="https://lists.openstreetmap.org/pipermail/talk/2013-August/068108.html">posted two months ago details of the space required</a>. It is possible to run a rendering server off of one 7200 RPM hard drive, but it won't be super-fast.</p>
<p>Rendering and geocoding are normally run on separate servers because they need independent databases - a database structured for one is not structured for the other. I don't have the same experience with nominatim as I do with osm2pgsql and rendering, but poldi, the server powering nominatim.osm.org, has a <a href="http://munin.openstreetmap.org/openstreetmap/poldi.openstreetmap/postgres_size_nominatim_9_1_main.html">1TB database</a>.</p>
<p>A rendering database takes under a day to import on reasonably powerful hardware.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '13, 08:45</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-27406" class="comments-container">
&#10;</div>
<div id="comment-tools-27406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27406-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27395"></span>

<div id="answer-container-27395" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27395-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> ... maybe needs osmconvert first do work via a speedy data format</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '13, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-27395" class="comments-container">
&#10;</div>
<div id="comment-tools-27395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27395-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27396"></span>

<div id="answer-container-27396" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27396-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The easiest way to slim down OSM data is by region instead of by feature class, so if you can work with e.g. "just Europe" or "just North America" then you'll already save a lot.</p>
<p>Pre-filtering by feature is possible (using e.g. the Osmosis or osmfilter tools) but it is not straightforward. Some in-depth knowledge will be required to actually define what exactly you want - these tools don't take "just the road map" for an answer. Does that include the traffic light, the barrier, the turning circle?</p>
<p>A typical "tile server" is based on a PostgreSQL database. You could set up a full rendering server on a big machine connected to the Internet, and then export from that a - regional or thematic - subset to deploy on your on-site server. Since the on-site subset wouldn't have to be updatable, this would incur significant space savings.</p>
<p>Another option is to pre-produce ready-made map tiles on a big machine and store them on the on-site machine. This works if you only need a regional extract or only a limited amount of detail, e.g. the world down to zoom level 12 or so.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '13, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-27396" class="comments-container">
<span id="27402"></span>
<div id="comment-27402" class="comment">
<div id="post-27402-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Between the unwanted history, type of data, and type of use, you can reduce the needed size drastically. The initial whole-world import takes a lot of time, but keeping it up to date is easyer.</p>
<p>Do your initial importing and filtering on a smalish country, like Denmark. You'll be able to iterate faster and get a proper estimate of what <em>you</em> will need once you add France, then Europe, then the rest of the world.</p>
</div>
<div id="comment-27402-info" class="comment-info">
<span class="comment-age">(21 Oct '13, 22:03)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="27426"></span>
<div id="comment-27426" class="comment">
<div id="post-27426-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, at this point, it won't be on one country. it is the whole world since this would be installed on customer on premise env and we don't know what country they would need</p>
</div>
<div id="comment-27426-info" class="comment-info">
<span class="comment-age">(22 Oct '13, 22:20)</span> <span class="comment-user userinfo">windfly</span>
</div>
</div>
</div>
<div id="comment-tools-27396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27396-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76162"></span>

<div id="answer-container-76162" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76162-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi I solved this and wrote an Medium article how to do this. Hope it will help:</p>
<p><a href="https://medium.com/dac-technology-blog/openstreetmap-map-size-reduction-guide-43372bbf38c9">https://medium.com/dac-technology-blog/openstreetmap-map-size-reduction-guide-43372bbf38c9</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '20, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/30591e74ea983d1d5f193b588868c497?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JacekDAC&#39;s gravatar image" />
<p><span>JacekDAC</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JacekDAC has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76162" class="comments-container">
&#10;</div>
<div id="comment-tools-76162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76162-form-container" class="comment-form-container">
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

