+++
type = "question"
title = "can NOT capture secure packets eg https"
description = '''my wireshark sniffer does not capture ssl/secure packets... searching packets for ssl or tcp.port == 443 gives nothing... any tip, to check/repair it? Interface is correct (only wifi have wep g)... also logged in Paypal and Gmail, but nothing...'''
date = "2011-09-08T08:22:00Z"
lastmod = "2011-09-08T15:36:00Z"
weight = 6211
keywords = [ "ssl", "secure", "https" ]
aliases = [ "/questions/6211" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [can NOT capture secure packets eg https](/questions/6211/can-not-capture-secure-packets-eg-https)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6211-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>my wireshark sniffer does not capture ssl/secure packets... searching packets for ssl or tcp.port == 443</p><p>gives nothing... any tip, to check/repair it? Interface is correct (only wifi have wep g)... also logged in Paypal and Gmail, but nothing...</p></div><div id="question-tags" class="tags-container tags">ssl secure https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '11, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/83f6c157853b4626dfd333b3a7f6fd9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lse123ws&#39;s gravatar image" /><p>lse123ws<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lse123ws has no accepted answers">0%</span></p></div></div><div id="comments-container-6211" class="comments-container"></div><div id="comment-tools-6211" class="comment-tools"></div><div class="clear"></div><div id="comment-6211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6222"></span>

<div id="answer-container-6222" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6222-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're capturing on an encrypted (if you want to call a WEP connection encrypted, it's more of an obfuscation nowadays :-)) you might not see anything useful until you decrypt the traffic, provided you have access to the encryption keys. I guess that's also why the filters do not match anything - because stuff is still encrypted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '11, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-6222" class="comments-container"></div><div id="comment-tools-6222" class="comment-tools"></div><div class="clear"></div><div id="comment-6222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

