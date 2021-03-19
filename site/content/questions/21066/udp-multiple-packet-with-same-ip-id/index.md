+++
type = "question"
title = "udp multiple packet with same ip id"
description = '''Multiple udp packets in a same session are showing same ip identification no. but has different data interestingly no fragmention also.'''
date = "2013-05-09T10:01:00Z"
lastmod = "2013-05-10T04:58:00Z"
weight = 21066
keywords = [ "udp" ]
aliases = [ "/questions/21066" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [udp multiple packet with same ip id](/questions/21066/udp-multiple-packet-with-same-ip-id)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21066-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Multiple udp packets in a same session are showing same ip identification no. but has different data interestingly no fragmention also.</p></div><div id="question-tags" class="tags-container tags">udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '13, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21066" class="comments-container"><span id="21067"></span><div id="comment-21067" class="comment"><div id="post-21067-score" class="comment-score"></div><div class="comment-text"><p>Can you post a capture file somewhere, perhaps www.cloudshark.org? Of course, it should not contain any confidential data.</p></div><div id="comment-21067-info" class="comment-info"><span class="comment-age">(09 May '13, 10:43)</span> Jim Aragon</div></div><span id="21078"></span><div id="comment-21078" class="comment"><div id="post-21078-score" class="comment-score"></div><div class="comment-text"><p>No sir i cannot due to limitation</p></div><div id="comment-21078-info" class="comment-info"><span class="comment-age">(09 May '13, 22:40)</span> kishan pandey</div></div></div><div id="comment-tools-21066" class="comment-tools"></div><div class="clear"></div><div id="comment-21066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21070"></span>

<div id="answer-container-21070" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21070-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the UDP session is long lived, you are bound to see multiple packets with the same identification fiels. The field is only 16 bits long, so it rolls over every 65536 packets. How much time (and packets) do you see between the packets with the same ID?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '13, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 May '13, 03:23</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-21070" class="comments-container"><span id="21079"></span><div id="comment-21079" class="comment"><div id="post-21079-score" class="comment-score"></div><div class="comment-text"><p>Amazing sir,its true there are 4 packets and gap between each of them is 65470 packets and time difference is around 110 seconds.Than it should be same in tcp as well?</p></div><div id="comment-21079-info" class="comment-info"><span class="comment-age">(09 May '13, 23:05)</span> kishan pandey</div></div><span id="21081"></span><div id="comment-21081" class="comment"><div id="post-21081-score" class="comment-score"></div><div class="comment-text"><p>Yes, it is the same for all protocols running on top of IP.</p></div><div id="comment-21081-info" class="comment-info"><span class="comment-age">(09 May '13, 23:49)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-21070" class="comment-tools"></div><div class="clear"></div><div id="comment-21070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21084"></span>

<div id="answer-container-21084" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21084-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Kurt thanks a lot, one small correction was than tshark -r file_1.pcap -T fields -e ip.id -e frame.number | sort &gt; file_1.txt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '13, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21084" class="comments-container"><span id="21085"></span><div id="comment-21085" class="comment"><div id="post-21085-score" class="comment-score"></div><div class="comment-text"><p>I guess this "answer" was meant to be a comment on <a href="http://ask.wireshark.org/questions/21080/udp-packet-loss">this</a> question, but I can't figure out how to move it.</p></div><div id="comment-21085-info" class="comment-info"><span class="comment-age">(10 May '13, 05:56)</span> grahamb ♦</div></div></div><div id="comment-tools-21084" class="comment-tools"></div><div class="clear"></div><div id="comment-21084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

