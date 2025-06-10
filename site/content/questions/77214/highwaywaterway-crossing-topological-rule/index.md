+++
type = "question"
title = "Highway/waterway crossing topological rule"
description = '''JOSM complains that a highway (highway=residential) crosses an underground waterway (waterway=stream; tunnel=culvert). Since the two don’t actually “touch”, do I need to add a node to make them connect anyway? Any available topological rules I should be aware of? Thank'''
date = "2020-10-24T13:21:00Z"
lastmod = "2020-10-26T18:54:00Z"
weight = 77214
keywords = [ "crossing", "josm", "waterway", "highway" ]
aliases = [ "/questions/77214" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Highway/waterway crossing topological rule](/questions/77214/highwaywaterway-crossing-topological-rule)

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
<span id="post-77214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77214-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>JOSM complains that a highway (highway=residential) crosses an underground waterway (waterway=stream; tunnel=culvert). Since the two don’t actually “touch”, do I need to add a node to make them connect anyway? Any available topological rules I should be aware of?</p>
<p>Thank</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '20, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a504353df13461ace2c733906a99ce16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfd553&#39;s gravatar image" />
<p><span>jfd553</span><br />
<span class="score" title="389 reputation points">389</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfd553 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77214" class="comments-container">
&#10;</div>
<div id="comment-tools-77214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77214-form-container" class="comment-form-container">
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

<span id="77215"></span>

<div id="answer-container-77215" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77215-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77215-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-77215-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfd553 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, just add layer=-1 on the culvert. This shows the relation between the two objects, (the highway implied as layer=0 with the culvert below tagged layer=-1).</p>
<p>Just looked and see you need the layer=-1 on both culverts. Also I notice the stream is joined to the Rue du Pavillon.</p>
<p>Sorry I mistakenly put a comment on the changeset instead of answering here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '20, 13:44</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Oct '20, 18:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-77215" class="comments-container">
<span id="77250"></span>
<div id="comment-77250" class="comment">
<div id="post-77250-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just to be clear, the tag that should be used here is "layer", not "level".</p>
</div>
<div id="comment-77250-info" class="comment-info">
<span class="comment-age">(26 Oct '20, 16:09)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="77255"></span>
<div id="comment-77255" class="comment">
<div id="post-77255-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've fixed the use of level instead of layer.</p>
</div>
<div id="comment-77255-info" class="comment-info">
<span class="comment-age">(26 Oct '20, 18:54)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-77215" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77215-form-container" class="comment-form-container">
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

