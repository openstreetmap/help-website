+++
type = "question"
title = "Revert changeset request"
description = '''Please could someone revert #48732521?  I added a foot path which no longer exists. I could just delete it, but the change has affected adjacent features so I thought it might be better to revert it.  Thanks. '''
date = "2017-05-24T09:00:00Z"
lastmod = "2017-05-24T10:19:00Z"
weight = 56271
keywords = [ "changeset", "revert" ]
aliases = [ "/questions/56271" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Revert changeset request](/questions/56271/revert-changeset-request)

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
<span id="post-56271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56271-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please could someone revert #48732521? I added a foot path which no longer exists. I could just delete it, but the change has affected adjacent features so I thought it might be better to revert it. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '17, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/dc2483c19cbc7aa88c181b83ca768f00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="molip&#39;s gravatar image" />
<p><span>molip</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="molip has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '17, 09:05</strong> </span></p>
</div>
</div>
<div id="comments-container-56271" class="comments-container">
&#10;</div>
<div id="comment-tools-56271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56271-form-container" class="comment-form-container">
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

<span id="56274"></span>

<div id="answer-container-56274" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56274-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56274-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56274-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="molip has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sure, reverted in #48940358.</p>
<p>Btw, there's a Reverter plugin for JOSM editor - using that, it is quite simple to revert the whole changeset: Data - Revert changeset - enter changeset number. It will read the changeset and create a reverse set of commands, which will restore the map to its previous state (e.g. if the changeset added a tag, this will add a command to remove it, etc.). When using this, it doesn't upload automatically - which is a feature: if there was a map edit in the meantime, it would go through the usual edit-conflict resolution tools.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '17, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '17, 09:44</strong> </span></p>
</div>
</div>
<div id="comments-container-56274" class="comments-container">
<span id="56277"></span>
<div id="comment-56277" class="comment">
<div id="post-56277-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I'll try using the reverter plugin next time.</p>
</div>
<div id="comment-56277-info" class="comment-info">
<span class="comment-age">(24 May '17, 10:19)</span> <span class="comment-user userinfo">molip</span>
</div>
</div>
</div>
<div id="comment-tools-56274" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56274-form-container" class="comment-form-container">
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

