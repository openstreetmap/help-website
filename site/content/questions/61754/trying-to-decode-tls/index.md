+++
type = "question"
title = "trying to decode TLS"
description = '''I&#x27;m trying to decrypt some TLS data that is coming to one of my local applications. From my research it seems like i&#x27;m supposed to set an SSLKEYLOGFILE environment variable and then point wireshark SSL to that file and then all TLS data should be encrypted. I did that and the data is still encrypted...'''
date = "2017-06-02T16:26:00Z"
lastmod = "2017-06-03T10:26:00Z"
weight = 61754
keywords = [ "tls", "ssl", "tlsv1.2" ]
aliases = [ "/questions/61754" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [trying to decode TLS](/questions/61754/trying-to-decode-tls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61754-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decrypt some TLS data that is coming to one of my local applications. From my research it seems like i'm supposed to set an SSLKEYLOGFILE environment variable and then point wireshark SSL to that file and then all TLS data should be encrypted. I did that and the data is still encrypted though... Is there something i'm missing?</p></div><div id="question-tags" class="tags-container tags">tls ssl tlsv1.2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '17, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/065a89fea561f43cd2ea6afb99d8275b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogidmt&#39;s gravatar image" /><p>yogidmt<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogidmt has no accepted answers">0%</span></p></div></div><div id="comments-container-61754" class="comments-container"></div><div id="comment-tools-61754" class="comment-tools"></div><div class="clear"></div><div id="comment-61754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61757"></span>

<div id="answer-container-61757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61757-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you researched the Wiki <a href="https://wiki.wireshark.org/SSL">page on SSL</a>?</p><p>Amongst other useful information, that page also informs you that the SSLKEYLOGFILE environment variable is for use with Firefox and Chrome\Chromium and is unlikely to work with your own application.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '17, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61757" class="comments-container"></div><div id="comment-tools-61757" class="comment-tools"></div><div class="clear"></div><div id="comment-61757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

