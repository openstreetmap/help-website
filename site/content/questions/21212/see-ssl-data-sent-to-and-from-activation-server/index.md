+++
type = "question"
title = "See SSL data sent to and from activation server"
description = '''Would I be able to setup WireShark to interpret the SSL data that is sent and received from a remote activation server?'''
date = "2013-05-17T02:54:00Z"
lastmod = "2013-05-17T03:14:00Z"
weight = 21212
keywords = [ "ssl" ]
aliases = [ "/questions/21212" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [See SSL data sent to and from activation server](/questions/21212/see-ssl-data-sent-to-and-from-activation-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Would I be able to setup WireShark to interpret the SSL data that is sent and received from a remote activation server?</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/00ab27886516c1ebe0908f2fd479c3e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lookoverthere&#39;s gravatar image" /><p>lookoverthere<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lookoverthere has no accepted answers">0%</span></p></div></div><div id="comments-container-21212" class="comments-container"></div><div id="comment-tools-21212" class="comment-tools"></div><div class="clear"></div><div id="comment-21212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21213"></span>

<div id="answer-container-21213" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21213-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If by "remote activation server" you mean a server which you manage yourself, then yes. You can use the private key of the server to decrypt the SSL session. If the "remote activation server" is not under your control and you don't have access to the private key, then you are out-of-luck.</p><p>An alternative would be to use a SSL proxy like <a href="http://fiddler2.com/">Fiddler</a> or <a href="http://www.charlesproxy.com/">Charles</a> to look into the session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '13, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21213" class="comments-container"><span id="21214"></span><div id="comment-21214" class="comment"><div id="post-21214-score" class="comment-score"></div><div class="comment-text"><p>It's a server not under my control unfortunately. Thanks for the other pointers though</p></div><div id="comment-21214-info" class="comment-info"><span class="comment-age">(17 May '13, 03:23)</span> lookoverthere</div></div></div><div id="comment-tools-21213" class="comment-tools"></div><div class="clear"></div><div id="comment-21213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

