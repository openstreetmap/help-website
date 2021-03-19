+++
type = "question"
title = "scsi transfer limited due to allocation length too small"
description = '''Im having slow read/write performance on my iscsi san. The packet traces show this message frequently &quot;scsi transfer limited due to allocation length too small&quot;. Any one have an idea of why these messages show up in the traces? Tushar.'''
date = "2012-04-26T15:03:00Z"
lastmod = "2013-06-10T09:19:00Z"
weight = 10469
keywords = [ "allocation", "transfer", "scsi", "length", "small" ]
aliases = [ "/questions/10469" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [scsi transfer limited due to allocation length too small](/questions/10469/scsi-transfer-limited-due-to-allocation-length-too-small)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10469-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im having slow read/write performance on my iscsi san. The packet traces show this message frequently "scsi transfer limited due to allocation length too small". Any one have an idea of why these messages show up in the traces? Tushar.</p></div><div id="question-tags" class="tags-container tags">allocation transfer scsi length small</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '12, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/b7cb3cdffa3d69b446038a1f44db1423?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tushar&#39;s gravatar image" /><p>tushar<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tushar has no accepted answers">0%</span></p></div></div><div id="comments-container-10469" class="comments-container"></div><div id="comment-tools-10469" class="comment-tools"></div><div class="clear"></div><div id="comment-10469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21884"></span>

<div id="answer-container-21884" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21884-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm somewhat new to the protocol, but I've spent the last week writing iSCSI and SCSI device emulation code. I've seen what you're talking about, and am about to implement the solutions into my emulation layer.... So what I think is happening there is the Inquery commmand sends out an inquery with the minimum allocaton length (36 bytes). However, that allocation length is not large enough to hold the response coming in. What should happen is the inquery will be reissued with a larger allocation length. Sometimes this occurs after a few other packets. I've seen this happen only on the INQUERY command EVPD flag is 0,but SCSI is obviously a big complex protocol and I THINK it can happen with lots of different commands. Again, I'm a bit new to this... there are hundreds of scsi commands and over a dozen iSCSI commands... and I'm currently just in the process of bashing through the issues as they come.</p><p>How this might contribute to the slowness on your SAN is maybe dependent on how often and which commands are generating these issues. Most of the SCSI traffic is going to be Read/Write requests (followed by "Data In" responses). If you're seeing these messages in response to REad/Write requests, then maybe the client doesn't like the buffer lengths that the server is wanting to send back. There's supposed to be a negotiation when the iSCSI protocol is connected that determines the agreed-upon maximum transfer size. In my case I think it is around 8K.<br />
</p><p>If they're only occurring on other control messages, then I think you're looking at a red herring.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '13, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/90b414fbb6c4fa323edd08b76a56a228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="evilrobot&#39;s gravatar image" /><p>evilrobot<br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="evilrobot has one accepted answer">100%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jun '13, 09:35</p></div></div><div id="comments-container-21884" class="comments-container"></div><div id="comment-tools-21884" class="comment-tools"></div><div class="clear"></div><div id="comment-21884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

