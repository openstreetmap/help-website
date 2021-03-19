+++
type = "question"
title = "ESP decryption table vs ISAKMP decryption table"
description = '''Hi, In ESP decryption table there are the following algorithms: HMAC-SHA-1-96 [RFC2404] HMAC-SHA-256-96 [draft-ietf-ipsec-ciph-sha-256-00] HMAC-SHA-256-128 [RFC4868] HMAC-SHA-384-192 [RFC4868] HMAC-SHA-512-256 [RFC4868] And in ISAKMP (IKEv2 or IKEv1) decryption table there are the following algorith...'''
date = "2016-08-08T02:10:00Z"
lastmod = "2016-08-08T02:31:00Z"
weight = 54640
keywords = [ "decryption", "name-resolving", "encryption", "esp" ]
aliases = [ "/questions/54640" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ESP decryption table vs ISAKMP decryption table](/questions/54640/esp-decryption-table-vs-isakmp-decryption-table)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54640-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In ESP decryption table there are the following algorithms: HMAC-SHA-1-96 [RFC2404] HMAC-SHA-256-96 [draft-ietf-ipsec-ciph-sha-256-00] HMAC-SHA-256-128 [RFC4868] HMAC-SHA-384-192 [RFC4868] HMAC-SHA-512-256 [RFC4868]</p><p>And in ISAKMP (IKEv2 or IKEv1) decryption table there are the following algorithms: HMAC_SHA1_96 [RFC2404] HMAC_SHA2_256_96 [draft-ietf-ipsec-ciph-sha-256-00] HMAC_SHA2_256_128 [RFC4868] HMAC_SHA2_384_192 [RFC4868] HMAC_SHA2_512_256 [RFC4868]</p><p>So, the only difference is the name?</p><p>Cheers, Codrut.</p></div><div id="question-tags" class="tags-container tags">decryption name-resolving encryption esp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '16, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/3979ee191d6e4d4cf918bfe41475e815?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Codrut%20Cristian%20Grosu&#39;s gravatar image" /><p>Codrut Crist...<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Codrut Cristian Grosu has no accepted answers">0%</span></p></div></div><div id="comments-container-54640" class="comments-container"></div><div id="comment-tools-54640" class="comment-tools"></div><div class="clear"></div><div id="comment-54640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54641"></span>

<div id="answer-container-54641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54641-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>They all refer to the same algorithm. The SHA-1 hash function has only one output size while SHA-2 has several ones (256, 384, 512). Whenever you see "SHA256", "SHA384" or "SHA512", it refers to "SHA-2".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '16, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-54641" class="comments-container"><span id="54642"></span><div id="comment-54642" class="comment"><div id="post-54642-score" class="comment-score"></div><div class="comment-text"><p>Thanks alot for clarifying this thing to me.</p></div><div id="comment-54642-info" class="comment-info"><span class="comment-age">(08 Aug '16, 02:38)</span> Codrut Crist...</div></div></div><div id="comment-tools-54641" class="comment-tools"></div><div class="clear"></div><div id="comment-54641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

