+++
type = "question"
title = "Osm tile server slow"
description = '''Hi all I want to build an android app using osm data. I have a tile server (followed : http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/) 1 core, 4 GB ram, 60 GB storage. (im using only 32MB raw osm data)  I need help with 2 things: 1) the rendering time for a tile is very l...'''
date = "2014-05-01T13:15:00Z"
lastmod = "2014-05-01T14:37:00Z"
weight = 32793
keywords = [ "performance", "tileserver" ]
aliases = [ "/questions/32793" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osm tile server slow](/questions/32793/osm-tile-server-slow)

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
<span id="post-32793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32793-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I want to build an android app using osm data.</p>
<p>I have a tile server (followed : <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/)">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/)</a></p>
<p>1 core, 4 GB ram, 60 GB storage. (im using only 32MB raw osm data)</p>
<p>I need help with 2 things:</p>
<p>1) the rendering time for a tile is very long, can take 10 sec. what can be the cause? (I checked my cache - only 32K)</p>
<p>.......... [question deleted] .................</p>
<p>Thank you all</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '14, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/f4891fcd3cba8f6e43f1b7828e32d8bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shmuli&#39;s gravatar image" />
<p><span>Shmuli</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shmuli has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 May '14, 14:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-32793" class="comments-container">
&#10;</div>
<div id="comment-tools-32793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32793-form-container" class="comment-form-container">
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

<span id="32794"></span>

<div id="answer-container-32794" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32794-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please do not ask two different question in one posting, I'll split it up now for you.</p>
<p>As to 1) you need to tell us which zoom levels you are talking about. Lower zoom levels will be slower than higher ones, so depending on what you are looking at 10s might be quite ok (given that you are not running a hi spec machine).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 May '14, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-32794" class="comments-container">
&#10;</div>
<div id="comment-tools-32794" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32794-form-container" class="comment-form-container">
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

