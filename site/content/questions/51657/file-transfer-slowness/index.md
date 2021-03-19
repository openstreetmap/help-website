+++
type = "question"
title = "File transfer slowness"
description = '''Have a VPLS network connecting 6 different sites back to our data center. Each site has a dedicated 50 MB connection with bursting up to 100 MB. Trying to do a file migration from one site to the data center and I&#x27;m only getting .5-.7 MBytes the other sites are fine. Tried doing some captures on the...'''
date = "2016-04-13T21:32:00Z"
lastmod = "2016-04-13T21:32:00Z"
weight = 51657
keywords = [ "unseen", "dropped", "slowness", "retransmissions" ]
aliases = [ "/questions/51657" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [File transfer slowness](/questions/51657/file-transfer-slowness)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51657-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Have a VPLS network connecting 6 different sites back to our data center. Each site has a dedicated 50 MB connection with bursting up to 100 MB. Trying to do a file migration from one site to the data center and I'm only getting .5-.7 MBytes the other sites are fine. Tried doing some captures on the VPLS interface while testing with iperf and I'm seeing retransmissions and unseen segment packets. Not sure if this could be causing the slowness or not.</p><p>Here is a snippet of the capture <a href="https://www.cloudshark.org/captures/619976c41207">https://www.cloudshark.org/captures/619976c41207</a></p></div><div id="question-tags" class="tags-container tags">unseen dropped slowness retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '16, 21:32</strong></p><img src="https://secure.gravatar.com/avatar/dd6aa5228fe1c94df3e3452c79342410?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wargresh&#39;s gravatar image" /><p>wargresh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wargresh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Apr '16, 05:47</p></div></div><div id="comments-container-51657" class="comments-container"><span id="51693"></span><div id="comment-51693" class="comment"><div id="post-51693-score" class="comment-score"></div><div class="comment-text"><p>you have not taken capture from beginning but it looks that RTT is around 2 ms,regarding your IPERF Testing on port 5001,i could see your iperf client only sending 17032 bytes/rtt so 17032*8 = 136256 bits and RTT is approx 2 ms = 136256/.002 = 68 mbits/sec.In your capture there are retransmission as well with RTO of 300 ms,no delayed ack.so the slowness could be due to 10.10.3.24 stop acking packets that caused RTO to kick in.if you can take a capture on 10.10.3.24 you could find out the reason.</p></div><div id="comment-51693-info" class="comment-info"><span class="comment-age">(14 Apr '16, 23:30)</span> kishan pandey</div></div><span id="51694"></span><div id="comment-51694" class="comment"><div id="post-51694-score" class="comment-score"></div><div class="comment-text"><p>or i feel 10.10.3.24 didn't received the packets,could be packet dropped.</p></div><div id="comment-51694-info" class="comment-info"><span class="comment-age">(14 Apr '16, 23:40)</span> kishan pandey</div></div><span id="51700"></span><div id="comment-51700" class="comment"><div id="post-51700-score" class="comment-score"></div><div class="comment-text"><p>Kishan,</p><p>Thanks for the information. I have performed a capture on 10.10.3.24 specifying the iperf traffic. Here is the link: <a href="https://www.cloudshark.org/captures/2229954b2e30">https://www.cloudshark.org/captures/2229954b2e30</a></p></div><div id="comment-51700-info" class="comment-info"><span class="comment-age">(15 Apr '16, 07:26)</span> wargresh</div></div><span id="51704"></span><div id="comment-51704" class="comment"><div id="post-51704-score" class="comment-score"></div><div class="comment-text"><p>yes,there is packet drop,10.10.3.24 didnt received packets and because iperf is only sending 16k bytes/rtt and waits for ack before sending any data,due to this behaviour fast retransmit is not triggered and sender is waiting for rto</p></div><div id="comment-51704-info" class="comment-info"><span class="comment-age">(15 Apr '16, 10:14)</span> kishan pandey</div></div></div><div id="comment-tools-51657" class="comment-tools"></div><div class="clear"></div><div id="comment-51657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

