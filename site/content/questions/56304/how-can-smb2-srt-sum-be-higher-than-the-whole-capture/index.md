+++
type = "question"
title = "How can SMB2 SRT sum be higher than the whole capture"
description = '''Hi, I have a dedicated link between two office that are in two different province. I need to transfer around 1GB file between the two office with a Mac Pro and we are stucked with an old Os version that still use SMBv1. Right now, I have a really slow transfer with the mac, but high transfer speed w...'''
date = "2016-10-11T18:38:00Z"
lastmod = "2016-10-24T06:59:00Z"
weight = 56304
keywords = [ "sum", "smb2", "smb", "srt" ]
aliases = [ "/questions/56304" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can SMB2 SRT sum be higher than the whole capture](/questions/56304/how-can-smb2-srt-sum-be-higher-than-the-whole-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56304-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a dedicated link between two office that are in two different province. I need to transfer around 1GB file between the two office with a Mac Pro and we are stucked with an old Os version that still use SMBv1. Right now, I have a really slow transfer with the mac, but high transfer speed when I use a windows instead (SMBv2). On the local network, the Mac Pro has no transfer speed issue.</p><p>The link has 9ms latency. I'm trying to find why SMBv1 and this mac is so slow on this link. I though it was becase the number of SMB request x avg latency.</p><p>However, when I look at the capture I did on my windows with SMBv2, the whole capture took 20sec, but when I check the SRT for SMB and I check the SRT (sum) for Write and Read SMB request, they are at around 180sec.</p><p>How is that possible if my capture only took 20sec?</p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags">sum smb2 smb srt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '16, 18:38</strong></p><img src="https://secure.gravatar.com/avatar/4280011fbed5b664bc69f36be9fc683e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JasonR&#39;s gravatar image" /><p>JasonR<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JasonR has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Oct '16, 19:56</p></div></div><div id="comments-container-56304" class="comments-container"></div><div id="comment-tools-56304" class="comment-tools"></div><div class="clear"></div><div id="comment-56304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56609"></span>

<div id="answer-container-56609" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56609-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>SMB2 can transfer multiple blocks at the same time. This is done to reduce the effect of large round-trip times on the response time. If the file transfer was using 10 simultaneous SMB2 read commands, each taking 18 seconds, the sum of smb2.time would be 180 seconds, even touch the wall-clock time only showed that 18 seconds have passed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '16, 06:59</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-56609" class="comments-container"></div><div id="comment-tools-56609" class="comment-tools"></div><div class="clear"></div><div id="comment-56609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

