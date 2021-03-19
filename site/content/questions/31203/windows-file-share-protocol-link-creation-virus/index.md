+++
type = "question"
title = "Windows File Share Protocol / Link Creation / Virus"
description = '''We have a PC or multiple PC&#x27;s in a VERY large network creating malicious links on our servers. I wan&#x27;t to see if someone cal help me make a quick filter for wireshark that will log only the link creation event so I can figure out where it is coming from without generating gigs and gigs of packet dat...'''
date = "2014-03-26T16:54:00Z"
lastmod = "2014-03-28T14:42:00Z"
weight = 31203
keywords = [ "filter", "virus", "samba", "packet" ]
aliases = [ "/questions/31203" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows File Share Protocol / Link Creation / Virus](/questions/31203/windows-file-share-protocol-link-creation-virus)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31203-score" class="post-score" title="current number of votes">0</div><span id="post-31203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a PC or multiple PC's in a VERY large network creating malicious links on our servers. I wan't to see if someone cal help me make a quick filter for wireshark that will log only the link creation event so I can figure out where it is coming from without generating gigs and gigs of packet data. I really need help soon!</p><p>Thank You So Much</p><p>-J</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-virus" rel="tag" title="see questions tagged &#39;virus&#39;">virus</span> <span class="post-tag tag-link-samba" rel="tag" title="see questions tagged &#39;samba&#39;">samba</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '14, 16:54</strong></p><img src="https://secure.gravatar.com/avatar/bc5ebda7d2d8ee0f7619dacb219f239e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pyrex&#39;s gravatar image" /><p><span>Pyrex</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pyrex has no accepted answers">0%</span></p></div></div><div id="comments-container-31203" class="comments-container"><span id="31250"></span><div id="comment-31250" class="comment"><div id="post-31250-score" class="comment-score"></div><div class="comment-text"><p>Could someone please help me? We will have to be at work all weekend and then some if we can''t stop this virus.</p></div><div id="comment-31250-info" class="comment-info"><span class="comment-age">(28 Mar '14, 12:37)</span> <span class="comment-user userinfo">Pyrex</span></div></div></div><div id="comment-tools-31203" class="comment-tools"></div><div class="clear"></div><div id="comment-31203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31257"></span>

<div id="answer-container-31257" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31257-score" class="post-score" title="current number of votes">0</div><span id="post-31257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is the wrong tool for you, for several reasons.</p><p>You should look at the owner of the created links (maybe that reveals the workstation).</p><p>You should also enable file and folder auditing on your file server to figure out who is doing what. Your local Windows guru should know how to do that.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '14, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31257" class="comments-container"></div><div id="comment-tools-31257" class="comment-tools"></div><div class="clear"></div><div id="comment-31257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

