+++
type = "question"
title = "TLS 1.2 Finished message calculation"
description = '''I&#x27;m using TLS_RSA_WITH_AES_256_GCM_SHA384 cipher suite. I tracked all handshake messages and successfully can decrypt the Client Finished message(I verified with wireshark). When I try to calculate the Finished message my self, I can&#x27;t get the same result as in the Finished message I just tracked. I...'''
date = "2016-10-20T00:02:00Z"
lastmod = "2016-10-20T00:21:00Z"
weight = 56526
keywords = [ "tlsv1.2" ]
aliases = [ "/questions/56526" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TLS 1.2 Finished message calculation](/questions/56526/tls-12-finished-message-calculation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56526-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using TLS_RSA_WITH_AES_256_GCM_SHA384 cipher suite. I tracked all handshake messages and successfully can decrypt the Client Finished message(I verified with wireshark).</p><p>When I try to calculate the Finished message my self, I can't get the same result as in the Finished message I just tracked.</p><p>I collected all messages (in my case Client_Hello, Server_Hello, Certificate, Server_Done, Client_Key_Exchange) and then use the following PRF(master_secret, finished_label, Hash(handshake_messages)) finished_label = "client finished"</p><p>When doing Hash(handshake_messages) I'm using the master_secret and SAH384</p><p>Also when collecting the data I'm taking only the message data (No TLS record - The first 5 bytes).</p><p>What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">tlsv1.2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '16, 00:02</strong></p><img src="https://secure.gravatar.com/avatar/bacee67f0acee64cbdea5e568e29dcaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gil%20Fefer&#39;s gravatar image" /><p>Gil Fefer<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gil Fefer has one accepted answer">100%</span></p></div></div><div id="comments-container-56526" class="comments-container"></div><div id="comment-tools-56526" class="comment-tools"></div><div class="clear"></div><div id="comment-56526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56527"></span>

<div id="answer-container-56527" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56527-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just solved it. The following is wrong: When doing Hash(handshake_messages) I'm using the master_secret and SAH384</p><p>What should be done is digest using SHA384 and not Hash with the master_secret.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '16, 00:21</strong></p><img src="https://secure.gravatar.com/avatar/bacee67f0acee64cbdea5e568e29dcaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gil%20Fefer&#39;s gravatar image" /><p>Gil Fefer<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gil Fefer has one accepted answer">100%</span></p></div></div><div id="comments-container-56527" class="comments-container"><span id="56530"></span><div id="comment-56530" class="comment"><div id="post-56530-score" class="comment-score"></div><div class="comment-text"><p>I converted your comment to an answer and accepted it so that it will not be listed as an unanswered question anymore... Please read the FAQ for details.</p></div><div id="comment-56530-info" class="comment-info"><span class="comment-age">(20 Oct '16, 04:14)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-56527" class="comment-tools"></div><div class="clear"></div><div id="comment-56527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

