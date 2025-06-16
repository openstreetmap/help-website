+++
type = "question"
title = "Setting up own OSM Server / Mirror Server"
description = '''I have the idea to setup my own Server with osm data so i dont have to take the server power from osm to download my maps to my android phone (locus). as an &quot;output&quot; i want to use the data on locus in sqlite format, not tiles. i tried to set up an ubuntu machine with help of the following instructio...'''
date = "2011-05-13T16:39:00Z"
lastmod = "2011-05-13T19:01:00Z"
weight = 5170
keywords = [ "android", "own", "private", "server", "locus" ]
aliases = [ "/questions/5170" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Setting up own OSM Server / Mirror Server](/questions/5170/setting-up-own-osm-server-mirror-server)

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
<span id="post-5170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5170-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the idea to setup my own Server with osm data so i dont have to take the server power from osm to download my maps to my android phone (locus). as an "output" i want to use the data on locus in sqlite format, not tiles.</p>
<p>i tried to set up an ubuntu machine with help of the following instructions: <a href="https://wiki.openstreetmap.org/wiki/The_Rails_Port">https://wiki.openstreetmap.org/wiki/The_Rails_Port</a> <a href="https://wiki.openstreetmap.org/wiki/Rails_on_Ubuntu">https://wiki.openstreetmap.org/wiki/Rails_on_Ubuntu</a> <a href="http://weait.com/content/build-your-own-openstreetmap-server">http://weait.com/content/build-your-own-openstreetmap-server</a></p>
<p>all i get to now is what you can see here: <a href="http://217.92.52.58/">http://217.92.52.58/</a> im kinda stuck now and hope to get some help over here</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-own" rel="tag" title="see questions tagged &#39;own&#39;">own</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-locus" rel="tag" title="see questions tagged &#39;locus&#39;">locus</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '11, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/5dda103dd13c2b35de9b65383c18c068?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sebbo&#39;s gravatar image" />
<p><span>sebbo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sebbo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5170" class="comments-container">
&#10;</div>
<div id="comment-tools-5170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5170-form-container" class="comment-form-container">
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

<span id="5171"></span>

<div id="answer-container-5171" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5171-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As I understand it Locus caches tiles rather than vector data in its sqlite database. You do not need the rails port to render tiles, just Postgres+Postgis and Mapnik are required.</p>
<p>For a limited area you might choose to generate all tiles using the <a href="http://generate_tiles.py"><code>generate_tiles.py</code></a> python script provided with mapnik. For larger areas some kind of selectivity for tile generation is useful using <a href="https://wiki.openstreetmap.org/wiki/Mod_tile">mod_tile</a> and renderd/<a href="https://wiki.openstreetmap.org/wiki/Tirex">tirex</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '11, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-5171" class="comments-container">
&#10;</div>
<div id="comment-tools-5171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5171-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5172"></span>

<div id="answer-container-5172" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5172-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>so i just need this: <a href="http://weait.com/content/build-your-own-openstreetmap-server">http://weait.com/content/build-your-own-openstreetmap-server</a></p>
<p>but how do i continue after that. i dont get it on how to use the <a href="http://generate_tiles.py">generate_tiles.py</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '11, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/5dda103dd13c2b35de9b65383c18c068?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sebbo&#39;s gravatar image" />
<p><span>sebbo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sebbo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5172" class="comments-container">
<span id="5173"></span>
<div id="comment-5173" class="comment">
<div id="post-5173-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I cant remember if you change the params in the file or add them on the command line, but basically you choose a bounding box + two tile levels and it will generate all the tiles for those levels &amp; bbox. You need to say which directory to use (usually tiles in the mapnik root). A useful set might be from z10 to z13 for a 1 degree square.</p>
</div>
<div id="comment-5173-info" class="comment-info">
<span class="comment-age">(13 May '11, 19:01)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-5172" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5172-form-container" class="comment-form-container">
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

