+++
type = "question"
title = "Two addresses for ICMP frames"
description = '''I am analyzing a pcap file and extracting data using tshark, but whenever I encounter an ICMP frame, the corresponding data being extracted by tshark is duplicated. For the following frame in wireshark, &quot;ICMP&quot;,&quot;68.232.181.238&quot;,&quot;152.81.230.67&quot; I get src ip dst ip protocol 68.232.181.238,152.81.230.67...'''
date = "2015-03-23T03:21:00Z"
lastmod = "2015-03-23T06:26:00Z"
weight = 40779
keywords = [ "field", "icmp", "tshark", "extraction" ]
aliases = [ "/questions/40779" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Two addresses for ICMP frames](/questions/40779/two-addresses-for-icmp-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40779-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analyzing a pcap file and extracting data using tshark, but whenever I encounter an ICMP frame, the corresponding data being extracted by tshark is duplicated.</p><p>For the following frame in wireshark,</p><p>"ICMP","68.232.181.238","152.81.230.67"</p><p>I get</p><p><code>src ip                                      dst ip              protocol 68.232.181.238,152.81.230.67    152.81.230.67,68.232.181.238    ICMP</code></p><p>the above output from tshark.</p><p>I just need one value each for source and destination ip addresses. I would greatly appreciate it if someone can let me know if there is a different way to extract src and dst ip addresses from pcap. Currently I am using -e ip.src and -e ip.dst to get the ip addresses.</p></div><div id="question-tags" class="tags-container tags">field icmp tshark extraction</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '15, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/2f11d67425fd89633a1599ed7c4a49ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nnmanobala&#39;s gravatar image" /><p>nnmanobala<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nnmanobala has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Mar '15, 03:22</p></div></div><div id="comments-container-40779" class="comments-container"></div><div id="comment-tools-40779" class="comment-tools"></div><div class="clear"></div><div id="comment-40779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40780"></span>

<div id="answer-container-40780" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40780-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <code>-E occurrence=f</code> to print the IP addresses of the packet (and skip the IP header of the original packet that caused the icmp message, which is included as icmp payload)</p><p>From <code>tshark -h</code>:</p><pre><code>  -E&lt;fieldsoption&gt;=&lt;value&gt; set options for output when -Tfields selected:
     header=y|n            switch headers on and off
     separator=/t|/s|&lt;char&gt; select tab, space, printable character as separator
     occurrence=f|l|a      print first, last or all occurrences of each field
     aggregator=,|/s|&lt;char&gt; select comma, space, printable character as
                           aggregator
     quote=d|s|n           select double, single, no quotes for values</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '15, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40780" class="comments-container"><span id="40781"></span><div id="comment-40781" class="comment"><div id="post-40781-score" class="comment-score"></div><div class="comment-text"><p>Your solution works perfectly for my requirement. Thank you very much.</p></div><div id="comment-40781-info" class="comment-info"><span class="comment-age">(23 Mar '15, 06:35)</span> nnmanobala</div></div></div><div id="comment-tools-40780" class="comment-tools"></div><div class="clear"></div><div id="comment-40780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

