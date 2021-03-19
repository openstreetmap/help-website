+++
type = "question"
title = "Wireshark on pppoe"
description = '''Hi everyone, I have just one network card in my PC (windows 7)and Wireshark displays the address 10.0.0.1 as its only address. I was asked to run the following(thanks Kurt for that) dumpcap -D -M ipconfig /all  Following are the results... Can someone explain why don&#x27;t I get a routable address in Wi...'''
date = "2012-07-31T01:43:00Z"
lastmod = "2012-07-31T23:49:00Z"
weight = 13175
keywords = [ "pppoe" ]
aliases = [ "/questions/13175" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on pppoe](/questions/13175/wireshark-on-pppoe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13175-score" class="post-score" title="current number of votes">0</div><span id="post-13175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, I have just one network card in my PC (windows 7)and Wireshark displays the address 10.0.0.1 as its only address. I was asked to run the following(thanks Kurt for that) dumpcap -D -M ipconfig /all Following are the results... Can someone explain why don't I get a routable address in Wireshark display(though it captures the packets and displys them fine). Regards I. Lesher</p><p>the respond for dumpcap -D -M</p><pre><code> 1. \Device\NPF_{7A460928-A487-4219-BEC1-32E09C8B2CEA}  Atheros AR8121/AR8113/AR8114 PCI-E Ethernet Controller(NDIS6.20)    10.0.0.1    network</code></pre><p>Here is the respond for ipconfig /all Actually I cut the answer since it continues with a list of Tunnel adapters which I believe don't contribute here. Regards I. Lesher</p><pre><code>Windows IP Configuration

   Host Name . . . . . . . . . . . . : kobi-PC
   Primary Dns Suffix  . . . . . . . : 
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No

PPP adapter ‡‰…˜ ”‘ ˜‡:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : ‡‰…˜ ”‘ ˜‡
   Physical Address. . . . . . . . . : 
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 85.250.119.39(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.255
   Default Gateway . . . . . . . . . : 0.0.0.0
   DNS Servers . . . . . . . . . . . : 194.90.1.5
                                       212.143.212.143
   NetBIOS over Tcpip. . . . . . . . : Disabled

Ethernet adapter Local Area Connection:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Atheros AR8121/AR8113/AR8114 PCI-E Ethernet Controller(NDIS6.20)
   Physical Address. . . . . . . . . : E0-CB-4E-D3-5C-F1
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::550c:2c41:4fe3:ec1c%11(Preferred) 
   IPv4 Address. . . . . . . . . . . : 10.0.0.1(Preferred) 
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : ‰…™‰™‰ 20 ‰…‰ 2012 18:47:09
   Lease Expires . . . . . . . . . . : ‰…‡‰™‰ 26 ‰…‰ 2012 11:47:19
   Default Gateway . . . . . . . . . : 10.0.0.138
   DHCP Server . . . . . . . . . . . : 10.0.0.138
   DHCPv6 IAID . . . . . . . . . . . : 249613134
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-16-D4-C3-6A-E0-CB-4E-D3-5C-F1
   DNS Servers . . . . . . . . . . . : 10.0.0.138
                                       10.0.0.138
   NetBIOS over Tcpip. . . . . . . . : Enabled

Tunnel adapter Local Area Connection* 23:

   Connection-specific DNS Suffix  . : 
   Description . . . . . . . . . . . : Microsoft 6to4 Adapter #16
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   IPv6 Address. . . . . . . . . . . : 2002:55fa:7727::55fa:7727(Preferred) 
   Default Gateway . . . . . . . . . : 2002:c058:6301::c058:6301
   DNS Servers . . . . . . . . . . . : 194.90.1.5
                                       212.143.212.143</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pppoe" rel="tag" title="see questions tagged &#39;pppoe&#39;">pppoe</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '12, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/c46b9d0cf13adb17325f5d9519406546?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="triplebit&#39;s gravatar image" /><p><span>triplebit</span><br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="triplebit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jul '12, 02:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-13175" class="comments-container"></div><div id="comment-tools-13175" class="comment-tools"></div><div class="clear"></div><div id="comment-13175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13177"></span>

<div id="answer-container-13177" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13177-score" class="post-score" title="current number of votes">0</div><span id="post-13177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>see my latest comment in <a href="http://ask.wireshark.org/questions/12938/pppoe-architecture-tracing">this question</a>. It's about ppp adapters and WinPcap. You cannot capture on the "virtual" ppp adapter. However, you can capture on the NIC that is connected to the DSL modem.</p><p>I believe, WinPcap does not show ppp adapters, as you cannot capture on them anyway...</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '12, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jul '12, 03:13</strong> </span></p></div></div><div id="comments-container-13177" class="comments-container"><span id="13180"></span><div id="comment-13180" class="comment"><div id="post-13180-score" class="comment-score"></div><div class="comment-text"><p>You can use Network Monitor from Microsoft to capture on PPP adaptors, and then load the captures in Wireshark.</p></div><div id="comment-13180-info" class="comment-info"><span class="comment-age">(31 Jul '12, 04:48)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="13206"></span><div id="comment-13206" class="comment"><div id="post-13206-score" class="comment-score"></div><div class="comment-text"><p>Thanks again Kurt, That explains completely my question. WinPcap has the ability to send packets, by injecting them to the network. Do you think that this feature is also available on the NIC that is connected to the DSL modem? Regrds I. Lesher</p></div><div id="comment-13206-info" class="comment-info"><span class="comment-age">(31 Jul '12, 21:53)</span> <span class="comment-user userinfo">triplebit</span></div></div><span id="13209"></span><div id="comment-13209" class="comment"><div id="post-13209-score" class="comment-score"></div><div class="comment-text"><p>That should work if you do it with the correct encapsulation.</p><blockquote><p>Sample without PPPoE encapsulation!<br />
<code>http://badishi.com/injecting-packets-with-winpcap/</code></p></blockquote></div><div id="comment-13209-info" class="comment-info"><span class="comment-age">(31 Jul '12, 23:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-13177" class="comment-tools"></div><div class="clear"></div><div id="comment-13177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

