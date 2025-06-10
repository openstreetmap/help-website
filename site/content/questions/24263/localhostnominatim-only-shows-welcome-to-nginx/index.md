+++
type = "question"
title = "[closed] localhost/nominatim only shows &quot;Welcome to nginx!&quot;"
description = '''Hello OpenStreetMap experts, I downloaded and installed Nomiatim and some openstreetmap data and indexed. It showed once the map after failing indexing. Once I indexed some data, however, it only shows the page &quot;Welcome to nginx!&quot;, nothing else, what could be the problem? Thanks! TJ'''
date = "2013-07-15T15:31:00Z"
lastmod = "2013-07-17T19:08:00Z"
weight = 24263
keywords = [ "map", "nominatim", "nginx" ]
aliases = [ "/questions/24263" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] localhost/nominatim only shows "Welcome to nginx!"](/questions/24263/localhostnominatim-only-shows-welcome-to-nginx)

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
<span id="post-24263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24263-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OpenStreetMap experts,</p>
<p>I downloaded and installed Nomiatim and some openstreetmap data and indexed. It showed once the map after failing indexing. Once I indexed some data, however, it only shows the page "Welcome to nginx!", nothing else, what could be the problem?</p>
<p>Thanks! TJ</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-nginx" rel="tag" title="see questions tagged &#39;nginx&#39;">nginx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jul '13, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/1586020f0a016a46e7c9a46dbdbd7d66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSM-TJ2013&#39;s gravatar image" />
<p><span>OSM-TJ2013</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSM-TJ2013 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>17 Jul '13, 21:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span></p>
</div>
</div>
<div id="comments-container-24263" class="comments-container">
<span id="24264"></span>
<div id="comment-24264" class="comment">
<div id="post-24264-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please add to your question information about which URL exactly you are calling in your browser to test it.</p>
</div>
<div id="comment-24264-info" class="comment-info">
<span class="comment-age">(15 Jul '13, 15:55)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24263" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24263-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The problem got it's solution." by RM87 17 Jul '13, 21:37

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24274"></span>

<div id="answer-container-24274" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24274-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Never mind, guys. I think it is due to the port conflict between apache and nginx. Nominatim works even without nginx (at least for my use case :)).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jul '13, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/1586020f0a016a46e7c9a46dbdbd7d66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSM-TJ2013&#39;s gravatar image" />
<p><span>OSM-TJ2013</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSM-TJ2013 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24274" class="comments-container">
<span id="24325"></span>
<div id="comment-24325" class="comment">
<div id="post-24325-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I misunderstood the menu actually. Nominatim could use either apache or nginx.</p>
</div>
<div id="comment-24325-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 19:08)</span> <span class="comment-user userinfo">OSM-TJ2013</span>
</div>
</div>
</div>
<div id="comment-tools-24274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24274-form-container" class="comment-form-container">
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

