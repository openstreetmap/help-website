+++
type = "question"
title = "Capture filter which is similar to cflow.templateid display filter"
description = '''I want to use capture filter to get all the cflow (Netflow) templates that are being sent by a router. I can use &quot;host 1.2.3.4&quot; as capture filter to filter out other IPs, but how to use cflow.templateid in capture filter section..  Basically router would be sending millions of flows on some UDP port...'''
date = "2016-05-22T22:05:00Z"
lastmod = "2016-05-23T00:57:00Z"
weight = 52826
keywords = [ "capture", "netflow", "capture-filter", "cflow", "templateid" ]
aliases = [ "/questions/52826" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter which is similar to cflow.templateid display filter](/questions/52826/capture-filter-which-is-similar-to-cflowtemplateid-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52826-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use capture filter to get all the cflow (Netflow) templates that are being sent by a router.</p><p>I can use "host 1.2.3.4" as capture filter to filter out other IPs, but how to use cflow.templateid in capture filter section..</p><p>Basically router would be sending millions of flows on some UDP port 9995 and I want to run it for atleast a day. Wireahrk would hang if I only use "host" filter since the captured data is too huge.</p></div><div id="question-tags" class="tags-container tags">capture netflow capture-filter cflow templateid</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '16, 22:05</strong></p><img src="https://secure.gravatar.com/avatar/468b29ae5f6ed3bf7aef23922429f06b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Satya_Mokalla&#39;s gravatar image" /><p>Satya_Mokalla<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Satya_Mokalla has no accepted answers">0%</span></p></div></div><div id="comments-container-52826" class="comments-container"></div><div id="comment-tools-52826" class="comment-tools"></div><div class="clear"></div><div id="comment-52826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52827"></span>

<div id="answer-container-52827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52827-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Display filter allows more detailed filtering than capture filter because it uses the results of packet dissection. Packet dissection consumes memory to maintain state information about the packet flows. Therefore, the best way to capture high volumes of traffic is to use dumpcap and post-process its output files which can be done multiple times. More details can be found <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/comment-page-1/#HowTo:%20dumpcap">here</a>.</p><p>If you can identify some byte patterns at fixed positions in the cflow payload and the cflow PDUs always fit into a single packet, you may be able to look for these patterns using a capture filter. To find the syntax necessary for an advanced case like yours, where you need to look into tcp payload which may be located at different offsets depending on the presence of tcp options, search for "Capture HTTP GET requests" at <a href="https://wiki.wireshark.org/CaptureFilters">this page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '16, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52827" class="comments-container"></div><div id="comment-tools-52827" class="comment-tools"></div><div class="clear"></div><div id="comment-52827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

