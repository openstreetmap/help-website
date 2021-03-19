+++
type = "question"
title = "Are AEAD cyphers accepted for IKEv2 decryption table?"
description = '''Hi, I&#x27;m working at a strongSwan plugin that will generate a IKEv2 decryption table for wireshark. In IKEv2 decryption table(wireshark) at encryption algorithm field there are only the following algorithms: &quot;3DES[RFC2451]&quot;, &quot;AES-CBC-128[RFC3602]&quot;, &quot;AES-CBC-192[RFC3602]&quot;, &quot;AES-CBC-256[RFC3602]&quot; and &quot;N...'''
date = "2016-08-02T00:49:00Z"
lastmod = "2016-08-02T05:09:00Z"
weight = 54492
keywords = [ "aead", "ikev2", "encryption", "decryption" ]
aliases = [ "/questions/54492" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Are AEAD cyphers accepted for IKEv2 decryption table?](/questions/54492/are-aead-cyphers-accepted-for-ikev2-decryption-table)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54492-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm working at a strongSwan plugin that will generate a IKEv2 decryption table for wireshark.</p><p>In IKEv2 decryption table(wireshark) at encryption algorithm field there are only the following algorithms: "3DES[RFC2451]", "AES-CBC-128[RFC3602]", "AES-CBC-192[RFC3602]", "AES-CBC-256[RFC3602]" and "NULL[RFC2410]".</p><p>But strongSwan accepts AEAD cyphers like: AES_CCM_ICV8, AES_CCM_ICV12, AES_CCM_ICV16, AES_GCM_ICV8, AES_GCM_ICV12, AES_GCM_ICV16, NULL_AUTH_AES_GMAC, CAMELLIA_CCM_ICV8, CAMELLIA_CCM_ICV12, CAMELLIA_CCM_ICV16 and CHACHA20_POLY1305.</p><p>So, wireshark can decrypt packets that are encrypted with AEAD cyphers?</p><p>Thanks, Codrut</p></div><div id="question-tags" class="tags-container tags">aead ikev2 encryption decryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '16, 00:49</strong></p><img src="https://secure.gravatar.com/avatar/3979ee191d6e4d4cf918bfe41475e815?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Codrut%20Cristian%20Grosu&#39;s gravatar image" /><p>Codrut Crist...<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Codrut Cristian Grosu has no accepted answers">0%</span></p></div></div><div id="comments-container-54492" class="comments-container"></div><div id="comment-tools-54492" class="comment-tools"></div><div class="clear"></div><div id="comment-54492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54503"></span>

<div id="answer-container-54503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54503-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Once the ISAKMP dissector is adapted to setup the decryption parameters for those it would be able to do so. Currently it's not. You could file an <a href="https://bugs.wireshark.org">enhancement request</a> to this effect referencing this question and providing a sample capture would help things along.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '16, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54503" class="comments-container"></div><div id="comment-tools-54503" class="comment-tools"></div><div class="clear"></div><div id="comment-54503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

