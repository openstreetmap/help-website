+++
type = "question"
title = "Q.921 decoding mistake"
description = '''I analyze SCTP/Q.921 IUA/Q.931 message and wireshark version 1.4.3 decodes them correctly. In a newer version (2.2.4) however, the IUA.DLCI.SAPI = 0 value is decoded as Radio Signaling Procedures and the upper layers get corrupted. In the older wireshark version the same parameter value is decoded a...'''
date = "2017-03-03T00:23:00Z"
lastmod = "2017-03-03T02:47:00Z"
weight = 59816
keywords = [ "q.921", "q.931" ]
aliases = [ "/questions/59816" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Q.921 decoding mistake](/questions/59816/q921-decoding-mistake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59816-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I analyze SCTP/Q.921 IUA/Q.931 message and wireshark version 1.4.3 decodes them correctly.</p><p>In a newer version (2.2.4) however, the IUA.DLCI.SAPI = 0 value is decoded as Radio Signaling Procedures and the upper layers get corrupted. In the older wireshark version the same parameter value is decoded as Call Control Procedures and the upper layer are shown correctly.</p><p>Reference, page 11: <a href="https://www.itu.int/rec/dologin_pub.asp?lang=e&amp;id=T-REC-Q.921-199709-I!!PDF-E&amp;type=items">https://www.itu.int/rec/dologin_pub.asp?lang=e&amp;id=T-REC-Q.921-199709-I!!PDF-E&amp;type=items</a></p><p>Please look at it and correct if possible.</p><p>Thank you Mark Ersek</p></div><div id="question-tags" class="tags-container tags">q.921 q.931</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '17, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/a2c6c708f46c93cd6fa41883b6b36d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark%20Ersek&#39;s gravatar image" /><p>Mark Ersek<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark Ersek has no accepted answers">0%</span></p></div></div><div id="comments-container-59816" class="comments-container"><span id="59818"></span><div id="comment-59818" class="comment"><div id="post-59818-score" class="comment-score">1</div><div class="comment-text"><p>A proper filed <a href="https://bugs.wireshark.org/bugzilla/">bug report</a>, with sample capture, would get you a long way of getting this solved.</p></div><div id="comment-59818-info" class="comment-info"><span class="comment-age">(03 Mar '17, 01:38)</span> Jaap ♦</div></div></div><div id="comment-tools-59816" class="comment-tools"></div><div class="clear"></div><div id="comment-59816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59821"></span>

<div id="answer-container-59821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59821-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In newer Wireshark, go to IUA dissector preferences and uncheck "Use GSM SAPI values" option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '17, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-59821" class="comments-container"><span id="59822"></span><div id="comment-59822" class="comment"><div id="post-59822-score" class="comment-score"></div><div class="comment-text"><p>Thanks, this helps. Mark</p></div><div id="comment-59822-info" class="comment-info"><span class="comment-age">(03 Mar '17, 02:59)</span> Mark Ersek</div></div></div><div id="comment-tools-59821" class="comment-tools"></div><div class="clear"></div><div id="comment-59821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

