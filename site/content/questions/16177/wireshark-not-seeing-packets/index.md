+++
type = "question"
title = "wireshark not seeing packets"
description = '''First off I only use wireless so when selecting the network card there is only one that has traffic on it (pretty sure Im not selecting the wrong one with such limited options). Next I will fill in a filter options (usually by port):  tcp.port == 23 Then I use the terminal (Mac 10.8) to open a telne...'''
date = "2012-11-21T12:40:00Z"
lastmod = "2012-11-27T11:12:00Z"
weight = 16177
keywords = [ "osx", "lion", "empty" ]
aliases = [ "/questions/16177" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark not seeing packets](/questions/16177/wireshark-not-seeing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16177-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First off I only use wireless so when selecting the network card there is only one that has traffic on it (pretty sure Im not selecting the wrong one with such limited options).<br />
Next I will fill in a filter options (usually by port):</p><p>tcp.port == 23</p><p>Then I use the terminal (Mac 10.8) to open a telnet session</p><p>But I see no traffic. If I turn off the filter I see traffic but no way to see (if they are there) my telnet traffic</p><p>This has to be a setting, I have had this working prior, and have similar problems when filtering for other traffic/ports.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_filter.png" alt="alt text" /></p><p>dumpcap:</p><blockquote><ol><li>en0 fe80::1240:f3ff:fe7f:d754,172.16.16.107 network</li><li>utun0 10.2.201.228 network</li><li>p2p0 network</li><li>en2 fe80::1240:f3ff:fe7f:d754 network</li><li>lo0 fe80::1,127.0.0.1,::1 loopback</li></ol></blockquote><p><strong>UPDATE</strong>: Just tried this on my windows box and it worked fine.<br />
</p><p>I was wrong and do still need this. I dont understand whats wrong, default install and not seeing but a few packet types.<br />
</p></div><div id="question-tags" class="tags-container tags">osx lion empty</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '12, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/2ba2bfbd35d331603015c215e893a32e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="owengerig&#39;s gravatar image" /><p>owengerig<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="owengerig has one accepted answer">100%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 27 Nov '12, 10:47</p></div></div><div id="comments-container-16177" class="comments-container"><span id="16178"></span><div id="comment-16178" class="comment"><div id="post-16178-score" class="comment-score"></div><div class="comment-text"><p>do you telnet your own machine (where wireshark is running) or a different one?</p></div><div id="comment-16178-info" class="comment-info"><span class="comment-age">(21 Nov '12, 12:47)</span> Kurt Knochner ♦</div></div><span id="16179"></span><div id="comment-16179" class="comment"><div id="post-16179-score" class="comment-score"></div><div class="comment-text"><p>telneting from my machine to another machine</p></div><div id="comment-16179-info" class="comment-info"><span class="comment-age">(21 Nov '12, 12:55)</span> owengerig</div></div><span id="16180"></span><div id="comment-16180" class="comment"><div id="post-16180-score" class="comment-score"></div><div class="comment-text"><p>if you ping the remote machine, do you see that in Wireshark?</p></div><div id="comment-16180-info" class="comment-info"><span class="comment-age">(21 Nov '12, 13:21)</span> Kurt Knochner ♦</div></div><span id="16275"></span><div id="comment-16275" class="comment"><div id="post-16275-score" class="comment-score"></div><div class="comment-text"><p>I dont think so but Im not sure how to filter ping traffic? I tried ip.addr == 127.0.0.1 with a continuous ping (to the 127 address) and NOTHING showed up.</p></div><div id="comment-16275-info" class="comment-info"><span class="comment-age">(25 Nov '12, 08:10)</span> owengerig</div></div><span id="16276"></span><div id="comment-16276" class="comment"><div id="post-16276-score" class="comment-score"></div><div class="comment-text"><p>if you ping localhost (127.0.0.1), you will only see that if you capture on the loopback interface (lo). At least on linux it works that way.</p><p>But why did you ping the localhost address and not the remote address??</p></div><div id="comment-16276-info" class="comment-info"><span class="comment-age">(25 Nov '12, 09:10)</span> Kurt Knochner ♦</div></div><span id="16318"></span><div id="comment-16318" class="comment not_top_scorer"><div id="post-16318-score" class="comment-score"></div><div class="comment-text"><p>i used the filter for the remote ip (ip.addr == 10.8.30.141) and did the continuous ping but did not see anything.</p></div><div id="comment-16318-info" class="comment-info"><span class="comment-age">(26 Nov '12, 07:05)</span> owengerig</div></div></div><div id="comment-tools-16177" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-16177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="16351"></span>

<div id="answer-container-16351" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16351-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I double clicked on the adapter en0</p><p>this brought up a menu I havnt seen before and it let me uncheck Monitor Mode (which changes Link-Layer header type from: 802.11 plus radiotap header to Ethernet)</p><p>after changing those options you have to click Start.</p><p>after that everything worked (saw my packets).</p><p>Here is why this is strange though. I went into preferences and made sure Monitor Mode was off and that ethernet was selected for the link-layer header type (even now its set to that). However when ever starting a new session with the Caption Options button it seems to enable Monitor Mode and other link-layer header type by default. So my settings were negated by using the Capture Options start method.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '12, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/2ba2bfbd35d331603015c215e893a32e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="owengerig&#39;s gravatar image" /><p>owengerig<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="owengerig has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Nov '12, 11:13</p></div></div><div id="comments-container-16351" class="comments-container"></div><div id="comment-tools-16351" class="comment-tools"></div><div class="clear"></div><div id="comment-16351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16201"></span>

<div id="answer-container-16201" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16201-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the capture options before you start your capture. Chances are that (based on the DISPLAY environment variable) a capture filter is set against your hosts traffic. Simply remove the capture filter and start the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '12, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16201" class="comments-container"><span id="16274"></span><div id="comment-16274" class="comment"><div id="post-16274-score" class="comment-score"></div><div class="comment-text"><p>I posted an image of my filters but still a little confused as to which one should be deleted? I have not added anything in here so these should be defaults. Which ones can/should I delete? Like I said these are defaults so I dont think I really need any of them?</p></div><div id="comment-16274-info" class="comment-info"><span class="comment-age">(25 Nov '12, 07:58)</span> owengerig</div></div><span id="16320"></span><div id="comment-16320" class="comment"><div id="post-16320-score" class="comment-score"></div><div class="comment-text"><p>I have since reinstalled wireshark and most of those are gone. still not working though</p></div><div id="comment-16320-info" class="comment-info"><span class="comment-age">(26 Nov '12, 07:12)</span> owengerig</div></div></div><div id="comment-tools-16201" class="comment-tools"></div><div class="clear"></div><div id="comment-16201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16325"></span>

<div id="answer-container-16325" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16325-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i used the filter for the remote ip (ip.addr == 10.8.30.141) and did the continuous ping but did not see anything.</p></blockquote><p>O.K. then you are (most certainly) capturing on the wrong interface. What is the output of the following command:</p><blockquote><p><code>dumpcap -D -M</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16325" class="comments-container"><span id="16328"></span><div id="comment-16328" class="comment"><div id="post-16328-score" class="comment-score"></div><div class="comment-text"><p>I type that in the terminal correct? I get nothing back. And if I capture on all devices I still get nothing (from the ping test)</p></div><div id="comment-16328-info" class="comment-info"><span class="comment-age">(26 Nov '12, 09:57)</span> owengerig</div></div><span id="16329"></span><div id="comment-16329" class="comment"><div id="post-16329-score" class="comment-score"></div><div class="comment-text"><p>Yes, in the terminal. No output at all? Did you try to run it with sudo?</p><blockquote><p><code>sudo dumpcap -D -M</code></p></blockquote></div><div id="comment-16329-info" class="comment-info"><span class="comment-age">(26 Nov '12, 10:15)</span> Kurt Knochner ♦</div></div><span id="16331"></span><div id="comment-16331" class="comment"><div id="post-16331-score" class="comment-score"></div><div class="comment-text"><p>Sorry didnt think to do sudo, see update for results.</p></div><div id="comment-16331-info" class="comment-info"><span class="comment-age">(26 Nov '12, 10:38)</span> owengerig</div></div><span id="16333"></span><div id="comment-16333" class="comment"><div id="post-16333-score" class="comment-score"></div><div class="comment-text"><p>O.K. so, did you capture on en0?</p></div><div id="comment-16333-info" class="comment-info"><span class="comment-age">(26 Nov '12, 11:59)</span> Kurt Knochner ♦</div></div><span id="16337"></span><div id="comment-16337" class="comment"><div id="post-16337-score" class="comment-score"></div><div class="comment-text"><p>yes and still nothing. Regardless of wether Im doing telnet or ping (10.8.30.141). With the filter ip.addr == 10.8.30.141</p></div><div id="comment-16337-info" class="comment-info"><span class="comment-age">(26 Nov '12, 12:15)</span> owengerig</div></div><span id="16339"></span><div id="comment-16339" class="comment not_top_scorer"><div id="post-16339-score" class="comment-score"></div><div class="comment-text"><p>o.k. something different. run tshark with sudo:</p><blockquote><p><code>sudo tshark -ni en0 host 10.8.30.141</code><br />
</p></blockquote><p>Then ping/telnet your host 10.8.30.141 in a second window. Do you see anything? If yes, try it without sudo. If that does not work, it's probably a privilege problem.</p><p>Then try to run Wireshark with sudo:</p><blockquote><p><code>sudo wireshark -ni en0 host 10.8.30.141</code><br />
</p></blockquote><p>Do you <strong>now</strong> see something?</p><p>BTW: Just by chance. There is a utun0 interface. You are not trying to ping something through a VPN tunnel, are you?</p></div><div id="comment-16339-info" class="comment-info"><span class="comment-age">(26 Nov '12, 12:49)</span> Kurt Knochner ♦</div></div><span id="16350"></span><div id="comment-16350" class="comment not_top_scorer"><div id="post-16350-score" class="comment-score"></div><div class="comment-text"><p>I have monitor and promiscuous modes enabled (try disabling them but it didnt help). is this normal though?</p></div><div id="comment-16350-info" class="comment-info"><span class="comment-age">(27 Nov '12, 11:03)</span> owengerig</div></div></div><div id="comment-tools-16325" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-16325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

