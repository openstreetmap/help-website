+++
type = "question"
title = "How to add turn restrictions to this junction (turn:lanes, relation, or ...)?"
description = '''I&#x27;m trying to map the service road at the NW corner of this junction: http://www.openstreetmap.org/#map=19/32.09684/34.82139 That road is currently marked as &quot;one lane forward, one bus lane backwards&quot; which is correct for most of it, but at the intersection it widens to two lanes in the forward dire...'''
date = "2017-05-04T12:12:00Z"
lastmod = "2017-05-04T23:56:00Z"
weight = 56028
keywords = [ "junction", "lanes", "turn_restrictions" ]
aliases = [ "/questions/56028" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to add turn restrictions to this junction (turn:lanes, relation, or ...)?](/questions/56028/how-to-add-turn-restrictions-to-this-junction-turnlanes-relation-or)

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
<span id="post-56028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56028-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to map the service road at the NW corner of this junction: <a href="http://www.openstreetmap.org/#map=19/32.09684/34.82139">http://www.openstreetmap.org/#map=19/32.09684/34.82139</a></p>
<p>That road is currently marked as "one lane forward, one bus lane backwards" which is correct for most of it, but at the intersection it widens to two lanes in the forward direction. One of those lanes is "right turns only", the other is left-or-straight. (That's in addition to the opposite bus lane.) How do I add these restrictions?</p>
<p>I'm not sure whether I should just add turn:lanes:forward="left;through|right", or whether relation(s) are also required.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-junction" rel="tag" title="see questions tagged &#39;junction&#39;">junction</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '17, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/8440750fd002fd989ab2e6b613ca3ccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsh4&#39;s gravatar image" />
<p><span>dsh4</span><br />
<span class="score" title="867 reputation points">867</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsh4 has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-56028" class="comments-container">
&#10;</div>
<div id="comment-tools-56028" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56028-form-container" class="comment-form-container">
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

<span id="56030"></span>

<div id="answer-container-56030" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56030-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dsh4 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">Turn restrictions</a> are only necessary if there are roads which you are not allowed to enter and this restriction is not already implied by other access or oneway tags.</p>
<p>Supposed you are allowed to enter all roads then <code>lanes:forward=2</code> and <code>turn:lanes:forward=left;through|right</code> are sufficient.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '17, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56030" class="comments-container">
<span id="56039"></span>
<div id="comment-56039" class="comment">
<div id="post-56039-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/158/scai">@scai</a>! I've made the change.</p>
</div>
<div id="comment-56039-info" class="comment-info">
<span class="comment-age">(04 May '17, 23:56)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
</div>
<div id="comment-tools-56030" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56030-form-container" class="comment-form-container">
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

