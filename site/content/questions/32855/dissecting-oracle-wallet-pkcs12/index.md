+++
type = "question"
title = "Dissecting Oracle Wallet PKCS#12"
description = '''Hi, I was trying to dissect an Oracle wallet file which comes in PKCS#12 format. While trying to display the content using openssl (openssl pkcs12 -in &amp;lt;filename&amp;gt; -nodes), I could see a message in the result saying: &quot;Warning unsupported bag type: secretBag&quot;. I tried to use Wireshark to view the...'''
date = "2014-05-17T06:09:00Z"
lastmod = "2014-05-17T06:09:00Z"
weight = 32855
keywords = [ "ber", "dissect", "oid", "pkcs12", "secretbag" ]
aliases = [ "/questions/32855" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting Oracle Wallet PKCS\#12](/questions/32855/dissecting-oracle-wallet-pkcs12)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32855-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I was trying to dissect an Oracle wallet file which comes in PKCS#12 format. While trying to display the content using openssl (openssl pkcs12 -in &lt;filename&gt; -nodes), I could see a message in the result saying: "Warning unsupported bag type: secretBag".</p><p>I tried to use Wireshark to view the content of the file, however in wireshark, no 'secretBag' was displayed. Interestingly, I could see a 'crlBag' which was not displayed in openssl. However, digging dipper into the content, I found the following message: "BER: Dissector for OID: 0.22.72.134.247.13.1.10 not implemented. Contact wireshark developers if you want this supported".</p><p>Has anyone ever encounter the same issue for that particular OID ? I wonder why wireshark did not display the "secretBag" content.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">ber dissect oid pkcs12 secretbag</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '14, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/11bac80a6d58b8f277e426795f692bda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gunawanjuanda&#39;s gravatar image" /><p>gunawanjuanda<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gunawanjuanda has no accepted answers">0%</span></p></div></div><div id="comments-container-32855" class="comments-container"></div><div id="comment-tools-32855" class="comment-tools"></div><div class="clear"></div><div id="comment-32855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

