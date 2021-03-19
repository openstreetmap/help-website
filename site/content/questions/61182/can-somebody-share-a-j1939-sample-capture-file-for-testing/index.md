+++
type = "question"
title = "Can somebody share a J1939 sample capture file for testing?"
description = '''Hi all, I&#x27;m looking to test out Wireshark prior to working with a customer. However, I lack a sample file from a J1939 application - does anybody have a few lines they can share for testing purposes? Simply trying to find my way around Wireshark with the J1939 dissector. Any help is much appreciated...'''
date = "2017-05-02T23:43:00Z"
lastmod = "2017-05-03T05:33:00Z"
weight = 61182
keywords = [ "sample", "j1939", "data", "capture" ]
aliases = [ "/questions/61182" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can somebody share a J1939 sample capture file for testing?](/questions/61182/can-somebody-share-a-j1939-sample-capture-file-for-testing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61182-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm looking to test out Wireshark prior to working with a customer. However, I lack a sample file from a J1939 application - does anybody have a few lines they can share for testing purposes? Simply trying to find my way around Wireshark with the J1939 dissector.</p><p>Any help is much appreciated! Best, Martin</p></div><div id="question-tags" class="tags-container tags">sample j1939 data capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '17, 23:43</strong></p><img src="https://secure.gravatar.com/avatar/bb505f6832bb10125678c300fff66aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfcss&#39;s gravatar image" /><p>mfcss<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfcss has no accepted answers">0%</span></p></div></div><div id="comments-container-61182" class="comments-container"></div><div id="comment-tools-61182" class="comment-tools"></div><div class="clear"></div><div id="comment-61182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61186"></span>

<div id="answer-container-61186" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61186-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12366">12366</a> has a sample J1939 capture attached. To get it dissected you have to use 'Decode As'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '17, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-61186" class="comments-container"><span id="61187"></span><div id="comment-61187" class="comment"><div id="post-61187-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!</p></div><div id="comment-61187-info" class="comment-info"><span class="comment-age">(03 May '17, 02:56)</span> mfcss</div></div><span id="61202"></span><div id="comment-61202" class="comment"><div id="post-61202-score" class="comment-score"></div><div class="comment-text"><p>Sorry, link to the screen here: <a href="http://imgur.com/a/xpnqc">http://imgur.com/a/xpnqc</a></p></div><div id="comment-61202-info" class="comment-info"><span class="comment-age">(03 May '17, 05:34)</span> mfcss</div></div><span id="61203"></span><div id="comment-61203" class="comment"><div id="post-61203-score" class="comment-score"></div><div class="comment-text"><p>The sample capture of the bug contains only one message.</p></div><div id="comment-61203-info" class="comment-info"><span class="comment-age">(03 May '17, 06:16)</span> Uli</div></div><span id="61221"></span><div id="comment-61221" class="comment"><div id="post-61221-score" class="comment-score"></div><div class="comment-text"><p>Ok thanks for your reply Uli - in case anybody has a larger file I would be very happy if they could share.</p></div><div id="comment-61221-info" class="comment-info"><span class="comment-age">(03 May '17, 22:11)</span> mfcss</div></div></div><div id="comment-tools-61186" class="comment-tools"></div><div class="clear"></div><div id="comment-61186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61201"></span>

<div id="answer-container-61201" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61201-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi again,</p><p>When I try loading the file I get a screen as below - is it correct that the file only contains a single message? Also, a bit unsure if I've decoded it correctly?</p><p>Is it possible with the J1939 functionality to get the values out in human-readable form?</p><p>Thanks, Martin</p><p><img src="https://i.imgur.com/3FOe1sn.jpg" alt="image link" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '17, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/bb505f6832bb10125678c300fff66aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfcss&#39;s gravatar image" /><p>mfcss<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfcss has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '17, 06:13</p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span></p></div></div><div id="comments-container-61201" class="comments-container"></div><div id="comment-tools-61201" class="comment-tools"></div><div class="clear"></div><div id="comment-61201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

