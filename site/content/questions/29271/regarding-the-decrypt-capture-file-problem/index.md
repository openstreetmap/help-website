+++
type = "question"
title = "Regarding the Decrypt Capture File Problem"
description = '''Hello Everybody, I captured some ICMP of 802.11 packets via the AirPcap, and I want to decode and display it from 802.11 to ICMP. I trial this method(http://wiki.wireshark.org/HowToDecrypt802.11), and go to generate Raw PSK(http://www.wireshark.org/tools/wpa-psk.html), put it into Edit -&amp;gt; Prefere...'''
date = "2014-01-29T08:29:00Z"
lastmod = "2014-01-29T11:15:00Z"
weight = 29271
keywords = [ "decrypt" ]
aliases = [ "/questions/29271" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Regarding the Decrypt Capture File Problem](/questions/29271/regarding-the-decrypt-capture-file-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29271-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Everybody,</p><p>I captured some ICMP of 802.11 packets via the AirPcap, and I want to decode and display it from 802.11 to ICMP. I trial this method(<a href="http://wiki.wireshark.org/HowToDecrypt802.11),">http://wiki.wireshark.org/HowToDecrypt802.11),</a> and go to generate Raw PSK(<a href="http://www.wireshark.org/tools/wpa-psk.html),">http://www.wireshark.org/tools/wpa-psk.html),</a> put it into Edit -&gt; Preferences -&gt; Protocol -&gt; IEEE 802.11. But the content still do not change. I also referenced this blog(<a href="http://www.lovemytool.com/blog/2010/05/wireshark-and-tshark-decrypt-sample-capture-file-by-joke-snelders.html#comment-6a00e008d95770883401a5115e361a970c),">http://www.lovemytool.com/blog/2010/05/wireshark-and-tshark-decrypt-sample-capture-file-by-joke-snelders.html#comment-6a00e008d95770883401a5115e361a970c),</a> but the outcome is the same.</p><p>The pcap file download like of Dropbox: <a href="https://dl.dropboxusercontent.com/u/9338839/Capture%20ICMP%20data.pcap">https://dl.dropboxusercontent.com/u/9338839/Capture%20ICMP%20data.pcap</a></p><p>Does someone can give me some advice to solve this problem? Thanks so much!</p></div><div id="question-tags" class="tags-container tags">decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '14, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/898bce1386a92ad2648d3d2265accdea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eric%20HT&#39;s gravatar image" /><p>Eric HT<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eric HT has no accepted answers">0%</span></p></div></div><div id="comments-container-29271" class="comments-container"><span id="29276"></span><div id="comment-29276" class="comment"><div id="post-29276-score" class="comment-score"></div><div class="comment-text"><p>What is the key (WPA password)? Without the key, nobody will be able to check your capture file.</p></div><div id="comment-29276-info" class="comment-info"><span class="comment-age">(29 Jan '14, 10:14)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29271" class="comment-tools"></div><div class="clear"></div><div id="comment-29271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29278"></span>

<div id="answer-container-29278" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29278-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>O.K. in the meantime I checked the capture file (dropbox). That capture file does not contain the EAPOL frames needed to be able to decrypt the traffic.</p><p>From: <a href="http://wiki.wireshark.org/HowToDecrypt802.11">http://wiki.wireshark.org/HowToDecrypt802.11</a></p><pre><code>WPA and WPA2 use keys derived from an EAPOL handshake to encrypt traffic. Unless all four handshake packets are present for the session you&#39;re trying to decrypt, Wireshark won&#39;t be able to decrypt the traffic. You can use the display filter eapol to locate EAPOL packets in your capture. </code></pre><p>So, you need to start your traffic capture 'earlier', to include the EAPOL frames.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '14, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '14, 11:16</p></div></div><div id="comments-container-29278" class="comments-container"></div><div id="comment-tools-29278" class="comment-tools"></div><div class="clear"></div><div id="comment-29278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

