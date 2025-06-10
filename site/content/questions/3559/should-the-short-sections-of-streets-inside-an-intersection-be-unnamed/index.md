+++
type = "question"
title = "Should the short sections of streets inside an intersection be unnamed?"
description = '''I have now posted two questions about mapping intersections of divided roads and turn restrictions. I am getting there, but I wanted to ask this separately. If two divided roads intersect, we are going to end up with four intersection nodes. This much is clear. If there are &quot;No U turn&quot; signs to be m...'''
date = "2011-03-05T09:46:00Z"
lastmod = "2011-03-05T12:18:00Z"
weight = 3559
keywords = [ "rendering", "turn_restrictions", "tagging" ]
aliases = [ "/questions/3559" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Should the short sections of streets inside an intersection be unnamed?](/questions/3559/should-the-short-sections-of-streets-inside-an-intersection-be-unnamed)

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
<span id="post-3559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3559-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have now posted two questions about mapping intersections of divided roads and turn restrictions. I am getting there, but I wanted to ask this separately.</p>
<p>If two divided roads intersect, we are going to end up with four intersection nodes. This much is clear. If there are "No U turn" signs to be made, then the ways need to be split in two and three parts respectively. The northbound side of Street A becomes the "from" of the relation, the southbound side is the "to", and the short section of Street B in-between is the "via".</p>
<p>Should I wipe out the name of this short "via" section? If I don't, it can lead to some interesting rendering. Or it may not. Is there a best practice for this?<br />
</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '11, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-3559" class="comments-container">
&#10;</div>
<div id="comment-tools-3559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3559-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="3562"></span>

<div id="answer-container-3562" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3562-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-3562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No you don't need to (or actually should't) remove the name from the short "via" section. Every decent renderer will omit the name on that short bit and any good renderer will merge the pieces with the same name internally and will perform label placement on the stitched way. This obviously only works if all touching parts of the street actually carry the name of the street.</p>
<p>Routing software benefits from the name on the short "via" part too. Many routers simply check if the name of the next part of the route is the same as the name on the current part. If not they will issue a command like "continue on to Street A". Obviously this gets a lot harder to check and generate if short unnamed stretches of Street A are present.</p>
<p>And last but not least: that part is part of Street A so it should carry that name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '11, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-3562" class="comments-container">
&#10;</div>
<div id="comment-tools-3562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3562-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3567"></span>

<div id="answer-container-3567" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3567-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>&gt; If I don't, it can lead to some interesting rendering</em></p>
<p>Don't let that concern you. Map what's correct. The renderers will figure it out for themselves, and if not, we'll fix the renderers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '11, 12:18</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-3567" class="comments-container">
&#10;</div>
<div id="comment-tools-3567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3567-form-container" class="comment-form-container">
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

