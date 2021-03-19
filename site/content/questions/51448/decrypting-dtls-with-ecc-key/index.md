+++
type = "question"
title = "Decrypting DTLS with ECC key"
description = '''Hi, I saw the question and answer in https://ask.wireshark.org/questions/47010/decode-with-known-psk-in-dtls#fmanswer - my question is similar, but in my case the key is ECC, and when I try to add the key I get an error message “can’t load private key”. Is there any way around this? Thanks,'''
date = "2016-04-06T22:44:00Z"
lastmod = "2016-04-08T13:47:00Z"
weight = 51448
keywords = [ "decryption", "dtls", "ecc" ]
aliases = [ "/questions/51448" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decrypting DTLS with ECC key](/questions/51448/decrypting-dtls-with-ecc-key)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51448-score" class="post-score" title="current number of votes">0</div><span id="post-51448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I saw the question and answer in <a href="https://ask.wireshark.org/questions/47010/decode-with-known-psk-in-dtls#fmanswer">https://ask.wireshark.org/questions/47010/decode-with-known-psk-in-dtls#fmanswer</a> - my question is similar, but in my case the key is ECC, and when I try to add the key I get an error message “can’t load private key”.<br />
Is there any way around this?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-dtls" rel="tag" title="see questions tagged &#39;dtls&#39;">dtls</span> <span class="post-tag tag-link-ecc" rel="tag" title="see questions tagged &#39;ecc&#39;">ecc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '16, 22:44</strong></p><img src="https://secure.gravatar.com/avatar/81b1c146f57c8aa114ae289d642784af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ranshe&#39;s gravatar image" /><p><span>ranshe</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ranshe has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-51448" class="comments-container"></div><div id="comment-tools-51448" class="comment-tools"></div><div class="clear"></div><div id="comment-51448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51518"></span>

<div id="answer-container-51518" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51518-score" class="post-score" title="current number of votes">0</div><span id="post-51518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ranshe has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You cannot use non-RSA private keys for decryption. Some TLS cipher suites use RSA for the key exchange (see <a href="https://tools.ietf.org/html/rfc5246#section-7.4.7">RFC 5246 (TLS 1.2) - 7.4.7.</a>) which can then be decrypted using a RSA private key, but there is not something similar for ECC certificates.</p><p>ECC certificates (<a href="https://tools.ietf.org/html/rfc5480">RFC 5480</a>, <a href="https://tools.ietf.org/html/rfc4492">RFC 4492</a>) appear to be used for ECDH key exchange and for authentication (fixed-ECDH certificates and ECDSA). This means that even if you posess the private key, you cannot use it for decryption of the traffic.</p><p>As an alternative, you can try to obtain the master secret into a "SSL Keylog file" and feed this file to Wireshark to enable decryption. This method is only possible if your DTLS library supports it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '16, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '16, 10:28</strong> </span></p></div></div><div id="comments-container-51518" class="comments-container"><span id="51523"></span><div id="comment-51523" class="comment"><div id="post-51523-score" class="comment-score"></div><div class="comment-text"><p>That's a bummer, but of course thanks for the answer.</p></div><div id="comment-51523-info" class="comment-info"><span class="comment-age">(08 Apr '16, 13:47)</span> <span class="comment-user userinfo">ranshe</span></div></div></div><div id="comment-tools-51518" class="comment-tools"></div><div class="clear"></div><div id="comment-51518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

