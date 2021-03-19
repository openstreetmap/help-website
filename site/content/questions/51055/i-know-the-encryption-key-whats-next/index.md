+++
type = "question"
title = "i know the encryption key, whats next ?"
description = '''i was inspecting a HTTPS site and i found the certificate packet and i found this key in it  Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02b) is this what i need to decrypt the traffic ?? i hope if someone could tell me what to do next in a more practical way'''
date = "2016-03-20T16:42:00Z"
lastmod = "2016-03-21T09:52:00Z"
weight = 51055
keywords = [ "ssl", "https" ]
aliases = [ "/questions/51055" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [i know the encryption key, whats next ?](/questions/51055/i-know-the-encryption-key-whats-next)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51055-score" class="post-score" title="current number of votes">0</div><span id="post-51055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i was inspecting a HTTPS site and i found the certificate packet and i found this key in it</p><p>Cipher Suite: TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 (0xc02b)</p><p>is this what i need to decrypt the traffic ??</p><p>i hope if someone could tell me what to do next in a more practical way</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '16, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/08f0927c223814704c76dad8fb4fdd94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mostafa%20Nafady&#39;s gravatar image" /><p><span>Mostafa Nafady</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mostafa Nafady has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Mar '16, 16:51</strong> </span></p></div></div><div id="comments-container-51055" class="comments-container"></div><div id="comment-tools-51055" class="comment-tools"></div><div class="clear"></div><div id="comment-51055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51059"></span>

<div id="answer-container-51059" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51059-score" class="post-score" title="current number of votes">0</div><span id="post-51059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mostafa Nafady has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Certificate packet contains the <em>public</em> key which cannot be used to decrypt traffic.</p><p>The mentioned cipher suite uses the Diffie-Hellman algorithm for key exchange which cannot be decrypted anyway using a RSA private key. If you are interested in browser traffic, have a look at using the SSL keylog method described at <a href="https://wiki.wireshark.org/SSL#SSL_dissection_in_Wireshark.">https://wiki.wireshark.org/SSL#SSL_dissection_in_Wireshark.</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '16, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-51059" class="comments-container"><span id="51066"></span><div id="comment-51066" class="comment"><div id="post-51066-score" class="comment-score"></div><div class="comment-text"><p>Thanks A lot for clarifying this for me</p></div><div id="comment-51066-info" class="comment-info"><span class="comment-age">(21 Mar '16, 07:52)</span> <span class="comment-user userinfo">Mostafa Nafady</span></div></div><span id="51071"></span><div id="comment-51071" class="comment"><div id="post-51071-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-51071-info" class="comment-info"><span class="comment-age">(21 Mar '16, 09:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-51059" class="comment-tools"></div><div class="clear"></div><div id="comment-51059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

