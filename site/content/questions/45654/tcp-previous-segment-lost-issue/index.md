+++
type = "question"
title = "TCP Previous segment lost issue?"
description = '''Hello,  Tying to exchange message on ssh server but not completed anyhow due to issue on TCP level.  Could any body help me out why there no message exchanged after &quot;TCP Previous segment lost&quot;?  Please find the Wireshark file at - https://www.cloudshark.org/captures/6c6df098b205 Thanks in advanced :...'''
date = "2015-09-07T03:24:00Z"
lastmod = "2015-09-07T04:30:00Z"
weight = 45654
keywords = [ "tcp", "wireshark" ]
aliases = [ "/questions/45654" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Previous segment lost issue?](/questions/45654/tcp-previous-segment-lost-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45654-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Tying to exchange message on ssh server but not completed anyhow due to issue on TCP level. Could any body help me out why there no message exchanged after "TCP Previous segment lost"?</p><p>Please find the Wireshark file at - <a href="https://www.cloudshark.org/captures/6c6df098b205">https://www.cloudshark.org/captures/6c6df098b205</a></p><p>Thanks in advanced :)<img src="https://osqa-ask.wireshark.org/upfiles/NoBackupWireshark.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '15, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/010ffa1f01aa73d3d3d58b3305299d83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sammi&#39;s gravatar image" /><p>sammi<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sammi has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 07 Sep '15, 03:34</p></div></div><div id="comments-container-45654" class="comments-container"></div><div id="comment-tools-45654" class="comment-tools"></div><div class="clear"></div><div id="comment-45654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45656"></span>

<div id="answer-container-45656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45656-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The trace taken at the server shows that the first 'full-MSS' segment from the client (tcp.seq==1717) that contained 1448 (not 1148 as initially posted] bytes did not make it to your server.</p><p>Your server sends an ACK with tcp.ack==1717 asking for the segment that is missing but it never arrives (most probably because the retransmitted packets suffer the same death).<br />
A quick circumvention could be to artificially reduce the MTU size towards the client's subnet using</p><pre><code>ip route add 10.1.68.0/24 via 10.1.6.1 mtu 1428</code></pre><p>You can try a ping to find out what maximum size goes through your infrastructure unfragmented.</p><pre><code>ping -s 1400 -M do 10.1.68.59</code></pre><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Sep '15, 07:56</p></div></div><div id="comments-container-45656" class="comments-container"><span id="45731"></span><div id="comment-45731" class="comment"><div id="post-45731-score" class="comment-score"></div><div class="comment-text"><p>Hi Matthias,</p><p>Could you please elaborate more because I didn't found 1148 bytes in trace for (tcp.seq==1717)? My colleague wants a reason to change the MTU size.</p><p>Thanks in advanced !</p><p>Regards, Sammi</p></div><div id="comment-45731-info" class="comment-info"><span class="comment-age">(09 Sep '15, 01:03)</span> sammi</div></div><span id="45809"></span><div id="comment-45809" class="comment"><div id="post-45809-score" class="comment-score">1</div><div class="comment-text"><p>@mrEEde, 1448 bytes are missing, not 1148. @sammi, look at the relative seq number of packet 61 (1717) and packet 62 (3165), then you will understand why 1448. Do the ping test before changing the MTU.</p></div><div id="comment-45809-info" class="comment-info"><span class="comment-age">(12 Sep '15, 05:57)</span> Roland</div></div><span id="45811"></span><div id="comment-45811" class="comment"><div id="post-45811-score" class="comment-score"></div><div class="comment-text"><p>Roland's right, the negotiated MSS is 1448 , well spotted!</p></div><div id="comment-45811-info" class="comment-info"><span class="comment-age">(12 Sep '15, 07:54)</span> mrEEde</div></div><span id="45812"></span><div id="comment-45812" class="comment"><div id="post-45812-score" class="comment-score"></div><div class="comment-text"><p>The negociated MSS is 1460. The missing packet had 1448 bytes of data.</p></div><div id="comment-45812-info" class="comment-info"><span class="comment-age">(12 Sep '15, 08:50)</span> Roland</div></div><span id="45814"></span><div id="comment-45814" class="comment"><div id="post-45814-score" class="comment-score">1</div><div class="comment-text"><p>A MSS of 1460 with negotiated timestamps option results in a net segment size of 1448 ...</p></div><div id="comment-45814-info" class="comment-info"><span class="comment-age">(12 Sep '15, 09:07)</span> mrEEde</div></div></div><div id="comment-tools-45656" class="comment-tools"></div><div class="clear"></div><div id="comment-45656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

