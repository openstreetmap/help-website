+++
type = "question"
title = "What is IPv4 packet with &quot;IPv6 Hop-by-Hop Option&quot;?"
description = '''Hi, I have a PCAP-file which contains multiple frames with Ip4 Header with as info &quot;IPv6 Hop-by-Hop Option&quot; (see screenshot below) My question is:  What kind of packets are this? In what situations you will see them in traffic? How can I filter on these Hop-by-Hop packets? (e.g. as display filter in...'''
date = "2016-02-03T05:45:00Z"
lastmod = "2016-02-03T05:53:00Z"
weight = 49766
keywords = [ "ipv6", "wireshark" ]
aliases = [ "/questions/49766" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is IPv4 packet with "IPv6 Hop-by-Hop Option"?](/questions/49766/what-is-ipv4-packet-with-ipv6-hop-by-hop-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49766-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a PCAP-file which contains multiple frames with <strong>Ip4</strong> Header with as info "IPv6 Hop-by-Hop Option" (see screenshot below)</p><p>My question is:</p><ul><li>What kind of packets are this?</li><li>In what situations you will see them in traffic?</li><li>How can I filter on these Hop-by-Hop packets? (e.g. as display filter in Wireshark, or via code in via libpcap). As far as I can see source/dest are 0.0.0.0. Is this always the case for this class of packets?</li></ul><p>Thanks</p><p><img src="https://osqa-ask.wireshark.org/upfiles/hophop.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ipv6 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '16, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/b29ba250b3689fdd86050f2671a828d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jos&#39;s gravatar image" /><p>Jos<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jos has no accepted answers">0%</span></p></img></div></div><div id="comments-container-49766" class="comments-container"></div><div id="comment-tools-49766" class="comment-tools"></div><div class="clear"></div><div id="comment-49766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49768"></span>

<div id="answer-container-49768" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49768-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That packet looks bogus all the way - It has source and destination IP zero, which is impossible on a live network, so it looks like someone messed with (=edited) the packet.</p><p>IPv6 Hop-by-Hop isn't relevant to IPv4 packets, either.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '16, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Feb '16, 05:54</p></div></div><div id="comments-container-49768" class="comments-container"><span id="49784"></span><div id="comment-49784" class="comment"><div id="post-49784-score" class="comment-score"></div><div class="comment-text"><p>Or a device 'lost its marbles' and produced this frame on its network interface...</p></div><div id="comment-49784-info" class="comment-info"><span class="comment-age">(03 Feb '16, 08:37)</span> Jaap ♦</div></div></div><div id="comment-tools-49768" class="comment-tools"></div><div class="clear"></div><div id="comment-49768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="49769"></span>

<div id="answer-container-49769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49769-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"IPv6 Hop-by-Hop" is the protocol that's defined by <a href="http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">IANA</a> for IP protocol number 0.</p><p>To filter, use a display filter of <code>ip.proto == 0</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '16, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49769" class="comments-container"></div><div id="comment-tools-49769" class="comment-tools"></div><div class="clear"></div><div id="comment-49769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

