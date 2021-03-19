+++
type = "question"
title = "Capture Filter for Arp poisoning"
description = '''Can you create a capture filter where you specify the packet offset and value of the gateway&#x27;s ip address and then have a not value for the packet offset and value of the gateway&#x27;s mac address. In this way the only packet&#x27;s captured would be the poisoner&#x27;s mac address. I can certainly create one as ...'''
date = "2012-05-10T10:03:00Z"
lastmod = "2012-05-10T11:24:00Z"
weight = 10901
keywords = [ "arp" ]
aliases = [ "/questions/10901" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter for Arp poisoning](/questions/10901/capture-filter-for-arp-poisoning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10901-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can you create a capture filter where you specify the packet offset and value of the gateway's ip address and then have a not value for the packet offset and value of the gateway's mac address. In this way the only packet's captured would be the poisoner's mac address.</p><p>I can certainly create one as a post filter:</p><p>arp.src.proto_ipv4 == xxx.xxx.xxx.xxx &amp;&amp; !arp.src.hw_mac == xx:xx:xx:xx:xx:xx</p><p>Filtering in the capture would be far more efficient.</p><p>Thanks</p><p>Victor</p></div><div id="question-tags" class="tags-container tags">arp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '12, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/33ac0ea40fe77b58643888b0d78424e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VictorD&#39;s gravatar image" /><p>VictorD<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VictorD has no accepted answers">0%</span></p></div></div><div id="comments-container-10901" class="comments-container"></div><div id="comment-tools-10901" class="comment-tools"></div><div class="clear"></div><div id="comment-10901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10902"></span>

<div id="answer-container-10902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10902-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use</p><pre><code>arp and ether[28:4]=0xc0a83001 and not (ether[22:2]=0x000c and ether[24:4]=0x29caffee)</code></pre><p>ether[28:4] must specify the hexadecimal notation of your arp.src.proto_ipv4 address</p><p>ether[22:2]=0x000c and ether[24:4]=0x29caffee are representing your arp.src.hw_mac split up into the first 2 bytes and the last 4 bytes. I don't know why, but the ether[xx:length] command does not seem to accept other "length" values for the number of following bytes other than 1,2 or 4. If someone has an idea why that is or what I'm missing, please feel free to add more information about that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-10902" class="comments-container"><span id="10903"></span><div id="comment-10903" class="comment"><div id="post-10903-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I'll try that.</p></div><div id="comment-10903-info" class="comment-info"><span class="comment-age">(10 May '12, 12:24)</span> VictorD</div></div><span id="10905"></span><div id="comment-10905" class="comment"><div id="post-10905-score" class="comment-score">1</div><div class="comment-text"><p>You can only use 1, 2 or 4 because the BPF virtual machine only knows how to handle bytes, 16 bit words and 32 bit words. The parser to compile your capture filter into BPF machine code is not enhanced to split "ether[22:6]" into bytes, 16 bit words or 32 bit words, so you need to do that manually.</p></div><div id="comment-10905-info" class="comment-info"><span class="comment-age">(10 May '12, 15:32)</span> SYN-bit ♦♦</div></div><span id="10906"></span><div id="comment-10906" class="comment"><div id="post-10906-score" class="comment-score"></div><div class="comment-text"><p>Here is the resulting machine code on 1, 2 or 4 byte comparisons:</p><pre><code>[email protected]:~$ sudo tcpdump -d &quot;ether[24:1]=0x11&quot;
(000) ldb      [24]
(001) jeq      #0x11            jt 2    jf 3
(002) ret      #65535
(003) ret      #0
[email protected]:~$ sudo tcpdump -d &quot;ether[24:2]=0x1122&quot;
(000) ldh      [24]
(001) jeq      #0x1122          jt 2    jf 3
(002) ret      #65535
(003) ret      #0
[email protected]:~$ sudo tcpdump -d &quot;ether[24:4]=0x11223344&quot;
(000) ld       [24]
(001) jeq      #0x11223344      jt 2    jf 3
(002) ret      #65535
(003) ret      #0
[email protected]:~$</code></pre><p>As you can see, the BPF virtual machine has separate instructions to fetch a 1, 2 or 4 byte value from the packet.</p></div><div id="comment-10906-info" class="comment-info"><span class="comment-age">(10 May '12, 15:33)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-10902" class="comment-tools"></div><div class="clear"></div><div id="comment-10902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

