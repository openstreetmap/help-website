+++
type = "question"
title = "tethereal shows one way traffic"
description = '''Hi, We are having issue while analyzing SIP traffic on centos. Centos server is getting SIP traffic coming via a Switch/Mirror port. I can see both way traffic when i use following command tethereal -i eth0 But i am unable to see incoming traffic when i use following command  ethereal -i eth0 port 5...'''
date = "2015-02-20T04:13:00Z"
lastmod = "2015-02-20T06:51:00Z"
weight = 39969
keywords = [ "sipcapture", "port" ]
aliases = [ "/questions/39969" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tethereal shows one way traffic](/questions/39969/tethereal-shows-one-way-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39969-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are having issue while analyzing SIP traffic on centos. Centos server is getting SIP traffic coming via a Switch/Mirror port.</p><p>I can see both way traffic when i use following command tethereal -i eth0</p><p>But i am unable to see incoming traffic when i use following command ethereal -i eth0 port 5060</p><p>This seems to happen just for SIP, because when i checked port 161 using below command. I can see both ways traffic tetheral -i eth0 port 161</p><p>Regards Farhan</p></div><div id="question-tags" class="tags-container tags">sipcapture port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '15, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/851bf2887fbd8cd5e5d5c3717ae6f5bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="farhan_ft&#39;s gravatar image" /><p>farhan_ft<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="farhan_ft has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '15, 19:02</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-39969" class="comments-container"><span id="39970"></span><div id="comment-39970" class="comment"><div id="post-39970-score" class="comment-score"></div><div class="comment-text"><p>and when i saved the output using -w option.</p><p>tethereal -i eth0 -w /tmp/trace.pcap</p><p>i can see incoming packets on port 5060...</p></div><div id="comment-39970-info" class="comment-info"><span class="comment-age">(20 Feb '15, 04:17)</span> farhan_ft</div></div><span id="39971"></span><div id="comment-39971" class="comment"><div id="post-39971-score" class="comment-score"></div><div class="comment-text"><p>This is the Ask Wireshark website, Ethereal is obsolete and no longer supported.</p><p>What is your OS version?</p></div><div id="comment-39971-info" class="comment-info"><span class="comment-age">(20 Feb '15, 04:44)</span> grahamb ♦</div></div><span id="39972"></span><div id="comment-39972" class="comment"><div id="post-39972-score" class="comment-score"></div><div class="comment-text"><p>You will be getting a lot of complaints about (t)ethereal being ancient. Never mind that, lets see if we can solve your problem.</p></div><div id="comment-39972-info" class="comment-info"><span class="comment-age">(20 Feb '15, 04:46)</span> Jaap ♦</div></div><span id="39973"></span><div id="comment-39973" class="comment"><div id="post-39973-score" class="comment-score"></div><div class="comment-text"><p>Are there VLANs involved when you capture SIP traffic?</p></div><div id="comment-39973-info" class="comment-info"><span class="comment-age">(20 Feb '15, 04:47)</span> Jaap ♦</div></div><span id="39975"></span><div id="comment-39975" class="comment"><div id="post-39975-score" class="comment-score"></div><div class="comment-text"><p>As i said i can see the traffic when i i saved the output using -w option. tethereal -i eth0 -w /tmp/trace.pcap</p><p>i can see incoming packets on port 5060... but when i use with PORT 5060. I can see only one way traffic. tethereal -i eth0.</p><p>centos1 2.6.32-220.el6.x86_64 #1 SMP Tue Dec 6 19:48:22 GMT 2011 x86_64 x86_64 x86_64 GNU/Linux</p></div><div id="comment-39975-info" class="comment-info"><span class="comment-age">(20 Feb '15, 04:57)</span> farhan_ft</div></div><span id="39976"></span><div id="comment-39976" class="comment not_top_scorer"><div id="post-39976-score" class="comment-score"></div><div class="comment-text"><p>When i have opened the Captured trace using command "tethereal -i eth0 -w /tmp/trace.pcap" and selected the incoming packet i can see "protocols in frame eth:ethertype:vlan:ethertype:ip:udp:sip:sdp"</p></div><div id="comment-39976-info" class="comment-info"><span class="comment-age">(20 Feb '15, 06:11)</span> farhan_ft</div></div><span id="39977"></span><div id="comment-39977" class="comment not_top_scorer"><div id="post-39977-score" class="comment-score"></div><div class="comment-text"><p>@farhan_ft</p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-39977-info" class="comment-info"><span class="comment-age">(20 Feb '15, 06:24)</span> grahamb ♦</div></div></div><div id="comment-tools-39969" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-39969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39978"></span>

<div id="answer-container-39978" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39978-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like the often overlooked issue with VLAN tags. If present the capture filter has to be made aware of it, so that it can (and will) adjust the offset for subsequent field comparisons in the packet.</p><p>This expression could help you then:</p><pre><code>&quot;udp port 5060 or (vlan and udp port 5060)&quot;</code></pre>This means:<ol><li>Filter on UDP port 5060 (catches untagged frames)</li><li>If present skip over the VLAN tag, or stop if not present</li><li>Again filter on UDP port 5060 (in the tagged frame)</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '15, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39978" class="comments-container"></div><div id="comment-tools-39978" class="comment-tools"></div><div class="clear"></div><div id="comment-39978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

