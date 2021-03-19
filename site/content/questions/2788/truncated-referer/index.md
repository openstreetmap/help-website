+++
type = "question"
title = "Truncated Referer"
description = '''Request packets have referer field but sometimes there are like this &quot;[truncated] Referer&quot; Does [truncated] shows something?'''
date = "2011-03-11T12:07:00Z"
lastmod = "2011-03-11T15:08:00Z"
weight = 2788
keywords = [ "referer" ]
aliases = [ "/questions/2788" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Truncated Referer](/questions/2788/truncated-referer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2788-score" class="post-score" title="current number of votes">0</div><span id="post-2788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Request packets have referer field but sometimes there are like this "[truncated] Referer" Does [truncated] shows something?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-referer" rel="tag" title="see questions tagged &#39;referer&#39;">referer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '11, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/0d1f835bfa8cc91838057ef65fc4d1c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A%20B&#39;s gravatar image" /><p><span>A B</span><br />
<span class="score" title="1 reputation points">1</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A B has no accepted answers">0%</span></p></div></div><div id="comments-container-2788" class="comments-container"></div><div id="comment-tools-2788" class="comment-tools"></div><div class="clear"></div><div id="comment-2788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2789"></span>

<div id="answer-container-2789" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2789-score" class="post-score" title="current number of votes">2</div><span id="post-2789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When Wireshark puts [truncated] on a protocol tree item (such as the HTTP Referer field), it means that the field is longer than Wireshark's internal display limit (ITEM_LABEL_LENGTH==240) so the display (in the protocol tree) has been truncated.</p><p>In other words, if the Referer field is, say, 300 characters long, it will be truncated to 240 minus the length of the field description ("[truncated] Referer:").</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '11, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Mar '12, 07:04</strong> </span></p></div></div><div id="comments-container-2789" class="comments-container"></div><div id="comment-tools-2789" class="comment-tools"></div><div class="clear"></div><div id="comment-2789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

