+++
type = "question"
title = "Trying to decrypt messages to and from my chat client"
description = '''Hello all, I&#x27;m trying to decrypt traffic that is going from and coming into my chat client (tldr I want to forward it, unencrypted). I see from wireshark that it is using a TLSv1.1 style handshake to set up the encryption. I don&#x27;t fully understand the process of what&#x27;s going on here. The overall que...'''
date = "2015-03-14T17:03:00Z"
lastmod = "2015-03-16T05:40:00Z"
weight = 40565
keywords = [ "tls", "decryption", "client", "rsa", "tcp" ]
aliases = [ "/questions/40565" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to decrypt messages to and from my chat client](/questions/40565/trying-to-decrypt-messages-to-and-from-my-chat-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40565-score" class="post-score" title="current number of votes">0</div><span id="post-40565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I'm trying to decrypt traffic that is going from and coming into my chat client (tldr I want to forward it, unencrypted). I see from wireshark that it is using a TLSv1.1 style handshake to set up the encryption. I don't fully understand the process of what's going on here.</p><p>The overall question is, if the chat client can encode and decode information going to and coming from the server, why can't I? I would think this should be as easy as finding the RSA key file stored on my local machine.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-client" rel="tag" title="see questions tagged &#39;client&#39;">client</span> <span class="post-tag tag-link-rsa" rel="tag" title="see questions tagged &#39;rsa&#39;">rsa</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '15, 17:03</strong></p><img src="https://secure.gravatar.com/avatar/60843d57113e94a31f320915c530d226?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Annomaly&#39;s gravatar image" /><p><span>Annomaly</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Annomaly has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '15, 17:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-40565" class="comments-container"></div><div id="comment-tools-40565" class="comment-tools"></div><div class="clear"></div><div id="comment-40565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40590"></span>

<div id="answer-container-40590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40590-score" class="post-score" title="current number of votes">0</div><span id="post-40590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In an RSA handshake, the client uses the public key in the certificate from the server to encrypt the premaster secret. The server is able to use its private key to decrypt the encrypted premaster secret. Then both client and server are able to use the premaster secret to create a session key for the encryption/decryption of the data stream.</p><p>Wireshark also uses the private key from the server to decrypt the premaster secret (which is sent by the client in the ClientKeyExchange handshake message). But as said, it is stored on the server, not the client.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '15, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40590" class="comments-container"><span id="40614"></span><div id="comment-40614" class="comment"><div id="post-40614-score" class="comment-score"></div><div class="comment-text"><p>Interesting. As far as I can tell the data is encrypted. To me that simply means: No text visible in any of the packets, I can't string.search(msg).</p><p>I can, however, view the premaster secret. I assume the private key is sent encrypted and session based, however, there must be a way to capture this. After all, I'm trying to "decrypt" my own messages.</p><ul><li>The struggles of a novice.</li></ul></div><div id="comment-40614-info" class="comment-info"><span class="comment-age">(16 Mar '15, 05:40)</span> <span class="comment-user userinfo">Annomaly</span></div></div></div><div id="comment-tools-40590" class="comment-tools"></div><div class="clear"></div><div id="comment-40590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

