+++
type = "question"
title = "Wireshark logs only client and server info?"
description = '''Hello,  I just want to know if Wireshark only collects information of client and server right? in between client and server there are many network components/elements. do we see that information also? for e.g. in wireshark log I see server is sending slow data but is it possible some router(or any n...'''
date = "2012-11-08T10:36:00Z"
lastmod = "2012-11-08T12:05:00Z"
weight = 15738
keywords = [ "slow", "server" ]
aliases = [ "/questions/15738" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark logs only client and server info?](/questions/15738/wireshark-logs-only-client-and-server-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15738-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I just want to know if Wireshark only collects information of client and server right? in between client and server there are many network components/elements. do we see that information also? for e.g. in wireshark log I see server is sending slow data but is it possible some router(or any network element in between client and server)may be slow?</p><p>Thanks, Manju</p></div><div id="question-tags" class="tags-container tags">slow server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '12, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/7a16903da64cd8c74a6ca6a5e9c0a2ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manju007&#39;s gravatar image" /><p>Manju007<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manju007 has no accepted answers">0%</span></p></div></div><div id="comments-container-15738" class="comments-container"></div><div id="comment-tools-15738" class="comment-tools"></div><div class="clear"></div><div id="comment-15738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15739"></span>

<div id="answer-container-15739" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15739-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can show you whatever happens on the "network segment" you capture on.</p><p>What "network segment" entails is a varying matter. For instance if you capture on an endpoint with an uplink to a switch you'll see the host traffic (to/from), broadcast traffic, multicast traffic for groups the endpoint has joined (in case of a multicast aware switch) and link-local traffic like IPv6 NDP, spanning tree and maybe switch specific traffic. But if the capture is taken from a monitor port it may be vastly different. Either you see all ingress and egress traffic of a collection of ports, or from a vlan, either with or without tags. Doing a capture on a switch or router uplink may show even other traffic, like OSPF, IS-IS, RIP or whatever.</p><p>So, bottom line is it all depends on the point you capture at.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-15739" class="comments-container"></div><div id="comment-tools-15739" class="comment-tools"></div><div class="clear"></div><div id="comment-15739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

