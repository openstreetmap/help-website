+++
type = "question"
title = "Error message from Osmose &quot;Missing tag or role on node&quot;"
description = '''I seem to be even more of a beginner than 2 weeks ago. After correcting what appears to be a fairly common beginner’s error, failing to join a new way to an existing way, Osmose reported a mass of other errors, up to 100 km away from any edits that I had done. The oddest were messages for nodes 8373...'''
date = "2022-02-25T16:10:00Z"
lastmod = "2022-02-28T12:51:00Z"
weight = 83583
keywords = [ "node", "role", "tags" ]
aliases = [ "/questions/83583" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Error message from Osmose "Missing tag or role on node"](/questions/83583/error-message-from-osmose-missing-tag-or-role-on-node)

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
<span id="post-83583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83583-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I seem to be even more of a beginner than 2 weeks ago. After correcting what appears to be a fairly common beginner’s error, failing to join a new way to an existing way, Osmose reported a mass of other errors, up to 100 km away from any edits that I had done. The oddest were messages for nodes 8373633505, 8361153367 and 1776155144 “Missing tag or role on node”.</p>
<p>Neither the wiki nor the forum shed any light on the problem.</p>
<p>Inspection of these nodes showed that they had a tag “relation:10169937” (French long distance hiking path 48) but no roles were associated with this relation and I found no obvious roles from studying the map. Examining the relation (I am learning!) I found that these three were the only nodes belonging to the relation.</p>
<p>It would seem therefore that the message should be “Missing role for relation on node”. There was certainly no missing tag.</p>
<p>The question is, therefore, should I just delete the relation from the nodes as no similar nodes on ways along the route have relations. Or will something terrible happen, like 10 more error messages for each node modified?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-role" rel="tag" title="see questions tagged &#39;role&#39;">role</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '22, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/aeb58377a8e6a08a91ccbe94158bad82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TinyTrouble&#39;s gravatar image" />
<p><span>TinyTrouble</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TinyTrouble has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83583" class="comments-container">
&#10;</div>
<div id="comment-tools-83583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83583-form-container" class="comment-form-container">
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

<span id="83595"></span>

<div id="answer-container-83595" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83595-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TinyTrouble has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>Don't take too much notice of osmose errors you are not responsible for. When you touch an object (ways or relations for example) you get some kind of ownership over it, even if you edit a small part of it.</p>
<p>But if you want the correct the errors, that's nice too.</p>
<p>It's pretty rare to add nodes to relations, especially without role. Untagged nodes, I don't see the use, except as via points in some special relations.</p>
<p>I think it's safe, and correct, to remove the nodes from the relation. It's probably a mistake from the original mapper.</p>
<p>As for knowing if it will lead to more errors, it might, for example if you edit another relation on the same node, or some way that is connected and is wrongly tagged... But again, that is not a problem ! It's pretty impossible, when you map a lot, to keep osmose errors to zero. You might get errors from others, on subjects you don't feel comfortable, or care, enough to try to correct.</p>
<p>There are also false positives.. Don't feel bad about it ! ;-)</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '22, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83595" class="comments-container">
<span id="83607"></span>
<div id="comment-83607" class="comment">
<div id="post-83607-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I will remove them from the relation in a simple edit that can be undone if it goes bizarre, it can be undone.</p>
<p>Regards</p>
</div>
<div id="comment-83607-info" class="comment-info">
<span class="comment-age">(28 Feb '22, 12:43)</span> <span class="comment-user userinfo">TinyTrouble</span>
</div>
</div>
<span id="83608"></span>
<div id="comment-83608" class="comment">
<div id="post-83608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>BTW, I do take notice of errors and warnings (even if they NOT MY FAULT!!) I was interested to see that the three ways I tagged as fixme, because I was not sure about the status of these ways and I have not yet checked with the local authority, have shown up as OSMI issues - that will remind me do do something about it.</p>
<p>Regards</p>
</div>
<div id="comment-83608-info" class="comment-info">
<span class="comment-age">(28 Feb '22, 12:51)</span> <span class="comment-user userinfo">TinyTrouble</span>
</div>
</div>
</div>
<div id="comment-tools-83595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83595-form-container" class="comment-form-container">
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

