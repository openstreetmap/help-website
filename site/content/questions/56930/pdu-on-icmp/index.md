+++
type = "question"
title = "PDU on ICMP?"
description = '''Hi guys My teacher asked us to analyse a computer&#x27;s network and answer a couple of questions. If we found ICMP v4 and v6 (which i was able to asnswer), what are the size of the ethernet frames (which i was also able to answer), which is the size of ICMP data (which i was also able to answer) so, you...'''
date = "2016-11-02T11:43:00Z"
lastmod = "2016-11-02T15:26:00Z"
weight = 56930
keywords = [ "icmpv6", "pdu", "icmp" ]
aliases = [ "/questions/56930" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PDU on ICMP?](/questions/56930/pdu-on-icmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56930-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys</p><p>My teacher asked us to analyse a computer's network and answer a couple of questions. If we found ICMP v4 and v6 (which i was able to asnswer), what are the size of the ethernet frames (which i was also able to answer), which is the size of ICMP data (which i was also able to answer) so, you see, that kind of thing about ICMP.</p><p>What i didn't get is that: he asked us to answer which PDU's ICMP have been captured? (???) (I've looked about 10 video lessons about ICMP on youtube and couldn't find anything about it!) And he also asks the difference between the size of the PDUs that have been captured. Well it would help if I only knew what are those pdus on icmps or anything of that sort.</p><p>I'm sorry I'm kind of stupid on the subject, but please do answer me, even if you are not really sure too, anything will help anything will do i'm just lost and any kind of help will be appreciated.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">icmpv6 pdu icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '16, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/53af4e00a1f565ee76ec5744b5e8dd86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbennett&#39;s gravatar image" /><p>pbennett<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbennett has no accepted answers">0%</span></p></div></div><div id="comments-container-56930" class="comments-container"><span id="56931"></span><div id="comment-56931" class="comment"><div id="post-56931-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us the trace? Here are some PDUs explained: <a href="https://crnetpackets.com/2016/01/27/the-relation-between-maximum-transmission-unit-mtu-and-the-maximum-segment-size-mss/">https://crnetpackets.com/2016/01/27/the-relation-between-maximum-transmission-unit-mtu-and-the-maximum-segment-size-mss/</a></p></div><div id="comment-56931-info" class="comment-info"><span class="comment-age">(02 Nov '16, 13:35)</span> Christian_R</div></div></div><div id="comment-tools-56930" class="comment-tools"></div><div class="clear"></div><div id="comment-56930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56933"></span>

<div id="answer-container-56933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56933-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>ICMP is a rudimentary messaging system, and is also used to test connectivity. Leaving aside connectivity testing, which is done with ping, many ICMP packets return the original packet--or the first few bytes of the original packet--that triggered the ICMP message.</p><p>So I'd suggest using Wireshark to see what's in the ICMP. Expand the Internet Control Message Protocol section in the Packet Details pane and see what's listed there.</p><p>I think what your teacher is asking is: "Was this ICMP generated in response to an IP packet, a TCP datagram, a UDP datagram, etc.?"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '16, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-56933" class="comments-container"></div><div id="comment-tools-56933" class="comment-tools"></div><div class="clear"></div><div id="comment-56933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

