+++
type = "question"
title = "IKE decryption with certificates"
description = '''Hi, I noticed that this method (see this question) to decrypt IKE (v1) packets doesn&#x27;t work when certificate are used instead of PSK. At first, I thought it would be the fragmentation as phase 1 message 5 and 6 exceeded the 1500 byte size and got fragmented into two packets. But after enabling JUMBO...'''
date = "2012-11-02T06:25:00Z"
lastmod = "2012-11-02T06:25:00Z"
weight = 15497
keywords = [ "certificates", "ike" ]
aliases = [ "/questions/15497" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IKE decryption with certificates](/questions/15497/ike-decryption-with-certificates)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15497-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I noticed that this method (see this <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets">question</a>) to decrypt IKE (v1) packets doesn't work when certificate are used instead of PSK. At first, I thought it would be the fragmentation as phase 1 message 5 and 6 exceeded the 1500 byte size and got fragmented into two packets. But after enabling JUMBO frames, the problem remained the same. I haven't changed all other algorithms (still 3DES, MD5 etc.) that I used in PSK test.</p><p>Any ideas? I'm happy to provide my capture and the pluto log file on request...</p><p>Cheers, Dominik</p></div><div id="question-tags" class="tags-container tags">certificates ike</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Nov '12, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/9ef210346444f3db3b3a3bcfe88f0e63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dominik&#39;s gravatar image" /><p>Dominik<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dominik has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 02 Nov '12, 06:40</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-15497" class="comments-container"><span id="15499"></span><div id="comment-15499" class="comment"><div id="post-15499-score" class="comment-score"></div><div class="comment-text"><p>Converted from an "answer" to a question from <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets">http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets</a></p></div><div id="comment-15499-info" class="comment-info"><span class="comment-age">(02 Nov '12, 06:41)</span> grahamb ♦</div></div></div><div id="comment-tools-15497" class="comment-tools"></div><div class="clear"></div><div id="comment-15497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

