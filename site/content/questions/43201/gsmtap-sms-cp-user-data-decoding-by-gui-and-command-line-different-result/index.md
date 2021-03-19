+++
type = "question"
title = "GSMTAP SMS-CP User Data -decoding- by GUI and Command Line different result"
description = '''Hi all, I want ask about such wireshark &#x27;strange&#x27;. when I ran wireshark with normal GUI, and set the filter (by typing in filter bar) with gsmtap, 2 messages had been shown there, unfortunately the content was wrong. But when I ran my wireshark again, load the same file that I used before, but it wa...'''
date = "2015-06-16T02:12:00Z"
lastmod = "2015-06-18T06:36:00Z"
weight = 43201
keywords = [ "gsmtap", "gsm_sms" ]
aliases = [ "/questions/43201" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [GSMTAP SMS-CP User Data -decoding- by GUI and Command Line different result](/questions/43201/gsmtap-sms-cp-user-data-decoding-by-gui-and-command-line-different-result)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43201-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I want ask about such wireshark 'strange'. when I ran wireshark with normal GUI, and set the filter (by typing in filter bar) with gsmtap, 2 messages had been shown there, unfortunately the content was wrong. But when I ran my wireshark again, load the same file that I used before, but it was run with command line "wireshark -k -f udp -Y gsmtap -i lo". 2 messages can be shown also, the strange is that with this way (command line), seems the packet is well. wireshark show it well. these printscreen has been attached here.</p><p>anybody can help figure out what going here? how actually wireshark decoding my file with 'strange'..</p><p>thanks Bass</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2smswrong.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/using_wireshark_script.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">gsmtap gsm_sms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '15, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/bd24f32fb23479c997d1c603e5b6bff0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bass&#39;s gravatar image" /><p>bass<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bass has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Jun '15, 03:04</p></div></div><div id="comments-container-43201" class="comments-container"><span id="43204"></span><div id="comment-43204" class="comment"><div id="post-43204-score" class="comment-score"></div><div class="comment-text"><p>The first assumption is that you are not looking at the same packet: the upper one is a reassembled LAPDm packet of 85 bytes, while the lower one is a reassembled packet of 45 bytes. Moreover the TP-PID and TP-DCS fields also differ. ANy chance to share the pcap?</p></div><div id="comment-43204-info" class="comment-info"><span class="comment-age">(16 Jun '15, 06:35)</span> Pascal Quantin</div></div><span id="43232"></span><div id="comment-43232" class="comment"><div id="post-43232-score" class="comment-score"></div><div class="comment-text"><p>here is the link: [1] <a href="https://drive.google.com/file/d/0B2PfFt7P5kAgZ0xxRU0wY2ZHaXM/view?usp=sharing">https://drive.google.com/file/d/0B2PfFt7P5kAgZ0xxRU0wY2ZHaXM/view?usp=sharing</a> [2] <a href="https://drive.google.com/file/d/0B2PfFt7P5kAgT21WRmFOYjJBMTg/view?usp=sharing">https://drive.google.com/file/d/0B2PfFt7P5kAgT21WRmFOYjJBMTg/view?usp=sharing</a></p><p>just wondering, why wireshark act different there..</p></div><div id="comment-43232-info" class="comment-info"><span class="comment-age">(17 Jun '15, 01:34)</span> bass</div></div><span id="43247"></span><div id="comment-43247" class="comment"><div id="post-43247-score" class="comment-score"></div><div class="comment-text"><p>"wireshark -k -f udp -Y gsmtap -i lo" command is starting a new capture, it's not loading an existing file. So I'm not sure to understand what you mean by "But when I ran my wireshark again, load the same file that I used before, but it was run with command line "wireshark -k -f udp -Y gsmtap -i lo"" as here you are doing a new capture and not loading an existing one.</p><p>At first glance I would say that you did not look at the same packets between both tries.</p></div><div id="comment-43247-info" class="comment-info"><span class="comment-age">(17 Jun '15, 06:12)</span> Pascal Quantin</div></div><span id="43268"></span><div id="comment-43268" class="comment"><div id="post-43268-score" class="comment-score"></div><div class="comment-text"><p>The capture files are not identical, different source ports!</p></div><div id="comment-43268-info" class="comment-info"><span class="comment-age">(17 Jun '15, 08:50)</span> Kurt Knochner ♦</div></div><span id="43292"></span><div id="comment-43292" class="comment"><div id="post-43292-score" class="comment-score"></div><div class="comment-text"><p>those pcap file is a 'result'. actually, I have cfile which is GSM packet, then decoding this cfile using gr-gsm. while decoding process, the result of decoding can be seen through wireshark. however, for this step, of course needed to run wireshark first. when I start wireshark, I did it using normal GUI (click icon, choosing Lo adapter, input filter etc), in another session by command line as mentioned before. using same Gr-GSM and cfile source, but as you see in the pcap file, seems the result different. pardon me for seems miss-information here..</p></div><div id="comment-43292-info" class="comment-info"><span class="comment-age">(17 Jun '15, 19:28)</span> bass</div></div><span id="43320"></span><div id="comment-43320" class="comment not_top_scorer"><div id="post-43320-score" class="comment-score"></div><div class="comment-text"><p>so I just wondering, why the wireshark acts different there,,</p></div><div id="comment-43320-info" class="comment-info"><span class="comment-age">(18 Jun '15, 03:26)</span> bass</div></div></div><div id="comment-tools-43201" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-43201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43326"></span>

<div id="answer-container-43326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43326-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In your capture <a href="https://drive.google.com/file/d/0B2PfFt7P5kAgT21WRmFOYjJBMTg/view?usp=sharing">https://drive.google.com/file/d/0B2PfFt7P5kAgT21WRmFOYjJBMTg/view?usp=sharing</a> we can see that the the destination port was not open, generating ICMP messages containing the GSMTAP packets. This confuses the LAPDm reassembly code that concatenates 5 frames (packets 7, 8, 11, 12, 13) instead of 3 (packets 7, 11 and 13). Eventually the GSMTAP dissector could discard error packets instead of feeding them in LAPDm dissector.</p><p>In your other capture, there is no ICMP error packets, so reassembly works properly.</p><p>So what matters here is not really Wireshark command line, but whether you have a program opening the socket or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '15, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jun '15, 06:37</p></div></div><div id="comments-container-43326" class="comments-container"><span id="43353"></span><div id="comment-43353" class="comment"><div id="post-43353-score" class="comment-score"></div><div class="comment-text"><p>thank you so much for your explanation.. it was really helpful</p></div><div id="comment-43353-info" class="comment-info"><span class="comment-age">(18 Jun '15, 19:46)</span> bass</div></div></div><div id="comment-tools-43326" class="comment-tools"></div><div class="clear"></div><div id="comment-43326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

