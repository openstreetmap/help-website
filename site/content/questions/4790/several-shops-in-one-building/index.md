+++
type = "question"
title = "Several shops in one building"
description = '''Hi, Is there any way for tagging several shops in one buildings. I&#x27;m thinking about having one haircut in the first floor, a lawyer and an smith in the second floor, etc. Is there any way for specifying the floor and the door (at the floor) in shop=[something]? Something like shop=haircut floor=1 do...'''
date = "2011-04-25T13:41:00Z"
lastmod = "2011-04-25T19:18:00Z"
weight = 4790
keywords = [ "shop", "building", "several", "tagging" ]
aliases = [ "/questions/4790" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Several shops in one building](/questions/4790/several-shops-in-one-building)

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
<span id="post-4790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4790-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Is there any way for tagging several shops in one buildings. I'm thinking about having one haircut in the first floor, a lawyer and an smith in the second floor, etc.</p>
<p>Is there any way for specifying the floor and the door (at the floor) in shop=[something]?</p>
<p>Something like</p>
<p>shop=haircut floor=1 door=2</p>
<p>shop=smith floor=2 door=1</p>
<p>...</p>
<p>How can it displays in OSM? Do we need OSM-3d for displaying?</p>
<p>In resume, is there any way for specifying having multiple shops in a single place (building in my case)?</p>
<p>Thanks in advance and sorry for my uglish english ;-)</p>
<p>Xan.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-several" rel="tag" title="see questions tagged &#39;several&#39;">several</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '11, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/7885cf9b6111344a62a77b00b1561364?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="somenxavier&#39;s gravatar image" />
<p><span>somenxavier</span><br />
<span class="score" title="80 reputation points">80</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="somenxavier has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4790" class="comments-container">
&#10;</div>
<div id="comment-tools-4790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4790-form-container" class="comment-form-container">
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

<span id="4807"></span>

<div id="answer-container-4807" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4807-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-4807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="somenxavier has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For tagging which floor something is on, the most popular tag is <code>level</code>. eg <code>level=3</code>.</p>
<p>For what door, that is probably best with some sort of <a href="http://wiki.openstreetmap.org/wiki/Key:addr">addr tag</a>. Though I'm not sure if there is a specific tag for that. There has some discussion of proposed tags for this on the <a href="http://lists.openstreetmap.org/pipermail/tagging/">Tagging mailing list</a> today.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '11, 19:18</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4807" class="comments-container">
&#10;</div>
<div id="comment-tools-4807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4807-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4801"></span>

<div id="answer-container-4801" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4801-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As with mapping a <a href="http://help.openstreetmap.org/questions/2969/how-to-tag-a-multi-function-facility">Multi-function facility</a> there is no hard and fast rule that will work for every combination of objects. Mapper discretion is required. For a <a href="http://wiki.openstreetmap.org/wiki/Project_of_the_week/2010/Oct_20">shopping mall</a> it is possible to add the building with the common elements of the objects; name of the mall, opening hours if consolidated. Then add nodes for each business as required.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '11, 18:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span> </br></p>
</div>
</div>
<div id="comments-container-4801" class="comments-container">
&#10;</div>
<div id="comment-tools-4801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4801-form-container" class="comment-form-container">
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

