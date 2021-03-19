+++
type = "question"
title = "TLS1.2 with client cert auth doesn&#x27;t send &quot;Certificate Verify&quot; message"
description = '''As part of the TLS handshake with client cert authentication, the client sends a &quot;Certificate Verify&quot; message (https://ask.wireshark.org/questions/43671/certificate-verify-message). What I have found from capturing packet dumps with Wireshark on multiple machines (Windows 10, Windows 2012 R2) is tha...'''
date = "2016-05-20T08:35:00Z"
lastmod = "2016-05-20T08:35:00Z"
weight = 52808
keywords = [ "tls", "ssl", "handshake", "windows" ]
aliases = [ "/questions/52808" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TLS1.2 with client cert auth doesn't send "Certificate Verify" message](/questions/52808/tls12-with-client-cert-auth-doesnt-send-certificate-verify-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52808-score" class="post-score" title="current number of votes">0</div><span id="post-52808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As part of the TLS handshake with client cert authentication, the client sends a "Certificate Verify" message (<a href="https://ask.wireshark.org/questions/43671/certificate-verify-message).">https://ask.wireshark.org/questions/43671/certificate-verify-message).</a></p><p>What I have found from capturing packet dumps with Wireshark on multiple machines (Windows 10, Windows 2012 R2) is that the Certificate Verify message is NEVER sent with TLS1.2.</p><p>However, if I explicitly set it to TLS1.1 or TLS1.0, the cert verify message is indeed sent and the connection is established.</p><p>Therefore, I need to know why this message isn't sent with TLS1.2 (at least on newer versions of Windows) and how can I get it to send that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '16, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/31718f77afbeabccddd4e78e531da5ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Noam%20Marks&#39;s gravatar image" /><p><span>Noam Marks</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Noam Marks has no accepted answers">0%</span></p></div></div><div id="comments-container-52808" class="comments-container"></div><div id="comment-tools-52808" class="comment-tools"></div><div class="clear"></div><div id="comment-52808-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

