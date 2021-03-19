+++
type = "question"
title = "need help: the code location of Ethernet trailer"
description = '''Hi guys, I am a novice on the wireshark developing.  As for some reason, I need to get the trailer of Ethernet trailer and displayed with a more readable format, who can tell me where is the code of Ethernet trailer in Wireshark code. Thanks in advance! Best Regards! Sam '''
date = "2011-08-26T23:10:00Z"
lastmod = "2011-08-29T11:33:00Z"
weight = 5900
keywords = [ "development" ]
aliases = [ "/questions/5900" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [need help: the code location of Ethernet trailer](/questions/5900/need-help-the-code-location-of-ethernet-trailer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5900-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I am a novice on the wireshark developing. As for some reason, I need to get the trailer of Ethernet trailer and displayed with a more readable format, who can tell me where is the code of Ethernet trailer in Wireshark code.</p><p>Thanks in advance!</p><p>Best Regards!</p><p>Sam</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '11, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/e9d668dd28830dd8f79d4dbb56e5f2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam&#39;s gravatar image" /><p>Sam<br />
<span class="score" title="51 reputation points">51</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '11, 12:24</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5900" class="comments-container"><span id="5908"></span><div id="comment-5908" class="comment"><div id="post-5908-score" class="comment-score"></div><div class="comment-text"><p>"More readable" in what sense? The trailer is just padding added to the packet to make sure it's at least the minimum packet size; there's no meaningful data in the trailer, so there's nothing more readable than a blob of hex digits.</p></div><div id="comment-5908-info" class="comment-info"><span class="comment-age">(28 Aug '11, 13:29)</span> Guy Harris ♦♦</div></div><span id="5913"></span><div id="comment-5913" class="comment"><div id="post-5913-score" class="comment-score"></div><div class="comment-text"><p>Harris,</p><p>There is a special requirement, we have every packets tagged with eight bytes in the trailer by a device. The eight bytes need to be picked up from the packets and do some analysis.</p><p>I will check the packets-eth.c file and find out how to fick up the eight bytes, will let you konw if any further info. Do you have any ideas on this? thanks.</p><p>Sam</p></div><div id="comment-5913-info" class="comment-info"><span class="comment-age">(29 Aug '11, 06:20)</span> Sam</div></div><span id="5916"></span><div id="comment-5916" class="comment"><div id="post-5916-score" class="comment-score"></div><div class="comment-text"><p>There's an Ethernet trailer heuristic sub dissector list "eth.trailer" where you can register to.</p></div><div id="comment-5916-info" class="comment-info"><span class="comment-age">(29 Aug '11, 06:58)</span> Jaap ♦</div></div><span id="5938"></span><div id="comment-5938" class="comment"><div id="post-5938-score" class="comment-score"></div><div class="comment-text"><p>thanks, Jaap. I will try it.</p><p>Sam</p></div><div id="comment-5938-info" class="comment-info"><span class="comment-age">(29 Aug '11, 19:03)</span> Sam</div></div><span id="8132"></span><div id="comment-8132" class="comment"><div id="post-8132-score" class="comment-score"></div><div class="comment-text"><p>i am trying get trailer data from remote computer with PHP codes. I dont know if there is get_ethernet_trailer() function or not. Do you know like this function in PHP?</p></div><div id="comment-8132-info" class="comment-info"><span class="comment-age">(25 Dec '11, 02:05)</span> lansas</div></div><span id="8133"></span><div id="comment-8133" class="comment not_top_scorer"><div id="post-8133-score" class="comment-score"></div><div class="comment-text"><p>Maybe somebody's implemented it in <a href="https://sourceforge.net/projects/phpcap/">phpcap</a> or atop phpcap. I've never worked with PHP, so I have no idea whether anybody's done so.</p></div><div id="comment-8133-info" class="comment-info"><span class="comment-age">(25 Dec '11, 02:15)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5900" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-5900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5923"></span>

<div id="answer-container-5923" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5923-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Note that Wireshark thinks the Ethernet trailer is the padding added to bring the packet length up to the minimum. If the packet did not need to have a trailer added, or if we cannot determine whether it needed to have a trailer added (e.g., with a protocol that doesn't run atop 802.2 and that doesn't include its own length field), we do not guarantee that all the "extra" data at the end of the packet will be recognized as or treated as a trailer.</p><p>If your capturing is done in a special fashion, i.e. it's not just done by doing regular libpcap/WinPcap capture on a regular Ethernet adapter, but it's written out as a pcap or pcap-ng file, you might want to request your own pcap link-layer type and have your own dissector for that (perhaps sharing code with the Ethernet dissector). If not, you might want to consider having a preference for the Ethernet dissector to tell it to treat the last 8 bytes of the raw frame data specially.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '11, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-5923" class="comments-container"><span id="5937"></span><div id="comment-5937" class="comment"><div id="post-5937-score" class="comment-score"></div><div class="comment-text"><p>Harris,</p><p>thanks for your advice, I will try to tell the Ethernet dissector to treat the last 8 bytes of the raw frame data specially, will tell you once I finish it. Maybe one week later, haha. thanks again.</p><p>Sam</p></div><div id="comment-5937-info" class="comment-info"><span class="comment-age">(29 Aug '11, 18:29)</span> Sam</div></div><span id="5948"></span><div id="comment-5948" class="comment"><div id="post-5948-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment", please see the FAQ)</p></div><div id="comment-5948-info" class="comment-info"><span class="comment-age">(30 Aug '11, 00:43)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-5923" class="comment-tools"></div><div class="clear"></div><div id="comment-5923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5902"></span>

<div id="answer-container-5902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5902-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How about <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-eth.c">epan/dissectors/packet-eth.c</a> ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '11, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5902" class="comments-container"><span id="5903"></span><div id="comment-5903" class="comment"><div id="post-5903-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot, will check it and get back to you later.</p><p>Sam</p></div><div id="comment-5903-info" class="comment-info"><span class="comment-age">(27 Aug '11, 04:01)</span> Sam</div></div></div><div id="comment-tools-5902" class="comment-tools"></div><div class="clear"></div><div id="comment-5902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

