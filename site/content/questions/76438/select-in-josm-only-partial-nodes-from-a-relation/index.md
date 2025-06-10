+++
type = "question"
title = "Select in JOSM only partial nodes from a relation"
description = '''How I can create a search expression in JOSM to select from an administrative boundary relation only the nodes from that relation that are in view? The utilsplugin2 have a tool that let you select middle nodes from a way. But I need to do the same using JOSM search function. Ctrl-F. Thanks, met.'''
date = "2020-09-04T23:35:00Z"
lastmod = "2020-09-05T12:50:00Z"
weight = 76438
keywords = [ "josm", "search", "selection", "nodes" ]
aliases = [ "/questions/76438" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Select in JOSM only partial nodes from a relation](/questions/76438/select-in-josm-only-partial-nodes-from-a-relation)

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
<span id="post-76438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76438-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How I can create a search expression in JOSM to select from an administrative boundary relation only the nodes from that relation that are in view?</p>
<p>The utilsplugin2 have a tool that let you select middle nodes from a way. But I need to do the same using JOSM search function. Ctrl-F.</p>
<p>Thanks,</p>
<p>met.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '20, 23:35</strong></p>
<img src="https://secure.gravatar.com/avatar/6783b46d5425152bbb4fc48e90eb279a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdelatorre&#39;s gravatar image" />
<p><span>mdelatorre</span><br />
<span class="score" title="177 reputation points">177</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdelatorre has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76438" class="comments-container">
&#10;</div>
<div id="comment-tools-76438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76438-form-container" class="comment-form-container">
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

<span id="76456"></span>

<div id="answer-container-76456" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76456-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For nodes that are part of the boundary relation directly you can right click on the relation in the <em>Tags/Memberships</em> panel then search for "type:node inview" with the find in selection option ticked.</p>
<p>For <a href="https://wiki.openstreetmap.org/wiki/Relation:boundary">boundaries</a> this will probably be elements with the roles <code>admin_centre</code> or <code>label</code>.</p>
<p>If you want nodes belonging to ways that are referenced by the relation you can press <code>E</code> before running the search.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '20, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76456" class="comments-container">
&#10;</div>
<div id="comment-tools-76456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76456-form-container" class="comment-form-container">
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

