+++
type = "question"
title = "TLS V1 Record Layer - Fatal, Description: Bad Certificate"
description = '''Hi Wireshark Experts, As a new user to Wireshark, I was looking for some guidance on the following set of logs: https://www.cloudshark.org/captures/cc0dbda0007f In these logs the following error is being thrown which is preventing a user from accessing one our server IPs when using TLS 1.0:  TLS V1 ...'''
date = "2016-09-02T12:57:00Z"
lastmod = "2016-09-02T15:55:00Z"
weight = 55306
keywords = [ "certificate" ]
aliases = [ "/questions/55306" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TLS V1 Record Layer - Fatal, Description: Bad Certificate](/questions/55306/tls-v1-record-layer-fatal-description-bad-certificate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55306-score" class="post-score" title="current number of votes">0</div><span id="post-55306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Wireshark Experts,</p><p>As a new user to Wireshark, I was looking for some guidance on the following set of logs: <a href="https://www.cloudshark.org/captures/cc0dbda0007f">https://www.cloudshark.org/captures/cc0dbda0007f</a></p><p>In these logs the following error is being thrown which is preventing a user from accessing one our server IPs when using TLS 1.0:</p><blockquote><p>TLS V1 Record Layer: Alert (Level: Fatal, Description: Bad Certificate) Content Type: Alert (21) Version: TLS 1.0 (0x0301) Length: 2 Alert Message: Level: Fatal (2) Description: Bad Certificate (42)</p></blockquote><p>Do the logs themselves give a clear indication of why this may be as I'm at a loss? We've doubled checked the certificates as I'm aware the error relates to: <em>"The certificate was corrupt or contained signatures that could not be correctly verified. This alert can occur if the client certificate was signed by a different CA than the one specified in the SSL profile"</em></p><p>Any assistance would be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-certificate" rel="tag" title="see questions tagged &#39;certificate&#39;">certificate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '16, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/d7da3cf132f6595c7fdc2d1ed7706df5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IMrob&#39;s gravatar image" /><p><span>IMrob</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IMrob has no accepted answers">0%</span></p></div></div><div id="comments-container-55306" class="comments-container"></div><div id="comment-tools-55306" class="comment-tools"></div><div class="clear"></div><div id="comment-55306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55311"></span>

<div id="answer-container-55311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55311-score" class="post-score" title="current number of votes">0</div><span id="post-55311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Seems as though not all clients trust the authority of 'DigiCert SHA2 Secure Server CA'. You should check their trust store.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '16, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55311" class="comments-container"></div><div id="comment-tools-55311" class="comment-tools"></div><div class="clear"></div><div id="comment-55311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

