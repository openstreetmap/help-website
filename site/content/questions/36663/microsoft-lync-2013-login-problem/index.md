+++
type = "question"
title = "Microsoft Lync 2013 login problem"
description = '''I am investigating strange behavior of Microsoft Lync login problem. The problem is: &quot;With same client PC(MAC address:c0:3f:d5:b0:a6:0a) and same login account, Lync login failed with IP add 10.212.76.119, while login successed with IP 10.212.76.73&quot; I have two Wireshark&#x27;s logs, one for problematic s...'''
date = "2014-09-27T22:09:00Z"
lastmod = "2014-09-28T00:00:00Z"
weight = 36663
keywords = [ "login", "lync" ]
aliases = [ "/questions/36663" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Microsoft Lync 2013 login problem](/questions/36663/microsoft-lync-2013-login-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36663-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am investigating strange behavior of Microsoft Lync login problem. The problem is: "With same client PC(MAC address:c0:3f:d5:b0:a6:0a) and same login account, Lync login failed with IP add 10.212.76.119, while login successed with IP 10.212.76.73"</p><p>I have two Wireshark's logs, one for problematic scenario and one for successful. I uploaded them here:</p><ul><li><strong>failure</strong>: <a href="https://www.cloudshark.org/captures/7329337bc0b5">https://www.cloudshark.org/captures/7329337bc0b5</a></li><li><strong>success</strong>: <a href="https://www.cloudshark.org/captures/e11a838297d5">https://www.cloudshark.org/captures/e11a838297d5</a></li></ul><p>I can see that both in problematic &amp; successful scenario there are series of "TCP Dup Ack" and "TCP Previous segment not captured", while in problematic scenario, no "TCP Retransmission" found.</p><p>Could anybody explain why it could be the possible reason for this to happen?</p><p>Thanks a lot in advance, Kevin</p></div><div id="question-tags" class="tags-container tags">login lync</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '14, 22:09</strong></p><img src="https://secure.gravatar.com/avatar/d844c6780e03ae884146f9c6c3861e55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hongtj&#39;s gravatar image" /><p>hongtj<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hongtj has no accepted answers">0%</span></p></div></div><div id="comments-container-36663" class="comments-container"></div><div id="comment-tools-36663" class="comment-tools"></div><div class="clear"></div><div id="comment-36663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36665"></span>

<div id="answer-container-36665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36665-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><ol><li>In 119 client capture after dup ack server 23 is sending reset.</li><li>Server 23 IP header consist AF31 assured forwarding qos setting.</li><li>If you see in working pcap the pattern was same first packet(1460 bytes - full mss) size is dropped and then retransmission were re-packetised with 3 full 536 bytes packets this indicates possible MTU issue in hops beetween client and server.</li><li>But for client 119,server 23 could be keep on sending full mss size packet(note that packets from 23 has DF bit set)and after multiple retransmission 23 gives up and sent RST,could be for several reason,For e.g, Device with lowest mtu not sending icmp fragmentation needed message because of ICMP rate limiting feature.</li></ol><p>You can check MTU setting on all hops between client and server.It looks there are 6 hops by looking at TTL of server 10.232.211.23 which is 122.This is just assumption capture at both end will clear the picture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '14, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '14, 09:27</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-36665" class="comments-container"><span id="36668"></span><div id="comment-36668" class="comment"><div id="post-36668-score" class="comment-score"></div><div class="comment-text"><p>Quite exactly! client 119 is linked with server 23 with GRE tunnel. Server 23 is marked with AF31 for QOS.</p><p>So it seems what we should do next is to find out where along the path the ICMP message is blocked or where along the path the DF bit has been setted. Is that correct?</p><p>Thanks a lot, Kevin</p></div><div id="comment-36668-info" class="comment-info"><span class="comment-age">(28 Sep '14, 07:15)</span> hongtj</div></div><span id="36712"></span><div id="comment-36712" class="comment"><div id="post-36712-score" class="comment-score"></div><div class="comment-text"><p>The better method of handling this would be to reduce the MSS in the syn packets as the enter the GRE tunnel. <a href="https://www.google.de/?gws_rd=ssl#q=adjust-mss+gre">https://www.google.de/?gws_rd=ssl#q=adjust-mss+gre</a></p></div><div id="comment-36712-info" class="comment-info"><span class="comment-age">(29 Sep '14, 14:20)</span> mrEEde</div></div></div><div id="comment-tools-36665" class="comment-tools"></div><div class="clear"></div><div id="comment-36665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

