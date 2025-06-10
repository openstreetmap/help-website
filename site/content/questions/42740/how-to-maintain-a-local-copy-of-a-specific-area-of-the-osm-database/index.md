+++
type = "question"
title = "How to maintain a local copy of a specific area of the OSM database"
description = '''I would like to maintain a partial mirror of the OSM database, so to be able to keep - and to fetch only the updates - of that specific area, that would be custom (the Alpine area) without the need to maintain a copy of the whole world. One purpose of that, would be to monitor daily changes for that...'''
date = "2015-04-30T14:27:00Z"
lastmod = "2015-04-30T15:43:00Z"
weight = 42740
keywords = [ "download", "area", "osm", "update", "database" ]
aliases = [ "/questions/42740" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to maintain a local copy of a specific area of the OSM database](/questions/42740/how-to-maintain-a-local-copy-of-a-specific-area-of-the-osm-database)

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
<span id="post-42740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42740-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to maintain a partial mirror of the OSM database, so to be able to keep - and to fetch only the updates - of that specific area, that would be custom (the Alpine area) without the need to maintain a copy of the whole world.</p>
<p>One purpose of that, would be to monitor daily changes for that area (simply out of curiosity), another - way more important - would be to be able to generate mapsforge map files that are very up-do-date without downloading the whole data for the area any time.</p>
<p>I was only able to find how to run a complete Planet mirror though. Is it possible to only mirror a part of the Planet? If so, how?</p>
<p>If that's not possible, what is the best way to keep a local OSM copy and fetch only the updates whenever I want to? There is plenty of documentation out there, but I am unable to realize what is the best road to follow (ie overpass vs postgresql, as far as I was able to understand). Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Apr '15, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/f022cde4d2a5b09ac1f52026b9b4b458?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Superfebs&#39;s gravatar image" />
<p><span>Superfebs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Superfebs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42740" class="comments-container">
&#10;</div>
<div id="comment-tools-42740" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42740-form-container" class="comment-form-container">
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

<span id="42743"></span>

<div id="answer-container-42743" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42743-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-42743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ol>
<li>create sub-section of planet file ("alpine.osm.pbf" or so) with osmosis and the --bp task (requires a .poly file describing the area)</li>
<li>create initial state.txt file for osmosis replication (file must contain timestamp of when your base snapshot was taken)</li>
<li>initialize osmosis replication (--rrii)</li>
<li>run osmosis to update your file like so: <code>osmosis --rri --simc --read-pbf alpine.osm.pbf --ac --bp file=alpine.poly clipIncompleteEntities=yes --write-pbf alpine-new.osm.pbf</code></li>
<li><code>mv alpine-new.osm.pbf alpine.osm.pbf</code> (or you can even compute the differences before you do)</li>
<li>goto 4 as often as you want</li>
</ol>
<p>This method downloads the world-wide diffs, applies them to your file (so that for a moment a new tree mapped in South America would be added) but then immediately cuts out your area of interest again so that only the bits that apply to your area are saved, and you will always have a current .osm.pbf file of your region.</p>
<p>Import into a database with osm2pgsql at will, but it's not necessary. Depends on what you want to do with the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '15, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42743" class="comments-container">
<span id="42744"></span>
<div id="comment-42744" class="comment">
<div id="post-42744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I'll tackle one step at a time. For what matters the first one, is there any GUI tool to generate a .poly file? (Sorry, I am a newbie).</p>
</div>
<div id="comment-42744-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 14:59)</span> <span class="comment-user userinfo">Superfebs</span>
</div>
</div>
<span id="42745"></span>
<div id="comment-42745" class="comment">
<div id="post-42745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10923/superfebs">@Superfebs</a>: I guess <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format">https://wiki.openstreetmap.org/wiki/Osmosis/Polygon_Filter_File_Format</a> will help you with this</p>
</div>
<div id="comment-42745-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 15:24)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42747"></span>
<div id="comment-42747" class="comment">
<div id="post-42747-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There is also good advice here: <a href="http://wiki.openstreetmap.org/wiki/User:EdLoach#Osmosis_to_keep_a_local_copy_of_a_.osm_file_updated">http://wiki.openstreetmap.org/wiki/User:EdLoach#Osmosis_to_keep_a_local_copy_of_a_.osm_file_updated</a> and Zverik's tools are very useful <a href="https://github.com/Zverik/regional">https://github.com/Zverik/regional</a> particularly limit_osc.py.</p>
<p>JOSM or QGIS can be used to create .poly files</p>
</div>
<div id="comment-42747-info" class="comment-info">
<span class="comment-age">(30 Apr '15, 15:43)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42743-form-container" class="comment-form-container">
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

