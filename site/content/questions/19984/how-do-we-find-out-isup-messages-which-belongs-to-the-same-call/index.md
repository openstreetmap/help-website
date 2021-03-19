+++
type = "question"
title = "How do we find out ISUP messages which belongs to the same call?"
description = '''I have a pcap file which contains ISUP frames. How do i find out the ISUP messages of a same call? what are the common things which identify the the ISUP messages of a single call uniquely.'''
date = "2013-04-01T01:22:00Z"
lastmod = "2013-04-07T20:49:00Z"
weight = 19984
keywords = [ "message", "isup", "wireshark" ]
aliases = [ "/questions/19984" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do we find out ISUP messages which belongs to the same call?](/questions/19984/how-do-we-find-out-isup-messages-which-belongs-to-the-same-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file which contains ISUP frames. How do i find out the ISUP messages of a same call? what are the common things which identify the the ISUP messages of a single call uniquely.</p></div><div id="question-tags" class="tags-container tags">message isup wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '13, 01:22</strong></p><img src="https://secure.gravatar.com/avatar/b2940a37e14d31283e43c55dc07a1fea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manoj%20G&#39;s gravatar image" /><p>Manoj G<br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manoj G has 2 accepted answers">33%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '13, 01:27</p></div></div><div id="comments-container-19984" class="comments-container"></div><div id="comment-tools-19984" class="comment-tools"></div><div class="clear"></div><div id="comment-19984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20159"></span>

<div id="answer-container-20159" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20159-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OPC(Originating Point Code), DPC(Destination Point Code) and CIC(Circuit Identification Code) for a call is unique. So these parameters can uniquely identify the messages belong to a particular call and differentiate from other calls....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '13, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/b2940a37e14d31283e43c55dc07a1fea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manoj%20G&#39;s gravatar image" /><p>Manoj G<br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manoj G has 2 accepted answers">33%</span></p></div></div><div id="comments-container-20159" class="comments-container"></div><div id="comment-tools-20159" class="comment-tools"></div><div class="clear"></div><div id="comment-20159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19987"></span>

<div id="answer-container-19987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19987-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to find the IAM with the subscriber number you are interested in then you can use the CIC value to get the rest of the messages unfortunatly that will give you all calls on that CIC so you would have to find the end off the call manually.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '13, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-19987" class="comments-container"><span id="20000"></span><div id="comment-20000" class="comment"><div id="post-20000-score" class="comment-score"></div><div class="comment-text"><p>@Anders: Thank you, but i did this already. I thought CIC may identify a call uniquely and when i tried, i got msges of more than one call with same CIC. But i'm not getting to know how manually identify other messages belong to a call having IAM. There should be some parameter to identify messages of a single call even if we are identifying manually. I'm not getting to know what will be that parameter. Any idea?</p></div><div id="comment-20000-info" class="comment-info"><span class="comment-age">(01 Apr '13, 19:58)</span> Manoj G</div></div></div><div id="comment-tools-19987" class="comment-tools"></div><div class="clear"></div><div id="comment-19987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

