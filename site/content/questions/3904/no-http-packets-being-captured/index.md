+++
type = "question"
title = "no HTTP packets being captured"
description = '''hello,  i use WS to capture the packtes from and to my IP-Camera Sony RZ-50 but Wireshark  dont shows HTTP Packets in the Capture file. i dont have a Capture Filter running and  i use the newest stable version 1.4.6 thanx in advance Michael '''
date = "2011-05-03T13:06:00Z"
lastmod = "2011-05-08T21:23:00Z"
weight = 3904
keywords = [ "http" ]
aliases = [ "/questions/3904" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [no HTTP packets being captured](/questions/3904/no-http-packets-being-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3904-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, i use WS to capture the packtes from and to my IP-Camera Sony RZ-50 but Wireshark dont shows HTTP Packets in the Capture file. i dont have a Capture Filter running and i use the newest stable version 1.4.6</p><p>thanx in advance Michael</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '11, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/baada888dc89f73d863e1da94b0bec0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haylebob&#39;s gravatar image" /><p>haylebob<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haylebob has no accepted answers">0%</span></p></div></div><div id="comments-container-3904" class="comments-container"><span id="3905"></span><div id="comment-3905" class="comment"><div id="post-3905-score" class="comment-score"></div><div class="comment-text"><p>Can you provide some more details (like the network interface used and how you're creating traffic)? If you don't see http in the capture, what traffic do you see?</p></div><div id="comment-3905-info" class="comment-info"><span class="comment-age">(03 May '11, 18:00)</span> helloworld</div></div><span id="3973"></span><div id="comment-3973" class="comment"><div id="post-3973-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>thank u for ur answer. the network interface is Realtek 10/100/1000 Ethenet NIC and i only get TCP Traffic Packages in the capture. I creating traffic by open my Brower FF 4.01 or IE8 for example and accessing my IP-Cam Sony RZ50 for checking what is tranferred to and from the Camera.</p><p>best regards Michael</p></div><div id="comment-3973-info" class="comment-info"><span class="comment-age">(06 May '11, 00:36)</span> haylebob</div></div></div><div id="comment-tools-3904" class="comment-tools"></div><div class="clear"></div><div id="comment-3904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3982"></span>

<div id="answer-container-3982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3982-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might actually be using HTTPS, in which case the traffic is encrypted and would not show as HTTP. You can setup Wireshark with the keys to decrypt the traffic, but it might require recompiling Wireshark for SSL decryption support. See the <a href="http://wiki.wireshark.org/SSL">Wireshark wiki</a> for more on this.</p><p>If you're on Windows and interested only in HTTP(S) capturing, you should consider using <a href="http://www.fiddler2.com/fiddler/help/httpsdecryption.asp">Fiddler</a> instead because it has better support for decrypting HTTPS.</p><p><strong>EDIT:</strong> Ok, so you're not using HTTPS. Then you should at least see HTTP in your packet capture when you "login" to the Welcome Page of the network camera (can you confirm?). As a sanity check, I would also confirm that you're really monitoring the correct network interface (in case you have multiple interfaces available).</p><p>Based on the <a href="http://pro.sony.com/bbsc/ssr/product-SNCRZ50N/">user manual of the RZ50N</a>, a Sony-proprietary ActiveX Control (IE Plugin) is installed to monitor/control the camera. This plugin probably uses some protocol on top of TCP (other than HTTP) for that. So, you might only see a few HTTP packets from your intitial "login" (there's actually no username/password prompt at the Welcome Page), followed by something else when the plugin takes over.</p><p>If you provide a sample packet capture (starting from initial login), we could help you some more.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '11, 21:18</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 May '11, 15:55</p></div></div><div id="comments-container-3982" class="comments-container"></div><div id="comment-tools-3982" class="comment-tools"></div><div class="clear"></div><div id="comment-3982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4012"></span>

<div id="answer-container-4012" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4012-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>hello,</p><p>thank you for tha answer. i dont using HTTPS or SSL decrpytion here.</p><p>best regards Michael</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '11, 21:23</strong></p><img src="https://secure.gravatar.com/avatar/baada888dc89f73d863e1da94b0bec0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="haylebob&#39;s gravatar image" /><p>haylebob<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="haylebob has no accepted answers">0%</span></p></div></div><div id="comments-container-4012" class="comments-container"></div><div id="comment-tools-4012" class="comment-tools"></div><div class="clear"></div><div id="comment-4012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

