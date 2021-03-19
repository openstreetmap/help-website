+++
type = "question"
title = "How can capture filters capture both Tx and Rx traffic?"
description = '''Hey all, I&#x27;m trying to filter capture traffic. I want to see all LPD traffic to/from a particular printer. However, regardless of whether I use &quot;host 1.2.3.4&quot; or &quot;tcp port 515&quot;, Wireshark captures only traffic originating from the printer; it doesn&#x27;t capture traffic from the other side of the TCP co...'''
date = "2014-04-17T23:57:00Z"
lastmod = "2014-04-21T16:32:00Z"
weight = 31959
keywords = [ "capture-filter" ]
aliases = [ "/questions/31959" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can capture filters capture both Tx and Rx traffic?](/questions/31959/how-can-capture-filters-capture-both-tx-and-rx-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31959-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey all,</p><p>I'm trying to filter capture traffic. I want to see all LPD traffic to/from a particular printer. However, regardless of whether I use "host 1.2.3.4" or "tcp port 515", Wireshark captures only traffic originating from the printer; it doesn't capture traffic from the other side of the TCP connection.</p><p>When I capture with no capture filters, both Tx and Rx are captured.</p><p>I'm running v1.10.6 on Mac OS 10.9.2.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 23:57</strong></p><img src="https://secure.gravatar.com/avatar/6fa43bd94cb4d0c5dc22ad6131b20eb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="noamb&#39;s gravatar image" /><p>noamb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="noamb has no accepted answers">0%</span></p></div></div><div id="comments-container-31959" class="comments-container"><span id="32002"></span><div id="comment-32002" class="comment"><div id="post-32002-score" class="comment-score"></div><div class="comment-text"><p>does your capturing system (or possibly the printer) use VLAN tagged traffic? In other words: Do you see vlan tags in the 'printer frames' while you capture without capture filter?</p></div><div id="comment-32002-info" class="comment-info"><span class="comment-age">(19 Apr '14, 16:11)</span> Kurt Knochner ♦</div></div><span id="32033"></span><div id="comment-32033" class="comment"><div id="post-32033-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, nope, there are no VLANs on this network.</p><p>Update: I tried these same captures using tcpdump instead of the Wireshark GUI.</p><pre><code>tcpdump -i en0 host 1.2.3.4
tcpdump -i en0 tcp port 515</code></pre><p>... both capture ONLY traffic originating from the printer. But</p><pre><code>tcpdump -i en0</code></pre><p>with no filters captures everything. Too much, though!</p><p>Help?</p></div><div id="comment-32033-info" class="comment-info"><span class="comment-age">(21 Apr '14, 14:35)</span> noamb</div></div><span id="32034"></span><div id="comment-32034" class="comment"><div id="post-32034-score" class="comment-score"></div><div class="comment-text"><p>Given that the same code path is used by Wireshark/dumpcap and by tcpdump when capturing traffic, it's not at all surprising that they give the same results.</p><p>If you capture without a capture filter (if you're using tcpdump, save the capture to a pcap file, using the <code>-w</code> flag), and then look at the capture in Wireshark and apply a display filter of <code>tcp.port == 515</code>, what do you see?</p></div><div id="comment-32034-info" class="comment-info"><span class="comment-age">(21 Apr '14, 15:15)</span> Guy Harris ♦♦</div></div><span id="32035"></span><div id="comment-32035" class="comment"><div id="post-32035-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy. Capturing without a filter and then using a display filter does show that bidirectional traffic was captured. However, that's too much traffic for me to capture and then filter.</p></div><div id="comment-32035-info" class="comment-info"><span class="comment-age">(21 Apr '14, 15:45)</span> noamb</div></div><span id="32036"></span><div id="comment-32036" class="comment"><div id="post-32036-score" class="comment-score"></div><div class="comment-text"><p>OK, so, when you capture without a filter and then use a display filter:</p><ul><li>do the packets going <em>to</em> the printer have the destination IP address of the printer (the one you replaced with "1.2.3.4" in your example)?</li><li>do the packets going <em>to</em> the printer have a TCP destination port number of 515?</li><li>do the packets going <em>to</em> the printer have an Ethernet type of 0x0800?</li></ul></div><div id="comment-32036-info" class="comment-info"><span class="comment-age">(21 Apr '14, 15:49)</span> Guy Harris ♦♦</div></div><span id="32037"></span><div id="comment-32037" class="comment not_top_scorer"><div id="post-32037-score" class="comment-score"></div><div class="comment-text"><p>Guy,</p><p>WHOOPS.</p><p>&lt;sheepish&gt;</p><p>Packets TO the printer:</p><pre><code>Ethertype = 0x8100 (VLAN)</code></pre><p>with VLAN ID 1. The packets FROM the printer are</p><pre><code>Ethertype = 0x0800 (IP)</code></pre><p>I don't get it, though -- how can I capture all the traffic despite this situation?</p><p>Crawling back to my hole now.</p><p>:)</p></div><div id="comment-32037-info" class="comment-info"><span class="comment-age">(21 Apr '14, 16:28)</span> noamb</div></div><span id="32040"></span><div id="comment-32040" class="comment not_top_scorer"><div id="post-32040-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Thanks Kurt, nope, <strong>there are no VLANs</strong> on this network.</p></blockquote><p>well... ;-)</p></div><div id="comment-32040-info" class="comment-info"><span class="comment-age">(21 Apr '14, 16:43)</span> Kurt Knochner ♦</div></div><span id="32042"></span><div id="comment-32042" class="comment not_top_scorer"><div id="post-32042-score" class="comment-score"></div><div class="comment-text"><p>Right Kurt, I stand 110% corrected. Thank you.</p></div><div id="comment-32042-info" class="comment-info"><span class="comment-age">(21 Apr '14, 17:00)</span> noamb</div></div></div><div id="comment-tools-31959" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-31959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32039"></span>

<div id="answer-container-32039" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32039-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"How can I capture all the traffic" meaning "why am I seeing all the traffic with no filter" or "how can I use a filter and still see all the traffic"?</p><p>The answer to the first question is "there's no filter, so it just gives you the packets without testing them, so the VLAN headers don't matter."</p><p>The answer to the second question is "host 1.2.3.4 or (vlan and host 1.2.3.4)" or "tcp port 515 or (vlan and tcp port 515)".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '14, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-32039" class="comments-container"></div><div id="comment-tools-32039" class="comment-tools"></div><div class="clear"></div><div id="comment-32039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

