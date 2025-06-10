+++
type = "question"
title = "Conditional destination"
description = '''Hello, there. I sometimes encounter destination signs like the ones on the right of this picture: these signs say that Vesoul and Mulhouse should be reached by HGV by taking the street ahead, and that Nancy and Chaumont should be reached by HGV by taking the street on the right. My question is: how ...'''
date = "2020-07-21T13:30:00Z"
lastmod = "2020-07-21T22:55:00Z"
weight = 75831
keywords = [ "restrictions", "destination", "conditional", "signs" ]
aliases = [ "/questions/75831" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Conditional destination](/questions/75831/conditional-destination)

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
<span id="post-75831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75831-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, there.</p>
<p>I sometimes encounter destination signs like the ones on the right of <a href="https://www.mapillary.com/map/im/mo0AKf9masIEfpJtySH8fw">this picture</a>: these signs say that Vesoul and Mulhouse should be reached by HGV by taking the street ahead, and that Nancy and Chaumont should be reached by HGV by taking the street on the right. My question is: how should I map these destination signs? In several cases, these restrictions are enforced on a road segment on the way to the signed destination, but it is not always the case: in this case, the restrictions are not really enforced along the route; they merely say <em>the road network manager prefer HGV to follow these roads</em>. Therefore, I cannot apply the destination restriction elsewhere, I must map the destination <em>and</em> the restriction at this junction, but how?</p>
<p>Awaiting your answers,</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span> <span class="post-tag tag-link-destination" rel="tag" title="see questions tagged &#39;destination&#39;">destination</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span> <span class="post-tag tag-link-signs" rel="tag" title="see questions tagged &#39;signs&#39;">signs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '20, 13:30</strong></p>
<img src="https://secure.gravatar.com/avatar/03b6014ac927da400a55374bbbe5152a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Penegal&#39;s gravatar image" />
<p><span>Penegal</span><br />
<span class="score" title="631 reputation points">631</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Penegal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75831" class="comments-container">
&#10;</div>
<div id="comment-tools-75831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75831-form-container" class="comment-form-container">
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

<span id="75843"></span>

<div id="answer-container-75843" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>6 instances <code>hgv=*</code> has been used on <code>type=destination_sign</code> relations, compared to ~3k <code>foot=*</code> and ~1k <code>bicycle=*</code>. (Former favors <code>hgv=designated</code>, latter <code>hgv=yes</code>. Someone for you to decide I guess.) Thereby, you can tag <code>destination=</code> in its usual keys.</p>
<p><code>destination:hgv=</code> (13 instances), alongside <code>destination:bicycle=</code> (~150 instances) etc, was suggested before. Not very relevant for an intersection here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '20, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '20, 23:04</strong> </span></p>
</div>
</div>
<div id="comments-container-75843" class="comments-container">
&#10;</div>
<div id="comment-tools-75843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75843-form-container" class="comment-form-container">
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

