+++
type = "question"
title = "Why do I see this unknown mac address in the captured packets?"
description = '''I am on a wifi network. I am using a wifi adapter to connect to a wifi hotspot. In the captured packets, I see a lot of packets to and from an unknown mac address. If I search the mac address&#x27;s vendor I get no vendor.  628 114.574792 manufacturer_xx:xx:xx 1a:e1:3d:ca:4c:ac ARP 42 Who has 192.xxx.xxx...'''
date = "2017-08-30T03:39:00Z"
lastmod = "2017-08-30T04:13:00Z"
weight = 63538
keywords = [ "arp", "wifi" ]
aliases = [ "/questions/63538" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why do I see this unknown mac address in the captured packets?](/questions/63538/why-do-i-see-this-unknown-mac-address-in-the-captured-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63538-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am on a wifi network. I am using a wifi adapter to connect to a wifi hotspot. In the captured packets, I see a lot of packets to and from an unknown mac address. If I search the mac address's vendor I get no vendor.</p><pre><code>628 114.574792  manufacturer_xx:xx:xx   1a:e1:3d:ca:4c:ac   ARP 42  Who has 192.xxx.xxx.1? Tell 192.xxx.xxx.xxx
629 114.588296  1a:e1:3d:ca:4c:ac   manufacturer_xx:xx:xx   ARP 42  192.xxx.xxx.1 is at 1a:e1:3d:ca:4c:ac</code></pre><p>The manufacturer_xx:xx:xx is my wifi adapter. 192.xxx.xxx.1 is the default gateway ip and 192.xxx.xxx.xxx is the machine ip. The interesting fact is 1a:e1:3d:ca:4c:ac is not the mac of the default gateway. The unknown mac is communicating a lot with the network. I have a pcapng file of 29,206 packets. If I apply display filter, <code>eth.dst == 1a:e1:3d:ca:4c:ac</code>, I see around 40.1% packets went to the unknown mac.</p></div><div id="question-tags" class="tags-container tags">arp wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '17, 03:39</strong></p><img src="https://secure.gravatar.com/avatar/81ef234f880b10875f98621703282747?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mgtheboss&#39;s gravatar image" /><p>mgtheboss<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mgtheboss has no accepted answers">0%</span></p></div></div><div id="comments-container-63538" class="comments-container"></div><div id="comment-tools-63538" class="comment-tools"></div><div class="clear"></div><div id="comment-63538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63539"></span>

<div id="answer-container-63539" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63539-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That looks like a <a href="https://en.wikipedia.org/wiki/MAC_address#Universal_vs._local">locally administered</a> MAC, as the U/L bit is set (this is the second bit of the first octet, i.e. 1a -&gt; 0001 10<strong>1</strong>0). As such there is no manufacturer.</p><p>Wireshark should be informing you of the fact that the MAC list locally administered, what does it show in the packet tree? An example is show <a href="https://packetsdropped.wordpress.com/2011/01/13/mac-address-universally-or-locally-administered-bit-and-individualgroup-bit/">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '17, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '17, 04:15</p></div></div><div id="comments-container-63539" class="comments-container"></div><div id="comment-tools-63539" class="comment-tools"></div><div class="clear"></div><div id="comment-63539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

