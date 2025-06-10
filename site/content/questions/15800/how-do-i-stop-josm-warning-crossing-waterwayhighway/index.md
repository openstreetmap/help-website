+++
type = "question"
title = "How do I stop Josm warning &quot;crossing waterway/highway&quot;?"
description = '''Using JOSM 5485 I have copied someone else&#x27;s method for a tiny road bridge over a stream. I cut the road way, added in a new small section a few metres either side of the stream. I kept the keys of the original way; &quot;highway=residential&quot;, &quot;name=rue de boyaval&quot; and a relation to walking route. I adde...'''
date = "2012-09-04T20:38:00Z"
lastmod = "2012-09-04T21:27:00Z"
weight = 15800
keywords = [ "bridge", "waterway", "warning", "highway", "josm" ]
aliases = [ "/questions/15800" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I stop Josm warning "crossing waterway/highway"?](/questions/15800/how-do-i-stop-josm-warning-crossing-waterwayhighway)

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
<span id="post-15800-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15800-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15800-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using JOSM 5485 I have copied someone else's method for a tiny road bridge over a stream. I cut the road way, added in a new small section a few metres either side of the stream. I kept the keys of the original way; "highway=residential", "name=rue de boyaval" and a relation to walking route.</p>
<p>I added "bridge=yes" to the section. Every time I try to upload to openstreetmap I get a warning message saying "crossing waterway/highway" - which of course I do know, being a bridge.</p>
<p>What am I doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-warning" rel="tag" title="see questions tagged &#39;warning&#39;">warning</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '12, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/014348ec5fb64c8b7718ff7ae2e19bdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Electrotechie&#39;s gravatar image" />
<p><span>Electrotechie</span><br />
<span class="score" title="121 reputation points">121</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Electrotechie has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15800" class="comments-container">
&#10;</div>
<div id="comment-tools-15800" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15800-form-container" class="comment-form-container">
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

<span id="15802"></span>

<div id="answer-container-15802" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15802-score" class="post-score" title="current number of votes">
11
</div>
<span id="post-15802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds like you just need layer=1</p>
<p>You can read more about the bridge and layer tags here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Key:bridge">Key:bridge</a></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Key:layer">Key:layer</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '12, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/b9a8b8a3b1418b4b0bb41041555b18a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dymo12&#39;s gravatar image" />
<p><span>Dymo12</span><br />
<span class="score" title="796 reputation points">796</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dymo12 has 2 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-15802" class="comments-container">
<span id="15803"></span>
<div id="comment-15803" class="comment">
<div id="post-15803-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Some users think that bridge/tunnel automatically imply layer=1/layer=-1 but this is not the case. They always have to be added, sometimes even with other values depending on additionally crossing ways.</p>
</div>
<div id="comment-15803-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 21:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="15804"></span>
<div id="comment-15804" class="comment">
<div id="post-15804-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Many thanks, that resolved the problem.</p>
</div>
<div id="comment-15804-info" class="comment-info">
<span class="comment-age">(04 Sep '12, 21:27)</span> <span class="comment-user userinfo">Electrotechie</span>
</div>
</div>
</div>
<div id="comment-tools-15802" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15802-form-container" class="comment-form-container">
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

