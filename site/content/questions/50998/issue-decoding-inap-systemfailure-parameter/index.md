+++
type = "question"
title = "Issue decoding INAP SystemFailure (parameter)"
description = '''Hi &#x27;Wireshark&#x27;, I have an issue with decoding a pcap trace containing an INAP error (error on an InitialDP). Wireshark says: BER Error: This field lies beyond the end of the known sequence definition. In my opinion, the packet is okay. And the BER error points to a field (SystemFailure parameter) th...'''
date = "2016-03-17T02:08:00Z"
lastmod = "2016-03-17T03:06:00Z"
weight = 50998
keywords = [ "inap" ]
aliases = [ "/questions/50998" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Issue decoding INAP SystemFailure (parameter)](/questions/50998/issue-decoding-inap-systemfailure-parameter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50998-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi 'Wireshark',</p><p>I have an issue with decoding a pcap trace containing an INAP error (error on an InitialDP).</p><p>Wireshark says:</p><p>BER Error: This field lies beyond the end of the known sequence definition.</p><p>In my opinion, the packet is okay. And the BER error points to a field (SystemFailure parameter) that Wireshark already has decoded properly. What's wrong?</p><p>I used the following wiresharks: 1.10.14 (Red Hat 4.8.3-7)</p><p>Link to pcap (packet number 7 has the 'yellow' decoding error).</p><p><a href="https://www.dropbox.com/s/ofvxa6jdq7kl627/errors.pcap?dl=0">https://www.dropbox.com/s/ofvxa6jdq7kl627/errors.pcap?dl=0</a></p></div><div id="question-tags" class="tags-container tags">inap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '16, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/34b4bce72dcf9f3410dd517437d936b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guadalagara&#39;s gravatar image" /><p>Guadalagara<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guadalagara has no accepted answers">0%</span></p></div></div><div id="comments-container-50998" class="comments-container"></div><div id="comment-tools-50998" class="comment-tools"></div><div class="clear"></div><div id="comment-50998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51000"></span>

<div id="answer-container-51000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51000-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As the issue is still present in 2.0.2, and as to me the message contents seems to be OK too, I'd recommend you to file a bug at <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">Wireshark bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '16, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51000" class="comments-container"><span id="51012"></span><div id="comment-51012" class="comment"><div id="post-51012-score" class="comment-score">1</div><div class="comment-text"><p>A fix is beeing reviewed <a href="https://code.wireshark.org/review/#/c/14501/">https://code.wireshark.org/review/#/c/14501/</a></p></div><div id="comment-51012-info" class="comment-info"><span class="comment-age">(17 Mar '16, 09:19)</span> Anders ♦</div></div><span id="51019"></span><div id="comment-51019" class="comment"><div id="post-51019-score" class="comment-score"></div><div class="comment-text"><p>That is what I call a quick response. Thanxs!</p></div><div id="comment-51019-info" class="comment-info"><span class="comment-age">(18 Mar '16, 03:14)</span> Guadalagara</div></div><span id="51020"></span><div id="comment-51020" class="comment"><div id="post-51020-score" class="comment-score"></div><div class="comment-text"><p>Note that the change is currently only in master, so you'll have to build your own copy, likely to be difficult on such an old platform, or copy the captures over to a more modern platform where you can build from master.</p></div><div id="comment-51020-info" class="comment-info"><span class="comment-age">(18 Mar '16, 03:19)</span> grahamb ♦</div></div><span id="51021"></span><div id="comment-51021" class="comment"><div id="post-51021-score" class="comment-score"></div><div class="comment-text"><p>Noted with thanks.</p></div><div id="comment-51021-info" class="comment-info"><span class="comment-age">(18 Mar '16, 03:28)</span> Guadalagara</div></div></div><div id="comment-tools-51000" class="comment-tools"></div><div class="clear"></div><div id="comment-51000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

