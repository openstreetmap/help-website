+++
type = "question"
title = "Howt to distinguish multiple conversations with the same addr1/port1 and addr2/port2 pair"
description = '''I am writing a dissector of a non-stateless protocol atop TCP. Suppose that there are multiple TCP streams with the same addr1/port1 and addr2/port2 pair, and that I want to assign each one a separate conversation, how to distinguish them within my dissecting context? Any guidance will be appreciate...'''
date = "2015-09-27T19:22:00Z"
lastmod = "2015-09-27T19:24:00Z"
weight = 46203
keywords = [ "conversation", "dissector", "tcp" ]
aliases = [ "/questions/46203" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Howt to distinguish multiple conversations with the same addr1/port1 and addr2/port2 pair](/questions/46203/howt-to-distinguish-multiple-conversations-with-the-same-addr1port1-and-addr2port2-pair)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46203-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a dissector of a non-stateless protocol atop TCP. Suppose that there are multiple TCP streams with the same addr1/port1 and addr2/port2 pair, and that I want to assign each one a separate conversation, how to distinguish them within my dissecting context?</p><p>Any guidance will be appreciated. Thanks.<br />
</p></div><div id="question-tags" class="tags-container tags">conversation dissector tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '15, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/1cb482522da3759460225164456f68a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peng%20Zheng&#39;s gravatar image" /><p>Peng Zheng<br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peng Zheng has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-46203" class="comments-container"></div><div id="comment-tools-46203" class="comment-tools"></div><div class="clear"></div><div id="comment-46203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46204"></span>

<div id="answer-container-46204" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46204-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess you can use the tcp.stream index. It's counted up for each new conversation using the same 5-tuple.</p><p>See also <a href="https://blog.packet-foo.com/2015/05/port-numbers-reused/">https://blog.packet-foo.com/2015/05/port-numbers-reused/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '15, 19:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-46204" class="comments-container"><span id="46213"></span><div id="comment-46213" class="comment"><div id="post-46213-score" class="comment-score"></div><div class="comment-text"><p>"assign each one a separate conversation", TCP already does it (create conversation) for me, so all I have to do is to check whether a per conversation data for my own protocol exists, if not, just create one and add it to the conversation. Right?</p></div><div id="comment-46213-info" class="comment-info"><span class="comment-age">(28 Sep '15, 02:21)</span> Peng Zheng</div></div></div><div id="comment-tools-46204" class="comment-tools"></div><div class="clear"></div><div id="comment-46204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

