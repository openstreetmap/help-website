+++
type = "question"
title = "Passive OS identification"
description = '''hi.If we want to identify a computer&#x27;s OS, A simple but effective passive method is to inspect  Initial TTL (8 bits) Window size (16 bits) Max segment size (16 bits) Window scaling value (8 bits) don&#x27;t fragment flag (1 bit) sackOK flag (1 bit) nopflag (1 bit)  Below are some typical initial TTL valu...'''
date = "2017-06-22T08:52:00Z"
lastmod = "2017-06-22T11:00:00Z"
weight = 62238
keywords = [ "fingerprint" ]
aliases = [ "/questions/62238" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Passive OS identification](/questions/62238/passive-os-identification)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62238-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi.If we want to identify a computer's OS, A simple but effective passive method is to inspect</p><pre><code>Initial TTL (8 bits)
Window size (16 bits)
Max segment size (16 bits)
Window scaling value (8 bits)
don&#39;t fragment flag (1 bit)
sackOK flag (1 bit)
nopflag (1 bit)</code></pre><p>Below are some typical initial TTL values and window sizes of common operating systems:</p><pre><code>Linux (kernel 2.4 and 2.6)  64  5840
Google&#39;s customized Linux   64  5720
FreeBSD 64  65535
Windows XP  128 65535
Windows 7, Vista and Server 2008    128 8192
Cisco Router (IOS 12.4) 255 4128</code></pre><p>can any one help me to find other parameters(Max segment size,don't fragment flag,...) for these common operating systems? can <code>TTL values and window sizes</code> get initial by different values mention here?</p></div><div id="question-tags" class="tags-container tags">fingerprint</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '17, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p>ghader<br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div></div><div id="comments-container-62238" class="comments-container"></div><div id="comment-tools-62238" class="comment-tools"></div><div class="clear"></div><div id="comment-62238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62243"></span>

<div id="answer-container-62243" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62243-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at the open-source nmap tool. Its OS fingerprint database covers 2600+ fingerprints.</p><p>If all you want is "something that does fingerprinting", nmap is pretty solid.</p><p>If, however, you want to dig into the actual mechanics of OS fingerprints, you can look at nmap's database without installing the tool.</p><p>Raw fingerprint data here -&gt; <a href="https://svn.nmap.org/nmap/nmap-os-db">https://svn.nmap.org/nmap/nmap-os-db</a></p><p>Explanation of nmap-os-db fingerprint format -&gt; <a href="https://nmap.org/book/osdetect-fingerprint-format.html">https://nmap.org/book/osdetect-fingerprint-format.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '17, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-62243" class="comments-container"></div><div id="comment-tools-62243" class="comment-tools"></div><div class="clear"></div><div id="comment-62243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

