+++
type = "question"
title = "Increase Tile Cache Value"
description = '''Hi, I have my own OSM server in use, which I created according to the following instructions.  https://switch2osm.org/manually-building-a-tile-server-18-04-lts/ Everything works fine, but I don&#x27;t find a place where I can increase the value of the Tile caches.  According to the HTTP Response Header t...'''
date = "2019-03-04T11:29:00Z"
lastmod = "2019-03-04T11:33:00Z"
weight = 68245
keywords = [ "tilecache" ]
aliases = [ "/questions/68245" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Increase Tile Cache Value](/questions/68245/increase-tile-cache-value)

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
<span id="post-68245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68245-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have my own OSM server in use, which I created according to the following instructions. <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a></p>
<p>Everything works fine, but I don't find a place where I can increase the value of the Tile caches. According to the HTTP Response Header the Cache for the Tiles are only Cached for about 5 Hours.</p>
<p>Response Header: Cache-Control: max-age=18065</p>
<p>At which point can I adjust this value so that the tiles are cached longer?</p>
<p>Thanks Hans</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilecache" rel="tag" title="see questions tagged &#39;tilecache&#39;">tilecache</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '19, 11:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0a617eab91f8135ff9cb328209be67f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tiblak1&#39;s gravatar image" />
<p><span>Tiblak1</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tiblak1 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68245" class="comments-container">
&#10;</div>
<div id="comment-tools-68245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68245-form-container" class="comment-form-container">
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

<span id="68246"></span>

<div id="answer-container-68246" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68246-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68246-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68246-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Tiblak1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The mod_tile configuration offers a multitude of options to control caching duration: <a href="https://github.com/openstreetmap/mod_tile/blob/master/debian/tileserver_site.conf#L51-L111">https://github.com/openstreetmap/mod_tile/blob/master/debian/tileserver_site.conf#L51-L111</a></p>
<p>Note that all this does not control how long a meta tile is cached on the server (meta tiles do not expire, ever) - it only controls how long the client is going to treat a response as up-to-date.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '19, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68246" class="comments-container">
&#10;</div>
<div id="comment-tools-68246" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68246-form-container" class="comment-form-container">
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

