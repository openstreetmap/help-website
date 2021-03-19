+++
type = "question"
title = "DNS leak: Looking up own hostname with DNS queries"
description = '''I was checking a proxied program for DNS leaks with tshark when I noticed this: 13.170066 10.0.2.15 -&amp;gt; 192.168.1.1 DNS 66 Standard query 0xd473 A [hostname] 13.753496 10.0.2.15 -&amp;gt; 192.168.1.1 DNS 66 Standard query 0x7bb4 A [hostname]  where [hostname] is the hostname of the machine the program...'''
date = "2013-02-09T10:13:00Z"
lastmod = "2013-02-09T11:53:00Z"
weight = 18469
keywords = [ "dns", "hostname", "tshark", "analysis", "wireshark" ]
aliases = [ "/questions/18469" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DNS leak: Looking up own hostname with DNS queries](/questions/18469/dns-leak-looking-up-own-hostname-with-dns-queries)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18469-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I was checking a proxied program for DNS leaks with tshark when I noticed this:</p><pre><code>13.170066    10.0.2.15 -&gt; 192.168.1.1  DNS 66 Standard query 0xd473  A [hostname]
13.753496    10.0.2.15 -&gt; 192.168.1.1  DNS 66 Standard query 0x7bb4  A [hostname]</code></pre><p>where [hostname] is the hostname of the machine the program and tshark are running on, 10.0.2.15 is the local machine, and 192.168.1.1 is the router.</p><p>Why does the computer look up its own hostname and how can I prevent this from leaking information about the computer?</p><p>Note that changing the hostname once is not useful since an (untrusted) proxy knows that it is the same computer connecting every time since the computer sends the same hostname.</p></div><div id="question-tags" class="tags-container tags">dns hostname tshark analysis wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '13, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/602bb755b4fbab9ae9239173076996ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Navin&#39;s gravatar image" /><p>Navin<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Navin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Feb '13, 10:14</p></div></div><div id="comments-container-18469" class="comments-container"></div><div id="comment-tools-18469" class="comment-tools"></div><div class="clear"></div><div id="comment-18469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18470"></span>

<div id="answer-container-18470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18470-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hard to say; you'd probably have to find out what program/service does this.</p><p>One explanation could be that you've turned on the network name resolution feature in the profile you're using, which will lead to tshark/Wireshark contacting the DNS server to find out FQDNs of IP addresses. Did you check if you can also see PTR record queries? Wireshark seems to do a A record query after a successfull PTR answer was received to verify if the information works both ways.</p><p>Depending on your OS you could try to find the program using a socket to connect to the DNS server, maybe using a tool like process monitor from Sysinternals. I tried it just now, and if you only let it show network activity and have Wireshark/tshark running at the same you can match port numbers to find the process that triggered the query. netstat might work too, but I doubt that the UDP port will be listed there long enough to get a good reading.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '13, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-18470" class="comments-container"></div><div id="comment-tools-18470" class="comment-tools"></div><div class="clear"></div><div id="comment-18470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

