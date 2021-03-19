+++
type = "question"
title = "Can GTP-U inner IP packets be fragmented?"
description = '''hi all,  My captured packet of GTP-U ,which makes up with inner ip ,inner udp and outer ip ,outer udp.As we know, the outer ip layer may be fragmented. My question : is the inner ip packet fragmented in some case ? thanks.'''
date = "2016-06-16T05:26:00Z"
lastmod = "2016-06-17T16:31:00Z"
weight = 53494
keywords = [ "ip", "fragmentation", "gtp-u" ]
aliases = [ "/questions/53494" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can GTP-U inner IP packets be fragmented?](/questions/53494/can-gtp-u-inner-ip-packets-be-fragmented)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53494-score" class="post-score" title="current number of votes">0</div><span id="post-53494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all, My captured packet of GTP-U ,which makes up with inner ip ,inner udp and outer ip ,outer udp.As we know, the outer ip layer may be fragmented. My question : is the inner ip packet fragmented in some case ?</p><p>thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-gtp-u" rel="tag" title="see questions tagged &#39;gtp-u&#39;">gtp-u</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '16, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/77193d74349d6e6d1f2c510a7d2c2667?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bigapple119&#39;s gravatar image" /><p><span>bigapple119</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bigapple119 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jun '16, 15:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-53494" class="comments-container"></div><div id="comment-tools-53494" class="comment-tools"></div><div class="clear"></div><div id="comment-53494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53495"></span>

<div id="answer-container-53495" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53495-score" class="post-score" title="current number of votes">1</div><span id="post-53495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As stated in 3GPP TS 29.281 version 13.1.0 Release 13</p><pre><code>4.2.4  Ingress GTP tunnel (GTPv1-U sending endpoint)
....
Fragmentation policy of the inner datagram is implementation dependent but shall interwork with IETF RFC 791 for inner IPv4 datagrams and IETF RFC 2460 for inner IPv6 packets.</code></pre><p>So I would assume the answer to be yes.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '16, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-53495" class="comments-container"><span id="53528"></span><div id="comment-53528" class="comment"><div id="post-53528-score" class="comment-score"></div><div class="comment-text"><p>Thanks firstly. I have seen the words in 3GPP TS 29.281 version 13.1.0 Release 13.Therefore,I have to consider the fragmented inner ip packet,when i dissect every layer of GTP-U.However,the inner-ip-packet's fragment flag are all not set, which GTP-U packets are displayed in wireshark.</p></div><div id="comment-53528-info" class="comment-info"><span class="comment-age">(17 Jun '16, 06:04)</span> <span class="comment-user userinfo">bigapple119</span></div></div></div><div id="comment-tools-53495" class="comment-tools"></div><div class="clear"></div><div id="comment-53495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53511"></span>

<div id="answer-container-53511" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53511-score" class="post-score" title="current number of votes">0</div><span id="post-53511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While possible, there are specific mechanisms in place to avoid it.</p><p>An inner IP MTU value is communicated down to the phone by the network which it is expected to honour, with the catch being that 3GPP accounts for tethered devices by imposing a requirement that the network needs to be able to support 1500 byte MTU for the "PDP PDU" if it becomes necessary (where, when transferred into GTP, fragmentation of the inner IP packet would then become necessary).</p><p>The wording of TS 23.060 is:</p><pre><code>When the MT and the TE are separated, e.g. a dongle based MS, it is not always possible to set the MTU value by
means of information provided by the network. The network shall have the capability of transferring N-PDUs
containing PDP PDUs, where the PDP PDUs are of 1500 octets, between the MS and GGSN/P-GW.</code></pre><p>There, "N-PDU" is a single GTP-transmitted packet between GTP tunnel endpoints, and "PDP PDU" is the end user's IP packet transmitted over the air.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '16, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-53511" class="comments-container"><span id="53529"></span><div id="comment-53529" class="comment"><div id="post-53529-score" class="comment-score"></div><div class="comment-text"><p>Yes,i found the words in the TS 23.060 of 2013.09. GTP-U is between nNodeB and S-GW,what you say below is equally applicable to 4G-LTE? Actually,i always think there are some mechanisms avoiding ip-fragment ,because Reassembling twice is inefficient. thanks a lot.</p></div><div id="comment-53529-info" class="comment-info"><span class="comment-age">(17 Jun '16, 06:18)</span> <span class="comment-user userinfo">bigapple119</span></div></div><span id="53547"></span><div id="comment-53547" class="comment"><div id="post-53547-score" class="comment-score"></div><div class="comment-text"><p>It's applicable to GTPv1-U in general, so yes.</p><p>At the control level from PGW down to the UE (whether for LTE, untrusted Wifi into the EPC, etc.), there is the concept of PCO options, where inner IP MTU can be communicated, but there are circumstances (such as dongles or tethering) where those mechanisms aren't fool-proof.</p></div><div id="comment-53547-info" class="comment-info"><span class="comment-age">(17 Jun '16, 16:31)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-53511" class="comment-tools"></div><div class="clear"></div><div id="comment-53511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

