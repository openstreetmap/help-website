+++
type = "question"
title = "Multipolygon render issue"
description = '''I&#x27;ve been editing a river with JOSM here, the relation is a multipolygon tagged as a waterway=riverbank. The problem is if I close the outer way in a only one way the render doesn&#x27;t show the inner ways, but if I split the the outer way in two ways like this and this the render shows every inner way ...'''
date = "2017-06-05T19:44:00Z"
lastmod = "2017-06-05T20:12:00Z"
weight = 56457
keywords = [ "josm", "riverbank", "render", "multipolygon" ]
aliases = [ "/questions/56457" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Multipolygon render issue](/questions/56457/multipolygon-render-issue)

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
<span id="post-56457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56457-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been editing a <a href="https://www.openstreetmap.org/way/23733695">river</a> with JOSM <a href="https://www.openstreetmap.org/#map=15/2.0634/22.6955">here</a>, <a href="https://www.openstreetmap.org/relation/385069">the relation</a> is a multipolygon tagged as a waterway=riverbank. The problem is if I <strong>close</strong> the outer way in a <em>only one way</em> the render doesn't show the inner ways, but if I <strong>split</strong> the the outer way in two ways like <a href="https://www.openstreetmap.org/way/23733695">this</a> and <a href="https://www.openstreetmap.org/way/498248278">this</a> the render shows every inner way like the islets. Why this happen in the render? Thanks for the help! I speak spanish C:</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jun '17, 19:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ca31deab650da597ab68e1f5d1c05af2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="diegodeg58&#39;s gravatar image" />
<p><span>diegodeg58</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="diegodeg58 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56457" class="comments-container">
&#10;</div>
<div id="comment-tools-56457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56457-form-container" class="comment-form-container">
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

<span id="56458"></span>

<div id="answer-container-56458" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56458-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="diegodeg58 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The outer ways are tagged with natural=water. When you join the two into a closed way, that way is then rendered as a solid body of water, ignoring the relation and its inners. All you need to do is remove natural=water from the outer way(s).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '17, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-56458" class="comments-container">
<span id="56459"></span>
<div id="comment-56459" class="comment">
<div id="post-56459-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for fast answer! It's fixed!</p>
</div>
<div id="comment-56459-info" class="comment-info">
<span class="comment-age">(05 Jun '17, 20:12)</span> <span class="comment-user userinfo">diegodeg58</span>
</div>
</div>
</div>
<div id="comment-tools-56458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56458-form-container" class="comment-form-container">
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

