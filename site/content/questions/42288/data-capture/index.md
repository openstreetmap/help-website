+++
type = "question"
title = "Data Capture."
description = '''Can some one tell me if this software is for capturing all the data that goes through my wireless router? If it is, where I could find the instructions to set it up or if it is not, what software could I use to accomplish this? We connect couples Ipads, an Iphone and note3, one laptop and a desktop....'''
date = "2015-05-10T15:20:00Z"
lastmod = "2015-05-10T19:25:00Z"
weight = 42288
keywords = [ "capture", "data" ]
aliases = [ "/questions/42288" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Data Capture.](/questions/42288/data-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42288-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can some one tell me if this software is for capturing all the data that goes through my wireless router? If it is, where I could find the instructions to set it up or if it is not, what software could I use to accomplish this? We connect couples Ipads, an Iphone and note3, one laptop and a desktop. I want to be able to capture all the data(websites browsed, email content, facebook, whatsapp messages, etc... Thanks.</p></div><div id="question-tags" class="tags-container tags">capture data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '15, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/e09bc3e4bbf06180dd80fd330dbf4695?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cubilla1506&#39;s gravatar image" /><p>cubilla1506<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cubilla1506 has no accepted answers">0%</span></p></div></div><div id="comments-container-42288" class="comments-container"></div><div id="comment-tools-42288" class="comment-tools"></div><div class="clear"></div><div id="comment-42288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42290"></span>

<div id="answer-container-42290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42290-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The simple answer is yes, Wireshark can capture the data going through a wireless router. If you are interested in capturing over the air (i.e., using a separate laptop/PC to capture WiFi packets) then please read the following Wiki: <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></p><p>Some wireless routers allow users to capture directly from the router using tcpdump or some other tool. If you do not want to capture over the air, then you might want to investigate this option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '15, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42290" class="comments-container"></div><div id="comment-tools-42290" class="comment-tools"></div><div class="clear"></div><div id="comment-42290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42291"></span>

<div id="answer-container-42291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42291-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think Wireshark's role is better described as an analyzer of captured data. When it comes to actually capturing packets, usually the main challenge is in getting your system to 'see' the packets you're trying to capture (eg: for your wireless router, the challenge is to get all the packets the router sees in one place where you can perform a capture). Once you have a system that is receiving all the packets you want to capture, many tools (tcpdump, snoop, dumpcap) can do the actual capture itself. The power of Wireshark lies in its ability to help analyze the packets once they are captured.</p><p>In fact, Wireshark itself doesn't really capture packets at all. Rather, it calls on dumpcap behind the scenes when you perform captures in the GUI.</p><p>So, for the task at hand I wouldn't start by asking about wireshark. Rather, start with what is fundamentally a network question (how do I get a system capable of capturing packets in a position in the network where it can receive all the packets that I want to capture).</p><p>There are many solutions for that task depending on the network. As mentioned if you have a Wifi router that supports native packet captures, that's one way. Another is "SPAN" ports, or "port mirroring", where a switch will forward all the packets it sees from one or more ports and forward them on to another port (as a "mirror" port) so that a system running Wireshark can capture the packets and analyze them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '15, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-42291" class="comments-container"></div><div id="comment-tools-42291" class="comment-tools"></div><div class="clear"></div><div id="comment-42291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

