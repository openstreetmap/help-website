+++
type = "question"
title = "Detection of direction of one way streets"
description = '''If one way street is going from south to north(longitude will be increasing) will the node references in the Way of that street will be such that the longitude of the first node ref is minimum and the longitude of the last node ref will be max. In short are the node ref in Way of &quot;one way&quot; roads alo...'''
date = "2012-08-23T14:17:00Z"
lastmod = "2012-08-24T05:40:00Z"
weight = 15450
keywords = [ "roads", "tags", "road", "oneway" ]
aliases = [ "/questions/15450" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Detection of direction of one way streets](/questions/15450/detection-of-direction-of-one-way-streets)

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
<span id="post-15450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If one way street is going from south to north(longitude will be increasing) will the node references in the Way of that street will be such that the longitude of the first node ref is minimum and the longitude of the last node ref will be max. In short are the node ref in Way of "one way" roads along the direction of that road?<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-oneway" rel="tag" title="see questions tagged &#39;oneway&#39;">oneway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '12, 14:17</strong></p>
<img src="https://secure.gravatar.com/avatar/73bfa9669a927682b021cd4e2132047c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jawadch&#39;s gravatar image" />
<p><span>jawadch</span><br />
<span class="score" title="121 reputation points">121</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jawadch has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Aug '12, 14:19</strong> </span></p>
</div>
</div>
<div id="comments-container-15450" class="comments-container">
<span id="15454"></span>
<div id="comment-15454" class="comment">
<div id="post-15454-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think that that's probably answered on <a href="/questions/15442/detection-of-intersections-in-the-maps">this related question</a>.</p>
</div>
<div id="comment-15454-info" class="comment-info">
<span class="comment-age">(23 Aug '12, 15:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15450-form-container" class="comment-form-container">
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

<span id="15463"></span>

<div id="answer-container-15463" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15463-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jawadch has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes. Technically, the order of the nd-entries in the way is what matters. The only exception is <code>oneway=-1</code> where it is in the opposite direction. <a href="https://wiki.openstreetmap.org/wiki/Key:oneway">https://wiki.openstreetmap.org/wiki/Key:oneway</a> tells you the details.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '12, 05:40</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-15463" class="comments-container">
&#10;</div>
<div id="comment-tools-15463" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15463-form-container" class="comment-form-container">
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

