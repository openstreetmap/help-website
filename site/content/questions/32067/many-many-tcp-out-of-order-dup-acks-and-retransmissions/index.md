+++
type = "question"
title = "Many many TCP &quot;out-of-order&quot; &quot;dup acks&quot; and &quot;retransmissions&quot;"
description = '''I have an issue where I have VMware hosts that are connected to 2 switches (not connected to each other at this point) that are connected to a Fortigate firewall w/ a software switch. The software switch has VLAN interfaces that serve as the default gateway for the associated networks. For traffic b...'''
date = "2014-04-22T12:22:00Z"
lastmod = "2014-10-21T01:21:00Z"
weight = 32067
keywords = [ "dup-ack", "out-of-order", "retransmissions" ]
aliases = [ "/questions/32067" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Many many TCP "out-of-order" "dup acks" and "retransmissions"](/questions/32067/many-many-tcp-out-of-order-dup-acks-and-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32067-score" class="post-score" title="current number of votes">0</div><span id="post-32067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an issue where I have VMware hosts that are connected to 2 switches (not connected to each other at this point) that are connected to a Fortigate firewall w/ a software switch. The software switch has VLAN interfaces that serve as the default gateway for the associated networks.</p><p>For traffic between the networks I am seeing many, many TCP errors of out-of-order, dup ack and retransmissions.</p><p>Example:</p><p>VM1 sends an LDAP syn to VM2. I immediately get three out-of-order errors, then a syn, ack from VM2 to VM1, followed by three more out-of-order errors. This also occurs with the errors being retransmissions and dup acks.</p><p>Thoughts?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-out-of-order" rel="tag" title="see questions tagged &#39;out-of-order&#39;">out-of-order</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '14, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/c335b5652398b9c3ab78b52e510412b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim5700&#39;s gravatar image" /><p><span>tim5700</span><br />
<span class="score" title="2 reputation points">2</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim5700 has no accepted answers">0%</span></p></div></div><div id="comments-container-32067" class="comments-container"></div><div id="comment-tools-32067" class="comment-tools"></div><div class="clear"></div><div id="comment-32067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32119"></span>

<div id="answer-container-32119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32119-score" class="post-score" title="current number of votes">0</div><span id="post-32119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Thoughts?</p></blockquote><p>Sounds like you are capturing the frames twice, which confuses Wireshark. Please add more details about your setup and where you actually captured the frames.</p><p>BTW: What kind of 'software switch' are you using? Is this a VMware vSwitch or something different?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32119" class="comments-container"><span id="32120"></span><div id="comment-32120" class="comment"><div id="post-32120-score" class="comment-score"></div><div class="comment-text"><p>My servers at this location are all VMware guests. My VMware hosts are connected to 1 Cisco 3750-x stack w/ two members and a Cisco 3850 stack w/ two members.</p><p>The two Cisco stacks are not trunked to one another. There is a Fortigate 1500D that both stacks connect to. The Fortigate contains the software switch I am referring. Within the Fortigate, there are multiple VLAN interfaces with IP addresses. Then the Fortigate's internal routing takes care of inter-subnet connectivity.</p><p>The packet capture in question was taken directly from the Fortigate.</p></div><div id="comment-32120-info" class="comment-info"><span class="comment-age">(23 Apr '14, 12:14)</span> <span class="comment-user userinfo">tim5700</span></div></div><span id="32122"></span><div id="comment-32122" class="comment"><div id="post-32122-score" class="comment-score"></div><div class="comment-text"><p>Like this?</p><pre><code>VM -- Cisco -- [VLAN If] Fortinet [VLAN If] --- Cisco -- VM</code></pre><p>Furthermore:</p><blockquote><p>The packet capture in question was <strong>taken directly from the Fortigate</strong>.</p></blockquote><p>can you please capture within the VMs or even better on a mirror port of the switch and then compare the results?</p></div><div id="comment-32122-info" class="comment-info"><span class="comment-age">(23 Apr '14, 12:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32119" class="comment-tools"></div><div class="clear"></div><div id="comment-32119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32372"></span>

<div id="answer-container-32372" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32372-score" class="post-score" title="current number of votes">0</div><span id="post-32372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is resolved.</p><p>In my packet captures I was really focused in on LDAP queries as this was really, really hindering my AD traffic. So looking at the packet captures from the server I saw the following:</p><p>Server sends a SYN After 3 seconds the server sends another SYN After 3 seconds the server sends another SYN After 3 seconds the server sends another SYN THEN gets a SYN, ACK Then traffic flows</p><p>So and so forth.</p><p>The same pattern shows up capturing from the SPAN port on the firewall's connection. However, it DOES NOT show up in the Fortigate's capture at all.</p><p>Here's the fix. In Server 2012, MS has set ECN to be enabled by default. The Fortigate is blackholing the TCP SYN packets flagged with ECN. Eventually, Windows gives up and stops trying to use ECN.</p><p>Disable it with:</p><p>Netsh interface tcp set global ecncapability=disabled</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '14, 19:19</strong></p><img src="https://secure.gravatar.com/avatar/c335b5652398b9c3ab78b52e510412b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim5700&#39;s gravatar image" /><p><span>tim5700</span><br />
<span class="score" title="2 reputation points">2</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim5700 has no accepted answers">0%</span></p></div></div><div id="comments-container-32372" class="comments-container"><span id="37218"></span><div id="comment-37218" class="comment"><div id="post-37218-score" class="comment-score"></div><div class="comment-text"><p>tim5700,</p><p>can't appreciate your solution enough!</p><p>Thanks man</p><p><em>couldn't thumb up</em></p></div><div id="comment-37218-info" class="comment-info"><span class="comment-age">(21 Oct '14, 01:21)</span> <span class="comment-user userinfo">if0else0</span></div></div></div><div id="comment-tools-32372" class="comment-tools"></div><div class="clear"></div><div id="comment-32372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

