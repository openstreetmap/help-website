+++
type = "question"
title = "SIP TLS is only shown as TCP"
description = '''I&#x27;m using an older version of Wireshark, which perfectly decodes SIP TLS traffic with port 5061 as TLS. With newer versions (e.g. 2.4.2) the same packets are simply decoded as TCP. I&#x27;ve checked the settings for the protocols. SIP-TLS port 5061 is set per default in the SIP protocol setting in the ol...'''
date = "2017-10-24T05:12:00Z"
lastmod = "2017-10-24T11:05:00Z"
weight = 64151
keywords = [ "tls", "sip" ]
aliases = [ "/questions/64151" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [SIP TLS is only shown as TCP](/questions/64151/sip-tls-is-only-shown-as-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64151-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using an older version of Wireshark, which perfectly decodes SIP TLS traffic with port 5061 as TLS. With newer versions (e.g. 2.4.2) the same packets are simply decoded as TCP. I've checked the settings for the protocols. SIP-TLS port 5061 is set per default in the SIP protocol setting in the old and in the current version. I've tried a workaround and added port 5061 to SSL/TLS ports of HTTP. This partly helps to decode SIP-TLS as TLS at least in one direction. However, this looks like a Wireshark bug, or did I just miss a setting that resloves my problem? Any ideas?</p></div><div id="question-tags" class="tags-container tags">tls sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '17, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/52ad30c06760b5d9ee6ddd1c881db694?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rolstein&#39;s gravatar image" /><p>rolstein<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rolstein has no accepted answers">0%</span></p></div></div><div id="comments-container-64151" class="comments-container"><span id="64152"></span><div id="comment-64152" class="comment"><div id="post-64152-score" class="comment-score"></div><div class="comment-text"><p>Screenshots</p></div><div id="comment-64152-info" class="comment-info"><span class="comment-age">(24 Oct '17, 05:25)</span> rolstein</div></div><span id="64153"></span><div id="comment-64153" class="comment"><div id="post-64153-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/SIP-TLS_default_setting_uWdBb4a.jpg" width="640" /> <img src="https://osqa-ask.wireshark.org/upfiles/SIP-TLS_only_shown_as_TCP_with_Wireshark_default_setting_9PZgjw2.jpg" width="640" /> <img src="https://osqa-ask.wireshark.org/upfiles/SIP-TLS_port_5061_added_to_SSL_in_HTTP_FuxKHku.jpg" width="640" /> <img src="https://osqa-ask.wireshark.org/upfiles/SIP-TLS_shown_as_TLS_after_port_5061_added_to_SSL_in_HTTP_g5aIfla.jpg" width="640" /></p></div><div id="comment-64153-info" class="comment-info"><span class="comment-age">(24 Oct '17, 05:27)</span> rolstein</div></div></div><div id="comment-tools-64151" class="comment-tools"></div><div class="clear"></div><div id="comment-64151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64160"></span>

<div id="answer-container-64160" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64160-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That looks like a bug in <code>proto_reg_handoff_sip()</code> failing to properly call <code>ssl_dissector_[add|delete]()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '17, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></img></div></div><div id="comments-container-64160" class="comments-container"><span id="64164"></span><div id="comment-64164" class="comment"><div id="post-64164-score" class="comment-score"></div><div class="comment-text"><p>Yes, that code was just wrong. I fixed it in <a href="https://code.wireshark.org/review/24041">this change</a>, so the current tip of the master branch, and the next 2.4.x release, should have that particular problem fixed.</p></div><div id="comment-64164-info" class="comment-info"><span class="comment-age">(24 Oct '17, 12:10)</span> Guy Harris ♦♦</div></div><span id="64174"></span><div id="comment-64174" class="comment"><div id="post-64174-score" class="comment-score"></div><div class="comment-text"><p>OK, thanks. Then I'll be waiting for the next version</p></div><div id="comment-64174-info" class="comment-info"><span class="comment-age">(24 Oct '17, 22:00)</span> rolstein</div></div></div><div id="comment-tools-64160" class="comment-tools"></div><div class="clear"></div><div id="comment-64160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

