+++
type = "question"
title = "Is there a filter for a Full TCP sequence ?"
description = '''Hello  Is there a filter or a way to filter a complete sequence of tcp full sequence of connection establishment, connection termination, and data transfer?  I want to display all packets belonging to a TCP session'''
date = "2014-04-10T09:16:00Z"
lastmod = "2016-07-18T22:36:00Z"
weight = 31714
keywords = [ "filter", "syn+ack", "fin", "syn", "tcp" ]
aliases = [ "/questions/31714" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a filter for a Full TCP sequence ?](/questions/31714/is-there-a-filter-for-a-full-tcp-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31714-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello<br />
Is there a filter or a way to filter a complete sequence of tcp full sequence of connection establishment, connection termination, and data transfer?<br />
I want to display all packets belonging to a TCP session</p></div><div id="question-tags" class="tags-container tags">filter syn+ack fin syn tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '14, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/40b7cd94ca4446f74aac679ac6dbcf99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ibrahim&#39;s gravatar image" /><p>Ibrahim<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ibrahim has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '14, 10:01</p></div></div><div id="comments-container-31714" class="comments-container"></div><div id="comment-tools-31714" class="comment-tools"></div><div class="clear"></div><div id="comment-31714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31716"></span>

<div id="answer-container-31716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31716-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd suggest a right-click on any packet ot the tcp session and then a "Follow TCP Stream" which translates to a "tcp.stream eq n" with n being an index number of the tcp session in the packet capture. Not sure if I understood your question correctly though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '14, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-31716" class="comments-container"><span id="31718"></span><div id="comment-31718" class="comment"><div id="post-31718-score" class="comment-score"></div><div class="comment-text"><p>I want to display all packets belonging to a TCP session</p></div><div id="comment-31718-info" class="comment-info"><span class="comment-age">(10 Apr '14, 10:01)</span> Ibrahim</div></div><span id="31719"></span><div id="comment-31719" class="comment"><div id="post-31719-score" class="comment-score"></div><div class="comment-text"><p>... and did the above answer NOT do what you wanted to achieve?</p></div><div id="comment-31719-info" class="comment-info"><span class="comment-age">(10 Apr '14, 10:27)</span> mrEEde</div></div></div><div id="comment-tools-31716" class="comment-tools"></div><div class="clear"></div><div id="comment-31716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54149"></span>

<div id="answer-container-54149" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54149-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>U could try by filtering the Source Port and Destination Port along with the MACs...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '16, 22:36</strong></p><img src="https://secure.gravatar.com/avatar/04786a4b8a03e945ce1ad9f285503d4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deepak%20Dominic&#39;s gravatar image" /><p>Deepak Dominic<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deepak Dominic has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jul '16, 22:37</p></div></div><div id="comments-container-54149" class="comments-container"></div><div id="comment-tools-54149" class="comment-tools"></div><div class="clear"></div><div id="comment-54149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

