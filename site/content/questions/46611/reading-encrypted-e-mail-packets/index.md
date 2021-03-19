+++
type = "question"
title = "reading encrypted e-mail packets"
description = '''i have downloaded wireshark now i want to read captured e-mails. what do the e-mails look like? i am using windows. i have a cisco linksys wireless g broadband wifi'''
date = "2015-10-16T05:33:00Z"
lastmod = "2015-10-16T06:04:00Z"
weight = 46611
keywords = [ "windows" ]
aliases = [ "/questions/46611" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [reading encrypted e-mail packets](/questions/46611/reading-encrypted-e-mail-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46611-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have downloaded wireshark now i want to read captured e-mails. what do the e-mails look like? i am using windows. i have a cisco linksys wireless g broadband wifi</p></div><div id="question-tags" class="tags-container tags">windows</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '15, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/d8a2a0f44a921e8826327262ee410297?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steve328&#39;s gravatar image" /><p>Steve328<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steve328 has no accepted answers">0%</span></p></div></div><div id="comments-container-46611" class="comments-container"></div><div id="comment-tools-46611" class="comment-tools"></div><div class="clear"></div><div id="comment-46611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46616"></span>

<div id="answer-container-46616" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46616-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>cisco linksys wireless g broadband wifi</p></blockquote><p>sounds like a home environment, right?</p><blockquote><p>now i want to read captured e-mails.</p></blockquote><p>That depends how you are accessing the mail server. As these days most of these connections to mail servers are encrypted (HTTPS, IMAPS, etc.) your chances to bee able to read e-mails with Wireshark are pretty bad, unless you own the mail server and are able to get the server RSA key. This is usually impossible with servers like gmail.com, yahoo.com or any other online mail servers and it's rather complicated (up to impossible) to get the key from a company mail server (like Exchange) unless you are the mail server admin.</p><p>If you read your mails through unencrypted channels (POP3, IMAP, HTTP), you would be able to see that in Wireshark, but then I would strongly recommend to switch to encryption, because others would be able to read your e-mail as well!</p><p>So, how do you read your mails?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46616" class="comments-container"></div><div id="comment-tools-46616" class="comment-tools"></div><div class="clear"></div><div id="comment-46616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

