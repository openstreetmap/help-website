+++
type = "question"
title = "Capture filter based on data in packet"
description = '''I need to sniff packets from a very busy proxy server (both interfaces, internal and external). What is worse, I will need to sniff for a day, maybe several days. Because of this I need a very precise filter. As a display filter it would look like this: http contains someurl or ip.addr eq 1.2.3.0/24...'''
date = "2014-03-27T05:09:00Z"
lastmod = "2014-03-27T11:42:00Z"
weight = 31215
keywords = [ "capture", "capture-filter", "tcpdump", "dumpcap" ]
aliases = [ "/questions/31215" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter based on data in packet](/questions/31215/capture-filter-based-on-data-in-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31215-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to sniff packets from a very busy proxy server (both interfaces, internal and external). What is worse, I will need to sniff for a day, maybe several days. Because of this I need a very precise filter. As a display filter it would look like this:</p><p>http contains someurl or ip.addr eq 1.2.3.0/24</p><p>or more slightly complex</p><p>(ip.dst eq 10.0.0.1 and http contain someurl) or ip.addr eq 1.2.3.0/24</p><p>The problem is obviously the "http contains someurl" part. This part is vital, as it will change 50 Mbps of traffic to only, say, 20 MB per day.</p><p>Any solution will do. Tshark, dumpcap, the GUI. I was thinking of something similar to this:</p><pre><code>Capture HTTP GET requests. This looks for the bytes &#39;G&#39;, &#39;E&#39;, &#39;T&#39;, and &#39; &#39; (hex values 47, 45, 54, and 20) just after the TCP header. &quot;tcp[12:1] &amp; 0xf0) &gt;&gt; 2&quot; figures out the TCP header length.</code></pre><p>``From Jefferson Ogata via the tcpdump-workers mailing list.</p><pre><code>port 80 and tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420</code></pre></div><div id="question-tags" class="tags-container tags">capture capture-filter tcpdump dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '14, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/c27c52191553b276cf576ccd38f7ab3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robstar&#39;s gravatar image" /><p>robstar<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robstar has no accepted answers">0%</span></p></div></div><div id="comments-container-31215" class="comments-container"><span id="31219"></span><div id="comment-31219" class="comment"><div id="post-31219-score" class="comment-score"></div><div class="comment-text"><p>Obviously I tried changing the hex-value to what I want to search, but that doesn't work. My guess is that it's searching in a very narrow part of the packet.</p><p>But how do I make it work?</p></div><div id="comment-31219-info" class="comment-info"><span class="comment-age">(27 Mar '14, 08:44)</span> robstar</div></div></div><div id="comment-tools-31215" class="comment-tools"></div><div class="clear"></div><div id="comment-31215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31229"></span>

<div id="answer-container-31229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31229-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do that with a 'simple' <strong>capture</strong> filter. You can try to use the capture filter generator, but the resulting filter might not work in all cases!!</p><blockquote><p><a href="http://www.wireshark.org/tools/string-cf.html">http://www.wireshark.org/tools/string-cf.html</a></p></blockquote><p>Just take a look a the default sample and the generated capture filter. Duh....</p><p>Here is my suggestion: use <strong><a href="http://ngrep.sourceforge.net/">ngrep</a></strong></p><blockquote><p>ngrep -d eth0 -O /var/tmp/http.pcap '/someurl' 'port 80 and (host 10.0.0.1 or net 1.2.3.0/24)'</p></blockquote><p>ngrep will write all <strong>frames</strong> that meet the search criteria to /var/tmp/http.pcap. It will <strong>not</strong> write the whole tcp stream, which is obvious!</p><p>There is also a Windows version of ngrep (please google/bing it).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31229" class="comments-container"></div><div id="comment-tools-31229" class="comment-tools"></div><div class="clear"></div><div id="comment-31229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

