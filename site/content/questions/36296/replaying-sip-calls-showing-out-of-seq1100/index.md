+++
type = "question"
title = "Replaying SIP calls, showing Out of Seq:1(100%)"
description = '''I&#x27;m trying to capture and replay VOIP conversations on my local network using Wireshark. I&#x27;ve tried multiple audio codecs and softphones but I&#x27;m unable to replay the audio using Telephony -&amp;gt; VOIP Calls -&amp;gt; Player -&amp;gt; Decode. Wireshark detects the VOIP call and shows the correct duration but e...'''
date = "2014-09-13T10:00:00Z"
lastmod = "2014-09-13T17:29:00Z"
weight = 36296
keywords = [ "decode", "sip", "rtp", "voip", "sequence" ]
aliases = [ "/questions/36296" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Replaying SIP calls, showing Out of Seq:1(100%)](/questions/36296/replaying-sip-calls-showing-out-of-seq1100)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36296-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture and replay VOIP conversations on my local network using Wireshark. I've tried multiple audio codecs and softphones but I'm unable to replay the audio using Telephony -&gt; VOIP Calls -&gt; Player -&gt; Decode. Wireshark detects the VOIP call and shows the correct duration but every decode results in showing "Out of seq:1(100%)" and "Duration:0:00" in the RTP player. The traffic is not being encrypted and the sequence numbers in Wireshark seem to be fine. Any ideas?</p></div><div id="question-tags" class="tags-container tags">decode sip rtp voip sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '14, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/6d3e6a3be6e3d57b8830f1fec2863731?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Recurzion&#39;s gravatar image" /><p>Recurzion<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Recurzion has no accepted answers">0%</span></p></div></div><div id="comments-container-36296" class="comments-container"></div><div id="comment-tools-36296" class="comment-tools"></div><div class="clear"></div><div id="comment-36296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36302"></span>

<div id="answer-container-36302" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36302-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Update: I resolved this issue by setting up my own SIP server using FreePBX. I assume that this problem was somehow related to NAT-ing the traffic from my internal network to the SIP provider and then back to my other softphone on the internal network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '14, 17:29</strong></p><img src="https://secure.gravatar.com/avatar/6d3e6a3be6e3d57b8830f1fec2863731?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Recurzion&#39;s gravatar image" /><p>Recurzion<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Recurzion has no accepted answers">0%</span></p></div></div><div id="comments-container-36302" class="comments-container"></div><div id="comment-tools-36302" class="comment-tools"></div><div class="clear"></div><div id="comment-36302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

