+++
type = "question"
title = "RST packets from an Apache host using ProxyPass"
description = '''I&#x27;ve got an Apache host that ProxyPass&#x27;es some connections for certain URL&#x27;s, for example &amp;lt;Location /partner/data &amp;gt;  ProxyPass https://incoming.partnervendor.com  ProxyPassReverse https://incoming.partnervendor.com &amp;lt;/Location&amp;gt; Pretty standard. Anything coming from /partner/data should pa...'''
date = "2017-10-27T13:12:00Z"
lastmod = "2017-10-28T10:28:00Z"
weight = 64305
keywords = [ "rst", "apache" ]
aliases = [ "/questions/64305" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RST packets from an Apache host using ProxyPass](/questions/64305/rst-packets-from-an-apache-host-using-proxypass)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64305-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got an Apache host that ProxyPass'es some connections for certain URL's, for example</p><p>&lt;Location /partner/data &gt;<br />
ProxyPass <a href="https://incoming.partnervendor.com">https://incoming.partnervendor.com</a><br />
ProxyPassReverse <a href="https://incoming.partnervendor.com">https://incoming.partnervendor.com</a><br />
&lt;/Location&gt;</p><p>Pretty standard. Anything coming from /partner/data should pass on to the vendor's host via https</p><p>What I'm seeing is very odd though. There are random clusters of RST packets being sent (from my host) to the IP of the above vendor. These don't make sense to me as</p><li>They're going from a high port &gt;1024 to a high port &gt;1024. The host only accepts connections on the standard web ports, and the ProxyPass is only to port 443</li><li>The RST packets all have a sequence ID of 1, which would indicate they're attempting to reset a connection that doesn't exist</li><li>They aren't consistent with any known connections. I see no SYN or ACK packets related to the IP's/ports of the RST, just RST's</li><p>I'm thinking this might be a bug with Apache or possibly the Linux OS, but as of yet Google search reveals nothing that would point to the root cause.</p><p>Packets are being captured with a tcpdump which is essentially capturing local-&gt;nonlocal or nonlocal-&gt;local on high ports:</p><pre><code>tcpdump -nn -i eth0 &#39;dst portrange 1024-65535 &amp;&amp; src portrange 1024-65535 &amp;&amp; ((src 192.168.50.1 &amp;&amp; ! dst net 192.168.0.0/16) || ( dst 192.168.50.1 &amp;&amp; ! src net 192.168.0.0/16))&#39;</code></pre></div><div id="question-tags" class="tags-container tags">rst apache</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '17, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/1f27405782615ad7d5e4da96aee91d09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phx&#39;s gravatar image" /><p>phx<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phx has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-64305" class="comments-container"><span id="64318"></span><div id="comment-64318" class="comment"><div id="post-64318-score" class="comment-score"></div><div class="comment-text"><p>Not a Wireshark question. You should post this on an Apache Web Server forum of some kind.</p></div><div id="comment-64318-info" class="comment-info"><span class="comment-age">(28 Oct '17, 02:00)</span> Jaap ♦</div></div></div><div id="comment-tools-64305" class="comment-tools"></div><div class="clear"></div><div id="comment-64305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64322"></span>

<div id="answer-container-64322" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64322-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I doubt it's an Apache question either, its just that Apache is the only place that references those IPs at all (but Apache itself is L7 and isn't low enough in the stack to cause this). I just showed the config for clarity of what the host is doing.</p><p>It could be a kernel bug, networking bug, or possibly wireshark/tcpdump missing info. But in general a SEQ-1 RST and/or an RST without associated session would seem to be against TCP standard.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '17, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/1f27405782615ad7d5e4da96aee91d09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phx&#39;s gravatar image" /><p>phx<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phx has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Oct '17, 10:56</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-64322" class="comments-container"></div><div id="comment-tools-64322" class="comment-tools"></div><div class="clear"></div><div id="comment-64322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

