+++
type = "question"
title = "how to decode 3gpp lte messages using tshark/wireshark"
description = '''i have a hex dump of lte signaling messages (including, lte-rrc, rlc-mac, nas etc) Want to decode these messages using wireshark gui or tshark. 1) In gui mode what all setting changes i need to do before uploading the hexdump (i have converted it to pcap format). Please specify the steps. 2) In Tsha...'''
date = "2015-11-27T09:42:00Z"
lastmod = "2015-11-29T03:32:00Z"
weight = 48030
keywords = [ "asn", "3gpp", "lterrc", "lte", "decoder" ]
aliases = [ "/questions/48030" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to decode 3gpp lte messages using tshark/wireshark](/questions/48030/how-to-decode-3gpp-lte-messages-using-tsharkwireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48030-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have a hex dump of lte signaling messages (including, lte-rrc, rlc-mac, nas etc) Want to decode these messages using wireshark gui or tshark. 1) In gui mode what all setting changes i need to do before uploading the hexdump (i have converted it to pcap format). Please specify the steps. 2) In Tshark please specify the command to decode these messages- for example to decode lte-rrc</p></div><div id="question-tags" class="tags-container tags">asn 3gpp lterrc lte decoder</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '15, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/d612f124ad6216012f3c867a382ca623?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xiong%20jee&#39;s gravatar image" /><p>Xiong jee<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xiong jee has no accepted answers">0%</span></p></div></div><div id="comments-container-48030" class="comments-container"></div><div id="comment-tools-48030" class="comment-tools"></div><div class="clear"></div><div id="comment-48030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48054"></span>

<div id="answer-container-48054" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48054-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="http://3gppdecoder.free.fr/?q=node/1">3GPP decoder</a> front-end.</p><p>Alternatively look at <a href="https://ask.wireshark.org/questions/39027/use-wireshark-as-a-decoder">this thread</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '15, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Nov '15, 03:36</p></div></div><div id="comments-container-48054" class="comments-container"><span id="48098"></span><div id="comment-48098" class="comment"><div id="post-48098-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thank you. i used different user_dlts and able to decode the message names- but only message names, but not the content. say example rrcconnectionrequest- i am able to get that the message is rrcconnectionrequest- but no content is available. How to configure wireshark so that i get all the contents of the messages.</p><p>Thanks, Xiong</p></div><div id="comment-48098-info" class="comment-info"><span class="comment-age">(30 Nov '15, 09:14)</span> Xiong jee</div></div><span id="48131"></span><div id="comment-48131" class="comment"><div id="post-48131-score" class="comment-score"></div><div class="comment-text"><p>Presumably you are talking about tshark, right? If yes please add the -V option. if not, please post a sample of what you are seeing, so that I can better understand what's happening.</p></div><div id="comment-48131-info" class="comment-info"><span class="comment-age">(01 Dec '15, 05:13)</span> Pascal Quantin</div></div></div><div id="comment-tools-48054" class="comment-tools"></div><div class="clear"></div><div id="comment-48054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

