+++
type = "question"
title = "Convert areas to lines with relations (iD)"
description = '''This is a bit complex, so please bear with me... I&#x27;m mapping the Serbia-Hungary border area using iD, and the country border normally splits a lot of administrative units from both sides of the border. Those are properly mapped using boundary lines involved as &quot;outer&quot; in a bunch of relations. So far...'''
date = "2018-12-01T11:43:00Z"
lastmod = "2018-12-03T02:15:00Z"
weight = 67024
keywords = [ "ideditor", "large_area", "relations", "area" ]
aliases = [ "/questions/67024" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Convert areas to lines with relations (iD)](/questions/67024/convert-areas-to-lines-with-relations-id)

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
<span id="post-67024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67024-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is a bit complex, so please bear with me... I'm mapping the Serbia-Hungary border area using iD, and the country border normally splits <strong>a lot</strong> of administrative units from both sides of the border. Those are properly mapped using boundary lines involved as "outer" in a bunch of relations. So far, so good.</p>
<p>However, someone has added a lot of Hungarian geophysical regions as iD Areas (find e.g. "Bácskai löszös síkság"), snapped to one another and, worse still, snapped to the country border as well (the latter is my own fault, many changesets ago, when I started the task but was still learning).</p>
<p>I would like to "convert" those areas to lines using proper boundary relations shared with other administrative regions, but I can't easily get rid of those areas (which are huge). As a result, I have a lot of overlapping lines at the country border, which are now a PITA to work with. For example, see <a href="https://www.openstreetmap.org/edit#map=19/46.03993/19.10457">https://www.openstreetmap.org/edit#map=19/46.03993/19.10457</a> - I can't unjoin the "Bácskai" boundary anymore because that node's edges are part of 30-odd relations that I don't feel like deleting and restoring.</p>
<p>Any advice is welcome. At minimum, I would like a way to unjoin just the selected line's edges from a node (as in the URL above), without touching the edges participating in relations. And an advice how to delete a REALLY long line using iD (constantly being hit by "This can't be deleted because not enough of it is currently visible.")</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-large_area" rel="tag" title="see questions tagged &#39;large_area&#39;">large_area</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Dec '18, 11:43</strong></p>
<img src="https://secure.gravatar.com/avatar/82883dda6a3f6ad7a7c74d15cfd24e43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Duja&#39;s gravatar image" />
<p><span>Duja</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Duja has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67024" class="comments-container">
<span id="67031"></span>
<div id="comment-67031" class="comment">
<div id="post-67031-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>you seem to really want to stick with iD - any specific reason for this? Why the hard way, when there is JOSM... really.</p>
</div>
<div id="comment-67031-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 21:26)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67032"></span>
<div id="comment-67032" class="comment">
<div id="post-67032-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"How to do it in iD" is still a reasonable question, even if iD wouldn't be the first choice of editor for doing this sort of thing.</p>
</div>
<div id="comment-67032-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 21:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67033"></span>
<div id="comment-67033" class="comment">
<div id="post-67033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: I did not claim anything else. :-)</p>
</div>
<div id="comment-67033-info" class="comment-info">
<span class="comment-age">(01 Dec '18, 22:06)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="67041"></span>
<div id="comment-67041" class="comment">
<div id="post-67041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I've just learned iD's ins, outs &amp; quirks, as well as most of basic OSM concepts, so I don't feel like switching to an entirely new environment. But I understand that iD simply wasn't designed with advanced stuff in mind, so not everything is actually doable there. In any case, thanks for the responses; I guess there's no rush to fix that, I have some 10,000 km2 to go to fix other stuff.</p>
</div>
<div id="comment-67041-info" class="comment-info">
<span class="comment-age">(02 Dec '18, 19:29)</span> <span class="comment-user userinfo">Duja</span>
</div>
</div>
<span id="67043"></span>
<div id="comment-67043" class="comment">
<div id="post-67043-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15986/duja">@Duja</a>: thanks for your comment. Yes, iD was (and is - AFAIK) designed to be simple to start with. I seldom use iD, so it is possible that your request is somehow doable in iD (let's wait for answers).</p>
</div>
<div id="comment-67043-info" class="comment-info">
<span class="comment-age">(02 Dec '18, 19:53)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67024" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67024-form-container" class="comment-form-container">
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

<span id="67046"></span>

<div id="answer-container-67046" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67046-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can convince iD to convert an area to a relation by combining it with another area (just draw a temporary area, combine them, delete the temp from the relation, delete the temp). Then you can split the line and merge parts with other boundaries and so on.</p>
<p>The guardrails that prevent editing large features will probably make such edits pretty tedious. They are tedious in any editor though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '18, 02:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-67046" class="comments-container">
&#10;</div>
<div id="comment-tools-67046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67046-form-container" class="comment-form-container">
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

