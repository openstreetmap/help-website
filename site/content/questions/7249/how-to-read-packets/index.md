+++
type = "question"
title = "How to read packets"
description = '''Again, I&#x27;m a total beginner in terms of computer technology.. So could someone give me some sort of a guideline or reference as to how to read packets and what they mean, in &quot;laymen&quot; terms? Thanks again.'''
date = "2011-11-05T11:30:00Z"
lastmod = "2011-11-07T17:39:00Z"
weight = 7249
keywords = [ "packets", "understanding" ]
aliases = [ "/questions/7249" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to read packets](/questions/7249/how-to-read-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7249-score" class="post-score" title="current number of votes">0</div><span id="post-7249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Again, I'm a total beginner in terms of computer technology..</p><p>So could someone give me some sort of a guideline or reference as to how to read packets and what they mean, in "laymen" terms?</p><p>Thanks again.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-understanding" rel="tag" title="see questions tagged &#39;understanding&#39;">understanding</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '11, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/674b318e60e61196db578df465ca14a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Iapologize&#39;s gravatar image" /><p><span>Iapologize</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Iapologize has no accepted answers">0%</span></p></div></div><div id="comments-container-7249" class="comments-container"></div><div id="comment-tools-7249" class="comment-tools"></div><div class="clear"></div><div id="comment-7249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7267"></span>

<div id="answer-container-7267" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7267-score" class="post-score" title="current number of votes">0</div><span id="post-7267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would start <a href="http://en.wikipedia.org/wiki/Network_packet">here</a> and start clicking the links in the <em>Terminology</em> section to dig deeper. In particular, read about the <a href="http://en.wikipedia.org/wiki/OSI_model">OSI Model</a> if you want to know what the purpose of the different layers you might see when you take a look at packets using a capturing tool.</p><p>How to read packets varies greatly depending on what link type and protocol type you're using. For most people this probably means starting by interpreting the <a href="http://en.wikipedia.org/wiki/Ethernet_frame">Ethernet frame</a>.</p><p>If you look at an Ethernet frame in Wireshark, the first thing you'll see is the destination MAC address. This tells you which device the packet is destined for, or if it's a broadcast or multicast address (intended for multiple devices). The Ethertype field indicates which kind of protocol the device reading the packet should use to interpret the rest of the packet. The various kinds of protocols which might operate over Ethernet are defined by <a href="http://www.iana.org/assignments/ethernet-numbers">IANA</a>.</p><p>If a device on an Ethernet network reads a packet and determines the protocol is IPv4, it would then go on to interpret the <a href="http://en.wikipedia.org/wiki/IPv4#Header">IPv4 header</a> and determine what kind of IP packet is inside. (Some possibilities are <a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol">TCP</a>, <a href="http://en.wikipedia.org/wiki/User_Datagram_Protocol">UDP</a>, or <a href="http://en.wikipedia.org/wiki/Internet_Control_Message_Protocol">ICMP</a> - your web browser talks TCP, for example.)</p><p>Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '11, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/7cd2dfec42419c9791031b2e86ea9b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikeP&#39;s gravatar image" /><p><span>MikeP</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikeP has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Nov '11, 17:57</strong> </span></p></div></div><div id="comments-container-7267" class="comments-container"></div><div id="comment-tools-7267" class="comment-tools"></div><div class="clear"></div><div id="comment-7267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

