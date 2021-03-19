+++
type = "question"
title = "Is there a bug regarding the AMQP dissector?"
description = '''Hello everybody, I am currently working on an AMQP pusblisher implementation and I am a bit confused. According to the specification of the protocol (http://www.amqp.org/sites/amqp.org/files/amqp.pdf), an AMQP value can also be a list. However, when I use a list as content of the AMQP value, Wiresha...'''
date = "2017-02-22T06:29:00Z"
lastmod = "2017-02-22T09:53:00Z"
weight = 59606
keywords = [ "subscriber", "publisher", "amqp", "bug" ]
aliases = [ "/questions/59606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a bug regarding the AMQP dissector?](/questions/59606/is-there-a-bug-regarding-the-amqp-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59606-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody,</p><p>I am currently working on an AMQP pusblisher implementation and I am a bit confused. According to the specification of the protocol (<a href="http://www.amqp.org/sites/amqp.org/files/amqp.pdf),">http://www.amqp.org/sites/amqp.org/files/amqp.pdf),</a> an AMQP value can also be a list. However, when I use a list as content of the AMQP value, Wireshark gives me the following error: Unexpected list type at frame position 28 of field "AMQP Value".</p><p>Therefore I would like to ask whether there is a known bug in the Wireshark dissector of the AMQP protocol. Note: my AMQP test subscriber from QPID is able to decode the sent message correctly.</p><p>Thank you for your reply in advance.</p><p>Best regards, Mario</p></div><div id="question-tags" class="tags-container tags">subscriber publisher amqp bug</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '17, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/128b142c3a9292444f555b1aad741960?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dranigl&#39;s gravatar image" /><p>dranigl<br />
<span class="score" title="14 reputation points">14</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dranigl has no accepted answers">0%</span></p></div></div><div id="comments-container-59606" class="comments-container"><span id="59615"></span><div id="comment-59615" class="comment"><div id="post-59615-score" class="comment-score"></div><div class="comment-text"><p>What Wireshark version?</p></div><div id="comment-59615-info" class="comment-info"><span class="comment-age">(22 Feb '17, 09:53)</span> grahamb ♦</div></div></div><div id="comment-tools-59606" class="comment-tools"></div><div class="clear"></div><div id="comment-59606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59614"></span>

<div id="answer-container-59614" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59614-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark bugs are held in <a href="https://bugs.wireshark.org">Bugzilla</a>, so if it is known it will be listed there.</p><p>If you can't see a bug entry for the issue, please raise one attaching a capture that illustrates the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '17, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59614" class="comments-container"></div><div id="comment-tools-59614" class="comment-tools"></div><div class="clear"></div><div id="comment-59614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

