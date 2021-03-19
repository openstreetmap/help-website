+++
type = "question"
title = "Traps to other destination is captured in my host NIC while running wireshark"
description = '''Hi, I am running wireshark in my host say with IP address A.I am having another host in my LAN say with IP address B. Let say a Router R sends SNMP traps to the host B . The wireshark running in my host A,is able to capture the SNMP trap packet.How does this happens? Thx'''
date = "2011-06-23T22:19:00Z"
lastmod = "2011-06-24T00:15:00Z"
weight = 4715
keywords = [ "udp", "snmp" ]
aliases = [ "/questions/4715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Traps to other destination is captured in my host NIC while running wireshark](/questions/4715/traps-to-other-destination-is-captured-in-my-host-nic-while-running-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am running wireshark in my host say with IP address A.I am having another host in my LAN say with IP address B. Let say a Router R sends SNMP traps to the host B . The wireshark running in my host A,is able to capture the SNMP trap packet.How does this happens?</p><p>Thx</p></div><div id="question-tags" class="tags-container tags">udp snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '11, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/4cb539d0c8fd224a57c132e1bbb8b730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JavaUser&#39;s gravatar image" /><p>JavaUser<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JavaUser has no accepted answers">0%</span></p></div></div><div id="comments-container-4715" class="comments-container"></div><div id="comment-tools-4715" class="comment-tools"></div><div class="clear"></div><div id="comment-4715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4716"></span>

<div id="answer-container-4716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4716-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are several options .Assuming that</p><ol><li>you capture in promiscuous mode</li><li>you're on a switched network with host B</li></ol><p>Then the router</p><ol><li>Might broadcast it</li><li>Might multicast it, for which the switch hasn't pruned your link</li><li>Might unicast it, for which the switch doesn't have a target port in its switching table</li></ol><p>So, have a good look at the traffic and see what applies.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4716" class="comments-container"></div><div id="comment-tools-4716" class="comment-tools"></div><div class="clear"></div><div id="comment-4716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

