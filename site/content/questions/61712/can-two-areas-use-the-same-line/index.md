+++
type = "question"
title = "can two areas use the same line"
description = '''can two areas share a line? for an example when a commercial area is next to a residential area can they share the line in betweent.'''
date = "2018-01-19T06:41:00Z"
lastmod = "2018-01-19T15:48:00Z"
weight = 61712
keywords = [ "landuse" ]
aliases = [ "/questions/61712" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can two areas use the same line](/questions/61712/can-two-areas-use-the-same-line)

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
<span id="post-61712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61712-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>can two areas share a line? for an example when a commercial area is next to a residential area can they share the line in betweent.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '18, 06:41</strong></p>
<img src="https://secure.gravatar.com/avatar/ae67c57089351bb0142ca42938745ee6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Luigiz6&#39;s gravatar image" />
<p><span>Luigiz6</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Luigiz6 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61712" class="comments-container">
&#10;</div>
<div id="comment-tools-61712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61712-form-container" class="comment-form-container">
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

<span id="61713"></span>

<div id="answer-container-61713" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61713-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-61713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>2 areas (or closed ways, the word "area" is only used in the iD editor) cannot share a line (or way). Their edges might overlap though and reuse the same points. The end-result looks as if they share the same way (line).</p>
<p>You could also build and area via a multipolygon-relation existing of ways, but this makes things more complex. This technique is used in some cases where the mapper wanted to reuse existing ways representing fences or hedges. Other mappers will draw the way representing the fence over the way of the landuses.</p>
<p>So you see there are plenty of ways to represent landuses, but the easiest is to have different areas, reusing the same points at their border.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '18, 06:53</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-61713" class="comments-container">
<span id="61730"></span>
<div id="comment-61730" class="comment">
<div id="post-61730-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As for the question of <em>should</em> they share nodes, it of course depends.</p>
<p>If one area semantically stops where the other begins (for example a forest beside a meadow), let them share nodes. If there's a significant gap (for example having to cross the street), don't share nodes. I some cases (for example a dividing wall between two areas) there's technically a gap between two areas but it's probably better to map as if no gap existed.</p>
</div>
<div id="comment-61730-info" class="comment-info">
<span class="comment-age">(19 Jan '18, 15:48)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61713-form-container" class="comment-form-container">
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

