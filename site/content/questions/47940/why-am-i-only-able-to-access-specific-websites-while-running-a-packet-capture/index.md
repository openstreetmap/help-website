+++
type = "question"
title = "Why am i only able to access specific websites while running a packet capture?"
description = '''I am unable to access specific websites like outlook.office365.com (time_out err) except when I am running a packet capture in wireshark2.0. Why? To safe time yes AV scans and malware scans have been ran with no success. What makes running a packet capture makes this work?'''
date = "2015-11-24T13:14:00Z"
lastmod = "2015-11-24T16:49:00Z"
weight = 47940
keywords = [ "how", "why", "internet" ]
aliases = [ "/questions/47940" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why am i only able to access specific websites while running a packet capture?](/questions/47940/why-am-i-only-able-to-access-specific-websites-while-running-a-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47940-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to access specific websites like outlook.office365.com (time_out err) except when I am running a packet capture in wireshark2.0. Why? To safe time yes AV scans and malware scans have been ran with no success.</p><p>What makes running a packet capture makes this work?</p></div><div id="question-tags" class="tags-container tags">how why internet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '15, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/42999987157485482480cc09f3f40f8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chicknbroth&#39;s gravatar image" /><p>chicknbroth<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chicknbroth has no accepted answers">0%</span></p></div></div><div id="comments-container-47940" class="comments-container"></div><div id="comment-tools-47940" class="comment-tools"></div><div class="clear"></div><div id="comment-47940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47945"></span>

<div id="answer-container-47945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47945-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What makes running a packet capture makes this work?</p></blockquote><p>Running Wireshark will change two things</p><ul><li><p>The interface will be switched into <strong><a href="https://en.wikipedia.org/wiki/Promiscuous_mode">promiscuous mode</a></strong> (listening to MAC addresses other than the hardcoded address of the NIC)<br />
</p></li><li><p>WinPcap (the capturing library on Windows - I assume you are running Windows) will inject itself into the network stack to be able to capture network frames</p></li></ul><p>So, one of these two modifications makes your website access work.</p><ul><li><p>If it works because of <strong><a href="https://en.wikipedia.org/wiki/Promiscuous_mode">promiscuous mode</a></strong> it could mean, that the reply packets from your internet router will be sent to another machine on the network (another MAC address). This could be caused by a duplicate IP address on the network. Windows should tell you if there is a duplicate IP. Did see those messages?</p></li><li><p>If it works because WinPcap injects itself into the network stack, then it's probably because of some security software (Endpoint security, AV, IPS, VPN client, etc.). Please <strong>disable</strong> any security software on that system, and repeat the test. We have had numerous similar reports.</p></li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '15, 16:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47945" class="comments-container"></div><div id="comment-tools-47945" class="comment-tools"></div><div class="clear"></div><div id="comment-47945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

