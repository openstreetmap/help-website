+++
type = "question"
title = "Can a custom dissector analyze TCP header option field as well as data field?"
description = '''I&#x27;m trying to create a custom dissector for my protocol. I have used one bit of an unused option field in TCP. I want to dissect the bit I used.  I know that I can dissect data field as I want it to be but I want to know if I can dissect the header field how I want it to be when they are already def...'''
date = "2017-05-14T21:40:00Z"
lastmod = "2017-05-16T23:35:00Z"
weight = 61397
keywords = [ "dissector" ]
aliases = [ "/questions/61397" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can a custom dissector analyze TCP header option field as well as data field?](/questions/61397/can-a-custom-dissector-analyze-tcp-header-option-field-as-well-as-data-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to create a custom dissector for my protocol. I have used one bit of an unused option field in TCP. I want to dissect the bit I used. I know that I can dissect data field as I want it to be but I want to know if I can dissect the header field how I want it to be when they are already defined in wireshark</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '17, 21:40</strong></p><img src="https://secure.gravatar.com/avatar/3a702eaa9f4d90c81f74480545063c71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ngn505&#39;s gravatar image" /><p>ngn505<br />
<span class="score" title="6 reputation points">6</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ngn505 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '17, 00:01</p></div></div><div id="comments-container-61397" class="comments-container"><span id="61400"></span><div id="comment-61400" class="comment"><div id="post-61400-score" class="comment-score"></div><div class="comment-text"><p>'one bit of an unused option field'? Are you referring to TCP options or to the reserved bits in the TCP header between the data offset and the control bits?</p></div><div id="comment-61400-info" class="comment-info"><span class="comment-age">(14 May '17, 23:46)</span> Jaap ♦</div></div><span id="61419"></span><div id="comment-61419" class="comment"><div id="post-61419-score" class="comment-score"></div><div class="comment-text"><p>I'm referring the TCP option and padding field</p></div><div id="comment-61419-info" class="comment-info"><span class="comment-age">(16 May '17, 00:02)</span> ngn505</div></div><span id="61423"></span><div id="comment-61423" class="comment"><div id="post-61423-score" class="comment-score"></div><div class="comment-text"><p>For what version of Wireshark are you developing?</p></div><div id="comment-61423-info" class="comment-info"><span class="comment-age">(16 May '17, 04:10)</span> Jaap ♦</div></div><span id="61427"></span><div id="comment-61427" class="comment"><div id="post-61427-score" class="comment-score"></div><div class="comment-text"><p>it's version 2.2.5</p></div><div id="comment-61427-info" class="comment-info"><span class="comment-age">(16 May '17, 04:43)</span> ngn505</div></div></div><div id="comment-tools-61397" class="comment-tools"></div><div class="clear"></div><div id="comment-61397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61451"></span>

<div id="answer-container-61451" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61451-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In master-2.2 branch the TCP dissector has a 'closed' list of TCP options it can dissect, otherwise it just presents the option data without interpretation. You'll have to add your code to the TCP dissector itself if you want to show the interpretation of that bit in new TCP option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '17, 23:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61451" class="comments-container"><span id="61474"></span><div id="comment-61474" class="comment"><div id="post-61474-score" class="comment-score"></div><div class="comment-text"><p>oh that's great. Thank you for your help</p><p>I got one more question tho.. I was trying to find the TCP dissector but any of lua files I could see doesn't have clues of TCP option. Is TCP dissector contained in dll file? Or could you tell me where if you know?</p></div><div id="comment-61474-info" class="comment-info"><span class="comment-age">(17 May '17, 22:26)</span> ngn505</div></div><span id="61476"></span><div id="comment-61476" class="comment"><div id="post-61476-score" class="comment-score"></div><div class="comment-text"><p>Wireshark is written in C / C++, not Lua. You can find the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-tcp.c;h=0cbb1d38c131e47103ebd9164724d0dca9e553ce;hb=refs/heads/master-2.2#l4962">TCP dissector here</a>.</p></div><div id="comment-61476-info" class="comment-info"><span class="comment-age">(17 May '17, 23:19)</span> Jaap ♦</div></div><span id="61480"></span><div id="comment-61480" class="comment"><div id="post-61480-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!</p></div><div id="comment-61480-info" class="comment-info"><span class="comment-age">(18 May '17, 00:45)</span> ngn505</div></div></div><div id="comment-tools-61451" class="comment-tools"></div><div class="clear"></div><div id="comment-61451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

