+++
type = "question"
title = "Adding Trail Segment on Roadway"
description = '''Hello - What are the mechanical steps to show a trail segment (Path) following a portion of an existing paved roadway? I can see examples of this is my area (the OSM feature is a Road and their is a relationship of this feature to the Hiking Route associated with the trail system), I am just not sur...'''
date = "2021-04-28T15:38:00Z"
lastmod = "2021-04-28T20:37:00Z"
weight = 79902
keywords = [ "trail", "road", "coaligned" ]
aliases = [ "/questions/79902" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding Trail Segment on Roadway](/questions/79902/adding-trail-segment-on-roadway)

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
<span id="post-79902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79902-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello - What are the mechanical steps to show a trail segment (Path) following a portion of an existing paved roadway? I can see examples of this is my area (the OSM feature is a Road and their is a relationship of this feature to the Hiking Route associated with the trail system), I am just not sure how to get there (do I add a new line that travels on top of the existing road?) --Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-trail" rel="tag" title="see questions tagged &#39;trail&#39;">trail</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-coaligned" rel="tag" title="see questions tagged &#39;coaligned&#39;">coaligned</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '21, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/63e6efaf5ae5774b948eb0e6bf40c84f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob009&#39;s gravatar image" />
<p><span>Rob009</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob009 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79902" class="comments-container">
<span id="79904"></span>
<div id="comment-79904" class="comment">
<div id="post-79904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(in case anyone hasn't seen it, this was also touched on in the discussion at <a href="/questions/79842/treatment-of-co-aligned-trails">https://help.openstreetmap.org/questions/79842/treatment-of-co-aligned-trails</a> )</p>
</div>
<div id="comment-79904-info" class="comment-info">
<span class="comment-age">(28 Apr '21, 16:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79902-form-container" class="comment-form-container">
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

<span id="79907"></span>

<div id="answer-container-79907" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79907-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You seem to be using the in-browser editor iD. Relation handling is very difficult in there. I advise switching to <a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a> if you want to continue working with relations. That tool is also more powerful in many other aspects.</p>
<p>But if you prefer staying with iD here is what you have to do:</p>
<ol>
<li>select the way you want to add to a relation</li>
<li>in the left side panel scroll down to the bottom and expand the relations list</li>
<li>click the plus icon</li>
<li>in the new drop down list chose one of the existing relations which represent the trail you want the segment to be added to. Note that the list only includes relations which are visible somewhere in the editor window. You cannot add other relations.</li>
<li>apply a role if applicable.</li>
</ol>
<p>So, no, do not add a new line but assign the existing road section to the route. If the route only covers part of the road you have to split the way first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '21, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '21, 18:02</strong> </span></p>
</div>
</div>
<div id="comments-container-79907" class="comments-container">
<span id="79911"></span>
<div id="comment-79911" class="comment">
<div id="post-79911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the pointer to JOSM. Yes, as a newbie I have been using iD as my editor.</p>
<p>[Looks like you answered my question on splitting in your original response. Sorry for the unnecessary question below.]</p>
<p>Ok, but your instructions assumes the length of the existing (road) way matches the length of the trail co-alignment, which will not always be the case. So I may need to divide the existing (road) way at the points where the co-aligned trail enters and exits the (road) way, correct? Please forgive my simplistic questions. --Thanks!</p>
</div>
<div id="comment-79911-info" class="comment-info">
<span class="comment-age">(28 Apr '21, 20:07)</span> <span class="comment-user userinfo">Rob009</span>
</div>
</div>
<span id="79912"></span>
<div id="comment-79912" class="comment">
<div id="post-79912-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, this is what the last sentence of TZorn's answer refers to. Splitting an existing way because only part of it belongs to a relation is very common when mapping route relations.</p>
</div>
<div id="comment-79912-info" class="comment-info">
<span class="comment-age">(28 Apr '21, 20:37)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-79907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79907-form-container" class="comment-form-container">
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

