+++
type = "question"
title = "Why is UDP 443 interpreted as QUIC?"
description = '''I captured traffic on my WLAN adapter while connected to my VPN, and all of the traffic which I know to be HTTP over SSL is being interpreted as QUIC. I understand that Google has attempted to hijack UDP 443 for its new protocol, but most of us still hold to the IANA standard that UDP 443 is HTTPS, ...'''
date = "2016-06-13T11:25:00Z"
lastmod = "2016-06-15T13:45:00Z"
weight = 53414
keywords = [ "443", "ssl", "quic", "https", "iana" ]
aliases = [ "/questions/53414" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is UDP 443 interpreted as QUIC?](/questions/53414/why-is-udp-443-interpreted-as-quic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53414-score" class="post-score" title="current number of votes">0</div><span id="post-53414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured traffic on my WLAN adapter while connected to my VPN, and all of the traffic which I know to be HTTP over SSL is being interpreted as QUIC.</p><p>I understand that Google has attempted to hijack UDP 443 for its new protocol, but most of us still hold to the IANA standard that UDP 443 is HTTPS, and Wireshark should interpret it that way as long as HTTPS is the far more common usage of that port.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-443" rel="tag" title="see questions tagged &#39;443&#39;">443</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-quic" rel="tag" title="see questions tagged &#39;quic&#39;">quic</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-iana" rel="tag" title="see questions tagged &#39;iana&#39;">iana</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '16, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/b468e4e16e13d50e47e4eda1e7b6ca02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael_Romans&#39;s gravatar image" /><p><span>Michael_Romans</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael_Romans has no accepted answers">0%</span></p></div></div><div id="comments-container-53414" class="comments-container"><span id="53428"></span><div id="comment-53428" class="comment"><div id="post-53428-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-53428-info" class="comment-info"><span class="comment-age">(14 Jun '16, 01:19)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="53472"></span><div id="comment-53472" class="comment"><div id="post-53472-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap,</p><p>I'll get another capture when I get back to my hotel tonight. Every time I connect to my VPN at SharkFest the tunnel breaks.</p></div><div id="comment-53472-info" class="comment-info"><span class="comment-age">(15 Jun '16, 11:38)</span> <span class="comment-user userinfo">Michael_Romans</span></div></div></div><div id="comment-tools-53414" class="comment-tools"></div><div class="clear"></div><div id="comment-53414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53477"></span>

<div id="answer-container-53477" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53477-score" class="post-score" title="current number of votes">0</div><span id="post-53477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The QUIC dissector registers for that port static guint g_quics_port = 443; and hogs the packets. You can turn the dissector off or do decode as.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '16, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-53477" class="comments-container"></div><div id="comment-tools-53477" class="comment-tools"></div><div class="clear"></div><div id="comment-53477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

