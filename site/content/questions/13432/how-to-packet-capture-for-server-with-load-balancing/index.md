+++
type = "question"
title = "how to packet capture for server with load balancing"
description = '''I apologize if this question is too basic and obvious. I want to do a packet capture on servers (OS type - Windows 2003, 2003R2, 2008, and 2008R2) with multiple NICs teamed together. The NICs might be teamed in a load balanced manner. Would the only way to do an accurate capture require port spannin...'''
date = "2012-08-07T09:35:00Z"
lastmod = "2012-08-07T11:10:00Z"
weight = 13432
keywords = [ "nic-team", "capture", "load-balance" ]
aliases = [ "/questions/13432" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to packet capture for server with load balancing](/questions/13432/how-to-packet-capture-for-server-with-load-balancing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13432-score" class="post-score" title="current number of votes">0</div><span id="post-13432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I apologize if this question is too basic and obvious.</p><p>I want to do a packet capture on servers (OS type - Windows 2003, 2003R2, 2008, and 2008R2) with multiple NICs teamed together. The NICs might be teamed in a load balanced manner.</p><p>Would the only way to do an accurate capture require port spanning (or port mirroring) to capture all the packets to and from the server or can running wireshark on the server itself be able to get a complete capture from more than one interface?</p><p>I have read that tcpdump allows for packet capture from all interfaces in non-promiscuous mode for Linux OS, but I don't know what options are available for Windows machines or non-Linux machines in general.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic-team" rel="tag" title="see questions tagged &#39;nic-team&#39;">nic-team</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-load-balance" rel="tag" title="see questions tagged &#39;load-balance&#39;">load-balance</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '12, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/04b354928d3526c5e801d01484126539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seanpcap&#39;s gravatar image" /><p><span>seanpcap</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seanpcap has no accepted answers">0%</span></p></div></div><div id="comments-container-13432" class="comments-container"></div><div id="comment-tools-13432" class="comment-tools"></div><div class="clear"></div><div id="comment-13432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13436"></span>

<div id="answer-container-13436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13436-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13436-score" class="post-score" title="current number of votes">0</div><span id="post-13436-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try the latest Windows version of Wireshark V1.8, it is exactly what you want. It can capture on multiple interfaces in promiscuous mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p><span>KeithFrench</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-13436" class="comments-container"></div><div id="comment-tools-13436" class="comment-tools"></div><div class="clear"></div><div id="comment-13436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

