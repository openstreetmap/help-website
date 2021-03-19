+++
type = "question"
title = "Capture filter expressions"
description = '''I have a home network which I am monitoring using wireshark and I need some help with a modified capture filter expression. I am trying to filter out traffic between any of my LOCAL devices and each other. This is particularly relevant to me because I have a number of IP cameras that generate a lot ...'''
date = "2014-06-17T09:03:00Z"
lastmod = "2014-06-17T12:16:00Z"
weight = 33899
keywords = [ "range", "capture-filter" ]
aliases = [ "/questions/33899" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Capture filter expressions](/questions/33899/capture-filter-expressions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33899-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a home network which I am monitoring using wireshark and I need some help with a modified capture filter expression. I am trying to filter out traffic between any of my LOCAL devices and each other. This is particularly relevant to me because I have a number of IP cameras that generate a lot of traffic when I connect to them from any of my local PCs. The intention is to only capture traffic to/from the public Internet and my devices.</p><p>Static addresses... - 192.168.1.43 = router - 192.168.1.61 = pc1, wired - 192.168.1.62 = pc2, wired - 192.168.1.72 = pc2, wireless - 192.168.1.63 = pc3, wired - 192.168.1.73 = pc3, wireless - 192.168.1.101 = IP camera #1 - 192.168.1.102 = IP camera #2 - 192.168.1.103 = IP camera #3 - 192.168.1.104 = IP camera #4 - 192.168.1.105 = IP camera #5</p><p>Original long-winded capture filter used by wireshark when started on the command line (.bat file). I have separated the components for clarity...</p><p>+++++++++++++++ start of filter +++++++++++++++</p><p>(not broadcast and not multicast)</p><p>and (not (src host 192.168.1.61 and dst host 192.168.1.43)) and (not (src host 192.168.1.62 and dst host 192.168.1.43)) and (not (src host 192.168.1.63 and dst host 192.168.1.43)) and (not (src host 192.168.1.72 and dst host 192.168.1.43)) and (not (src host 192.168.1.73 and dst host 192.168.1.43))</p><p>and (not (src host 192.168.1.61 and dst host 192.168.1.101)) and (not (src host 192.168.1.61 and dst host 192.168.1.102)) and (not (src host 192.168.1.61 and dst host 192.168.1.103)) and (not (src host 192.168.1.61 and dst host 192.168.1.104)) and (not (src host 192.168.1.61 and dst host 192.168.1.105))</p><p>and (not (src host 192.168.1.62 and dst host 192.168.1.101)) and (not (src host 192.168.1.62 and dst host 192.168.1.102)) and (not (src host 192.168.1.62 and dst host 192.168.1.103)) and (not (src host 192.168.1.62 and dst host 192.168.1.104)) and (not (src host 192.168.1.62 and dst host 192.168.1.105))</p><p>and (not (src host 192.168.1.63 and dst host 192.168.1.101)) and (not (src host 192.168.1.63 and dst host 192.168.1.102)) and (not (src host 192.168.1.63 and dst host 192.168.1.103)) and (not (src host 192.168.1.63 and dst host 192.168.1.104)) and (not (src host 192.168.1.63 and dst host 192.168.1.105))</p><p>+++++++++++++++ end of filter +++++++++++++++</p><p>When the above filter, which works, is declared on a single line it is over 1200 characters in length, which I find a little excessive! I want to simplify the filter using IP address RANGES.</p><p>According to examples provided at <a href="http://wiki.wireshark.org/CaptureFilters...">http://wiki.wireshark.org/CaptureFilters...</a></p><ul><li><p>Capture traffic to or from a range of IP addresses: net 192.168.0.0/24 (or net 192.168.0.0 mask 255.255.255.0)</p></li><li><p>Capture traffic from a range of IP addresses: src net 192.168.0.0/24 (or src net 192.168.0.0 mask 255.255.255.0)</p></li><li><p>Capture traffic to a range of IP addresses: dst net 192.168.0.0/24 (or dst net 192.168.0.0 mask 255.255.255.0)</p></li></ul><p>[Group 1] So based on the above I tried using... (not broadcast and not multicast)</p><p>and (not (src net 192.168.1.0/32 and dst host 192.168.1.43))</p><p>and (not (src net 192.168.1.0/32 and dst net 192.168.1.0/32))</p><p>NB. I used "/32" rather than "/24" because I read somewhere that there are only 32 bits in an IPv4 address, although I might be confusing the meaning here.</p><p>I have also tried...</p><p>[Group 2] based on "dotted-quad" filter expressions shown at <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html...">http://www.tcpdump.org/manpages/pcap-filter.7.html...</a></p><p>(not broadcast and not multicast)</p><p>and (not ((src net 192.168.1.0 mask 255.255.255.0) and dst host 192.168.1.43))</p><p>and (not ((src net 192.168.1.0 mask 255.255.255.0) and (dst net 192.168.1.0 mask 255.255.255.0)))</p><p>and also...</p><p>[Group 3] based on "dotted-triple" filter expressions shown at <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html...">http://www.tcpdump.org/manpages/pcap-filter.7.html...</a></p><p>(not broadcast and not multicast)</p><p>and (not ((src net 192.168.1 mask 255.255.255.0) and dst host 192.168.1.43))</p><p>and (not ((src net 192.168.1 mask 255.255.255.0) and (dst net 192.168.1 mask 255.255.255.0)))</p><p>All of these last 3 filters are valid as far as Wireshark is concerned, i.e. no errors reported. My question is - are these last 3 [groups] of filter expressions equivalent to the original lengthy filter? (I have read up on IP addresses and subnet masks, but am I still confused so need help please)</p></div><div id="question-tags" class="tags-container tags">range capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '14, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/bf30570c015382d7f482135a7b40f0f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gargoil666uk&#39;s gravatar image" /><p>gargoil666uk<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gargoil666uk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jun '14, 09:05</p></div></div><div id="comments-container-33899" class="comments-container"></div><div id="comment-tools-33899" class="comment-tools"></div><div class="clear"></div><div id="comment-33899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33904"></span>

<div id="answer-container-33904" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33904-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>how about this:</p><blockquote><p>'not (src net 192.168.1.0/24 and dst net 192.168.1.0/24)'</p></blockquote><p>which means: Every packet where (source <strong>and</strong> destination address) of a packet are <strong>not</strong> in the network 192.168.1.0/24.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '14, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jun '14, 12:34</p></div></div><div id="comments-container-33904" class="comments-container"><span id="33920"></span><div id="comment-33920" class="comment"><div id="post-33920-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, that did the trick. It was so obvious, but I had spent too much time staring at my variations that I couldn't see the wood for the trees.</p></div><div id="comment-33920-info" class="comment-info"><span class="comment-age">(18 Jun '14, 04:08)</span> gargoil666uk</div></div><span id="33922"></span><div id="comment-33922" class="comment"><div id="post-33922-score" class="comment-score"></div><div class="comment-text"><p>Good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-33922-info" class="comment-info"><span class="comment-age">(18 Jun '14, 04:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33904" class="comment-tools"></div><div class="clear"></div><div id="comment-33904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

