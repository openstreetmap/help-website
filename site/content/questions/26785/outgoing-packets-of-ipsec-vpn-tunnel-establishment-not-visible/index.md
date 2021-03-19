+++
type = "question"
title = "Outgoing packets of IPsec VPN tunnel establishment not visible"
description = '''Hi Guys, I am trying to capture a VPN tunnel establishment between 2 firewalls. While I am able to get the trace on TCPDUMP, however when I write it to a pcap file, the outgoing packets are not present. What could I be doing wrong or is there something else I need to do while I do the capture? 01:05...'''
date = "2013-11-08T11:51:00Z"
lastmod = "2013-11-08T11:51:00Z"
weight = 26785
keywords = [ "sa", "vpn", "tcpdump", "ipsec" ]
aliases = [ "/questions/26785" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Outgoing packets of IPsec VPN tunnel establishment not visible](/questions/26785/outgoing-packets-of-ipsec-vpn-tunnel-establishment-not-visible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26785-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I am trying to capture a VPN tunnel establishment between 2 firewalls. While I am able to get the trace on TCPDUMP, however when I write it to a pcap file, the outgoing packets are not present. What could I be doing wrong or is there something else I need to do while I do the capture?</p><p>01:05:52.154481 In IP 192.168.3.1.500 &gt; 192.168.4.2.500: isakmp: phase 1 I ident: [|sa] 01:05:52.186367 Out IP 192.168.4.2.500 &gt; 192.168.3.1.500: isakmp: phase 1 R ident: [|sa]</p><p>"In" packets are not visible. Any help would be appreciated. Thanks Rahul</p></div><div id="question-tags" class="tags-container tags">sa vpn tcpdump ipsec</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '13, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/b623c78251ba855c9305db43e110ea55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rahultn&#39;s gravatar image" /><p>Rahultn<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rahultn has no accepted answers">0%</span></p></div></div><div id="comments-container-26785" class="comments-container"><span id="26788"></span><div id="comment-26788" class="comment"><div id="post-26788-score" class="comment-score"></div><div class="comment-text"><ul><li>what is your (exact) tcpdump command for writing the pcap file?</li><li>where do you capture? On one of the firewalls, or somewhere in between?</li></ul></div><div id="comment-26788-info" class="comment-info"><span class="comment-age">(08 Nov '13, 15:37)</span> Kurt Knochner ♦</div></div><span id="26791"></span><div id="comment-26791" class="comment"><div id="post-26791-score" class="comment-score"></div><div class="comment-text"><p>Thanks for response Kurt. FW1 ------ FW2 On the FW2 receiving interface I did the capture</p><blockquote><p>tcpdump -ni &lt;int&gt; -w File.pcap</p></blockquote><p>On this dump i am able to see bidirectional traffic, but when I write it to a pcap file and open it only<br />
192.168.4.2.500 &gt; 192.168.3.1.500: isakmp: phase 1 R ident: [|sa] is available.</p><p>(Correction to the q: Incoming packets are visible)</p></div><div id="comment-26791-info" class="comment-info"><span class="comment-age">(08 Nov '13, 15:45)</span> Rahultn</div></div><span id="26793"></span><div id="comment-26793" class="comment"><div id="post-26793-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Thanks for response Kurt. FW1 ------ FW2 <strong>On the FW2 receiving interface I did the capture</strong></p></blockquote><p>What type of firewall is this?</p><p>To repeat it:</p><ul><li>if you run tcpdump on the console (tcpdump -ni &lt;int&gt;) you <strong>do</strong> see IKE traffic <strong>in both</strong> directions</li><li>if you let tcpdump write a file (tcpdump -ni &lt;int&gt; -w file.pcap) you <strong>don't</strong> see IKE <strong>in both</strong> directions?</li></ul><p>If so (and you used <strong>no other options</strong> for tcpdump as the one you posted), <strong>how did you check the content of the pcap file?</strong></p><p>BTW: Are there tagged VLAN ports involved on firewall FW2 (the interface you sniffed)?</p></div><div id="comment-26793-info" class="comment-info"><span class="comment-age">(08 Nov '13, 16:01)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26785" class="comment-tools"></div><div class="clear"></div><div id="comment-26785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

