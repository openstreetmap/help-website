+++
type = "question"
title = "Reply status: No Exception (0)"
description = '''I am new to wireshark and trying to troubleshoot a network issue. I see the following in my capture results: 0.008 10.76.128.37 10.78.200.136 GIOP 90 GIOP 1.2 Reply s=12 id=14135068: No Exception  Transmission Control Protocol, Src Port: lrs-paging (3700), Dst Port: 60613 (60613), Seq: 575, Ack: 513...'''
date = "2012-11-28T11:46:00Z"
lastmod = "2012-11-28T11:46:00Z"
weight = 16400
keywords = [ "capture" ]
aliases = [ "/questions/16400" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reply status: No Exception (0)](/questions/16400/reply-status-no-exception-0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16400-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark and trying to troubleshoot a network issue. I see the following in my capture results:</p><pre><code>0.008 10.76.128.37 10.78.200.136 GIOP 90 GIOP 1.2 Reply s=12 id=14135068: No Exception

Transmission Control Protocol, Src Port: lrs-paging (3700), Dst Port: 60613 (60613), Seq: 575, Ack: 513, Len: 41
General Inter-ORB Protocol
Magic number: GIOP
Version: 1.2
Message Flags: 0x00, (Big Endian)
Message type: Reply
Message size: 12
General Inter-ORB Protocol Reply
Request id: 14135068
Reply status: No Exception (0)
ServiceContextList
Sequence length: 0</code></pre><p>Does this indicate a connection issue?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '12, 11:46</strong></p><img src="https://secure.gravatar.com/avatar/9804bf8bf161b03fae3a156bfcfce2f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zmaster&#39;s gravatar image" /><p>zmaster<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zmaster has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '12, 14:48</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16400" class="comments-container"><span id="16401"></span><div id="comment-16401" class="comment"><div id="post-16401-score" class="comment-score"></div><div class="comment-text"><p>Not knowing the protocol very well id look at ServiceContextList Sequence length: 0. As this is a reply with No Exception I'd intepreat that as "OK" but perhaps a ServiceContextList is expected in the result. Any logs in the application?</p></div><div id="comment-16401-info" class="comment-info"><span class="comment-age">(28 Nov '12, 12:03)</span> Anders ♦</div></div><span id="16403"></span><div id="comment-16403" class="comment"><div id="post-16403-score" class="comment-score"></div><div class="comment-text"><p>No logs from the application yet due to limited access to this customer environment. I have asked the server folks for server/application logs.</p><p>Notice the latency in the time column and the traffic pattern.</p><p>Thanks!</p></div><div id="comment-16403-info" class="comment-info"><span class="comment-age">(28 Nov '12, 12:43)</span> zmaster</div></div><span id="16404"></span><div id="comment-16404" class="comment"><div id="post-16404-score" class="comment-score">1</div><div class="comment-text"><p>There's only one packet shown, so I'm not sure how to see a traffic pattern.</p></div><div id="comment-16404-info" class="comment-info"><span class="comment-age">(28 Nov '12, 14:50)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-16400" class="comment-tools"></div><div class="clear"></div><div id="comment-16400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

