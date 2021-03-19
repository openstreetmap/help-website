+++
type = "question"
title = "Remove duplicate packets by data."
description = '''I am analyzing UDP traffic from one of the server. It is sending me multiple UDP packets with the same data. The only thing which is changing is &quot;Time to leave&quot; in IP layer. it is starting with 116 and then I get multiple UDP packets each with decrementing &quot;Time to leave&quot;. ( up to 1 ) First of all I...'''
date = "2015-11-13T13:06:00Z"
lastmod = "2015-11-14T10:57:00Z"
weight = 47583
keywords = [ "udp", "wireshark", "ttl" ]
aliases = [ "/questions/47583" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Remove duplicate packets by data.](/questions/47583/remove-duplicate-packets-by-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47583-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analyzing UDP traffic from one of the server.</p><p>It is sending me multiple UDP packets with the same data.</p><p>The only thing which is changing is "Time to leave" in IP layer. it is starting with 116 and then I get multiple UDP packets each with decrementing "Time to leave". ( up to 1 )</p><p>First of all I do not understand why I am receiving multiple packets.</p><p>Second, how can I tell wireshark to skip all other (similar) UDP packets and keep only one ( since data is same )?</p><p>I tried "editcap -d" without any luck.</p><p>EDIT 1:</p><p>I am trying to analyze the traffic between my console and game server. I do not know how server is configured.</p><p>MY setup looks like below:</p><pre><code>My console is connected to pc via ethernet cable ( Local Area Connection ).
My pc is connected to wifi router for internet connection ( Wireless Network Connection ).
I am sharing my internet connection with LAN via WNC.
Wireshark is listening on LAN.</code></pre><p>pcap file can be found at: <a href="http://wikisend.com/download/687476/test.pcapng">here</a></p></div><div id="question-tags" class="tags-container tags">udp wireshark ttl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '15, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/680a67b778d97fec10098354f9405fe8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashitpro&#39;s gravatar image" /><p>ashitpro<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashitpro has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Nov '15, 15:33</p></div></div><div id="comments-container-47583" class="comments-container"><span id="47598"></span><div id="comment-47598" class="comment"><div id="post-47598-score" class="comment-score"></div><div class="comment-text"><p>With "windows 7 professional" OS - i am facing same problem ?</p></div><div id="comment-47598-info" class="comment-info"><span class="comment-age">(14 Nov '15, 00:35)</span> srinu_bel</div></div></div><div id="comment-tools-47583" class="comment-tools"></div><div class="clear"></div><div id="comment-47583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="47608"></span>

<div id="answer-container-47608" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47608-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>As the TTLs of the packets towards the PS4 are decrementetd - for whaterver reason - the TTL (Time to live - not Time To Leave) will also be 64 once as they are sent. TTL 64 is also the TTL for packets that are received from the console.</p><p>So you can skip all those duplicates using</p><p>udp.stream==0 and ip.ttl==64</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_089.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '15, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-47608" class="comments-container"></div><div id="comment-tools-47608" class="comment-tools"></div><div class="clear"></div><div id="comment-47608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47584"></span>

<div id="answer-container-47584" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47584-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would assume that there is a routing loop somewhere. The TTL is decremented with each pass of a packet through a router. Are they decrementing by one (so you get each packet 115 times) or faster?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '15, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-47584" class="comments-container"><span id="47586"></span><div id="comment-47586" class="comment"><div id="post-47586-score" class="comment-score"></div><div class="comment-text"><p>Decrementing by 1. Hence I receive 115 packets.</p></div><div id="comment-47586-info" class="comment-info"><span class="comment-age">(13 Nov '15, 13:23)</span> ashitpro</div></div><span id="47588"></span><div id="comment-47588" class="comment"><div id="post-47588-score" class="comment-score"></div><div class="comment-text"><p>Please provide some details regarding your network. Is the machine where you capture connected directly to the server, do you have just a single network card on the machine where you take the capture, do you have some capture/display filters set? What are the IP address and routing settings on the server and the machine where you take the capture And can you post the capture somewhere and provide a link?</p></div><div id="comment-47588-info" class="comment-info"><span class="comment-age">(13 Nov '15, 13:36)</span> sindy</div></div><span id="47592"></span><div id="comment-47592" class="comment"><div id="post-47592-score" class="comment-score"></div><div class="comment-text"><p>I have added more information about my setup in question. Hope that helps.</p></div><div id="comment-47592-info" class="comment-info"><span class="comment-age">(13 Nov '15, 15:34)</span> ashitpro</div></div><span id="47599"></span><div id="comment-47599" class="comment"><div id="post-47599-score" class="comment-score"></div><div class="comment-text"><p>OK. Please take &amp; post another capture, this time on both the LAN and the WNC (if you are using Wireshark to capture, simply tick both interfaces before starting to capture, the result will be a pcapng file). Something is terribly wrong somewhere, the question now is where exactly. A capture at both interfaces should show whether your PC multiplicates the packets or whether they come that way from outside (and waste your connection bandwidth).</p><p>The use of term "connection sharing" typically suggests that you use Microsoft Windows and that the PC acts as a router with NAT; however, 192.168.137.0/24 is not typical for such setup. So what is the OS on your PC? The "connection sharing" setup should be deducible from the capture at both interfaces.</p></div><div id="comment-47599-info" class="comment-info"><span class="comment-age">(14 Nov '15, 00:41)</span> sindy</div></div></div><div id="comment-tools-47584" class="comment-tools"></div><div class="clear"></div><div id="comment-47584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47594"></span>

<div id="answer-container-47594" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47594-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to take a look at this years Sharkfest presentation by Robert Bullen regarding his deduping tool "Super Deduper". It contains a download link on slide 15.</p><p><a href="https://sharkfest.wireshark.org/assets/presentations15/18.pptx">https://sharkfest.wireshark.org/assets/presentations15/18.pptx</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '15, 17:04</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-47594" class="comments-container"></div><div id="comment-tools-47594" class="comment-tools"></div><div class="clear"></div><div id="comment-47594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

