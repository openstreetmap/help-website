+++
type = "question"
title = "Can&#x27;t decrypt ssl traffic"
description = '''I am trying to decrypt SSL traffic between a client and my server. I have added my server&#x27;s private key to wireshark, and I can decrypt data that I send from a test app on my local LAN. I see the following ssl packets: client hello server hello, certificate, server hello done client key exchange, ch...'''
date = "2014-12-18T10:44:00Z"
lastmod = "2014-12-18T13:05:00Z"
weight = 38631
keywords = [ "iis", "ssl_decrypt" ]
aliases = [ "/questions/38631" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't decrypt ssl traffic](/questions/38631/cant-decrypt-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38631-score" class="post-score" title="current number of votes">0</div><span id="post-38631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt SSL traffic between a client and my server. I have added my server's private key to wireshark, and I can decrypt data that I send from a test app on my local LAN.</p><p>I see the following ssl packets:</p><p>client hello server hello, certificate, server hello done client key exchange, change cipher spec, finished change cipher spec, finished HTTP data</p><p>But when I can't decrypt data from a different client.</p><p>I see these ssl packets</p><p>client hello server hello, change cipher spec, encrypted handshake message change cipher spec, encrypted handshake message, application data application data</p><p>There is nothing in the \data\debug_file.txt that indicates that a DH key exchange is going on?</p><p>Can someone explain why the two different clients are behaving differently.</p><p>Is there something on the IIS side I can do to force the clients to connect the same way?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iis" rel="tag" title="see questions tagged &#39;iis&#39;">iis</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '14, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/dff28ce5c2d5bcd36c2b00e3b7641e46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cslewis2014&#39;s gravatar image" /><p><span>cslewis2014</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cslewis2014 has no accepted answers">0%</span></p></div></div><div id="comments-container-38631" class="comments-container"><span id="38632"></span><div id="comment-38632" class="comment"><div id="post-38632-score" class="comment-score"></div><div class="comment-text"><p>What cipher is being used? You can see this in the server hello.</p></div><div id="comment-38632-info" class="comment-info"><span class="comment-age">(18 Dec '14, 11:01)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38633"></span><div id="comment-38633" class="comment"><div id="post-38633-score" class="comment-score"></div><div class="comment-text"><p>It appears to be TLS_RSA..</p></div><div id="comment-38633-info" class="comment-info"><span class="comment-age">(18 Dec '14, 13:05)</span> <span class="comment-user userinfo">cslewis2014</span></div></div></div><div id="comment-tools-38631" class="comment-tools"></div><div class="clear"></div><div id="comment-38631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

