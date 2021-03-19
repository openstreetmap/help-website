+++
type = "question"
title = "DCE RPC Question"
description = '''I have a user who prints out of an application to a centralized server everyone uses and when he prints from his pc it&#x27;s normal times. However, when printing out of the application its taking 40 seconds one time 1:15 another. When looking through my capture I see a delta of 59 seconds and a few pack...'''
date = "2017-02-14T13:59:00Z"
lastmod = "2017-02-14T13:59:00Z"
weight = 59425
keywords = [ "rpc", "dce", "question" ]
aliases = [ "/questions/59425" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DCE RPC Question](/questions/59425/dce-rpc-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59425-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a user who prints out of an application to a centralized server everyone uses and when he prints from his pc it's normal times. However, when printing out of the application its taking 40 seconds one time 1:15 another. When looking through my capture I see a delta of 59 seconds and a few packets above this the PC request something then 59 seconds later the server responds with nca_s_fault_cancel and when look this up online I don't understand what it's doing to be honest. If anyone could point me in the right direction I would appreciate it.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">rpc dce question</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '17, 13:59</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p>rock90<br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div></div><div id="comments-container-59425" class="comments-container"><span id="59438"></span><div id="comment-59438" class="comment"><div id="post-59438-score" class="comment-score"></div><div class="comment-text"><p>Can you upload a trace file, please?</p><p>To analyze RPC we have to identify the transport protocol (plain TCP or SMB or SMB2). We also need a few details from the handshake.</p><p>Can you please upload a trace file that includes the begins (for plan TCP) with the TCP session on port 135 plus all following frames or with the SMB handshake.</p><p>Please be advised that the SMB/SMB2 handshake might include a password. Details depend on your individual configuration.</p></div><div id="comment-59438-info" class="comment-info"><span class="comment-age">(15 Feb '17, 11:28)</span> packethunter</div></div><span id="64154"></span><div id="comment-64154" class="comment"><div id="post-64154-score" class="comment-score"></div><div class="comment-text"><p>Hello,</p><p>Have you ever found a solution for your question? We have the same captures on an RDS environment where we experience freezes when opening windows explorer or trying to print.</p><p>Thank you, Kind regards,</p><p>KrisV</p></div><div id="comment-64154-info" class="comment-info"><span class="comment-age">(24 Oct '17, 05:50)</span> krisv</div></div></div><div id="comment-tools-59425" class="comment-tools"></div><div class="clear"></div><div id="comment-59425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

