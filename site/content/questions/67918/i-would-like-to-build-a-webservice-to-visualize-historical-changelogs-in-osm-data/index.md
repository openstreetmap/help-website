+++
type = "question"
title = "I would like to build a webservice to visualize historical changelogs in OSM data"
description = '''Hello everyone, I am new here and english ist not my native language so I`m sorry for mistakes and inconveniences. I am a college Student of Geoscience and I started a project some weeks ago. I built an Tileserver which gives out a slippy map from some european countries I renderd from osm.pbf files...'''
date = "2019-02-07T00:31:00Z"
lastmod = "2019-02-07T13:40:00Z"
weight = 67918
keywords = [ "rendering", "postgresql", "changes", "mapnik", "history" ]
aliases = [ "/questions/67918" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [I would like to build a webservice to visualize historical changelogs in OSM data](/questions/67918/i-would-like-to-build-a-webservice-to-visualize-historical-changelogs-in-osm-data)

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
<span id="post-67918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67918-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,<br />
I am new here and english ist not my native language so I`m sorry for mistakes and inconveniences.<br />
I am a college Student of Geoscience and I started a project some weeks ago.<br />
I built an Tileserver which gives out a slippy map from some european countries I renderd from osm.pbf files from Geofabrik.de .<br />
It is build on an Ubuntu Server 18.10 LTS, 64Bit, runnig in a VM with an Xeon CPU with 3,70Ghz, but just one Core and 5GB of Ram. It is running an apache server and a Postrgresql-Database with PostGis. I do imports of osm.pbf-files with osm2pgsql, for example Switzerland. For the rendering and tileserving I use Mapnik with renderd and mod_tile. For displaying the map tiles i use Leaflet and Openlayers. It works.</p>
<p>Now i would like to show the change history of nodes, ways and relatives which were done over the last months or years. Something like switzerland on a slippy map and with a manually used switch or slider you can show the same map but a month ago or a year by sliding left or right.<br />
First I thougth about to download the oldest planet.osm.pbf file from Geofabrik.de from 2013, use the tool osmconvert to get the data from switzerland and import this data in Postgresql.<br />
Then render new tiles of the old switzerland dataset and let them be served from a second mod_tile (mod_tile2) directory.<br />
Then I could use a javascript layerswipe in openlayers, to show a map from 2018 and switch to layer upon to show the same map from 2013.<br />
For example like this comparison of OpenStreetMap from 2008 but with a slider - (<a href="http://osmz.ru/osm2008.html#8/47.066/8.550)">http://osmz.ru/osm2008.html#8/47.066/8.550)</a><br />
If this should work i repeat the procedure with 2014, 2015, 2016 and 2017. Starting by every first Planet.osm.pbf of a year.</p>
<p>My real questions are now, how stupid is this idea?<br />
Would this work the way I planned or should I dump this idea?<br />
Where are the problems and risks ... or impossibilities?<br />
Where could I find even older OSM data to work with?<br />
I searched the net for solutions like this but didn`t found a similar procedure.</p>
<p>I know there a better ways to show the history of changes in OSM maps. But I lack the knowledge and the comprehension to get to a complex solution like these ones. And I don`t know if my tileserver as it is now ... and my skills, are suited for these kind of solutions.</p>
<p>A more fashionable solution would be a gif animation like from the gallery of Geofabrik.de to show the historical developement from 2006 to 2009.<br />
<a href="http://www.geofabrik.de/de/gallery/history/index.html">http://www.geofabrik.de/de/gallery/history/index.html</a></p>
<p>I am also very interested in a solution like the awesome project of the user "yogi__ks" as an kind of overlay on a existing map:<br />
<a href="https://www.openstreetmap.org/user/yogi_ks/diary/35067">https://www.openstreetmap.org/user/yogi_ks/diary/35067</a><br />
Will test this out separately on a second VM</p>
<p>I would appreciate every suggestion, scolding or educational web link.</p>
<p>Thank you very much for reading and for responding. And sorry for this amount of text.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '19, 00:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9ef6971262ce33e76c8120425a953ff3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Grohnwald&#39;s gravatar image" />
<p><span>Grohnwald</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Grohnwald has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-67918" class="comments-container">
&#10;</div>
<div id="comment-tools-67918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67918-form-container" class="comment-form-container">
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

<span id="67919"></span>

<div id="answer-container-67919" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67919-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>Maybe a planet file with a full history would be useful to you?</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Planet.osm/full">https://wiki.openstreetmap.org/wiki/Planet.osm/full</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '19, 01:25</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span> </br></br></p>
</div>
</div>
<div id="comments-container-67919" class="comments-container">
<span id="67921"></span>
<div id="comment-67921" class="comment">
<div id="post-67921-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the answer. I stumbled over this idea by my "researches" but I didn't got the comprehension how to show the order of events of changes for months or years from only one planet file. I know there are ways, but I don't know how to perform them with my currently server Setup. Maybe you have link for me which I could follow?</p>
</div>
<div id="comment-67921-info" class="comment-info">
<span class="comment-age">(07 Feb '19, 03:56)</span> <span class="comment-user userinfo">Grohnwald</span>
</div>
</div>
</div>
<div id="comment-tools-67919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67919-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67920"></span>

<div id="answer-container-67920" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67920-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't help with your project but if you only want Switzerland data you can download go here <a href="https://download.geofabrik.de/europe/switzerland.html">https://download.geofabrik.de/europe/switzerland.html</a> and click on "Raw directory index" to get older files going back to 2014.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '19, 02:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a69c47928edc8d3686d5236d45f1f146?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rassilon&#39;s gravatar image" />
<p><span>Rassilon</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rassilon has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-67920" class="comments-container">
<span id="67922"></span>
<div id="comment-67922" class="comment">
<div id="post-67922-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the suggestion. I wanted also to import and render other countries and perform the procedure like on switzerland. But I got problems with my slippymap when I did import and render tiles from osm.pbf files of another country. Some zoomlayers did show blank tiles, some zoomlayers were completely blank. A colleague of mine suggested the reason could be the different timestamp of the different osm_pbf files I used. So thought I extract the data for every country in one mod_tile directory from the same planet file.</p>
</div>
<div id="comment-67922-info" class="comment-info">
<span class="comment-age">(07 Feb '19, 04:21)</span> <span class="comment-user userinfo">Grohnwald</span>
</div>
</div>
</div>
<div id="comment-tools-67920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67920-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67923"></span>

<div id="answer-container-67923" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67923-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The correct resources tools to do this are:</p>
<ul>
<li>Full History files (from Geofabrik)</li>
<li>Osmium or Osmium tool (which can generate a time-snapshot from the .osh file)</li>
</ul>
<p>You should look at MaZderMind's <a href="https://github.com/MaZderMind/osm-history-renderer">GitHub repository</a> too.</p>
<p>The fundamental problem is re-inventing the wheel for osm2pgsql's polygon assembly routines, which is non-trivial (particularly for relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '19, 13:40</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-67923" class="comments-container">
&#10;</div>
<div id="comment-tools-67923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67923-form-container" class="comment-form-container">
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

