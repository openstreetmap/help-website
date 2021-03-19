+++
type = "question"
title = "Difference between using src and dst in tcpdump commands"
description = '''Hi, Could you please explain the difference between working nature of below two commands. tcpdump -w xpackets2.pcap -i eth0 src host-name tcpdump -w xpackets2.pcap -i eth0 dst host-name Thanks in advance.'''
date = "2013-12-24T01:23:00Z"
lastmod = "2013-12-24T12:19:00Z"
weight = 28356
keywords = [ "commands", "tcpdump" ]
aliases = [ "/questions/28356" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Difference between using src and dst in tcpdump commands](/questions/28356/difference-between-using-src-and-dst-in-tcpdump-commands)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28356-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Could you please explain the difference between working nature of below two commands.</p><p>tcpdump -w xpackets2.pcap -i eth0 src host-name</p><p>tcpdump -w xpackets2.pcap -i eth0 dst host-name</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">commands tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '13, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/57906d92ff804f06bf0894e8a4b425ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manivas&#39;s gravatar image" /><p>Manivas<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manivas has no accepted answers">0%</span></p></div></div><div id="comments-container-28356" class="comments-container"><span id="28359"></span><div id="comment-28359" class="comment"><div id="post-28359-score" class="comment-score"></div><div class="comment-text"><p>i telnet to the particular ip address from putty and executing some commands on that. I need to capture the packets for both sending commands to that particular ip address from putty and responses from that same ip address for these commands.</p><p>So could you please suggest the tcpdump commands to work for this.</p><p>Thanks in advance.</p></div><div id="comment-28359-info" class="comment-info"><span class="comment-age">(24 Dec '13, 01:56)</span> Manivas</div></div></div><div id="comment-tools-28356" class="comment-tools"></div><div class="clear"></div><div id="comment-28356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28372"></span>

<div id="answer-container-28372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28372-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Using a capture filter of 'src host-name' limits the captured packets to those originating from host-name. Similarly 'dst host-name' limits packets to those going to host-name.</p><p>To capture both types of packets you need to use a filter of 'host host-name'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '13, 12:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-28372" class="comments-container"><span id="28403"></span><div id="comment-28403" class="comment"><div id="post-28403-score" class="comment-score"></div><div class="comment-text"><p>Hi Thanks,</p><p>You are suggesting that to capture packets sending to particular ip address and receiving from that same particular ip address in linux machine, we need to use the command like below.</p><p>"tcpdump -w xpackets2.pcap -i eth0 host host-name"</p></div><div id="comment-28403-info" class="comment-info"><span class="comment-age">(26 Dec '13, 05:38)</span> Manivas</div></div><span id="28405"></span><div id="comment-28405" class="comment"><div id="post-28405-score" class="comment-score"></div><div class="comment-text"><p>Sure, replacing the "host-name" part with the IP address of interest.</p><p>See the first example on the Wireshark <a href="http://wiki.wireshark.org/CaptureFilters">Capture Filters</a> Wiki page.</p></div><div id="comment-28405-info" class="comment-info"><span class="comment-age">(26 Dec '13, 06:39)</span> grahamb ♦</div></div></div><div id="comment-tools-28372" class="comment-tools"></div><div class="clear"></div><div id="comment-28372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

