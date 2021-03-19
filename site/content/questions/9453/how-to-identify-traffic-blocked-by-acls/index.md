+++
type = "question"
title = "How to identify traffic blocked by ACLs"
description = '''Is there a method for determining if a particular entry(s) in a network trace are being blocked by ACLs? If so, can you help me identify where in the trace it would show the packet being rejected/blocked? For example, we&#x27;ve written ACLs to prevent traffic on certain ports directed toward a particula...'''
date = "2012-03-09T04:17:00Z"
lastmod = "2012-03-09T04:37:00Z"
weight = 9453
keywords = [ "attributes", "filtering", "traffic", "acl" ]
aliases = [ "/questions/9453" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to identify traffic blocked by ACLs](/questions/9453/how-to-identify-traffic-blocked-by-acls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9453-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a method for determining if a particular entry(s) in a network trace are being blocked by ACLs? If so, can you help me identify where in the trace it would show the packet being rejected/blocked?</p><p>For example, we've written ACLs to prevent traffic on certain ports directed toward a particular host. In the network trace I see the client and host entries on the defined ports. But i can't tell if they are being blocked. We do see the counters on our firewall going up, so that's a good inidcating our ACL is working. But was hoping wireshark would somehow confirm the traffic is being blocked. Please let me know if I can provide a better example or further information. Appreciate the help.</p></div><div id="question-tags" class="tags-container tags">attributes filtering traffic acl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '12, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/916ac7049f8367e878392386f009d278?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sdeb&#39;s gravatar image" /><p>sdeb<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sdeb has no accepted answers">0%</span></p></div></div><div id="comments-container-9453" class="comments-container"></div><div id="comment-tools-9453" class="comment-tools"></div><div class="clear"></div><div id="comment-9453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9454"></span>

<div id="answer-container-9454" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9454-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>&lt;trivial mode&gt;<br />
In order to know if something is blocked, you would need to make a trace on both sides of the blocking device and compare the packets<br />
&lt;/trivial mode&gt;</em></p><p>If you can only capture packets on one side of the connection, then you could deduct some information about the ACL's, but you are never sure. For instance, capturing on the client side of the filtering device could show you SYN packets being sent, but no SYN/ACK coming back. This could be due to the ACL, but also due to a routing problem, the server not being up, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '12, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '12, 04:38</p></div></div><div id="comments-container-9454" class="comments-container"></div><div id="comment-tools-9454" class="comment-tools"></div><div class="clear"></div><div id="comment-9454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

