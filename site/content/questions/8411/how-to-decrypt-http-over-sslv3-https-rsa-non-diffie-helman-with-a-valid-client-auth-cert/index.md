+++
type = "question"
title = "how to decrypt http over sslv3 (https) rsa NON diffie helman with a valid client auth cert"
description = '''I have a valid sslv3 client authentication cert. that I use to access a company&#x27;s web-site. The transaction works fine in a standard web browser. I would like to decrypt the ssl session (the server to client application data specifically). Maybe it is simply my ignorance, but shouldn&#x27;t this be possi...'''
date = "2012-01-16T10:06:00Z"
lastmod = "2012-03-20T18:41:00Z"
weight = 8411
keywords = [ "authentication", "client", "decrypt", "rsa", "sslv3" ]
aliases = [ "/questions/8411" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to decrypt http over sslv3 (https) rsa NON diffie helman with a valid client auth cert](/questions/8411/how-to-decrypt-http-over-sslv3-https-rsa-non-diffie-helman-with-a-valid-client-auth-cert)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8411-score" class="post-score" title="current number of votes">0</div><span id="post-8411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a valid sslv3 client authentication cert. that I use to access a company's web-site. The transaction works fine in a standard web browser. I would like to decrypt the ssl session (the server to client application data specifically). Maybe it is simply my ignorance, but shouldn't this be possible? I believe the client to server app data is encrypted with their public cert, so I am not sure if is this is accessible intra-wireshark, but I would minimally like to get the responses decrypted.</p><p>This transaction is completely captured in wireshark (no reused/resumed ssl sessions). It is not a DH exchange. (1) I have tried using the .pfx file format which is how the cert was delivered to me.<br />
(2) I have tried converting to PEM and just including the unencrypted client private rsa key using openssl. (3) I have tried converting to PEM and including the unencrypted rsa priv. client key + the client and server certs. (4) I have tried converting to PEM and including the unencrypted rsa priv. client key + the client cert.</p><p>openssl version &gt;1.0, and w.s. version 1.6.2 w/GnuTLS. Debug log for all includes a "ssl init private key file X successfully loaded". In case (1), The cert imports are interesting. "NameOnCert (Error), KeyID (number)". But in all cases: can't decrypt pre-master secret. no decoders available both client and server packets.</p><p>I think I am hitting something fundamental -- any insight would be greatly appreciated. Thanks Chris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-authentication" rel="tag" title="see questions tagged &#39;authentication&#39;">authentication</span> <span class="post-tag tag-link-client" rel="tag" title="see questions tagged &#39;client&#39;">client</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span> <span class="post-tag tag-link-rsa" rel="tag" title="see questions tagged &#39;rsa&#39;">rsa</span> <span class="post-tag tag-link-sslv3" rel="tag" title="see questions tagged &#39;sslv3&#39;">sslv3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '12, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/48fefc1f881b760b6aba934bd5f98919?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_chris_&#39;s gravatar image" /><p><span>_chris_</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_chris_ has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-8411" class="comments-container"></div><div id="comment-tools-8411" class="comment-tools"></div><div class="clear"></div><div id="comment-8411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9667"></span>

<div id="answer-container-9667" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9667-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9667-score" class="post-score" title="current number of votes">0</div><span id="post-9667-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Chris, I hope you have gotten your answer by now, but for others who search this topic:<br />
</p><p>Yes, it is something very fundamental!<br />
</p><ol><li><p>The SSL or TLS encryption is set up based ONLY on the public and privage keys of the Server Certificate. (For both directions of information transfer.) The Client Certificate (which you indicate that you have) is used only for authentication and will be of no use whatsoever in decrypting captured HTTP session data from Wireshark. Now if you had the private key of the Server Certificate, it would be a very different matter.<br />
</p></li><li><p>One way to capture the traffic for analysis without using a browser (and without using a Wireshark capture) is to use <em>Fiddler 2</em> or <em>Charles</em> as a local man-in-the-middle HTTPS proxy. To do this you need to be able to change the proxy setup of your browser.<br />
</p></li></ol><p>Inetdog</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 18:41</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p><span>inetdog</span><br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Mar '12, 18:43</strong> </span></p></div></div><div id="comments-container-9667" class="comments-container"></div><div id="comment-tools-9667" class="comment-tools"></div><div class="clear"></div><div id="comment-9667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

