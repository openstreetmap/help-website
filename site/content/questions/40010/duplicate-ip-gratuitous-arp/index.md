+++
type = "question"
title = "Duplicate Ip - Gratuitous ARP"
description = '''I am using six cisco network switches in my network. While analyzing network traffic using Wireshark, i found errors like Ip Duplication- Gratuitous ARP. So can anyone tell me how these errors are effecting in behavior of my network using IO graph and TCP stream graph, as i am new to wireshark. I am...'''
date = "2015-02-21T16:18:00Z"
lastmod = "2015-02-23T05:38:00Z"
weight = 40010
keywords = [ "ip", "conflict" ]
aliases = [ "/questions/40010" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate Ip - Gratuitous ARP](/questions/40010/duplicate-ip-gratuitous-arp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40010-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using six cisco network switches in my network. While analyzing network traffic using Wireshark, i found errors like Ip Duplication- Gratuitous ARP. So can anyone tell me how these errors are effecting in behavior of my network using IO graph and TCP stream graph, as i am new to wireshark. I am attaching the capture file. <a href="https://drive.google.com/file/d/0B8asXfpLSWu5YWh5OUtSN0t5eGM/view?usp=sharing">https://drive.google.com/file/d/0B8asXfpLSWu5YWh5OUtSN0t5eGM/view?usp=sharing</a><br />
</p></div><div id="question-tags" class="tags-container tags">ip conflict</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '15, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/26db4cdccaf9209d05b0c74fff16b967?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mohdaftab93&#39;s gravatar image" /><p>mohdaftab93<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mohdaftab93 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-40010" class="comments-container"></div><div id="comment-tools-40010" class="comment-tools"></div><div class="clear"></div><div id="comment-40010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40022"></span>

<div id="answer-container-40022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40022-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>These Gratuitous ARPs are a sign for an IP address "collision", meaning use of the IP address 192.168.1.254 on the devices answering with Gratuitous ARPs to a dedicated MAC (not the broadcast address).</p><p>That's most certainly because your are using Cisco Small Business Switches (SG300) and they all have 192.168.1.254 as the default management IP address.</p><p>So, to answer your question: No, those ARP messages won't interfere with your network! However you should assign every switch its own address, if you want to manage them and/or if you want to get rid of those ARPs.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '15, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40022" class="comments-container"></div><div id="comment-tools-40022" class="comment-tools"></div><div class="clear"></div><div id="comment-40022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

