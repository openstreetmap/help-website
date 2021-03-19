+++
type = "question"
title = "Retransmission and RTO"
description = '''I am hoping to confirm I am on the right track in understanding TCP retransmissions. I have uploaded the trace file to CloudShark. https://www.cloudshark.org/captures/0e6fc62cdd21 We can see that frame #9 ACKed frame #8 but frame#10 is a retransmission of frame #8. So would it seem the frame #9 ACK ...'''
date = "2015-08-17T13:21:00Z"
lastmod = "2015-08-18T05:58:00Z"
weight = 45169
keywords = [ "rto" ]
aliases = [ "/questions/45169" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Retransmission and RTO](/questions/45169/retransmission-and-rto)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45169-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am hoping to confirm I am on the right track in understanding TCP retransmissions. I have uploaded the trace file to CloudShark. <a href="https://www.cloudshark.org/captures/0e6fc62cdd21">https://www.cloudshark.org/captures/0e6fc62cdd21</a></p><p>We can see that frame #9 ACKed frame #8 but frame#10 is a retransmission of frame #8. So would it seem the frame #9 ACK was not received by TCP causing the RTO timer to expire resulting in the retransmission seen in frame #10?</p><p>I guess my confusion is if 10.69.67.100 actually received the ACK of frame #9, did the RTO timer expire early causing an unnecessary retransmission?</p><p>I am researching and reading some relevant papers and RFC's but still not certain of the analysis. Any comments are definitely appreciated.</p><p>I am sure you can see that I did anonymize the trace file but the ip.id values for 10.69.67.100 were sequential starting in frame #4 and sequential for 172.16.1.216 starting in frame #7.</p><p>Cheers GP</p></div><div id="question-tags" class="tags-container tags">rto</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '15, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/68b7271b161241faff6b70c8f1769d63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GP%20CC&#39;s gravatar image" /><p>GP CC<br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GP CC has no accepted answers">0%</span></p></div></div><div id="comments-container-45169" class="comments-container"></div><div id="comment-tools-45169" class="comment-tools"></div><div class="clear"></div><div id="comment-45169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45199"></span>

<div id="answer-container-45199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45199-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This seems to be a timing issue with the delay-ack timer at the windows client (200ms) matching the Retransmission-Time-Out of 200ms at the Linux server.<br />
The trace was taken at the server running Linux under VMWare and frame 9 - a delayed ACK - was not lost but was arriving shortly <strong><em>after</em></strong> the 200ms RTO at the server already expired and the (assumed to be lost) segment was already put on the retransmission queue resulting in this spurious retransmission.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/RTO.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '15, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-45199" class="comments-container"><span id="45204"></span><div id="comment-45204" class="comment"><div id="post-45204-score" class="comment-score"></div><div class="comment-text"><p>Thank you mrEEde for your review and comments.</p><p>I believe the capture was taken off the same switch as the server but am still trying to confirm that.</p><p>Just based on what we see in the trace file is it possible to be 100% sure of the suspected spurious retransmission? Please do not take the question wrong, I am just trying to understand better.</p><p>I am reading on SACK also, does the fact that frame #11 (the DUP ACK) include a SLE/SRE of 463-468 provide any extra confirmation that the original frame #8 was actually received?</p><p>Again your comments are greatly appreciated.</p><p>Cheers GP</p></div><div id="comment-45204-info" class="comment-info"><span class="comment-age">(18 Aug '15, 08:56)</span> GP CC</div></div><span id="45207"></span><div id="comment-45207" class="comment"><div id="post-45207-score" class="comment-score">1</div><div class="comment-text"><p>The trace was taken close to the server as the TTL of the server's packets are still at its initial value of 64 whereas the clients packets arrive with a TTL of 127 which is 128 decremented by 1 router (Juniper).</p><p>Is it possible to be 100% sure ? - It is 50% possible to be 200% sure ;-) The retransmission was not necessary (or spurious) as the client's ACK in #9 asked the server to continue with seq 468 so there is no need to send 463 again. As the server retransmits 463 the client's dup_ACK still asks for 468, why Windows TCP attaches a SACK option is as needless as the re-transmission itself as there was no gap to report.</p></div><div id="comment-45207-info" class="comment-info"><span class="comment-age">(18 Aug '15, 10:40)</span> mrEEde</div></div></div><div id="comment-tools-45199" class="comment-tools"></div><div class="clear"></div><div id="comment-45199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

