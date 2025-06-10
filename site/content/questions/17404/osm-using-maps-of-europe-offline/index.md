+++
type = "question"
title = "OSM - using maps of Europe offline"
description = '''I like to use OSM-maps of Europe in an own applications. At run time, however, there is never an online connection to the Internet. Therefore, I must use the maps offline. Unfortunately, the maps (for now) are too large to store. Max. available disk space is 15 GB. Although I only need roads + terra...'''
date = "2012-11-02T12:00:00Z"
lastmod = "2012-11-05T17:28:00Z"
weight = 17404
keywords = [ "osm-maps" ]
aliases = [ "/questions/17404" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OSM - using maps of Europe offline](/questions/17404/osm-using-maps-of-europe-offline)

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
<span id="post-17404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17404-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I like to use OSM-maps of Europe in an own applications. At run time, however, there is never an online connection to the Internet. Therefore, I must use the maps offline.</p>
<p>Unfortunately, the maps (for now) are too large to store. Max. available disk space is 15 GB. Although I only need roads + terrain (no point of views, gas stations, etc.).</p>
<p>I test Mapnik but I didn´t find a solution to compress the maps effective. It would be no problem to install a web server in addition to my program and get the tiles as png (or other) from there. But the disk space required may just not be larger 15 GB !</p>
<p>Any help ist appreciated. Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm-maps" rel="tag" title="see questions tagged &#39;osm-maps&#39;">osm-maps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '12, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/70f20a209a1ae9e9739c0f0042687700?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="goulasch&#39;s gravatar image" />
<p><span>goulasch</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="goulasch has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17404" class="comments-container">
<span id="17492"></span>
<div id="comment-17492" class="comment">
<div id="post-17492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>no other hints ?</p>
</div>
<div id="comment-17492-info" class="comment-info">
<span class="comment-age">(05 Nov '12, 12:10)</span> <span class="comment-user userinfo">goulasch</span>
</div>
</div>
</div>
<div id="comment-tools-17404" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17404-form-container" class="comment-form-container">
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

<span id="17406"></span>

<div id="answer-container-17406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17406-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should look into vector rendering options. Gosmore, for example, can put the whole planet into a 15 GB binary file and render from there; other options exist as well and which one you choose probably depends on your platform and programming language of choice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '12, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17406" class="comments-container">
<span id="17410"></span>
<div id="comment-17410" class="comment">
<div id="post-17410-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thx for the fast answer.</p>
<p>I think Gosmore is a viewer. I need an app/web server with an API in C++ in order to obtain the desired map tiles to present in my app.</p>
</div>
<div id="comment-17410-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 13:22)</span> <span class="comment-user userinfo">goulasch</span>
</div>
</div>
</div>
<div id="comment-tools-17406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17406-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17499"></span>

<div id="answer-container-17499" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17499-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="http://wiki.openstreetmap.org/wiki/Tilemill">Tilemill</a> or other solutions from Mapbox.</p>
<p>There are more hints and howto at their website.</p>
<p>Maybe you can use Tilemill by keeping OSM data (after filtering) in a database and do a realtime rendering?</p>
<p>Or look for their application "Tilestream"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '12, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '12, 17:32</strong> </span></p>
</div>
</div>
<div id="comments-container-17499" class="comments-container">
&#10;</div>
<div id="comment-tools-17499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17499-form-container" class="comment-form-container">
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

