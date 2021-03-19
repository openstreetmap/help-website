+++
type = "question"
title = "Https dumpcap decryption"
description = '''Hi, Ive recently had a dumpcap file created using my usual standard way and realised that the capture has https packets within it. Is there any way i can get to see what information is in here. Ive read up a bit on it and they advise that you need the public key from the location your wanting inform...'''
date = "2017-04-02T13:27:00Z"
lastmod = "2017-04-02T23:18:00Z"
weight = 60528
keywords = [ "https" ]
aliases = [ "/questions/60528" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Https dumpcap decryption](/questions/60528/https-dumpcap-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60528-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Ive recently had a dumpcap file created using my usual standard way and realised that the capture has https packets within it. Is there any way i can get to see what information is in here. Ive read up a bit on it and they advise that you need the public key from the location your wanting information and the private key from the device. Unfortunatly theae are wireless captures, is there anything that can be done to read this old capture? Many thanks</p></div><div id="question-tags" class="tags-container tags">https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '17, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/02ee5258c47902d7e590a0eea45d5d0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msriptide&#39;s gravatar image" /><p>msriptide<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msriptide has no accepted answers">0%</span></p></div></div><div id="comments-container-60528" class="comments-container"></div><div id="comment-tools-60528" class="comment-tools"></div><div class="clear"></div><div id="comment-60528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60535"></span>

<div id="answer-container-60535" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60535-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is the specific intention of these methods that you can't do that, so no, there's nothing practical that can be done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '17, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60535" class="comments-container"><span id="60537"></span><div id="comment-60537" class="comment"><div id="post-60537-score" class="comment-score"></div><div class="comment-text"><p>Ah, ok. Then is there any idiots guides to setting it up so i can get these during live capture. Ive seen some about setting up ssl within preferences to log some info. Just to give a bit of extra information, im running this on a ubuntu linux setup using wireless monitor mode. Ive seen one where you can set womething up if using a static cqpture under windows but i couldnt find anything moe</p></div><div id="comment-60537-info" class="comment-info"><span class="comment-age">(02 Apr '17, 23:53)</span> msriptide</div></div><span id="60542"></span><div id="comment-60542" class="comment"><div id="post-60542-score" class="comment-score"></div><div class="comment-text"><p>Some links:</p><p><a href="https://wiki.wireshark.org/SSL">https://wiki.wireshark.org/SSL</a></p><p><a href="https://support.citrix.com/article/CTX116557">https://support.citrix.com/article/CTX116557</a></p><p><a href="https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/">https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/</a></p><p><a href="http://packetpushers.net/using-wireshark-to-decode-ssltls-packets/">http://packetpushers.net/using-wireshark-to-decode-ssltls-packets/</a></p><p><a href="https://www.trustwave.com/Resources/SpiderLabs-Blog/Intercepting-SSL-And-HTTPS-Traffic-With-mitmproxy-and-SSLsplit/">https://www.trustwave.com/Resources/SpiderLabs-Blog/Intercepting-SSL-And-HTTPS-Traffic-With-mitmproxy-and-SSLsplit/</a></p><p>I am not sure if you discovered issues with both WPA2 decryption and then applying TLS decryption. I would expect it should work but have not tested it. If there are issues, there are some other techniques that could be used to massage the raw data into a form that might work. See,for instance,</p><p><a href="https://www.aircrack-ng.org/doku.php?id=airdecap-ng">https://www.aircrack-ng.org/doku.php?id=airdecap-ng</a></p></div><div id="comment-60542-info" class="comment-info"><span class="comment-age">(03 Apr '17, 03:57)</span> Bob Jones</div></div><span id="60593"></span><div id="comment-60593" class="comment"><div id="post-60593-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for replying, i've only just realised there was an answer here. I've read most of the information that i can find and i don't think im going to be able to sort that out. i've abandoned the old captures and just wanted to concentrate on any new ones. I've had no problems with the captures i've been getting but i've realised that recently there are alot of packets that have just the one information for a website and then stop. i've realised that this is because those sites are Https. because im capturing in wireless monitor mode to get everything going in and out of the network i don't knwo if there is any way for me to get any of the keys needed, and i really think im stuck for getting anything to decrypt. Do you know of any way i could sort this. i really don't want to resort to man in the middle. many thanks</p></div><div id="comment-60593-info" class="comment-info"><span class="comment-age">(05 Apr '17, 11:34)</span> msriptide</div></div><span id="60617"></span><div id="comment-60617" class="comment"><div id="post-60617-score" class="comment-score"></div><div class="comment-text"><p>Oh and as a side note i dont really want to do a mitmproxy link as i don't have my computer on all the time (its a laptop) so cant set it as a proxy on the mobile device as it wont be able to connect. Any help would be appreciated.</p></div><div id="comment-60617-info" class="comment-info"><span class="comment-age">(06 Apr '17, 09:22)</span> msriptide</div></div><span id="60620"></span><div id="comment-60620" class="comment"><div id="post-60620-score" class="comment-score"></div><div class="comment-text"><p>@msriptide</p><p>Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-60620-info" class="comment-info"><span class="comment-age">(06 Apr '17, 09:38)</span> grahamb ♦</div></div></div><div id="comment-tools-60535" class="comment-tools"></div><div class="clear"></div><div id="comment-60535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

