+++
type = "question"
title = "How to tag the maxheight of a bridge if the sign is on the bridge?"
description = '''I don&#x27;t know which is the correct way to tag the maximum height limit for vehicles using a highway, if the maxheight sign is on the bridge. 1 Do I tag the bridge? highway=primary  bridge=yes  layer=1  maxheight=3.8 m 2 Do I tag the road below the bridge? highway=primary  maxheight=3.8 m  There is al...'''
date = "2020-11-11T06:09:00Z"
lastmod = "2020-11-16T04:04:00Z"
weight = 77499
keywords = [ "bridge", "maxheight", "highway" ]
aliases = [ "/questions/77499" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag the maxheight of a bridge if the sign is on the bridge?](/questions/77499/how-to-tag-the-maxheight-of-a-bridge-if-the-sign-is-on-the-bridge)

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
<span id="post-77499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77499-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I don't know which is the correct way to tag the maximum height limit for vehicles using a highway, if the maxheight sign is on the bridge.</p>
<p>1 Do I tag the bridge?</p>
<p>highway=primary<br />
bridge=yes<br />
layer=1<br />
maxheight=3.8 m</p>
<p>2 Do I tag the road below the bridge?</p>
<p>highway=primary<br />
maxheight=3.8 m</p>
<p><img src="https://help.openstreetmap.org/upfiles/Mapillary.png" alt="This is a sample image of a bridge with a maxheight sign" /></p>
<p>There is also the tag maxheight:physical. Which to use?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-maxheight" rel="tag" title="see questions tagged &#39;maxheight&#39;">maxheight</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '20, 06:09</strong></p>
<img src="https://secure.gravatar.com/avatar/6783b46d5425152bbb4fc48e90eb279a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdelatorre&#39;s gravatar image" />
<p><span>mdelatorre</span><br />
<span class="score" title="177 reputation points">177</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdelatorre has no accepted answers">0%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '20, 06:11</strong> </span></p>
</div>
</div>
<div id="comments-container-77499" class="comments-container">
&#10;</div>
<div id="comment-tools-77499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77499-form-container" class="comment-form-container">
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

<span id="77500"></span>

<div id="answer-container-77500" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77500-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-77500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to tag the road below. If necessary split the road in three pieces at the points where the road passes underneath the bridge. Then tag the piece underneath the bridge with the maxheight. In your case it looks like the road is not made as access to any other place except going forward. So it might be ok to tag the whole stretch of the road with the maxheight (assuming a truck with more than 3m would not use this road to go anywhere else than pass under the bridge).</p>
<p>Use <code>maxheight</code>. This is the main tag used by routers. <code>maxheight:physical</code>could be used if legal and physical maxheight differ.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '20, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</div>
</div>
<div id="comments-container-77500" class="comments-container">
<span id="77562"></span>
<div id="comment-77562" class="comment">
<div id="post-77562-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help!</p>
</div>
<div id="comment-77562-info" class="comment-info">
<span class="comment-age">(16 Nov '20, 04:04)</span> <span class="comment-user userinfo">mdelatorre</span>
</div>
</div>
</div>
<div id="comment-tools-77500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77500-form-container" class="comment-form-container">
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

