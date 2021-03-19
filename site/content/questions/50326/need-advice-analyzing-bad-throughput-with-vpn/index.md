+++
type = "question"
title = "Need advice analyzing bad throughput with vpn"
description = '''Hi, I&#x27;m trying SSL VPN and get really bad throughput (about 1-2 Mbit/s). Normal untunneled traffic reaches about 60-70 Mbit/s. Here is my pcap data: https://www.cloudshark.org/captures/8226ca16543d I am connecting from a client (192.168.1.15) to a server (192.168.1.10) through a gateway. I&#x27;m aware o...'''
date = "2016-02-19T01:13:00Z"
lastmod = "2016-02-19T01:13:00Z"
weight = 50326
keywords = [ "vpn", "throughput" ]
aliases = [ "/questions/50326" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need advice analyzing bad throughput with vpn](/questions/50326/need-advice-analyzing-bad-throughput-with-vpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying SSL VPN and get really bad throughput (about 1-2 Mbit/s). Normal untunneled traffic reaches about 60-70 Mbit/s. Here is my pcap data:</p><p><a href="https://www.cloudshark.org/captures/8226ca16543d">https://www.cloudshark.org/captures/8226ca16543d</a></p><p>I am connecting from a client (<code>192.168.1.15</code>) to a server (<code>192.168.1.10</code>) through a gateway. I'm aware of the general problems with SSL-VPN as compared to e.g. L2TP or PPTP (ie specifically, running TCP over TCP), but I hope someone can give some feedback on whether my pcap data contains anything obvious. I can see there are fast retransmissions but I'm not sure if they would contribute to the slow throughput as they are not that many. There are quite a few Dup ACK but same thing here - I don't know if these can explain the slow speed. What about MTU? But I don't know what should be the right value here.</p><p>Am I looking at the wrong things? What <em>should</em> I be looking at?</p><p>Any comments or ideas are greatly appreciated!</p></div><div id="question-tags" class="tags-container tags">vpn throughput</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '16, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/56e5e44d5dc2d9ad0bb4e0ced530c56b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cepheidlight&#39;s gravatar image" /><p>cepheidlight<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cepheidlight has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Feb '16, 01:16</p></div></div><div id="comments-container-50326" class="comments-container"></div><div id="comment-tools-50326" class="comment-tools"></div><div class="clear"></div><div id="comment-50326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

