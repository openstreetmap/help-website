+++
type = "question"
title = "Decrypting SSL traffic over a Proxy"
description = '''I would like to decrypt TLS traffic. Normally I know how to do this, but in this case I do not have a direct connection to the server. Instead, I need to access the server over a web proxy. My proxy listens on port 8080. My client performs an HTTP CONNECT to the proxy to connect with port 443 of my ...'''
date = "2017-05-31T05:09:00Z"
lastmod = "2017-05-31T05:09:00Z"
weight = 61708
keywords = [ "tls", "proxy" ]
aliases = [ "/questions/61708" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting SSL traffic over a Proxy](/questions/61708/decrypting-ssl-traffic-over-a-proxy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61708-score" class="post-score" title="current number of votes">0</div><span id="post-61708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to decrypt TLS traffic. Normally I know how to do this, but in this case I do not have a direct connection to the server. Instead, I need to access the server over a web proxy.</p><p>My proxy listens on port 8080. My client performs an <code>HTTP CONNECT</code> to the proxy to connect with port 443 of my server. After that, the SSL traffic between client and server is tunneled.</p><p>Diffie-Hellman is deactivated; the Cipher Suite is <code>TLS_RSA_WITH_AES_256_CBC_SHA</code>. I have the Certificate with Private Key in the RSA keys list. In this list, I have the IP address and port of the proxy.</p><p>However, Wireshark doesn't decrypt the traffic and I don't know why. Is it possible to decrypt traffic with this setup?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '17, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/a2c23c2f7f917ac5ead4ee58ac748293?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChristophAlbert&#39;s gravatar image" /><p><span>ChristophAlbert</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChristophAlbert has no accepted answers">0%</span></p></div></div><div id="comments-container-61708" class="comments-container"></div><div id="comment-tools-61708" class="comment-tools"></div><div class="clear"></div><div id="comment-61708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

