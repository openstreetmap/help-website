+++
type = "question"
title = "Wireshark filter"
description = '''Hey there,  Im currently working on a filter that captures source IP address, visited URL and a timestamp.  So far i&#x27;ve been trying: (frame[54:16] == 47:45:54:20:2f:20:48:54:54:50:2f:31:2e:31:0d:0a), which works well on traffic generated from my PC, but I have to change the frame part to frame[66:16...'''
date = "2014-02-27T10:51:00Z"
lastmod = "2014-02-27T15:39:00Z"
weight = 30241
keywords = [ "wireshark" ]
aliases = [ "/questions/30241" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark filter](/questions/30241/wireshark-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30241-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there,</p><p>Im currently working on a filter that captures source IP address, visited URL and a timestamp.</p><p>So far i've been trying: (frame[54:16] == 47:45:54:20:2f:20:48:54:54:50:2f:31:2e:31:0d:0a), which works well on traffic generated from my PC, but I have to change the frame part to frame[66:16] to see traffic generated from apple devices.</p><p>Can anybody tell me more about how the frame filter works? I guess It has something to do with location/position in the frame but I dont have a clue why there is 54 for PC traffic and 66 for apple devices. Is there a universal syntax to display traffic from all types of devices?</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/916ab3898b7d08d2767ada015ce1866c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="added&#39;s gravatar image" /><p>added<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="added has no accepted answers">0%</span></p></div></div><div id="comments-container-30241" class="comments-container"></div><div id="comment-tools-30241" class="comment-tools"></div><div class="clear"></div><div id="comment-30241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30247"></span>

<div id="answer-container-30247" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30247-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Im currently working on a filter that captures source IP address, visited URL and a timestamp.</p></blockquote><p>In Wireshark/TShark, the term "filter" refers to something that a packet does, or doesn't match - i.e., all it does is say "this packet passes" or "this packet doesn't pass". In that context, "capture source IP address" means "packets with this IP source address pass the filter and other packets don't", "capture visited URL" means "packets that are HTTP requests using this URL pass the filter and other packets don't", and "capture timestamp" means "packets with this timestamp pass the filter and other packets don't".</p><p>The Wireshark display filter you show looks for "GET / HTTP/1.1{CR}{LF}", so you appear to be trying to construct a filter that passes only HTTP requests with a visited URL of /.</p><p>The <code>frame[]</code> filter looks at raw byte values at very specific offsets in the packet. There is <em>no</em> guarantee that the payload of a TCP segment - which is what would contain the HTTP request line in your example - will be at a fixed offset in the packet; the link-layer header is variable-length in some networks such as 802.11, an IPv4 header can have options and thus be bigger than 20 bytes, a TCP header can have options and thus be bigger than 20 bytes, and the packet might have an IPv6 header plus a variable number of extension headers rather than an IPv4 header.</p><p>So a <code>frame[]</code> filter is, in general, a lot less useful than people might think.</p><p>A <code>tcp[]</code> filter looks at the TCP header and payload, so it's <em>more</em> useful in this case, but it still doesn't handle TCP options making the TCP header bigger than 20 bytes.</p><p>What you really want here is:</p><pre><code>http.request.method == &quot;GET&quot; and http.request.uri == &quot;/&quot;</code></pre><p>which is a <strong><em>LOT</em></strong> easier than trying to match raw bytes in a packet. That one will work no matter <em>how</em> big the link-layer, IP, and TCP headers are.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-30247" class="comments-container"></div><div id="comment-tools-30247" class="comment-tools"></div><div class="clear"></div><div id="comment-30247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30244"></span>

<div id="answer-container-30244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30244-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The difference is 12 bytes so it is most proably the tcp timestamp option that apple supports and your PC doesn't. Try<br />
<code>tcp[20:16]==4745:5420:2f20:4854:5450:2f31:2e31:0d0a || tcp[32:16]==4745:5420:2f20:4854:5450:2f31:2e31:0d0a</code><br />
or<br />
<code>tcp contains ...</code> to create a more generic filter</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '14, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-30244" class="comments-container"></div><div id="comment-tools-30244" class="comment-tools"></div><div class="clear"></div><div id="comment-30244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

