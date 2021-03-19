+++
type = "question"
title = "Best criteria to zero in on packets related to arp poisoning."
description = '''Asked a question earlier about arp poisoning. This question is slightly different.  Given a pcap with arp poisoning, pcap, wonder if the criteria to catch arp poisoning is to detect ARP request whose destination is not broadcast. If not, what&#x27;s the best rule to get packets related to arp poisoning. ...'''
date = "2015-05-24T08:47:00Z"
lastmod = "2015-05-25T19:34:00Z"
weight = 42640
keywords = [ "wireshark" ]
aliases = [ "/questions/42640" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Best criteria to zero in on packets related to arp poisoning.](/questions/42640/best-criteria-to-zero-in-on-packets-related-to-arp-poisoning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42640-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Asked a <a href="https://ask.wireshark.org/questions/42257/arp-poisoning-pcap">question</a> earlier about arp poisoning. This question is slightly different.<br />
</p><p>Given a pcap with arp poisoning, <a href="http://chrissanders.org/captures/arppoison.pcap">pcap</a>, wonder if the criteria to catch arp poisoning is to detect ARP request whose destination is not broadcast. If not, what's the best rule to get packets related to arp poisoning.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '15, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span> </br></p></div></div><div id="comments-container-42640" class="comments-container"></div><div id="comment-tools-42640" class="comment-tools"></div><div class="clear"></div><div id="comment-42640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42653"></span>

<div id="answer-container-42653" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42653-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you already <em>know</em> that there is arp poisoning in the trace file, that's one thing. I'd do something like this as a display filter in your example. This would look for all arp requests whose IP is the gateway and whose source mac address is not the gateway's mac. Note, you can't just filter on all non-broadcasted ARP requests since often ARP requests are unicast (already-known ARP mappings will be queried periodically, unicasted to the mac address already understood to own the IP as a way of efficiently refreshing the ARP cache):</p><p>tshark -r example.pcap -Y 'arp.opcode==1&amp;&amp;arp.src.proto_ipv4=="172.16.0.1"&amp;&amp;!arp.src.hw_mac=="00:21:70:c0:56:f0"'</p><p>While it might be useful in post-incident analysis, practically speaking Wireshark is just not a good tool to use as a detection system for something like this. I highly recommend something like Snort, which is a dedicated intrusion detection system that watches packet streams for malicious content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '15, 19:34</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-42653" class="comments-container"><span id="42654"></span><div id="comment-42654" class="comment"><div id="post-42654-score" class="comment-score"></div><div class="comment-text"><p>Thanks @Quadratic for the tshark command and the comment on snort. I accepted your answer. If you have any pointers to the following, please let me know: given a big pcap (you don't know the mappings of ip to mac yet), how do we detect the presence of arp poisoning/spoof by some tools or commands.</p></div><div id="comment-42654-info" class="comment-info"><span class="comment-age">(25 May '15, 22:21)</span> pktUser1001</div></div><span id="42686"></span><div id="comment-42686" class="comment"><div id="post-42686-score" class="comment-score"></div><div class="comment-text"><p>If you have a large pcap, that filter is fine provided you know the gateway IP and MAC address. If it's a huge file you might want to chop it up with something like Wireshark's "editcap" command line utility to manage the queries but the method works.</p><p>Snort can take the '-r' flag to read a .pcap file also. It's more tailored for this but if the task is as simple as described then there's no reason you can't do it with Tshark/Wireshark. As a normal real-time intrusion detection tool Snort is definitely the way to go though.</p></div><div id="comment-42686-info" class="comment-info"><span class="comment-age">(26 May '15, 18:20)</span> Quadratic</div></div></div><div id="comment-tools-42653" class="comment-tools"></div><div class="clear"></div><div id="comment-42653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

