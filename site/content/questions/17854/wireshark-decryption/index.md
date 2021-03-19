+++
type = "question"
title = "Wireshark Decryption?"
description = '''Hello,  First of all, I am very new to this and I am having difficulties. I have some questions about the decryption feature. Is this only used when in monitoring mode to capture wireless traffic? How do I know what my key is? Also, when wireshark is used to capture the traffic on a local machine, i...'''
date = "2013-01-22T04:05:00Z"
lastmod = "2013-01-22T05:27:00Z"
weight = 17854
keywords = [ "decyption" ]
aliases = [ "/questions/17854" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Decryption?](/questions/17854/wireshark-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17854-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>First of all, I am very new to this and I am having difficulties.</p><p>I have some questions about the decryption feature.</p><p><strong>Is this only used when in monitoring mode to capture wireless traffic?</strong></p><p><strong>How do I know what my key is?</strong></p><p>Also, when wireshark is used to capture the traffic on a local machine, ie the machine it is running on, does it need an encryption key? Or does it automatically decrypt the traffic?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">decyption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '13, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/8bc2d3a2c0b5c2ffafc475dfa705a471?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ToNyW87&#39;s gravatar image" /><p>ToNyW87<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ToNyW87 has no accepted answers">0%</span></p></div></div><div id="comments-container-17854" class="comments-container"></div><div id="comment-tools-17854" class="comment-tools"></div><div class="clear"></div><div id="comment-17854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17855"></span>

<div id="answer-container-17855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17855-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you are referring to 802.11 wireless traffic, then capturing and decryption are different entities and no key is need to capture traffic. To then decrypt and view the captured traffic you will need a key and your capture must contain the 4 EAPOL handshake packets that set the session key.</p><p>See the Wiki pages on 802.11 <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">capturing</a> and <a href="http://wiki.wireshark.org/HowToDecrypt802.11">decryption</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '13, 05:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-17855" class="comments-container"></div><div id="comment-tools-17855" class="comment-tools"></div><div class="clear"></div><div id="comment-17855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

