+++
type = "question"
title = "WPA decoding in realtime possible?"
description = '''Hello I heard that Wireshark does support decoding WPA. Does Wireshark decode WPA-traffic in realtime? Thank you very much! Joe'''
date = "2016-01-14T09:56:00Z"
lastmod = "2016-01-19T08:03:00Z"
weight = 49222
keywords = [ "decode", "capture", "wpa" ]
aliases = [ "/questions/49222" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WPA decoding in realtime possible?](/questions/49222/wpa-decoding-in-realtime-possible)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49222-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I heard that Wireshark does support decoding WPA. Does Wireshark decode WPA-traffic in realtime?</p><p>Thank you very much!</p><p>Joe</p></div><div id="question-tags" class="tags-container tags">decode capture wpa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '16, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/c08acf577aad3b14e932ee8f48cf7d20?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joseph123&#39;s gravatar image" /><p>joseph123<br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joseph123 has no accepted answers">0%</span></p></div></div><div id="comments-container-49222" class="comments-container"><span id="49235"></span><div id="comment-49235" class="comment"><div id="post-49235-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "in real time"?</p></div><div id="comment-49235-info" class="comment-info"><span class="comment-age">(14 Jan '16, 18:54)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-49222" class="comment-tools"></div><div class="clear"></div><div id="comment-49222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49379"></span>

<div id="answer-container-49379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49379-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If <strong>in realtime</strong> means <strong>while Wireshark is capturing data</strong>, then the answer is yes, as long as Wireshark is able to see the 4 EAPOL frames, see the Wiki.</p><blockquote><p><a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></p></blockquote><p>If <strong>in realtime</strong> means <strong>output on the CLI while tshark is capturing</strong>, then please see my answer to the following question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/24249/decrypt-wpa-with-tshark">https://ask.wireshark.org/questions/24249/decrypt-wpa-with-tshark</a><br />
</p></blockquote><p>If you substitute <strong>-nr input.pcap</strong> with <strong>-ni interface</strong> (while 'interface' is a placeholder for the wifi interface name), you will get the decrypted WPA output at the CLI.</p><p>If <strong>in realtime</strong> means something different, please tell us what it means to you.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '16, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-49379" class="comments-container"></div><div id="comment-tools-49379" class="comment-tools"></div><div class="clear"></div><div id="comment-49379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

