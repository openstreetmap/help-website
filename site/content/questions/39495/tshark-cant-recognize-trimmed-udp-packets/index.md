+++
type = "question"
title = "tshark can&#x27;t recognize trimmed udp packets"
description = '''Hi there, I am using iperf to generate udp traffic between two wireless nodes.  Simulatenously I am sniffing the traffic on a seperate monitor interface with tcpdump where snaplen option is set to 102 (i trim the packets to reduce the trace size) When I open the trace in Wireshark, it is recognized ...'''
date = "2015-01-30T04:13:00Z"
lastmod = "2015-01-30T05:45:00Z"
weight = 39495
keywords = [ "iperf", "udp", "tshark", "snaplen", "ip" ]
aliases = [ "/questions/39495" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark can't recognize trimmed udp packets](/questions/39495/tshark-cant-recognize-trimmed-udp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39495-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I am using <code>iperf</code> to generate udp traffic between two wireless nodes.</p><p>Simulatenously I am sniffing the traffic on a seperate monitor interface with <code>tcpdump</code> where <code>snaplen</code> option is set to 102 (i trim the packets to reduce the trace size)</p><p>When I open the trace in Wireshark, it is recognized as an udp packet. However, tshark doesn't even recognize these packets as ip packets. Filters such as <code>ip</code>, <code>ip.addr</code>, <code>udp</code> display no results in tshark, while in Wireshark they work perfectly fine.</p><p>Does anyone know why this is, and is there a way to change this behaviour of tshark?</p></div><div id="question-tags" class="tags-container tags">iperf udp tshark snaplen ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '15, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/2cd7abf8008d63d7e08f46aa75bff063?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itrustedyou&#39;s gravatar image" /><p>itrustedyou<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itrustedyou has no accepted answers">0%</span></p></div></div><div id="comments-container-39495" class="comments-container"></div><div id="comment-tools-39495" class="comment-tools"></div><div class="clear"></div><div id="comment-39495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39498"></span>

<div id="answer-container-39498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39498-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since Wireshark and tshark use the same dissection engine, they should show the same results. Assuming you're using tshark and wireshark on the same machine.</p><p>One other thing to take into account is to check whether you're using the same configuration profile in tshark and wireshark.</p><p>Can you share the output of <code>tshark -nlr &lt;pcap-file&gt; -V -c1</code>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '15, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39498" class="comments-container"><span id="39576"></span><div id="comment-39576" class="comment"><div id="post-39576-score" class="comment-score"></div><div class="comment-text"><p>I am using them on the same machine.</p><p>here is the output I get from your command, for one of the unrecognized UDP packets - <a href="http://paste2.org/_dkjdkMtA">http://paste2.org/_dkjdkMtA</a></p><p>Thank you very much for your answer!</p></div><div id="comment-39576-info" class="comment-info"><span class="comment-age">(02 Feb '15, 12:07)</span> itrustedyou</div></div></div><div id="comment-tools-39498" class="comment-tools"></div><div class="clear"></div><div id="comment-39498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

