+++
type = "question"
title = "Is it correct to assume that before learning Wireshark I should learn TCP/IP and other protocols so I can know what I&#x27;m looking for on a trace file?"
description = '''Hey guys!! Is it correct to assume that before learning Wireshark I should learn TCP/IP and other protocols so I can know what I&#x27;m looking for on a trace file? Because I see in every Wireshark video a lot of &quot;how to do this or that inside Wireshark&quot; but I&#x27;m kind of clueless of what I was supposed to...'''
date = "2014-02-24T11:58:00Z"
lastmod = "2014-02-24T12:39:00Z"
weight = 30148
keywords = [ "newbie" ]
aliases = [ "/questions/30148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it correct to assume that before learning Wireshark I should learn TCP/IP and other protocols so I can know what I'm looking for on a trace file?](/questions/30148/is-it-correct-to-assume-that-before-learning-wireshark-i-should-learn-tcpip-and-other-protocols-so-i-can-know-what-im-looking-for-on-a-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys!!</p><p>Is it correct to assume that before learning Wireshark I should learn TCP/IP and other protocols so I can know what I'm looking for on a trace file?</p><p>Because I see in every Wireshark video a lot of "how to do this or that inside Wireshark" but I'm kind of clueless of what I was supposed to look for in the first place..</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">newbie</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '14, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/6a24e499a575770e6ba8e4c74d822420?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafaelbn&#39;s gravatar image" /><p>rafaelbn<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafaelbn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Feb '14, 14:16</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-30148" class="comments-container"></div><div id="comment-tools-30148" class="comment-tools"></div><div class="clear"></div><div id="comment-30148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30152"></span>

<div id="answer-container-30152" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30152-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, this is a bit difficult to answer - it sure helps to know how TCP/IP and other protocols work to be able to understand what Wireshark is showing you, but learning protocols from a book/RFC is not exactly helpful either. My advice would be to focus on simple things first, and then work your way up by running Wireshark while doing some tests to see how protocols behave.</p><p>For example: run Wireshark, ping another PC or other network device, and check how Ethernet addresses change from source to destination when the answer comes back. Then take a look at ARP, which is used to resolve IP addresses to MAC adresses - because if a IP is pinged it needs to know what MAC it has. Next check out IP, then ICMP (which is used by ping), and so on. If you're curious about network functionality Wireshark is a great learning tool to watch things happen.</p><p>If you can't figure something out that you've seen in Wireshark you can always come back here and ask specific questions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '14, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-30152" class="comments-container"><span id="30153"></span><div id="comment-30153" class="comment"><div id="post-30153-score" class="comment-score"></div><div class="comment-text"><p>I think I got the basics covered. I currently hold Cisco CCNP. But every now and then I got some "network is broken" kind of problem and can't always find out what's wrong. And Wireshark shows it but I guess I can't see it because I don't understand how every protocol works... And all my peers, when we fire up Wireshark seems desperation mode kicking in because we don't know what to look for...</p><p>I guess that's me sayin I don't get networks that well BUT that's going to change!!</p><p>Any suggestions where to go next as far as protocols?</p></div><div id="comment-30153-info" class="comment-info"><span class="comment-age">(24 Feb '14, 12:56)</span> rafaelbn</div></div><span id="30154"></span><div id="comment-30154" class="comment"><div id="post-30154-score" class="comment-score"></div><div class="comment-text"><p>What I do when someone says "the network is broken" is pretty simple:</p><ol><li>find someone who can show me the problem</li><li>capture packets at a location where the problematic communication needs to pass through</li><li>Analyze the packets for the nodes involved by using a conversation filter on their IPs and/or ports.</li></ol><p>Problems are usually either "the communication is slow", "the communication breaks down" or "I can' get a connection". For that you should know who TCP works (Three Way Handshake, Reset, FIN, Push etc), and you need to look at timings. Things that should be fast need to be verified. Things that can take some time (like a client reading a web page and only requesting the next a minute later) can be ignored. Of course there are always exceptions, but that is something that is learned with experience.</p></div><div id="comment-30154-info" class="comment-info"><span class="comment-age">(24 Feb '14, 13:06)</span> Jasper ♦♦</div></div><span id="30155"></span><div id="comment-30155" class="comment"><div id="post-30155-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I can't see it because I don't understand how <strong>every protocol</strong> works</p></blockquote><p>well, I guess nobody knows how <strong>every</strong> protocol works. But if you know enough basic protocols, you can easily learn/understand pretty much every protocol, at least well enough to find 'typical' problems with the help of Mr. Google.</p><p>So, here are some questions:</p><ul><li>which protocols are you familiar with (poor, good, champ)?</li><li>which protocols are you trying to understand in those "network is broken" kind of problems?</li><li>can you describe a typical problem and what you did to find the reason?</li></ul></div><div id="comment-30155-info" class="comment-info"><span class="comment-age">(24 Feb '14, 13:13)</span> Kurt Knochner ♦</div></div><span id="30160"></span><div id="comment-30160" class="comment"><div id="post-30160-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I currently hold Cisco CCNP.</p></blockquote><p>From <a href="http://www.cisco.com/web/learning/certifications/professional/ccnp/index.html">Cisco's page on CCNP</a> I infer that you at least have to know <em>something</em> about IP to get it, so you've presumably learned IP, at least.</p><p>For some problems it would be useful to know something about TCP as well; if, for example, a routing/switching-layer problem manifests itself as slow or failing attempts to establish a TCP connection to a Web site, it might appear in a trace as initial SYNs with no SYN+ACK response (due to the initial SYN not making it from the client to the server, or the SYN+ACK response to that initial SYN not making it from the server to the client), so knowing about the TCP three-way handshake would help.</p></div><div id="comment-30160-info" class="comment-info"><span class="comment-age">(24 Feb '14, 17:00)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-30152" class="comment-tools"></div><div class="clear"></div><div id="comment-30152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

