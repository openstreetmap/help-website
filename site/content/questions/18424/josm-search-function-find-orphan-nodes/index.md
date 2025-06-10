+++
type = "question"
title = "JOSM search function: Find orphan nodes"
description = '''I need to find all nodes created by a specific user with no tags that are not part of a way I am using the Ctrl-F search function: &quot;user:example tags:0 type:node&quot; There is the parent option but I am not sure how to use it or how to negate it. &quot;user:example tags:0 type:node -parent&quot; also selects node...'''
date = "2012-12-13T16:49:00Z"
lastmod = "2012-12-13T16:55:00Z"
weight = 18424
keywords = [ "josm", "search" ]
aliases = [ "/questions/18424" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM search function: Find orphan nodes](/questions/18424/josm-search-function-find-orphan-nodes)

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
<span id="post-18424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18424-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to find all nodes created by a specific user with no tags that <em>are not part of a way</em></p>
<p>I am using the Ctrl-F search function:</p>
<p>"user:example tags:0 type:node"</p>
<p>There is the parent option but I am not sure how to use it or how to negate it.</p>
<p>"user:example tags:0 type:node -parent" also selects nodes that are part of a way</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '12, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18424" class="comments-container">
&#10;</div>
<div id="comment-tools-18424" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18424-form-container" class="comment-form-container">
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

<span id="18425"></span>

<div id="answer-container-18425" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18425-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-18425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is covered by the very last example on <a href="http://wiki.openstreetmap.org/wiki/JOSM/Search_function">JOSM/Search_function help</a>: "type:node untagged -child"</p>
<p>So the right expression is</p>
<p>"user:example type:node untagged -child"<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '12, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-18425" class="comments-container">
&#10;</div>
<div id="comment-tools-18425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18425-form-container" class="comment-form-container">
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

