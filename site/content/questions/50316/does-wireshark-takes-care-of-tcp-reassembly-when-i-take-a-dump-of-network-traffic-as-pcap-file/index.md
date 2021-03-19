+++
type = "question"
title = "Does Wireshark takes care of TCP reassembly when I take a dump of network traffic as .pcap file"
description = '''When I take a dump of network traffic and save in the .pcap file. I load that pcap file in the wireshark for analyzing and what I find is there is a re-transmission of the tcp packet in the wireshark.  Question: What my question is why the re-transmission is showing up in the wireshark. Didnt the TC...'''
date = "2016-02-18T15:22:00Z"
lastmod = "2016-02-18T15:24:00Z"
weight = 50316
keywords = [ "retransmission", "tcp" ]
aliases = [ "/questions/50316" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark takes care of TCP reassembly when I take a dump of network traffic as .pcap file](/questions/50316/does-wireshark-takes-care-of-tcp-reassembly-when-i-take-a-dump-of-network-traffic-as-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50316-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I take a dump of network traffic and save in the .pcap file. I load that pcap file in the wireshark for analyzing and what I find is there is a re-transmission of the tcp packet in the wireshark.</p><p>Question: What my question is why the re-transmission is showing up in the wireshark. Didnt the TCP took care of the re-transmission.</p></div><div id="question-tags" class="tags-container tags">retransmission tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '16, 15:22</strong></p><img src="https://secure.gravatar.com/avatar/d20d7102fd9001359c35732770f6f143?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fixmessenger&#39;s gravatar image" /><p>fixmessenger<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fixmessenger has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Feb '16, 02:35</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-50316" class="comments-container"></div><div id="comment-tools-50316" class="comment-tools"></div><div class="clear"></div><div id="comment-50316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50317"></span>

<div id="answer-container-50317" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50317-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that's why you see it. Wireshark shows what was recorded, and if there was packet loss TCP sent a retransmission that got recorded, too. Wireshark is not hiding anything.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '16, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-50317" class="comments-container"></div><div id="comment-tools-50317" class="comment-tools"></div><div class="clear"></div><div id="comment-50317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

