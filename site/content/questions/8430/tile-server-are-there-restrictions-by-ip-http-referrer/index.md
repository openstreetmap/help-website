+++
type = "question"
title = "Tile Server - Are there restrictions by IP / HTTP Referrer?"
description = '''Hi, We are using the Openlayers in a web application we have developed and are pulling tiles from tile.openstreetmap.org. We expect the our app to only produce a relatvely low volume of traffic. From the tile usage policy I understand there are limited resources etc.. in terms of usage does anyone k...'''
date = "2011-10-13T12:14:00Z"
lastmod = "2011-10-13T15:54:00Z"
weight = 8430
keywords = [ "tiles", "server" ]
aliases = [ "/questions/8430" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Tile Server - Are there restrictions by IP / HTTP Referrer?](/questions/8430/tile-server-are-there-restrictions-by-ip-http-referrer)

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
<span id="post-8430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8430-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>We are using the Openlayers in a web application we have developed and are pulling tiles from <a href="http://tile.openstreetmap.org">tile.openstreetmap.org</a>. We expect the our app to only produce a relatvely low volume of traffic.</p>
<p>From the tile usage policy I understand there are limited resources etc.. in terms of usage does anyone know if there are restrictions in the number of 'concurrent' connections which can be made to this resource either by 'IP' or 'HTTP Referrer' where by no tiles would be returned based on the number of connections/IP/users alone? i.e. could the situation arise where x number of my users are quite happily receiving map tiles then when x + 1 tried to access the tile server they could not.</p>
<p>Regards</p>
<p>John</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '11, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/569344db98e03e54adaa0756f214bca0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnsmacd&#39;s gravatar image" />
<p><span>johnsmacd</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnsmacd has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8430" class="comments-container">
&#10;</div>
<div id="comment-tools-8430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8430-form-container" class="comment-form-container">
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

<span id="8431"></span>

<div id="answer-container-8431" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8431-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-8431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="johnsmacd has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are currently two different kinds of server protection measures in place.</p>
<p>One is a "delay pool" that will slow down requests deemed excessive, but never block them completely. The exact configuration of these is not revealed and may change at any time.</p>
<p>The other is a manual blocking of certain requests (be that by IP, Referer, access pattern or whatever) by the admins. Such a block would lead to you not receiving any tiles, or receiving a tile with an error message, and these blocks are usually made when an admin finds excessive requests in the log files. Again, what exactly is deemed excessive is not revealed, but an app that requests a few thousand tiles each day will certainly fly below the radar.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '11, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-8431" class="comments-container">
<span id="8433"></span>
<div id="comment-8433" class="comment">
<div id="post-8433-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you.</p>
</div>
<div id="comment-8433-info" class="comment-info">
<span class="comment-age">(13 Oct '11, 15:04)</span> <span class="comment-user userinfo">johnsmacd</span>
</div>
</div>
</div>
<div id="comment-tools-8431" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8431-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8434"></span>

<div id="answer-container-8434" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8434-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-8434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use tiles from other sources. MapQuest open renders tiles from OSM data using their own style and they have no restrictions on the usage of their tiles. You can of course render your own tiles, but managing the infrastructure to do that is more than some people want to do. There are companies which will render and host tiles based on OSM too, for a fee of course.</p>
<p>Anyone writing an app may be surprised by its popularity. Even if your intended audience is small it is best to write into the app a means of switching the source of tiles dynamically, controlled centrally, so that if it suddenly become popular you can direct the traffic to another site to use tiles from there. Expecting users to change the URL or needing to download a new version to redirect the app to a new source is not good enough - it takes too long and in the meantime your app may be blocked, your users annoyed and the volunteer OSM admins put to unnecessary work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '11, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-8434" class="comments-container">
&#10;</div>
<div id="comment-tools-8434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8434-form-container" class="comment-form-container">
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

