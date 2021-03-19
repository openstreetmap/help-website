+++
type = "question"
title = "Capturing traffic to any host within a specific domain"
description = '''I need to capture HTTP GET and POST requests to (responses from aren&#x27;t of interest) any host that is within .example.com. This will be a long running capture and the machine is fairly heavily used, so I&#x27;m keenly interested in controlling what is captured rather than just what is displayed. There are...'''
date = "2012-04-03T10:13:00Z"
lastmod = "2012-04-04T12:52:00Z"
weight = 9916
keywords = [ "capture", "domain", "http", "wildcard" ]
aliases = [ "/questions/9916" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing traffic to any host within a specific domain](/questions/9916/capturing-traffic-to-any-host-within-a-specific-domain)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9916-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to capture HTTP GET and POST requests to (responses from aren't of interest) any host that is within <em>.<a href="http://example.com">example.com</a>. This will be a long running capture and the machine is fairly heavily used, so I'm keenly interested in controlling what is captured rather than just what is displayed. There are probably hundreds of hosts within</em> .<a href="http://example.com">example.com</a>, some I won't even know about. So a wildcard is key. These requests may come from a browser or other type of application, so I need to use a lower level approach. My initial impression was that this isn't possible via a capture filter, but I thought I'd ping the experts before giving up. Is it possible with Wireshark at all?</p><p>Note: although I'm currently interested in just HTTP requests, if there is a way to do a similar thing without limiting it to HTTP (which conveniently provides the HOST header) or a specific direction, I would be interested in the more general case too :)</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">capture domain http wildcard</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '12, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/57a45a0d67a3696b7339150063e638f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheBitsCometh&#39;s gravatar image" /><p>TheBitsCometh<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheBitsCometh has no accepted answers">0%</span></p></div></div><div id="comments-container-9916" class="comments-container"></div><div id="comment-tools-9916" class="comment-tools"></div><div class="clear"></div><div id="comment-9916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9942"></span>

<div id="answer-container-9942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9942-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capture filters can't work with wildcards nor can they handle re-assembly. Your best bet is to use dumpcap using the "-b filesize" option to split data accross files. You can then use tshark with a display filter to extract the packets of interest.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '12, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9942" class="comments-container"><span id="9958"></span><div id="comment-9958" class="comment"><div id="post-9958-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the additional info. Will roll up my sleeves this weekend and hopefully get something running.</p></div><div id="comment-9958-info" class="comment-info"><span class="comment-age">(05 Apr '12, 05:13)</span> TheBitsCometh</div></div></div><div id="comment-tools-9942" class="comment-tools"></div><div class="clear"></div><div id="comment-9942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9920"></span>

<div id="answer-container-9920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9920-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check out these examples from <a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a> and tailor to your situation...</p><p>Capture traffic to a range of IP addresses: dst net 192.168.0.0/24 or dst net 192.168.0.0 mask 255.255.255.0</p><p>I haven't researched it, but I'm guessing 0/24 means all IPs ending ".0" up to and including ".24", but it might mean twentyfour IPs starting at 0 (ie, 0-23).</p><p>The mask should capture anything going to 192.168.0.* where * is from 0 to 255.</p><p>Also in the above capture examples: Capture HTTP GET requests. This looks for the bytes 'G', 'E', 'T', and ' ' (hex values 47, 45, 54, and 20) just after the TCP header. "tcp[12:1] &amp; 0xf0) &gt;&gt; 2" figures out the TCP header length. (From Jefferson Ogata via the tcpdump-workers mailing list.)</p><pre><code>port 80 and tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420</code></pre><p>So all you have to do is find your IPs for .<a href="http://example.com">example.com</a> and combine that with the GET and POST filters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '12, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/c609362c709623fe3591a5da33a4937b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PReinie&#39;s gravatar image" /><p>PReinie<br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PReinie has no accepted answers">0%</span></p></div></div><div id="comments-container-9920" class="comments-container"><span id="9921"></span><div id="comment-9921" class="comment"><div id="post-9921-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your time and reply. A point I failed to explicitly mention (sorry) is that *.<a href="http://example.com">example.com</a> aren't neatly tucked into known blocks of IP Addresses. I don't know what the specific hosts are and they are surely spread across many providers/blocks.</p><p>At first I thought that approach to identifying a GET wouldn't work in some (especially POST) cases where the HTTP request is spread across multiple packets. However, your comment made me dig a bit deeper and I've just come across some discussions regarding the reassemble options. I'm not familiar with Wireshark at that level yet, but perhaps now that I have something to search for and read I'll figure out some way to implement a Host: pattern match. Note: This was too big to fit into a "comment", so I was forced to make it an "answer".<br />
</p></div><div id="comment-9921-info" class="comment-info"><span class="comment-age">(03 Apr '12, 13:06)</span> TheBitsCometh</div></div><span id="9974"></span><div id="comment-9974" class="comment"><div id="post-9974-score" class="comment-score"></div><div class="comment-text"><p>So maybe you have to make it a find/discover phase, first capturing "many" of the known IPs from a list of many-more, and then capturing of the known set those GET and POST communications you need. (Rome wasn't built in a day.)</p><p>Add on more IPs as you deem fit. Have you ever whittled? You start with a large piece (big chunk), and end up with a much (usually) smaller piece (also a chunk, of lesser dimensions), the end being what you want. If it's not, repeat (with a new piece, not gluing it back together). Granted, not many people whittle now, but it's a concept used in, shall we say, "artisan crafting", and sometimes, that's what we (as engineers) have to do, in a different world). Hell, Jobs wouldn't have given it another thunk! (Thunk being the past-tense of thought, in my words. ;) )</p></div><div id="comment-9974-info" class="comment-info"><span class="comment-age">(05 Apr '12, 22:02)</span> PReinie</div></div><span id="9976"></span><div id="comment-9976" class="comment"><div id="post-9976-score" class="comment-score"></div><div class="comment-text"><p>I admire and acknowledge the benefits of iterative approaches :) The domains/systems of interest are large and dynamic (think global ad/content delivery networks). So although I am hesitant to rule out any IP blocks, it indeed may prove useful to refine things once I have some sense of what they are. I'm still mulling over approaches. In addition to what we've been discussing, I'm also considering:</p><p>1) For HTTP, route through an HTTP proxy that supports logging based on HTTP header pattern matching. 2) For HTTPS, consider the possibilities of setting up a MITM HTTPS proxy with similar logging capability. Note: Entirely my computers and my local network. No other users would be affected by the MITM.</p><p>While thinking about this, one approach did come to mind which I'll share for fun. Use a DNS proxy to redirect "hostnames of interest" traffic to local private IP Addresses corresponding to a proxy that captures the data of interest and then forwards it to the real destination IP Address that was saved by the DNS proxy.</p></div><div id="comment-9976-info" class="comment-info"><span class="comment-age">(05 Apr '12, 23:25)</span> TheBitsCometh</div></div></div><div id="comment-tools-9920" class="comment-tools"></div><div class="clear"></div><div id="comment-9920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

