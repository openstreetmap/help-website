+++
type = "question"
title = "Website upload feature failing, Retransmissions and Out Of Order packets present"
description = '''Hi all. I&#x27;m a web developer who&#x27;s on a team developing a feature that allows users to upload files up to 10MB to a government website. We&#x27;re experiencing intermittant problems with this upload feature. The feature works great internally, and in most test environments.  In our UAT environment which m...'''
date = "2011-02-07T19:33:00Z"
lastmod = "2011-02-08T03:15:00Z"
weight = 2211
keywords = [ "retransmissions", "post", "upload", "out-of-order" ]
aliases = [ "/questions/2211" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Website upload feature failing, Retransmissions and Out Of Order packets present](/questions/2211/website-upload-feature-failing-retransmissions-and-out-of-order-packets-present)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2211-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all. I'm a web developer who's on a team developing a feature that allows users to upload files up to 10MB to a government website. We're experiencing intermittant problems with this upload feature. The feature works great internally, and in most test environments.<br />
</p><p>In our UAT environment which mimics prod we're experiencing the following problems:</p><p>POSTs seem to freeze to the web server. They sometimes work, but especially for large files being posted fail. We've tried a few different methods (ajax, flash, silverlight) to upload files, but all of them seem to have trouble with large POST bodys.</p><p>The difference between our working environments and our non-working environments is that we are behind a load balancer (F5), and possible some other fitering devices. I'm not aware of the details of these devices and they are managed by a separate team for security reasons (government is picky here). This equipment has all worked fine before, but we've never had a need to post 10MB files before either.</p><p>When I cap the client side I see a a normal HTTP session, then as soon as the upload fails I see 3 ACKs followed by a Fast Retransmission, then a series of retransmissions then some OOO packets. Would this disrupt a HTTP Post operation?</p></div><div id="question-tags" class="tags-container tags">retransmissions post upload out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '11, 19:33</strong></p><img src="https://secure.gravatar.com/avatar/8365382fba0792018ff5addd2a142812?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kellen_Sunderland&#39;s gravatar image" /><p>Kellen_Sunde...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kellen_Sunderland has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Feb '11, 19:35</p></div></div><div id="comments-container-2211" class="comments-container"></div><div id="comment-tools-2211" class="comment-tools"></div><div class="clear"></div><div id="comment-2211-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2225"></span>

<div id="answer-container-2225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2225-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like your HTTP Post operation gets into trouble at some point. What I would do is try to capture the same upload session on the client and the server at the same time, and then compare where the frames show inconsistencies. I'd probably do this with the exact same file twice, once where it works fine locally and once where it doesn't work remotely.</p><p>My guess would be that at some point the server doesn't receive client data anymore even though the client keeps sending, or maybe the server data gets interrupted as well. If you see that this happens you need to identify the device that disrupts the upload, which can be difficult if there are security rules for capturing network data at systems you do not have access to yourself (or even if you have access).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '11, 03:16</p></div></div><div id="comments-container-2225" class="comments-container"></div><div id="comment-tools-2225" class="comment-tools"></div><div class="clear"></div><div id="comment-2225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

