+++
type = "question"
title = "Wireshark bluetooth packet layout"
description = '''I recently moved all my work involving Bluetooth in wireshark to a windows 10 virtual machine. I fixed an initial error with encapsulation where I added user 10 DLT = 157 with btle as the protocol, which was the same as I did before and it worked fine. However this time, while I get no errors, the l...'''
date = "2015-12-11T12:50:00Z"
lastmod = "2016-01-27T07:25:00Z"
weight = 48460
keywords = [ "wireshark" ]
aliases = [ "/questions/48460" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark bluetooth packet layout](/questions/48460/wireshark-bluetooth-packet-layout)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48460-score" class="post-score" title="current number of votes">0</div><span id="post-48460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently moved all my work involving Bluetooth in wireshark to a windows 10 virtual machine. I fixed an initial error with encapsulation where I added user 10 DLT = 157 with btle as the protocol, which was the same as I did before and it worked fine. However this time, while I get no errors, the layout is different and it is missing a lot of info like source and destination, payload, any handle values. The type of packets displayed are "Empty PDU", "Control Opcode: LL_START_ENC_RSP", and "L2CAP Fragment". Please forgive me if any terminology used here is incorrect, I am still new to wireshark and learning. Any help with getting this back to the normal layout would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '15, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/45d919513f998537906e8092ace32654?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nearl002&#39;s gravatar image" /><p><span>nearl002</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nearl002 has no accepted answers">0%</span></p></div></div><div id="comments-container-48460" class="comments-container"></div><div id="comment-tools-48460" class="comment-tools"></div><div class="clear"></div><div id="comment-48460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48470"></span>

<div id="answer-container-48470" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48470-score" class="post-score" title="current number of votes">1</div><span id="post-48470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nearl002 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It seems to be a bug, please fill the bug on Bugzilla. DLT_USER are not currently supported by centralised "bluetooth" dissector where all additional/useful operations done or data have been stored.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '15, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p><span>Michał Łabędzki</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-48470" class="comments-container"><span id="48473"></span><div id="comment-48473" class="comment"><div id="post-48473-score" class="comment-score"></div><div class="comment-text"><p>Thank you for looking into it.</p></div><div id="comment-48473-info" class="comment-info"><span class="comment-age">(12 Dec '15, 04:58)</span> <span class="comment-user userinfo">nearl002</span></div></div><span id="49548"></span><div id="comment-49548" class="comment"><div id="post-49548-score" class="comment-score"></div><div class="comment-text"><p>I am encountering the same series of messages.</p><p>Was a bug report ever created? If so, did you receive an answer? Or an estimate of when it would be addressed?</p><p>Thanks in advance.</p></div><div id="comment-49548-info" class="comment-info"><span class="comment-age">(27 Jan '16, 06:40)</span> <span class="comment-user userinfo">Lorie</span></div></div><span id="49553"></span><div id="comment-49553" class="comment"><div id="post-49553-score" class="comment-score"></div><div class="comment-text"><p>As I remember there is no bug request yet (and no sample capture file) - please create. To speed up work on this I need capture file, this issue in on my TODO list, but it is not ready right now.</p></div><div id="comment-49553-info" class="comment-info"><span class="comment-age">(27 Jan '16, 07:25)</span> <span class="comment-user userinfo">Michał Łabędzki</span></div></div></div><div id="comment-tools-48470" class="comment-tools"></div><div class="clear"></div><div id="comment-48470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

