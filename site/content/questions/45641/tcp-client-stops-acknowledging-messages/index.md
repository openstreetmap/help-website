+++
type = "question"
title = "TCP client stops acknowledging messages"
description = '''Hi,  In our setup we have a TCP server that continuously sends data (@35 Mbyte/sec) to a single TCP client and, after running for more than 24hours continuously, the client side stops acknowledging the messages with as a result that the server side retransmitting the data over and over again. We cau...'''
date = "2015-09-05T10:31:00Z"
lastmod = "2015-09-07T10:32:00Z"
weight = 45641
keywords = [ "ack", "tcp" ]
aliases = [ "/questions/45641" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP client stops acknowledging messages](/questions/45641/tcp-client-stops-acknowledging-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45641-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In our setup we have a TCP server that continuously sends data (@35 Mbyte/sec) to a single TCP client and, after running for more than 24hours continuously, the <strong>client side stops acknowledging</strong> the messages with as a result that the server side retransmitting the data over and over again. We caught this issue using wireshark running on another Dell Server with a fast raid controller for storage. Any ideas on why the client side stops sending ACKs?</p><p>A couple of keywords on our setup: . Server side: a FPGA . Client side: Dell Server (windows server 2012) with a Intel 4P I350-t network adapter . TCP client using overlapped IO</p><p>Kind regard, Peter</p></div><div id="question-tags" class="tags-container tags">ack tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '15, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/a2b471899958da293a3882bb553832a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peter73&#39;s gravatar image" /><p>peter73<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peter73 has no accepted answers">0%</span></p></div></div><div id="comments-container-45641" class="comments-container"><span id="45647"></span><div id="comment-45647" class="comment"><div id="post-45647-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a capture file somewhere publicly accessible, like <a href="http://www.cloudshark.org">http://www.cloudshark.org</a>, dropbox or somwhere else, and post a link to the capture file.</p></div><div id="comment-45647-info" class="comment-info"><span class="comment-age">(06 Sep '15, 12:12)</span> Christian_R</div></div><span id="45653"></span><div id="comment-45653" class="comment"><div id="post-45653-score" class="comment-score"></div><div class="comment-text"><p>I've placed an export of the capture in my dropbox, <a href="https://dl.dropboxusercontent.com/u/29942579/Retransmit_Export_2015_09_07.pcapng">https://dl.dropboxusercontent.com/u/29942579/Retransmit_Export_2015_09_07.pcapng</a></p><p>Many thanks for your support, Peter</p></div><div id="comment-45653-info" class="comment-info"><span class="comment-age">(07 Sep '15, 01:37)</span> peter73</div></div></div><div id="comment-tools-45641" class="comment-tools"></div><div class="clear"></div><div id="comment-45641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45655"></span>

<div id="answer-container-45655" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45655-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would say it is due to the client losing the ARP entry for the server.<br />
Adding a static ARP might circumvent this problem ...</p><pre><code>arp /s 192.168.4.1 00-50-c2-43-63-1d 00-AA-00-4F-2A-9C</code></pre><p>NB: You are receiving multicast packets for the ip.dst == 192.168.9.255 which is far away from your interface's IP address 192.168.4.100 so maybe this is a misconfiguration issue and is contributing to this problem...</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 04:00</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-45655" class="comments-container"><span id="45658"></span><div id="comment-45658" class="comment"><div id="post-45658-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply. What can be the reason for the client to loose the ARP entry? is there a log that shows this was the case? I'll will check the multicast from 192.168.9.255, no idea at the moment where this is coming from.</p><p>Regards, Peter</p></div><div id="comment-45658-info" class="comment-info"><span class="comment-age">(07 Sep '15, 04:50)</span> peter73</div></div><span id="45665"></span><div id="comment-45665" class="comment"><div id="post-45665-score" class="comment-score"></div><div class="comment-text"><p>The multicast is coming one of the other interface of the the machine doing the wireshark capture, no problem there because this is not used operationally.</p></div><div id="comment-45665-info" class="comment-info"><span class="comment-age">(07 Sep '15, 08:38)</span> peter73</div></div></div><div id="comment-tools-45655" class="comment-tools"></div><div class="clear"></div><div id="comment-45655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45672"></span>

<div id="answer-container-45672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45672-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Till packet 9 server is sending data to client on mac a0:36:9f:2b:f2:f4 and it received ack also but from packet 12 server is sending data to same client(same session) on mac a0:36:9f:2b:f2:84 and may be a different client system where that session doesnt exist,so no ack sent by this client.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-45672" class="comments-container"><span id="45674"></span><div id="comment-45674" class="comment"><div id="post-45674-score" class="comment-score"></div><div class="comment-text"><p>Holy smokes! I totally missed that. Thank you very much for pointing this out!</p></div><div id="comment-45674-info" class="comment-info"><span class="comment-age">(07 Sep '15, 13:07)</span> peter73</div></div></div><div id="comment-tools-45672" class="comment-tools"></div><div class="clear"></div><div id="comment-45672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

