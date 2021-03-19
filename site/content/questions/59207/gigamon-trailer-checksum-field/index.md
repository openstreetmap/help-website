+++
type = "question"
title = "Gigamon trailer checksum field"
description = '''Hello, I&#x27;m trying to build a packet with gigamon trailer in Scapy for the purpose of testing. I&#x27;ve successfully created gigamon header before. However gigamon trailer uses 2 byte checksum field and I cannot understand how to calculate it. I see that Wireshark verifies this field. Does anyone know th...'''
date = "2017-02-01T02:58:00Z"
lastmod = "2017-02-01T05:00:00Z"
weight = 59207
keywords = [ "checksum", "dissector", "algorithm" ]
aliases = [ "/questions/59207" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Gigamon trailer checksum field](/questions/59207/gigamon-trailer-checksum-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59207-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to build a packet with gigamon trailer in Scapy for the purpose of testing. I've successfully created gigamon header before. However gigamon trailer uses 2 byte checksum field and I cannot understand how to calculate it. I see that Wireshark verifies this field. Does anyone know the algorithm for computing gigamon trailer checksum?</p><p>Thank you, Alex</p></div><div id="question-tags" class="tags-container tags">checksum dissector algorithm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '17, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/0f40170b2a1265cc12dd18994a0fbfc1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex%20Os&#39;s gravatar image" /><p>Alex Os<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex Os has no accepted answers">0%</span></p></div></div><div id="comments-container-59207" class="comments-container"></div><div id="comment-tools-59207" class="comment-tools"></div><div class="clear"></div><div id="comment-59207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59213"></span>

<div id="answer-container-59213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59213-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-gmhdr.c;h=2c21cf04f225af03dc2533f6f277f343a7830353;hb=HEAD">packet_gmhdr.c</a>, in particular the function <code>dissect_gmtrailer()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '17, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59213" class="comments-container"><span id="59221"></span><div id="comment-59221" class="comment"><div id="post-59221-score" class="comment-score"></div><div class="comment-text"><p>Thank you!</p></div><div id="comment-59221-info" class="comment-info"><span class="comment-age">(01 Feb '17, 06:43)</span> Alex Os</div></div><span id="59225"></span><div id="comment-59225" class="comment"><div id="post-59225-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-59225-info" class="comment-info"><span class="comment-age">(01 Feb '17, 08:35)</span> Jaap ♦</div></div></div><div id="comment-tools-59213" class="comment-tools"></div><div class="clear"></div><div id="comment-59213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

