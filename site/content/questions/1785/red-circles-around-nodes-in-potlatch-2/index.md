+++
type = "question"
title = "Red circles around nodes in Potlatch 2"
description = '''Can anyone explain to me why I&#x27;m seeing this strange &quot;rendering&quot; in Potlatch 2? It happens to me only for one particular way. '''
date = "2010-12-12T19:54:00Z"
lastmod = "2011-04-12T11:02:00Z"
weight = 1785
keywords = [ "potlatch2" ]
aliases = [ "/questions/1785" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Red circles around nodes in Potlatch 2](/questions/1785/red-circles-around-nodes-in-potlatch-2)

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
<span id="post-1785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1785-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can anyone explain to me why I'm seeing this strange "rendering" in Potlatch 2? It happens to me only for <a href="https://www.openstreetmap.org/browse/way/88004479">one particular way</a>.</p>
<p><img src="http://i.imgur.com/CTSVI.png" alt="Screenshot" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '10, 19:54</strong></p>
<img src="https://secure.gravatar.com/avatar/b0d98734d95fa6d3fed729b2a919855d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fluteflute&#39;s gravatar image" />
<p><span>fluteflute</span><br />
<span class="score" title="731 reputation points">731</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fluteflute has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '10, 19:55</strong> </span></p>
</div>
</div>
<div id="comments-container-1785" class="comments-container">
&#10;</div>
<div id="comment-tools-1785" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1785-form-container" class="comment-form-container">
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

<span id="1786"></span>

<div id="answer-container-1786" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1786-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-1786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fluteflute has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Those red circles mean there are duplicate nodes there, ie several nodes with exactly the same coordinates.</p>
<p>Checking that location, it looks like the way for the school is duplicated. See <a href="https://www.openstreetmap.org/browse/way/88004479/history">way 88004479</a> and <a href="https://www.openstreetmap.org/browse/way/88004554/history">way 88004554</a>. They both have the same tags, and both have nodes in the same locations, so these nodes are duplicates. So if you just delete one of those ways, it will fix the problem (and get rid of the red circles in Potlatch).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '10, 21:32</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-1786" class="comments-container">
<span id="4408"></span>
<div id="comment-4408" class="comment">
<div id="post-4408-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would like to clean up, and keep/merge into the most informative node. So how do I get a list of the modes at such a point? so I can delete the lesser informative nodes.</p>
</div>
<div id="comment-4408-info" class="comment-info">
<span class="comment-age">(12 Apr '11, 10:33)</span> <span class="comment-user userinfo">jarl</span>
</div>
</div>
<span id="4409"></span>
<div id="comment-4409" class="comment">
<div id="post-4409-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you click on the way links above it lists the member nodes. If they are part of a way that represents a school though it is unlikely (but not impossible) that the nodes contain any tags of their own.</p>
</div>
<div id="comment-4409-info" class="comment-info">
<span class="comment-age">(12 Apr '11, 11:02)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-1786" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1786-form-container" class="comment-form-container">
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

