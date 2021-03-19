+++
type = "question"
title = "File transfer cature question runs slow"
description = '''I have a large capture (185mg)of an excel file transfer across a wan connection from a windows file share to a windows laptop. the file takes a long time to transfer. It&#x27;s using SMB2. After the data is transferred I see thousands of NBSS Continuation Messages. Trying to see if this is normal behavie...'''
date = "2014-12-10T10:38:00Z"
lastmod = "2014-12-10T11:33:00Z"
weight = 38512
keywords = [ "smb2", "smb", "tcp" ]
aliases = [ "/questions/38512" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [File transfer cature question runs slow](/questions/38512/file-transfer-cature-question-runs-slow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38512-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a large capture (185mg)of an excel file transfer across a wan connection from a windows file share to a windows laptop. the file takes a long time to transfer. It's using SMB2. After the data is transferred I see thousands of NBSS Continuation Messages. Trying to see if this is normal behavier. I'm not sure how NBSS is supposed to work</p></div><div id="question-tags" class="tags-container tags">smb2 smb tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '14, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/aec4ca5e380f6923e98c1957f690cc9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johansek&#39;s gravatar image" /><p>johansek<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johansek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '15, 19:08</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-38512" class="comments-container"></div><div id="comment-tools-38512" class="comment-tools"></div><div class="clear"></div><div id="comment-38512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38513"></span>

<div id="answer-container-38513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38513-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>SMB/SMB2 are designed for local file transfers. They are inefficient for transfers across a WAN. They are sensitive to latency. The higher the round-trip latency, the longer the transfer is going to take. FTP is a far more efficient protocol for transfers over a WAN, so you might try transferring the same file via FTP and see how long it takes. If the FTP transfer is quicker, the time difference is simply due to the difference in how the protocols operate. If the FTP transfer takes as long as the SMB2 transfer, then something else is going on.</p><p>If possible, post an actual capture file (assuming it does not contain confidential date) to <a href="http://www.cloudshark.org">Cloudshark</a> or some other publicly accessible place and post a link to the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '14, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-38513" class="comments-container"></div><div id="comment-tools-38513" class="comment-tools"></div><div class="clear"></div><div id="comment-38513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

