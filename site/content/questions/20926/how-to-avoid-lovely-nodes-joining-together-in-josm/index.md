+++
type = "question"
title = "How to avoid lovely nodes joining together in JOSM ?"
description = '''As soon as nodes are able to reach each other, they join. But I placed the nodes where I thought they belong too. Is there a way or method to avoid this independent behavior of the nodes besides zooming in ? Or is it something that always happens and I’m the only one to bother about it ? Greetz'''
date = "2013-03-23T00:43:00Z"
lastmod = "2013-03-23T06:26:00Z"
weight = 20926
keywords = [ "independent", "nodes", "behavior", "josm" ]
aliases = [ "/questions/20926" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to avoid lovely nodes joining together in JOSM ?](/questions/20926/how-to-avoid-lovely-nodes-joining-together-in-josm)

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
<span id="post-20926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20926-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As soon as nodes are able to reach each other, they join. But I placed the nodes where I thought they belong too. Is there a way or method to avoid this independent behavior of the nodes besides zooming in ? Or is it something that always happens and I’m the only one to bother about it ? Greetz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-independent" rel="tag" title="see questions tagged &#39;independent&#39;">independent</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-behavior" rel="tag" title="see questions tagged &#39;behavior&#39;">behavior</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '13, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '13, 19:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a1156d45a55699715b80fc3cadd0c8d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmehl&#39;s gravatar image" />
<p><span>mmehl</span><br />
<span class="score" title="565 reputation points">565</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span></p>
</div>
</div>
<div id="comments-container-20926" class="comments-container">
&#10;</div>
<div id="comment-tools-20926" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20926-form-container" class="comment-form-container">
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

<span id="20930"></span>

<div id="answer-container-20930" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20930-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-20930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The default behaviour of JOSM when placing nodes is to reuse an existing node if the new one would be very close to it (at the currently used zoom). Often this is what you want – sharing nodes is necessary to make routeable highway junctions and so on.</p>
<p>Still, it's of course not always intended. To force JOSM to create a new node, press <strong>Ctrl</strong> while clicking to place the new node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '13, 06:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-20930" class="comments-container">
&#10;</div>
<div id="comment-tools-20930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20930-form-container" class="comment-form-container">
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

