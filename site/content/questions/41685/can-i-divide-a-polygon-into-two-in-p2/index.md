+++
type = "question"
title = "Can I divide a polygon into two in P2?"
description = '''Hi all! I haven&#x27;t succeeded in finding out how to divide a polygon, e.g. a lake, into two in order to be able to have different names on different parts of the polygon. I am using Potlatch2. Is it at all possible?'''
date = "2015-03-13T15:13:00Z"
lastmod = "2015-03-13T16:04:00Z"
weight = 41685
keywords = [ "potlatch2", "editing", "polygon", "divide" ]
aliases = [ "/questions/41685" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I divide a polygon into two in P2?](/questions/41685/can-i-divide-a-polygon-into-two-in-p2)

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
<span id="post-41685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41685-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all! I haven't succeeded in finding out how to divide a polygon, e.g. a lake, into two in order to be able to have different names on different parts of the polygon. I am using Potlatch2. Is it at all possible?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-divide" rel="tag" title="see questions tagged &#39;divide&#39;">divide</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '15, 15:13</strong></p>
<img src="https://secure.gravatar.com/avatar/ee36eca105728c1d226d30cb7a86a47f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RogerE&#39;s gravatar image" />
<p><span>RogerE</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RogerE has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Mar '15, 16:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41685" class="comments-container">
&#10;</div>
<div id="comment-tools-41685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41685-form-container" class="comment-form-container">
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

<span id="41686"></span>

<div id="answer-container-41686" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41686-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-41686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No, there's no explicit function in P2 to do that. You can split the polygon at the relevant nodes (by clicking on them and pressing 'X' or using the scissors icon) and rejoin, but that's likely to be a bit of a faff, especially if there's a multipolygon involved. I believe JOSM's utilsplugin2 has a "split area" function but I haven't tried it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '15, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-41686" class="comments-container">
<span id="41687"></span>
<div id="comment-41687" class="comment">
<div id="post-41687-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Split areas works really well, and is one of the things I'll fire JOSM up to do if I have more than one or two polygons to split.</p>
</div>
<div id="comment-41687-info" class="comment-info">
<span class="comment-age">(13 Mar '15, 16:04)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41686" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41686-form-container" class="comment-form-container">
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

