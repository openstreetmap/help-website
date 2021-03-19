+++
type = "question"
title = "Using tcprewrite seed only with source IP"
description = '''Hi, I use tcprewrite command to randomize the IPs of different pcaps: tcprewrite --seed=$RANDOM --infile=a.pcap --outfile=B.pcap This changes IPs of both source of destination. Is there anyway I can limit this change to source IPs or destination IPs alone and not both?'''
date = "2014-02-12T01:52:00Z"
lastmod = "2014-02-12T02:53:00Z"
weight = 29743
keywords = [ "tcprewrite", "tcpdump", "tcpreplay" ]
aliases = [ "/questions/29743" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using tcprewrite seed only with source IP](/questions/29743/using-tcprewrite-seed-only-with-source-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29743-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I use tcprewrite command to randomize the IPs of different pcaps:</p><p>tcprewrite --seed=$RANDOM --infile=a.pcap --outfile=B.pcap</p><p>This changes IPs of both source of destination. Is there anyway I can limit this change to source IPs or destination IPs alone and not both?</p></div><div id="question-tags" class="tags-container tags">tcprewrite tcpdump tcpreplay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '14, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/7de50997071624d6dc5a409a0386b2ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorolia&#39;s gravatar image" /><p>rorolia<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorolia has no accepted answers">0%</span></p></div></div><div id="comments-container-29743" class="comments-container"></div><div id="comment-tools-29743" class="comment-tools"></div><div class="clear"></div><div id="comment-29743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29744"></span>

<div id="answer-container-29744" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29744-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it is possible. Also, the source address in one packet is the destination address in the answer packet, so keeping only half and replacing the other doesn't make any sense I think.</p><p>If you're not bound to Linux tools and need more control over your replacements check out <a href="http://www.tracewrangler.com">TraceWrangler</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 02:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29744" class="comments-container"><span id="29745"></span><div id="comment-29745" class="comment"><div id="post-29745-score" class="comment-score"></div><div class="comment-text"><p>And of course tcprewrite isn't part of the Wireshark suite so you may got more focused help over at the help specifically for that application.</p></div><div id="comment-29745-info" class="comment-info"><span class="comment-age">(12 Feb '14, 02:04)</span> grahamb ♦</div></div><span id="29747"></span><div id="comment-29747" class="comment"><div id="post-29747-score" class="comment-score"></div><div class="comment-text"><p>The problem of source IP becoming dest IP can be solved if rewrite is occurring only on src IPs in case of request packets and dest ip in case of response packet</p></div><div id="comment-29747-info" class="comment-info"><span class="comment-age">(12 Feb '14, 02:07)</span> rorolia</div></div><span id="29749"></span><div id="comment-29749" class="comment"><div id="post-29749-score" class="comment-score"></div><div class="comment-text"><p>In the case of UDP (and other protocols), how do you identify what is a request and what is a response packet, who is 'client' and who is 'server', as there is no session establishment protocol like TCP 3-way handshake??</p></div><div id="comment-29749-info" class="comment-info"><span class="comment-age">(12 Feb '14, 02:21)</span> Kurt Knochner ♦</div></div><span id="29750"></span><div id="comment-29750" class="comment"><div id="post-29750-score" class="comment-score"></div><div class="comment-text"><p>As long as you know the subenets in your capture file, you could use --pnat instead of --seed</p><pre><code>Changing Networks via Pseudo-NAT, Source/Destination IP Map

Pseudo-NAT works very much like network address translation. It allows you to map IP addresses in one subnet to IP addresses in another subnet. Each source and destination subnet is expressed in CIDR notation, and needn&#39;t be the same size. You can specify multiple CIDR pairs and use the --pnat flag twice if you use a cache file. The format is: &lt;match_cidr&gt;:&lt;rewrite_cidr&gt;,...

    $ tcprewrite --pnat=10.0.0.0/8:172.16.0.0/12,192.168.0.0/16:172.16.0.0/12 --infile=input.pcap --outfile=output.pcap --skipbroadcast

would rewrite any IP in either 10.0.0.0/8 or 192.168.0.0/16 to be in the 172.16.0.0/12 subnet. You could also rewrite IP&#39;s differently depending on the direction of the packet:

    $ tcprewrite --pnat=10.0.0.0/8:192.168.0.0/24 --pnat=10.0.0.0/8:192.168.1.0/24 --cachefile=input.cache --infile=input.pcap --outfile=output.pcap --skipbroadcast

Would cause traffic in 10.0.0.0/8 to be remapped to different subnets depending on the classification of the node as client or server. The result is that both source and destination IP&#39;s will be remapped properly to maintain the session.

Alternatively to the --pnat option you can use --srcipmap and/or --dstipmap to apply different rules to the source and destination IP addresses in packets. --srcipmap and --dstipmap work just like --pnat and use the same &lt;match_cidr&gt;:&lt;rewrite_cidr&gt;,... format. </code></pre></div><div id="comment-29750-info" class="comment-info"><span class="comment-age">(12 Feb '14, 02:21)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29744" class="comment-tools"></div><div class="clear"></div><div id="comment-29744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29753"></span>

<div id="answer-container-29753" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29753-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I am not sure if this is what you want. I used to change source IP to something else or destination IP to something else. And, this is how I am doing it.</p><hr /><p>tcprewrite --srcipmap=a.a.a.a/32:c.c.c.c/32 --infile=file1.pcap --outfile=file1_temp.pcap<br />
tcprewrite --srcipmap=b.b.b.b/32:d.d.d.d/32 --infile=file1_temp.pcap --outfile=file1_new.pcap</p><p>request:<br />
a.a.a.a(src),b.b.b.b(dst) -&gt; c.c.c.c(src),b.b.b.b(dst)<br />
response:<br />
b.b.b.b(src),a.a.a.a(dst) -&gt; d.d.d.d(src),a.a.a.a(dst)<br />
<br />
</p><hr /><p>tcprewrite --dstipmap=a.a.a.a/32:d.d.d.d/32 --infile=file2.pcap --outfile=file2_temp.pcap<br />
tcprewrite --dstipmap=b.b.b.b/32:c.c.c.c/32 --infile=file2_temp.pcap --outfile=file2_new.pcap</p><p>request:<br />
a.a.a.a(src),b.b.b.b(dst) -&gt; a.a.a.a(src),c.c.c.c(dst)<br />
response:<br />
b.b.b.b(src),a.a.a.a(dst) -&gt; b.b.b.b(src),d.d.d.d(dst)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/c1ab41a3eb718abcabc86051c1bcd165?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hunghoong&#39;s gravatar image" /><p>hunghoong<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hunghoong has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-29753" class="comments-container"></div><div id="comment-tools-29753" class="comment-tools"></div><div class="clear"></div><div id="comment-29753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

