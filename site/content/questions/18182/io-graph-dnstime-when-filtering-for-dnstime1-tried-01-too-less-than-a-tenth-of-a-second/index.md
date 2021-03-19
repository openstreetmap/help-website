+++
type = "question"
title = "IO Graph dns.time when filtering for dns.time&lt;=.1 (tried 0.1 too) less than a tenth of a second"
description = '''I have a file that has 1 million packets captured in it. When loading in the file, I filtered it with the filter of dns.time&amp;lt;=0.1. I then tried to create a graph via Statistics|IO Graph. I set the Y access to Unit:Advanced... Set Filter:dns.time&amp;lt;=0.1, Calc:AVG(*)dns.time. The capture shows tha...'''
date = "2013-01-31T07:19:00Z"
lastmod = "2013-02-05T15:20:00Z"
weight = 18182
keywords = [ "graph", "dns", "dns.time" ]
aliases = [ "/questions/18182" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IO Graph dns.time when filtering for dns.time&lt;=.1 (tried 0.1 too) less than a tenth of a second](/questions/18182/io-graph-dnstime-when-filtering-for-dnstime1-tried-01-too-less-than-a-tenth-of-a-second)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18182-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a file that has 1 million packets captured in it. When loading in the file, I filtered it with the filter of dns.time&lt;=0.1. I then tried to create a graph via Statistics|IO Graph. I set the Y access to Unit:Advanced... Set Filter:dns.time&lt;=0.1, Calc:AVG(*)dns.time. The capture shows that the time span (x Axis) shows 260s. However, the graph shows all but approximately the last 5 data points (seconds) as the maximum on the graph.</p><p>Am I experiencing a bug or am I specifying the graph parameters incorrectly?</p><p>I originally tried to graph things without putting a filter cap on the data (which lead me to load the data with a ceiling filter on dns.time).</p><p>How can I extract the dns.time data in csv format with timestamps?</p></div><div id="question-tags" class="tags-container tags">graph dns dns.time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '13, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/8f489ed90495d381524a2bcfb11b8477?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PacketLooker&#39;s gravatar image" /><p>PacketLooker<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PacketLooker has no accepted answers">0%</span></p></div></div><div id="comments-container-18182" class="comments-container"><span id="18332"></span><div id="comment-18332" class="comment"><div id="post-18332-score" class="comment-score"></div><div class="comment-text"><p>I'm having problems to understand the problem description. Can you please add a screenshoot of the IO Graph window?</p></div><div id="comment-18332-info" class="comment-info"><span class="comment-age">(05 Feb '13, 13:58)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18182" class="comment-tools"></div><div class="clear"></div><div id="comment-18182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18337"></span>

<div id="answer-container-18337" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18337-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I was able to reproduce the issue on my Mac. The problem is the binding of responses to requests. It is based on the dns transaction id in combination with the source/destination ip addresses and ports. When there is a collision, the dns.time will be negative for some of the requests. In my case, this happens for the MDNS packets sent by my mac, as they have the same ports (5353) and IP addresses and transaction id (0x0000).</p><p>When you use the filter "dns.time&gt;0 and dns.time&lt;=0.1", do you get better results?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '13, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18337" class="comments-container"></div><div id="comment-tools-18337" class="comment-tools"></div><div class="clear"></div><div id="comment-18337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

