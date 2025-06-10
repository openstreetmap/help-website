+++
type = "question"
title = "renderd / mod_tile socket protocol"
description = '''Hi, I am looking to understand the protocol between renderd and mod_tile. I can capture the data thats going across the network, thats easy, and I have found this https://github.com/openstreetmap/mod_tile/blob/master/protocol.h but of course that does not tell me how the c variables translate into b...'''
date = "2013-07-21T17:03:00Z"
lastmod = "2014-10-19T18:10:00Z"
weight = 24406
keywords = [ "renderd", "protocol", "mod_tile" ]
aliases = [ "/questions/24406" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [renderd / mod_tile socket protocol](/questions/24406/renderd-mod_tile-socket-protocol)

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
<span id="post-24406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24406-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am looking to understand the protocol between renderd and mod_tile. I can capture the data thats going across the network, thats easy, and I have found this <a href="https://github.com/openstreetmap/mod_tile/blob/master/protocol.h">https://github.com/openstreetmap/mod_tile/blob/master/protocol.h</a> but of course that does not tell me how the c variables translate into bits on the network and I am unable to find much more with Google.</p>
<p>Any documentation on what mod_tile sends down the socket to renderd and what renderd sends back would be very helpful.</p>
<p>Thanks</p>
<p>Scott</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '13, 17:03</strong></p>
<img src="https://secure.gravatar.com/avatar/b46466f8e6ef72cc352e347c1c34794f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott07&#39;s gravatar image" />
<p><span>Scott07</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott07 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24406" class="comments-container">
&#10;</div>
<div id="comment-tools-24406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24406-form-container" class="comment-form-container">
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

<span id="24408"></span>

<div id="answer-container-24408" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24408-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Scott07 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The struct you're seeing in protocol.h is what gets sent over the network, verbatim. See <a href="https://github.com/openstreetmap/mod_tile/blob/master/mod_tile.c#L216">https://github.com/openstreetmap/mod_tile/blob/master/mod_tile.c#L216</a> which does the sending. The same struct is used as a return message, see <a href="https://github.com/openstreetmap/mod_tile/blob/master/mod_tile.c#L246">https://github.com/openstreetmap/mod_tile/blob/master/mod_tile.c#L246</a> which receives the message.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '13, 19:24</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24408" class="comments-container">
&#10;</div>
<div id="comment-tools-24408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24408-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37750"></span>

<div id="answer-container-37750" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37750-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-37750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="http://www.volkerschatz.com/net/osm/renderd.html">http://www.volkerschatz.com/net/osm/renderd.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '14, 18:10</strong></p>
<img src="https://secure.gravatar.com/avatar/949ad6078b25df082120f77160e39877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mat42x&#39;s gravatar image" />
<p><span>mat42x</span><br />
<span class="score" title="16 reputation points">16</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mat42x has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37750" class="comments-container">
&#10;</div>
<div id="comment-tools-37750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37750-form-container" class="comment-form-container">
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

