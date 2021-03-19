+++
type = "question"
title = "validate capture (can&#x27;t see all traffic)"
description = '''Hi, Goal : monitor bandwith of 15 computers. Box --&amp;gt; router (WAN+me) --&amp;gt; Switch1(7) --&amp;gt; Switch2(7) When i use statistic i can see my traffic(source+dest) but not from other people. Correctly set up the capture in promiscuous mode. Thanks for you help.'''
date = "2014-04-27T01:53:00Z"
lastmod = "2014-04-27T09:22:00Z"
weight = 32213
keywords = [ "router", "switch", "traffic", "bandwith" ]
aliases = [ "/questions/32213" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [validate capture (can't see all traffic)](/questions/32213/validate-capture-cant-see-all-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32213-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Goal : monitor bandwith of 15 computers. Box --&gt; router (WAN+me) --&gt; Switch1(7) --&gt; Switch2(7)</p><p>When i use statistic i can see my traffic(source+dest) but not from other people. Correctly set up the capture in promiscuous mode.</p><p>Thanks for you help.</p></div><div id="question-tags" class="tags-container tags">router switch traffic bandwith</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '14, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/396e506c6174e75bd34e08a21d243e3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lebonvoin&#39;s gravatar image" /><p>lebonvoin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lebonvoin has no accepted answers">0%</span></p></div></div><div id="comments-container-32213" class="comments-container"></div><div id="comment-tools-32213" class="comment-tools"></div><div class="clear"></div><div id="comment-32213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32217"></span>

<div id="answer-container-32217" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32217-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you can see your traffic but not others, my first thought is that the method you're using to capture the traffic isn't correct.</p><p>From your diagram, if I am correct that the "Box" is the system running Wireshark and it is connected directly to the router's WAN port, then it will not receive any local LAN traffic between the 15 hosts. Only traffic destined for IP network(s) for which the router would send out the WAN port will be received by the "Box" in that diagram. To be clear, what do you mean by "WAN + me"? Are you mirroring off of the router to a separate physical machine from "Box"? How is this being done?</p><p>A few things to consider here:</p><ul><li>Traffic between machines served by Switch2 on the same vlan will never leave Switch2 toward Switch1.</li><li>Traffic between machines served by Switch1 on the same vlan will never leave Switch1 toward the router or Switch2</li><li>Traffic between machines served across Switch1 and Switch2 on the same vlan will never reach the router.</li><li>Even for traffic which reaches the router, unless the destination IP network is outside of your LAN(s) from an IP routing perspective, it will never be sent across the WAN port to the "Box".</li></ul><p>In the setup you describe, the "Box" will see IP traffic routed to or from it by the 15 machines but it will not see any LAN traffic at all.</p><p>To be clear on the objective here, is the goal to measure all bandwidth leaving the WAN port specifically? If so, the traffic that you say you observe is exactly what I would expect to see - (all traffic to and from "Box" should be present in a packet capture performed on "Box" to and from the local LANs). Is the goal to see all traffic from all machines, period? If so, I'd suggest "SPAN" or "Port Mirroring" on the switches if they support it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '14, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Apr '14, 09:30</p></div></div><div id="comments-container-32217" class="comments-container"><span id="32337"></span><div id="comment-32337" class="comment"><div id="post-32337-score" class="comment-score"></div><div class="comment-text"><p>Thanks, i put a 48p switch and i see everything.</p><p>Regards.</p></div><div id="comment-32337-info" class="comment-info"><span class="comment-age">(01 May '14, 04:04)</span> lebonvoin</div></div></div><div id="comment-tools-32217" class="comment-tools"></div><div class="clear"></div><div id="comment-32217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

