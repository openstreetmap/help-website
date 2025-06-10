+++
type = "question"
title = "Should a bridge in farmland being tagged ?"
description = '''A rather large waterway through farmland has got some bridges. Youre allowed to tag and map all visible objects and tag them. Here the problem the bridges are marked as beiing fault, no way around, disconnected. What to do ? Dont map them or tag and map them but how ?'''
date = "2012-09-23T00:05:00Z"
lastmod = "2012-09-23T09:50:00Z"
weight = 16358
keywords = [ "bridge", "tag", "mapping", "objects" ]
aliases = [ "/questions/16358" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Should a bridge in farmland being tagged ?](/questions/16358/should-a-bridge-in-farmland-being-tagged)

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
<span id="post-16358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16358-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A rather large waterway through farmland has got some bridges. Youre allowed to tag and map all visible objects and tag them. Here the problem the bridges are marked as beiing fault, no way around, disconnected. What to do ? Dont map them or tag and map them but how ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '12, 00:05</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-16358" class="comments-container">
<span id="16366"></span>
<div id="comment-16366" class="comment">
<div id="post-16366-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where are they "marked as being fault"?</p>
</div>
<div id="comment-16366-info" class="comment-info">
<span class="comment-age">(23 Sep '12, 09:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16358" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16358-form-container" class="comment-form-container">
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

<span id="16359"></span>

<div id="answer-container-16359" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16359-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-16359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, if the bridges actually exist, and are permanent, then it is worth mapping them. Probably tagging them as <code>highway=track</code> or <code>highway=path</code>, plus <code>bridge=yes</code> and <code>layer=1</code>.</p>
<p>I'm not sure where you are seeing this marked as a fault? Some quality assurance tools like Keepright will highlight "floating islands", ie a highway that is not connected to the rest of the map. But this is not necessarily an error.</p>
<p>It is possible to have a bridge (or other path or track), which is not connected to any other highways. And if this is the case on the ground, then that is how it should be mapped, even if it is highlighted as an error. Note Keepright has an option to mark errors as a "false positive", which allows them to be ignored. Other tools may have similar options.</p>
<p>If there is some sort of path or track across the farmland to the bridges, then it is worth mapping that as well. But if there isn't, and people just go any route across the fields, then there is no path to map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '12, 02:55</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-16359" class="comments-container">
&#10;</div>
<div id="comment-tools-16359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16359-form-container" class="comment-form-container">
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

