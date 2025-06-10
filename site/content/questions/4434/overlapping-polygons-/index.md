+++
type = "question"
title = "overlapping polygons - ?"
description = '''I am new here, so please bear with me: I am trying to fix a series of buildings that have somehow become &quot;members&quot; of a landuse multipolygon (making for strange rendering in some circumstances) - I would like to extract them as independant elements. Yet should I do so, if I understand correctly, I c...'''
date = "2011-04-12T18:48:00Z"
lastmod = "2011-04-12T19:57:00Z"
weight = 4434
keywords = [ "building", "landuse", "overlap", "multipolygon" ]
aliases = [ "/questions/4434" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [overlapping polygons - ?](/questions/4434/overlapping-polygons-)

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
<span id="post-4434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4434-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am new here, so please bear with me: I am trying to fix a series of buildings that have somehow become "members" of a landuse multipolygon (making for strange rendering in some circumstances) - I would like to extract them as independant elements. Yet should I do so, if I understand correctly, I cannot just place the building over the land-use multipolygon, I must cut a hole in it the same shape of the building, then place the building over the hole - is this correct? Or is there a simpler solution?</p>
<p>Thanks in advance,</p>
<p>ThePromenader.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '11, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/52a6a6b11937c74b955186933f651b8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThePromenader&#39;s gravatar image" />
<p><span>ThePromenader</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThePromenader has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4434" class="comments-container">
&#10;</div>
<div id="comment-tools-4434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4434-form-container" class="comment-form-container">
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

<span id="4436"></span>

<div id="answer-container-4436" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4436-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general you shouldn't simply place objects "over" larger objects if they replace larger object. So you create a small <code>landuse=industrial</code> area on top of a large town with <code>landuse=residential</code> but use the multipolygon hole-with-fill methode you mentioned. Buildings however often don't really displace the landuse. So you don't have to cut tons of little hole in the <code>landuse=residential</code> area to place little <code>building=yes</code> areas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '11, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-4436" class="comments-container">
&#10;</div>
<div id="comment-tools-4436" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4436-form-container" class="comment-form-container">
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

