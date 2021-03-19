+++
type = "question"
title = "What is normal ARP percentage in the Protocol Hierarchy Statistics?"
description = '''I have captured around 30,000 packets and am looking at the ARP statistics and noticed that the ARP traffic seems a little high. What percentage should it be? Thanks.'''
date = "2012-07-05T14:59:00Z"
lastmod = "2012-07-05T16:12:00Z"
weight = 12472
keywords = [ "arp", "statistics" ]
aliases = [ "/questions/12472" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is normal ARP percentage in the Protocol Hierarchy Statistics?](/questions/12472/what-is-normal-arp-percentage-in-the-protocol-hierarchy-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12472-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captured around 30,000 packets and am looking at the ARP statistics and noticed that the ARP traffic seems a little high. What percentage should it be?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">arp statistics</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '12, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/1359ef232b23c3991993217b7a7ccda7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gump3rs&#39;s gravatar image" /><p>Gump3rs<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gump3rs has no accepted answers">0%</span></p></div></div><div id="comments-container-12472" class="comments-container"><span id="12477"></span><div id="comment-12477" class="comment"><div id="post-12477-score" class="comment-score"></div><div class="comment-text"><p>what exactly is "a little high" and how many devices are there on the network?</p></div><div id="comment-12477-info" class="comment-info"><span class="comment-age">(06 Jul '12, 01:01)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12472" class="comment-tools"></div><div class="clear"></div><div id="comment-12472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12473"></span>

<div id="answer-container-12473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12473-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The answer is not as simple as "What percentage should it be?" For example, over a one-minute period, I captured 905 packets on my workstation, of which 681 were ARP requests. That's 75% of the total. However, my computer was idle at the time so during that time period, there were only 61 packets to/from my computer. There were 793 broadcasts of one sort or another, including the ARPs.</p><p>This is a switched network, so I see all the ARP requests, because they are broadcasts, but I don't see non-broadcast traffic to/from other systems, so I have no idea what percentage of total network traffic the ARPs constitute.</p><p>During another one-minute period when I was actively opening and refreshing web pages, I captured 4,510 packets, of which 716 were ARPs. Even though there were 5% more ARPs this time, because the link was much more active, they constituted only 16% of the total traffic.</p><p>So, rather than what percentage of total traffic the ARPs are, a better questions is: Is the absolute level of ARP traffic on your network so high that it's causing a problem? That's unlikely. ARP traffic is rarely so high that it causes network congestion. However, note that Wireshark does have the capability to detect ARP request storms, so you might want to make sure that's enabled and possibly tinker with the values. The default setting is to detect 30 or more ARP requests in 100 ms or less as an ARP request storm.</p><p>To get a feel for what constitutes the range of "normal" ARP levels, capture traffic in as many different locations/networks/times as you can. If performance on those networks is acceptable, then ARP levels are acceptable as well. If performance on those networks is not acceptable, something is wrong, although it is likely something other than excessive ARPs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '12, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jul '12, 18:40</p></div></div><div id="comments-container-12473" class="comments-container"></div><div id="comment-tools-12473" class="comment-tools"></div><div class="clear"></div><div id="comment-12473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

