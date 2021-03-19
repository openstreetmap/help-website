+++
type = "question"
title = "How many retransmissions are considered to be bad"
description = '''Hello, my cuestions is if I have captured 2000 packets and I have retransmissions, how many retransmissions percent is considered to be a problem? Thanks'''
date = "2013-09-02T10:36:00Z"
lastmod = "2013-09-02T11:33:00Z"
weight = 24283
keywords = [ "retransmissions" ]
aliases = [ "/questions/24283" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How many retransmissions are considered to be bad](/questions/24283/how-many-retransmissions-are-considered-to-be-bad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24283-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, my cuestions is if I have captured 2000 packets and I have retransmissions, how many retransmissions percent is considered to be a problem? Thanks</p></div><div id="question-tags" class="tags-container tags">retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '13, 10:36</strong></p><img src="https://secure.gravatar.com/avatar/c350038a7dd33938cf13107a22cfb311?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ogoname&#39;s gravatar image" /><p>ogoname<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ogoname has no accepted answers">0%</span></p></div></div><div id="comments-container-24283" class="comments-container"></div><div id="comment-tools-24283" class="comment-tools"></div><div class="clear"></div><div id="comment-24283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24284"></span>

<div id="answer-container-24284" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24284-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on how much they hurt you or the people using the network. As a simple way to determine the "cost" of the retransmission you see, you should find out how long the communications need to recover from packet loss.</p><p>This is usually determined by finding the packet where the retransmission should have been if it hadn't been lost, and measuring the time until the retransmitted packet arrived. Add all the delays for the connection and ask yourself if the user would notice. My rule of thumb is: everything above a two digit number of millisecond can be noticed. If your total delay goes into seconds, you're in trouble in many cases.</p><p>If you still need a percentage I'd say you should stay well below 10% in the ratio of retransmission to packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '13, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24284" class="comments-container"><span id="24285"></span><div id="comment-24285" class="comment"><div id="post-24285-score" class="comment-score"></div><div class="comment-text"><p>Thank you, very much. Regards</p></div><div id="comment-24285-info" class="comment-info"><span class="comment-age">(02 Sep '13, 11:38)</span> ogoname</div></div></div><div id="comment-tools-24284" class="comment-tools"></div><div class="clear"></div><div id="comment-24284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

