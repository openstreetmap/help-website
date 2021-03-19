+++
type = "question"
title = "Can wireshark sniff a certain port/can wireshark apply filters like WPE pro?"
description = '''Im wanting to edit sent packets so say if the default is &quot;11 22 33 44 55 66&quot; i want it to send &quot;11 22 33 33 55 66&quot;. Can this be done in wireshark? Also i cant attach anything to the actual process but i know the port it connects through so can i sniff just that port? Or maybe if i can just sniff eve...'''
date = "2011-07-11T09:11:00Z"
lastmod = "2011-07-11T19:41:00Z"
weight = 4983
keywords = [ "sniffing", "filtering" ]
aliases = [ "/questions/4983" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can wireshark sniff a certain port/can wireshark apply filters like WPE pro?](/questions/4983/can-wireshark-sniff-a-certain-portcan-wireshark-apply-filters-like-wpe-pro)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4983-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im wanting to edit sent packets so say if the default is "11 22 33 44 55 66" i want it to send "11 22 33 33 55 66". Can this be done in wireshark? Also i cant attach anything to the actual process but i know the port it connects through so can i sniff just that port? Or maybe if i can just sniff every single packet sent/received that would work too.</p></div><div id="question-tags" class="tags-container tags">sniffing filtering</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '11, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/5d2baf14814996d351e59f36751be699?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iamabot&#39;s gravatar image" /><p>iamabot<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iamabot has no accepted answers">0%</span></p></div></div><div id="comments-container-4983" class="comments-container"></div><div id="comment-tools-4983" class="comment-tools"></div><div class="clear"></div><div id="comment-4983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4988"></span>

<div id="answer-container-4988" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4988-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Q&amp;A sites work best if you ask one question at a time, so each question has its own separate set of answers, and people looking for the answers to particular questions can more easily find them.</p><p>I'll answer the first question here. The answer is "no" - Wireshark currently neither supports editing packets nor re-transmitting the edited packets. <a href="http://wiki.wireshark.org/Tools">The Tools page of the Wireshark wiki</a> has links to a number of traffic generator tools under "Traffic generators", for example <a href="http://bittwist.sourceforge.net/">Bit-Twist</a> and <a href="http://www.secdev.org/projects/scapy/">Scapy</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '11, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4988" class="comments-container"></div><div id="comment-tools-4988" class="comment-tools"></div><div class="clear"></div><div id="comment-4988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4989"></span>

<div id="answer-container-4989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4989-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As for the second question (which is unrelated to the first, so, again, it should have been asked separately):</p><p>If by "the port it connects through" you mean a TCP or UDP port, and by "apply filters like WPE pro" and "can I sniff just that port" you mean you only want to capture traffic going to or coming from that port, you can use a capture filter such as "udp port XXX" or "tcp port XXX" (or "port XXX", which will capture traffic to or from that TCP port <em>or</em> that UDP port).</p><p>(Note that if you have VLANs on the network on which you're capturing, and the traffic is going over the VLAN, you might have to capture on the "VLAN interface" for that network rather than on the raw interface, or capture with a filter such as "udp port XXX or (vlan and udp port XXX)". Don't worry about that unless you don't see the traffic.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '11, 19:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4989" class="comments-container"></div><div id="comment-tools-4989" class="comment-tools"></div><div class="clear"></div><div id="comment-4989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

