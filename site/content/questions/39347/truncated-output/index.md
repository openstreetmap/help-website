+++
type = "question"
title = "Truncated output"
description = '''When capturing DHCP packets there is a specific field we wish to capture. This is being cut off at 24 characters so we cannot completely verify that it is correct. If we select the option -T pdml then it outputs the entire value but changing to XML would require a large amount of rework in some code...'''
date = "2015-01-21T20:53:00Z"
lastmod = "2015-01-22T06:02:00Z"
weight = 39347
keywords = [ "dhcp", "centos" ]
aliases = [ "/questions/39347" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Truncated output](/questions/39347/truncated-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39347-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When capturing DHCP packets there is a specific field we wish to capture. This is being cut off at 24 characters so we cannot completely verify that it is correct. If we select the option -T pdml then it outputs the entire value but changing to XML would require a large amount of rework in some code we have. Is there a way to stop tshark truncating output? Notice the second last line in the capture below has ... on the end of it indicating the data has been truncated. We are using CentOS 6.2. This is just a basic TCP/IP capture, nothing fancy except that we are looking at DHCP traffic.</p><p>Our command line is this:</p><p><code>tshark -V -i vlan2090 -R "bootp.hw.mac_addr contains "00:17:33:00:00:00""</code></p><p>and output (which I've abbreviated) is like this:</p><p><code>Frame 77 (384 bytes on wire, 384 bytes captured)     Arrival Time: Dec  8, 2014 14:06:55.751253000 ........................     Option: (t=43,l=41) Vendor-Specific Information         Option: (43) Vendor-Specific Information         Length: 41         Value: 01276163732E6578616D706C652E636F6D20322041424344...     Option: (t=6,l=8) Domain Name Server</code></p></div><div id="question-tags" class="tags-container tags">dhcp centos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '15, 20:53</strong></p><img src="https://secure.gravatar.com/avatar/db77a027ffc17d668f13ab8230fb67b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikeKulls&#39;s gravatar image" /><p>MikeKulls<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikeKulls has no accepted answers">0%</span></p></div></div><div id="comments-container-39347" class="comments-container"></div><div id="comment-tools-39347" class="comment-tools"></div><div class="clear"></div><div id="comment-39347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39356"></span>

<div id="answer-container-39356" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39356-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried just printing the field itself instead of the whole packet? I don't think individual field output is truncated. In other words, do this (all in one line):</p><pre><code>tshark -V -i vlan2090 -R &quot;bootp.hw.mac_addr contains &quot;00:17:33:00:00:00&quot;&quot; -T fields -e bootp.option.vendor.value</code></pre><p>Or you can output multiple fields, if you need to see more than just that one per DHCP packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '15, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39356" class="comments-container"></div><div id="comment-tools-39356" class="comment-tools"></div><div class="clear"></div><div id="comment-39356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

