+++
type = "question"
title = "Conditional TCP reassembly based on DSCP bits"
description = '''I am looking into writing a Wireshark plugin to handle the Layer 3 DSR (Direct Server Return) scheme we are using. Currently traffic cannot be reassembled due to the load balancing scheme we are using. What happens is that based on various DSCP bits, an incoming packet will get its destination addre...'''
date = "2010-09-27T18:48:00Z"
lastmod = "2010-10-07T08:33:00Z"
weight = 344
keywords = [ "reassembly", "tcp", "dscp" ]
aliases = [ "/questions/344" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Conditional TCP reassembly based on DSCP bits](/questions/344/conditional-tcp-reassembly-based-on-dscp-bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-344-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking into writing a Wireshark plugin to handle the Layer 3 DSR (Direct Server Return) scheme we are using. Currently traffic cannot be reassembled due to the load balancing scheme we are using.</p><p>What happens is that based on various DSCP bits, an incoming packet will get its destination address rewritten (via iptables) to match that of the load balancer. This combined with an alias on the loopback interface allows a host behind the load balancer to accept traffic coming from the load balancer, and the reply packet goes directly to the client.</p><p>My question is whether this can even be done in a plugin. I suspect that I may have to modify the packet reassembly code to support to a DSCP-bit-&gt;IP lookup table to perform the same address rewrite done on the servers so that the streams can be properly reassembled.</p><p>Thanks,</p><p>Peter</p></div><div id="question-tags" class="tags-container tags">reassembly tcp dscp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '10, 18:48</strong></p><img src="https://secure.gravatar.com/avatar/e61a616a18096689fe022aad5af04e63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pafriend&#39;s gravatar image" /><p>pafriend<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pafriend has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Sep '10, 18:49</p></div></div><div id="comments-container-344" class="comments-container"></div><div id="comment-tools-344" class="comment-tools"></div><div class="clear"></div><div id="comment-344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="457"></span>

<div id="answer-container-457" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-457-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I used the wrong terminology. My problem is not with reassembly, but with building the conversation. After spending some time looking at the code, it looks like it is technically possible to modify find_conversation() to support a conditionally rewritten address, but it appears such a change would cause numerous problems in other parts of the code like SSL decryption. I took the easy way out of whipped up a tool with libpcap to take an existing trace file and perform the same mangle operations done by iptables on the server. This new trace file can then be handled as usual by Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '10, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/e61a616a18096689fe022aad5af04e63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pafriend&#39;s gravatar image" /><p>pafriend<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pafriend has no accepted answers">0%</span></p></div></div><div id="comments-container-457" class="comments-container"></div><div id="comment-tools-457" class="comment-tools"></div><div class="clear"></div><div id="comment-457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

