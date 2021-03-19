+++
type = "question"
title = "Changing peer IP in pcap using tcprewrite"
description = '''I&#x27;m new to networking, so sorry in advance if my question is unclear. I have auto generated pcaps, each with one TCP flow which I would like to transmit using a traffic generator. The problem is that on those pcaps both the peers have the same IP, which is something the traffic generator does not li...'''
date = "2017-06-11T07:04:00Z"
lastmod = "2017-06-11T07:04:00Z"
weight = 61931
keywords = [ "tcprewrite", "pcap" ]
aliases = [ "/questions/61931" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Changing peer IP in pcap using tcprewrite](/questions/61931/changing-peer-ip-in-pcap-using-tcprewrite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61931-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to networking, so sorry in advance if my question is unclear. I have auto generated pcaps, each with one TCP flow which I would like to transmit using a traffic generator. The problem is that on those pcaps both the peers have the same IP, which is something the traffic generator does not like.</p><p>So, I tried to change the IPs using tcprewrite --endpoints. It worked for some pcaps. For others I got a strange behavior where the sender is always IP1 and the receiver is always IP2, (i.e the traffic always goes from IP1 to IP2, instead of being bidirectional). For example:</p><p><code> 21:41:48.477466 IP 127.17.242.242.5901 &gt; localhost.55617: Flags [P.], seq 2055024698:2055024710, ack ... 21:41:48.477907 IP 127.17.242.242.55617 &gt; localhost.5901: Flags [P.], seq 920220669:920220681, ack ... 21:41:48.478148 IP 127.17.242.242.5901 &gt; localhost.55617: Flags [P.], seq 12:14, ack 13, ... 21:41:48.478213 IP 127.17.242.242.55617 &gt; localhost.5901: Flags [P.], seq 12:13, ack 3, ... 21:41:48.478495 IP 127.17.242.242.5901 &gt; localhost.55617: Flags [P.], seq 14:30, ack 14, ... 21:41:51.383253 IP 127.17.242.242.55617 &gt; localhost.5901: Flags [P.], seq 13:29, ack 19, ... 21:41:51.383418 IP 127.17.242.242.5901 &gt; localhost.55617: Flags [P.], seq 30:34, ack 30, ... 21:41:51.383657 IP 127.17.242.242.55617 &gt; localhost.5901: Flags [P.], seq 29:30, ack 23, ...</code></p><p>Also now I have 2 flows, since the IPs got scrambles in relation to the ports (the ports stayed the same as they were).</p><p>Any idea what might cause this problem? Or is there a way to achieve what I want without tcprewrite?</p><p>Thanks Alot</p></div><div id="question-tags" class="tags-container tags">tcprewrite pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '17, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/335d2cac0871130fe7a369f697642591?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eladw&#39;s gravatar image" /><p>eladw<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eladw has no accepted answers">0%</span></p></div></div><div id="comments-container-61931" class="comments-container"></div><div id="comment-tools-61931" class="comment-tools"></div><div class="clear"></div><div id="comment-61931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

