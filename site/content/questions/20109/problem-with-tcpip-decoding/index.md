+++
type = "question"
title = "problem with tcp/ip decoding"
description = '''Hi, I noticed this question as &quot;problem with tcp/ip decoding&quot;, but may be dog is buried elsewhere. I have a streams with asterix radar data. For reading I am using wireshark 1.0.7 with built-in asterix plugin. The decoding gives nothing readable. I have testing streams and the asterix plugin works p...'''
date = "2013-04-05T04:38:00Z"
lastmod = "2013-04-05T04:54:00Z"
weight = 20109
keywords = [ "asterix", "tc" ]
aliases = [ "/questions/20109" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [problem with tcp/ip decoding](/questions/20109/problem-with-tcpip-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20109-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I noticed this question as "problem with tcp/ip decoding", but may be dog is buried elsewhere. I have a streams with asterix radar data. For reading I am using wireshark 1.0.7 with built-in asterix plugin. The decoding gives nothing readable. I have testing streams and the asterix plugin works perfectly for them. What I noticed that in my streams wireshark properly recognize the the TCP and IP header's lengths as 20 bytes but correspondence numbers in the header are wrong:</p><pre><code>0000    2c d4 44 8f 44 58 2c d4    44 8f 43 d3 08 00 ***45*** 00
0010    00 4a 65 f5 40 00 80 06    7e b0 0a 01 01 03 0a 01
0020    01 04 0b b9 c4 fd 14 fc    a9 61 63 ca c3 d2 ***50*** 18
0030    f8 8f a6 67 00 00 01 04    30 00 20 f9 17 09 20 84
0040    02 5f 7c 96 21 00 38 20    83 d0 00 00 00 04 0a 5c
0050    30 15 21 00 03 13 00 00</code></pre><p>Data bloc starts with the right bye number but asterix cannot recognize that. If somebody has idea please help me manage with this.</p><p>p.p If needed some more information I'm ready to give it.</p></div><div id="question-tags" class="tags-container tags">asterix tc</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '13, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/051dc3913f843de628623a41312561ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="furna&#39;s gravatar image" /><p>furna<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="furna has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Apr '13, 05:48</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-20109" class="comments-container"></div><div id="comment-tools-20109" class="comment-tools"></div><div class="clear"></div><div id="comment-20109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20111"></span>

<div id="answer-container-20111" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20111-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am using wireshark 1.0.7 with built-in asterix plugin.</p></blockquote><p>I cannot find any <strong>asterix plugin</strong> (radar data format) in the standard Wireshark distribution, so I guess that plugin is something proprietary. If that is the case, it is best to answer the developer of that plugin for help.</p><p>There are sites with information about that plugin:</p><blockquote><p><code>http://www.recherche.enac.fr/asterix/doku.php?id=useren</code><br />
<code>http://code.google.com/p/asterixplugin/</code><br />
</p></blockquote><p>But again, that plugin is not part of the standard Wireshark distribution and any problem with the protocol dissection should be sent to the developers of that plugin.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '13, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Apr '13, 04:54</p></div></div><div id="comments-container-20111" class="comments-container"><span id="20112"></span><div id="comment-20112" class="comment"><div id="post-20112-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. Of course I'll try there as well. The French plugin is the exactly what I'm using. But could you comment the difference between the header's lengths. The bolded numbers are the corresponding bytes for IP (0x45) and TCP (0x50) header lengths. But in the Packet Detail Pane these lengths are properly recognized as 20 bytes. Is this a problem or everything is alright?</p></div><div id="comment-20112-info" class="comment-info"><span class="comment-age">(05 Apr '13, 05:21)</span> furna</div></div><span id="20114"></span><div id="comment-20114" class="comment"><div id="post-20114-score" class="comment-score"></div><div class="comment-text"><p>Yes it's alright: the length is a multiple of 32 bits words (see <a href="http://en.wikipedia.org/wiki/Ipv4">http://en.wikipedia.org/wiki/Ipv4</a> and <a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol).">http://en.wikipedia.org/wiki/Transmission_Control_Protocol).</a> According to the captures provided with this customized Wireshark 1.0.7 portable version, the plugin is designed to run on top of 802.3 and not TCP/IP. It does not seem to offer the ability to decode the TCP data payload as asterix.</p></div><div id="comment-20114-info" class="comment-info"><span class="comment-age">(05 Apr '13, 05:55)</span> Pascal Quantin</div></div><span id="20115"></span><div id="comment-20115" class="comment"><div id="post-20115-score" class="comment-score"></div><div class="comment-text"><p>Thank you!!!!</p></div><div id="comment-20115-info" class="comment-info"><span class="comment-age">(05 Apr '13, 05:58)</span> furna</div></div></div><div id="comment-tools-20111" class="comment-tools"></div><div class="clear"></div><div id="comment-20111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

