+++
type = "question"
title = "TLS1.2 Hello Requests"
description = '''Hello, can somebody have a look and confirm that wireshark is right in interpreting 4 zeroes as Hello Requests.  Anyone knows what that is? Regards Matthias  Trace is available on Cloudshark  TLS1.2_HS.pcapng'''
date = "2015-04-04T10:12:00Z"
lastmod = "2015-04-04T22:44:00Z"
weight = 41189
keywords = [ "aead", "cipher", "request", "hello", "aes-gcm" ]
aliases = [ "/questions/41189" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TLS1.2 Hello Requests](/questions/41189/tls12-hello-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41189-score" class="post-score" title="current number of votes">2</div><span id="post-41189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, can somebody have a look and confirm that wireshark is right in interpreting 4 zeroes as Hello Requests. Anyone knows what that is?<br />
Regards Matthias <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-215.png" alt="alt text" /> Trace is available on Cloudshark <a href="https://www.cloudshark.org/captures/d4c6e9019495">TLS1.2_HS.pcapng</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-aead" rel="tag" title="see questions tagged &#39;aead&#39;">aead</span> <span class="post-tag tag-link-cipher" rel="tag" title="see questions tagged &#39;cipher&#39;">cipher</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-hello" rel="tag" title="see questions tagged &#39;hello&#39;">hello</span> <span class="post-tag tag-link-aes-gcm" rel="tag" title="see questions tagged &#39;aes-gcm&#39;">aes-gcm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '15, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Apr '15, 22:48</strong> </span></p></div></div><div id="comments-container-41189" class="comments-container"></div><div id="comment-tools-41189" class="comment-tools"></div><div class="clear"></div><div id="comment-41189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41191"></span>

<div id="answer-container-41191" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41191-score" class="post-score" title="current number of votes">1</div><span id="post-41191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your capture is using an AEAD cipher suite. These have an explicit nonce in their TLSCipherText fragment data:</p><pre><code>  struct {
     opaque nonce_explicit[SecurityParameters.record_iv_length];
     aead-ciphered struct {
         opaque content[TLSCompressed.length];
     };
  } GenericAEADCipher;</code></pre><p>This explicit nonce for AES-GCM cipher suites may be a 64-bit counter which is also the case in your capture. The heuristics of Wireshark works as follows: if the record fragment for a Handshake message can be "decoded" (because the initial byte is a valid handshake message type), it will be dissected.</p><p>So what you are seeing is a bug that occurs when the records cannot be decrypted, and only occurs when using the AES-GCM AEAD cipher suites.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '15, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-41191" class="comments-container"><span id="41195"></span><div id="comment-41195" class="comment"><div id="post-41195-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the explanation.</p></div><div id="comment-41195-info" class="comment-info"><span class="comment-age">(04 Apr '15, 22:44)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-41191" class="comment-tools"></div><div class="clear"></div><div id="comment-41191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

