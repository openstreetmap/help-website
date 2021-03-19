+++
type = "question"
title = "Retransmission on LAN"
description = '''Hi All, I am new with Wireshark. I did test via my LAN and get the result like the data below : ****************************************************************************************** 1 2013-03-20 03:55:50.803 172.17.3.41 172.17.3.61 TCP 66 51844 &amp;gt; ssh [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=25...'''
date = "2013-03-19T21:28:00Z"
lastmod = "2013-03-20T03:43:00Z"
weight = 19665
keywords = [ "retransmissions" ]
aliases = [ "/questions/19665" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Retransmission on LAN](/questions/19665/retransmission-on-lan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19665-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am new with Wireshark. I did test via my LAN and get the result like the data below : <code>****************************************************************************************** 1   2013-03-20 03:55:50.803 172.17.3.41 172.17.3.61 TCP 66  51844 &gt; ssh [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1 2   2013-03-20 03:55:50.804 172.17.3.61 172.17.3.41 TCP 66  ssh &gt; 51844 [SYN, ACK] Seq=0 Ack=1 Win=14600 Len=0 MSS=1460 SACK_PERM=1 WS=64 3   2013-03-20 03:55:50.804 172.17.3.41 172.17.3.61 TCP 54  51844 &gt; ssh [ACK] Seq=1 Ack=1 Win=65536 Len=0 4   2013-03-20 03:55:50.871 172.17.3.61 172.17.3.41 SSH 75  Server Protocol: SSH-2.0-OpenSSH_5.3\r 5   2013-03-20 03:55:51.071 172.17.3.61 172.17.3.41 SSH 75  [TCP Retransmission] Encrypted response packet len=21 6   2013-03-20 03:55:51.072 172.17.3.41 172.17.3.61 TCP 66  51844 &gt; ssh [ACK] Seq=1 Ack=22 Win=65536 Len=0 SLE=1 SRE=22 7   2013-03-20 03:55:54.564 172.17.3.41 172.17.3.61 TCP 54  51844 &gt; ssh [FIN, ACK] Seq=1 Ack=22 Win=65536 Len=0 8   2013-03-20 03:55:54.565 172.17.3.61 172.17.3.41 TCP 60  ssh &gt; 51844 [FIN, ACK] Seq=22 Ack=2 Win=14656 Len=0 9   2013-03-20 03:55:54.565 172.17.3.41 172.17.3.61 TCP 54  51844 &gt; ssh [ACK] Seq=2 Ack=23 Win=65536 Len=0 ***************************************************************************</code> As you seen on packet no.5 , there is TCP Retransmission. Could I know why this happen &amp; what is the cause of ? and If I am not wrong the retransmission of packet no.5 is for packet no 4 , isn't it ?</p><p>Please your Advice..</p><p>Best Regards, Hadi</p></div><div id="question-tags" class="tags-container tags">retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '13, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/aad0fb978bd526805a6676f7cc800cc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vazr84&#39;s gravatar image" /><p>vazr84<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vazr84 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Mar '13, 03:35</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-19665" class="comments-container"></div><div id="comment-tools-19665" class="comment-tools"></div><div class="clear"></div><div id="comment-19665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19670"></span>

<div id="answer-container-19670" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19670-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like packet no. 5 is a retransmission of no. 4 since there is nothing else that could that one be a retransmission for. The first three packets have 0 TCP payload bytes, and no. 5 has 21 bytes, so it needs to be a retransmission of no. 4.</p><p>Reason for the retransmission is probably that 172.17.3.61 didn't acknowledge the packet (either because it was lost, or because it was lazy), so 172.17.3.41 sent it again after 200ms. The round trip time between the two IPs is about 1ms, so there should have been an acknowledge from 172.17.3.61 way faster than 200ms, but there wasn't. Thus, retransmission.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '13, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19670" class="comments-container"></div><div id="comment-tools-19670" class="comment-tools"></div><div class="clear"></div><div id="comment-19670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

