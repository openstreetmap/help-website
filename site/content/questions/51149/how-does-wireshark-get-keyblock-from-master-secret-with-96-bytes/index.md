+++
type = "question"
title = "How does wireshark get keyblock from Master Secret with 96 Bytes"
description = '''I have the Client Random and Master Secret. It was written by FF like stated here. So I have the Master Secret in a 96 Bytes Hexvalue. Can someone tell where in the Source Code of wireshark I can find the function that takes this value and calculates the 128 or 256 bit AES Key for calculating the Ke...'''
date = "2016-03-24T05:02:00Z"
lastmod = "2016-03-24T07:40:00Z"
weight = 51149
keywords = [ "ssl", "master-key", "ssl_decrypt" ]
aliases = [ "/questions/51149" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How does wireshark get keyblock from Master Secret with 96 Bytes](/questions/51149/how-does-wireshark-get-keyblock-from-master-secret-with-96-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51149-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the Client Random and Master Secret. It was written by FF like stated <a href="https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Key_Log_Format">here</a>. So I have the Master Secret in a 96 Bytes Hexvalue. Can someone tell where in the Source Code of wireshark I can find the function that takes this value and calculates the 128 or 256 bit AES Key for calculating the KeyBlock (where can find that function too?) which is needed to decrypt the SSL data.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">ssl master-key ssl_decrypt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '16, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/1683ee6ee87a65cb866ff23869f5de45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monkey521&#39;s gravatar image" /><p>monkey521<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monkey521 has no accepted answers">0%</span></p></div></div><div id="comments-container-51149" class="comments-container"></div><div id="comment-tools-51149" class="comment-tools"></div><div class="clear"></div><div id="comment-51149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51156"></span>

<div id="answer-container-51156" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51156-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you would like to know how keys are derived from this master secret, have a look at <a href="https://tools.ietf.org/html/rfc5246#section-6.3">RFC 5246 section 6.3</a> (TLS 1.2, Key Calculation).</p><p>As for the Wireshark source code, have a look at epan/dissectors/packet-ssl-utils.c, function ssl_generate_keyring_material. You can also enable the SSL debug log at the SSL protocol preferences and read the generated file for better understanding.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '16, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-51156" class="comments-container"><span id="51157"></span><div id="comment-51157" class="comment"><div id="post-51157-score" class="comment-score"></div><div class="comment-text"><p>thank you this looks like what i have been looking for. now i need to learn some c to translate it into java ;)</p></div><div id="comment-51157-info" class="comment-info"><span class="comment-age">(24 Mar '16, 08:52)</span> monkey521</div></div></div><div id="comment-tools-51156" class="comment-tools"></div><div class="clear"></div><div id="comment-51156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

