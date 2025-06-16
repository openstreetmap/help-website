+++
type = "question"
title = "About save change on related elements"
description = '''Hi all I have a problem on how do osm save changes if two elements related to each other. As a case with a node included in a way, if there is a change made to that node, will the way also change? (both version numbers will change?) Thanks for help. Martin'''
date = "2014-02-06T13:41:00Z"
lastmod = "2014-02-06T17:19:00Z"
weight = 30500
keywords = [ "save-changes" ]
aliases = [ "/questions/30500" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [About save change on related elements](/questions/30500/about-save-change-on-related-elements)

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
<span id="post-30500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30500-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all</p>
<p>I have a problem on how do osm save changes if two elements related to each other. As a case with a node included in a way, if there is a change made to that node, will the way also change? (both version numbers will change?)</p>
<p>Thanks for help.</p>
<p>Martin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-save-changes" rel="tag" title="see questions tagged &#39;save-changes&#39;">save-changes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '14, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/4c6b1343c60b83eaa6e7114be590837d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Digmaa&#39;s gravatar image" />
<p><span>Digmaa</span><br />
<span class="score" title="100 reputation points">100</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Digmaa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30500" class="comments-container">
&#10;</div>
<div id="comment-tools-30500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30500-form-container" class="comment-form-container">
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

<span id="30501"></span>

<div id="answer-container-30501" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30501-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you move a node, or add tags to a node, and the node is part of a way, then the way will not change - the way will still be "last modified 2 years ago" even if - due to the changed location of the member node - the way will have looked totally different on the map yesterday.</p>
<p>The same is true for modifying a node or way or relation which are part of a relation - the parent relation will not change.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '14, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30501" class="comments-container">
<span id="30504"></span>
<div id="comment-30504" class="comment">
<div id="post-30504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>so that can I say the change made on each type of element is "isolated", in other words, the changes on different types elements are exclusive to each other?</p>
</div>
<div id="comment-30504-info" class="comment-info">
<span class="comment-age">(06 Feb '14, 15:55)</span> <span class="comment-user userinfo">Digmaa</span>
</div>
</div>
<span id="30505"></span>
<div id="comment-30505" class="comment">
<div id="post-30505-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Digma</span>: Yes. You only change what you (helped by your editor) change. Have a look at one of <a href="https://www.openstreetmap.org/user/Digmaa/history">your changesets</a> and view the osmChange XML (link on bottom of each changeset page). Ways are just a list of nodes – see <span>elements in our wiki</span>.</p>
</div>
<div id="comment-30505-info" class="comment-info">
<span class="comment-age">(06 Feb '14, 17:19)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30501-form-container" class="comment-form-container">
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

