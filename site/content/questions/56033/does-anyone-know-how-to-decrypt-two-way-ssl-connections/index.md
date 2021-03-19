+++
type = "question"
title = "Does anyone know how to decrypt two way SSL connections?"
description = '''Hi, Does anyone know how to decrypt two way SSL connections? I have client and server private keys. Thanks'''
date = "2016-09-30T13:23:00Z"
lastmod = "2016-10-16T13:31:00Z"
weight = 56033
keywords = [ "clientauthentication" ]
aliases = [ "/questions/56033" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does anyone know how to decrypt two way SSL connections?](/questions/56033/does-anyone-know-how-to-decrypt-two-way-ssl-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56033-score" class="post-score" title="current number of votes">0</div><span id="post-56033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Does anyone know how to decrypt two way SSL connections? I have client and server private keys.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-clientauthentication" rel="tag" title="see questions tagged &#39;clientauthentication&#39;">clientauthentication</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '16, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/2225544834d3a980a2310a9fd18a0b56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juniorr&#39;s gravatar image" /><p><span>Juniorr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juniorr has no accepted answers">0%</span></p></div></div><div id="comments-container-56033" class="comments-container"></div><div id="comment-tools-56033" class="comment-tools"></div><div class="clear"></div><div id="comment-56033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56396"></span>

<div id="answer-container-56396" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56396-score" class="post-score" title="current number of votes">1</div><span id="post-56396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can add the certificates under Edit | Preferences | Protocols | SSL . You need to capture the entire conversation - including the initial handshake. There is a great presentation that goes into detail about it:</p><p><a href="https://www.wireshark.org/lists/wireshark-users/201001/msg00151.html">https://www.wireshark.org/lists/wireshark-users/201001/msg00151.html</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '16, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/0ca762ea8fec4622f09ecc44fc10384c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Keseymour&#39;s gravatar image" /><p><span>Keseymour</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Keseymour has no accepted answers">0%</span></p></div></div><div id="comments-container-56396" class="comments-container"></div><div id="comment-tools-56396" class="comment-tools"></div><div class="clear"></div><div id="comment-56396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56425"></span>

<div id="answer-container-56425" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56425-score" class="post-score" title="current number of votes">0</div><span id="post-56425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In a TLS session with mutual authentication there are two certificates involved:</p><ul><li>The server certificate.</li><li>The client certificate.</li></ul><p>The server certificate is used for authentication and <em>may</em> (or may not) be used for key exchange. The client certificate is used for authentication only.</p><p>Practically speaking, if you only have only a private RSA key for the client, you cannot perform any decryption. If you have a private RSA key for the server <em>and</em> the server is agreeing on a RSA key exchange, you can configure the RSA private key at Preferences -&gt; Protocols -&gt; SSL -&gt; RSA Keys list. Otherwise, if a Diffie-Hellman key exchange (instead of a RSA one) is in use, even posession of the RSA private key file will not allow you to decrypt the session (use the SSL Keylog file instead).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '16, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-56425" class="comments-container"></div><div id="comment-tools-56425" class="comment-tools"></div><div class="clear"></div><div id="comment-56425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

