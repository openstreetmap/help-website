+++
type = "question"
title = "access POI list from remote"
description = '''Hi, not sure I have chosen the best subject. Imagine there is a Leaflet / OSM map on a certain server and it&#x27;s displaying a bunch of POI in my browser - let&#x27;s say all the shops of a company. As a user I can click on them, get details in a small popup etc. I am not into Leaflet, but as far as I can s...'''
date = "2021-05-03T14:47:00Z"
lastmod = "2021-05-06T14:03:00Z"
weight = 79977
keywords = [ "request", "list", "poi" ]
aliases = [ "/questions/79977" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [access POI list from remote](/questions/79977/access-poi-list-from-remote)

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
<span id="post-79977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79977-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>not sure I have chosen the best subject. Imagine there is a Leaflet / OSM map on a certain server and it's displaying a bunch of POI in my browser - let's say all the shops of a company. As a user I can click on them, get details in a small popup etc.</p>
<p>I am not into Leaflet, but as far as I can see, everything seems to be made via Javascript / Ajax requests. I would like to "read" the list of POI via PHP from that server without "having to deal" with the map itself. How? Any advise appreciated.</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 May '21, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/b90963059b3808a4a6911aff320b1b05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="humpataa&#39;s gravatar image" />
<p><span>humpataa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="humpataa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79977" class="comments-container">
&#10;</div>
<div id="comment-tools-79977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79977-form-container" class="comment-form-container">
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

<span id="80030"></span>

<div id="answer-container-80030" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80030-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The list of POI is probably in a geojson, or GPX file. You'll have to read the code to find the path. Or you can check the calls in the network tab of the developer tab of your browser.</p>
<p>Please share the url of the map if you want more specific help.</p>
<p>Also be aware that it's probably illegal to scrape data this way, it should be mentioned in the ToS of the website. If your usecase is legitimate, you should contact them to have confirmation.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '21, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-80030" class="comments-container">
&#10;</div>
<div id="comment-tools-80030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80030-form-container" class="comment-form-container">
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

