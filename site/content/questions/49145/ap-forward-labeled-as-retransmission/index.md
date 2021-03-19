+++
type = "question"
title = "AP Forward Labeled As Retransmission"
description = '''In an 802.11 infrastructure network, all communication between STAs passes through the AP (access point). This means that when one STA wants to send a packet to another STA in the network, the sending STA sends the packet to the AP, and then the AP forwards the packet to the destination STA. I am mo...'''
date = "2016-01-12T12:58:00Z"
lastmod = "2016-01-12T13:48:00Z"
weight = 49145
keywords = [ "ap", "forwarding", "retransmission", "tcp", "tcp_retransmission" ]
aliases = [ "/questions/49145" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [AP Forward Labeled As Retransmission](/questions/49145/ap-forward-labeled-as-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49145-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In an 802.11 infrastructure network, all communication between STAs passes through the AP (access point). This means that when one STA wants to send a packet to another STA in the network, the sending STA sends the packet to the AP, and then the AP forwards the packet to the destination STA.</p><p>I am monitoring TCP communications between two STAs on a network, and I have found that Wireshark labels a TCP message's second hop (from the AP to the final destination) as a TCP retransmission. This behavior seems incorrect, because the second hop is not actually a retransmission. In addition to being misleading, this behavior makes it difficult to procure statistics on the true number of TCP retransmissions.</p><p>Are there any settings or fixes to alleviate this issue?</p><p>I am using Wireshark v1.12.9 on a Windows 7 PC.</p></div><div id="question-tags" class="tags-container tags">ap forwarding retransmission tcp tcp_retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/6acf3c1293dde7d08c204b9265e46764?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J_Turner&#39;s gravatar image" /><p>J_Turner<br />
<span class="score" title="71 reputation points">71</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J_Turner has no accepted answers">0%</span></p></div></div><div id="comments-container-49145" class="comments-container"></div><div id="comment-tools-49145" class="comment-tools"></div><div class="clear"></div><div id="comment-49145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49147"></span>

<div id="answer-container-49147" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49147-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you're using monitoring mode, as otherwise you should be unable to see those packets at all.</p><p>In such case, the fastest workaround should be to filter out only the frames between any of the two STAs and the AP, using a display filter such as <code>(wlan.da == xx-xx-xx-xx-xx-xx and vlan.ra == xx-xx-xx-xx-xx-xx) or (wlan.sa == xx-xx-xx-xx-xx-xx and wlan.ta == xx-xx-xx-xx-xx-xx)</code> where xx-xx-xx-xx-xx-xx is the MAC of one of the STAs, and then use <code>File -&gt; Export Specified Packets</code> to save the filtered frames into a new pcap(ng) file, choosing the "Displayed" column and "All packets" row when specifying which frames to save.</p><p>Using the newly created file for tcp analysis should then be OK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '16, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jan '16, 13:50</p></div></div><div id="comments-container-49147" class="comments-container"><span id="49148"></span><div id="comment-49148" class="comment"><div id="post-49148-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick answer. I have successfully accomplished this using filtering, but this solution is specific to each file (actually to each MAC ID). I would like a solution that is generic and can be used for any capture file/MAC IDs. Otherwise, I have to create a specific filter for every STA/AP combo that I want to analyze.</p></div><div id="comment-49148-info" class="comment-info"><span class="comment-age">(12 Jan '16, 13:57)</span> J_Turner</div></div><span id="49149"></span><div id="comment-49149" class="comment"><div id="post-49149-score" class="comment-score"></div><div class="comment-text"><p>Hehe, you've made me try what I haven't believed would work (because I've always thought that you must compare a dissected protocol field to a constant, not to another dissected protocol field):</p><p><code>(wlan.ta == wlan.sa and wlan.ra == wlan.bssid) or (wlan.ra == wlan.da and wlan.ta == wlan.bssid)</code></p><p>Is this quick workaround generic enough for your purpose?</p><p>If not, you'll have to wait for someone deeper into it to answer.</p></div><div id="comment-49149-info" class="comment-info"><span class="comment-age">(12 Jan '16, 14:06)</span> sindy</div></div><span id="49156"></span><div id="comment-49156" class="comment"><div id="post-49156-score" class="comment-score"></div><div class="comment-text"><p>That one was a nonsense as it was selecting all packets again.</p><p><code>wlan.ta == wlan.sa and wlan.ra == wlan.bssid</code></p><p>should be more useful as it chooses only STA -&gt; AP packets.</p></div><div id="comment-49156-info" class="comment-info"><span class="comment-age">(12 Jan '16, 22:10)</span> sindy</div></div><span id="49175"></span><div id="comment-49175" class="comment"><div id="post-49175-score" class="comment-score"></div><div class="comment-text"><p>Good thinking! It is more helpful to me to filter out the duplicate packets, so the filter could be:</p><p>!(wlan.sa != wlan.bssid &amp;&amp; wlan.fc.ds == 2)</p><p>This filter is yellow, but it does yield the expected result. Can you think of another (non-yellow) way to filter out the AP -&gt; STA packets. Note that in my case, it is possible for packets to originate with the AP (embedded system where Ad-hoc is not employed).</p></div><div id="comment-49175-info" class="comment-info"><span class="comment-age">(13 Jan '16, 08:15)</span> J_Turner</div></div><span id="49185"></span><div id="comment-49185" class="comment"><div id="post-49185-score" class="comment-score"></div><div class="comment-text"><p>After thinking a bit more, I'd say that <code>wlan.ta == wlan.sa</code> should be sufficient and "green" for all cases. It will show both the packets for which the AP is the real originator and the packets which are sent by any STAs, it will only block the packets retranslated by the AP.</p><p>Once you confirm this works for you, I'll edit also the original response in this sense.</p></div><div id="comment-49185-info" class="comment-info"><span class="comment-age">(13 Jan '16, 11:34)</span> sindy</div></div><span id="51840"></span><div id="comment-51840" class="comment not_top_scorer"><div id="post-51840-score" class="comment-score"></div><div class="comment-text"><p>I tried the wlan.ta == wlan.sa, but it filters out the 802.11 acknowledge messages, CTS-to-self, and other short, non-standard messages that I would like to see.</p><p>I believe all of these "non-standard" messages are control frames, so I think this will work: (wlan.ta == wlan.sa || wlan.fc.type == 1)</p></div><div id="comment-51840-info" class="comment-info"><span class="comment-age">(21 Apr '16, 08:53)</span> J_Turner</div></div></div><div id="comment-tools-49147" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-49147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

