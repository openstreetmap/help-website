+++
type = "question"
title = "Decrypting radius packets not working"
description = '''I am trying to decrypt the password sent from a NAS device to a RADIUS server. I know the shared-secret key and have entered it in Preferences--&amp;gt;Protocols--&amp;gt;Radius--&amp;gt;Shared Key However in the wireshark decode, I would expect the password to be shown. However it doesn&#x27;t appear to decode/decr...'''
date = "2014-04-09T09:35:00Z"
lastmod = "2014-04-10T00:29:00Z"
weight = 31675
keywords = [ "decryption", "radius" ]
aliases = [ "/questions/31675" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting radius packets not working](/questions/31675/decrypting-radius-packets-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31675-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to decrypt the password sent from a NAS device to a RADIUS server. I know the shared-secret key and have entered it in Preferences--&gt;Protocols--&gt;Radius--&gt;Shared Key</p><p>However in the wireshark decode, I would expect the password to be shown. However it doesn't appear to decode/decrypt properly.</p><p>What am I missing?</p></div><div id="question-tags" class="tags-container tags">decryption radius</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '14, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/3a479abf51a39ef972afd093836e173d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimmy-work&#39;s gravatar image" /><p>jimmy-work<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimmy-work has no accepted answers">0%</span></p></div></div><div id="comments-container-31675" class="comments-container"></div><div id="comment-tools-31675" class="comment-tools"></div><div class="clear"></div><div id="comment-31675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31705"></span>

<div id="answer-container-31705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31705-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>RADIUS generally just carries the password as supplied by the client as it is. So it is up to the client to use whatever scheme like PAP,CHAP, PEAP to encrypt the password, which the RADIUS server will then send to the authenticating server via say LDAP or a SQL database for verification.</p><p>The shared key is used for the client (say a switch, wireless access point) to be able to authenticate the and trust the RADIUS server it is sending requests to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '14, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '14, 00:31</p></div></div><div id="comments-container-31705" class="comments-container"></div><div id="comment-tools-31705" class="comment-tools"></div><div class="clear"></div><div id="comment-31705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

