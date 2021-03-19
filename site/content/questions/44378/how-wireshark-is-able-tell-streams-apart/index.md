+++
type = "question"
title = "How wireshark is able tell streams apart."
description = '''Hello All, I am wondering how wireshark is able to tell what frames/packets belong to which stream. It seems to be able to tell where one stream starts and ends even if more than one stream share a single connection. For example if I send more than one HTTP connection using one single socket, wiresh...'''
date = "2015-07-22T11:01:00Z"
lastmod = "2015-07-22T11:06:00Z"
weight = 44378
keywords = [ "follow.tcp.stream", "follow_ssl_stream", "stream", "wireshark" ]
aliases = [ "/questions/44378" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How wireshark is able tell streams apart.](/questions/44378/how-wireshark-is-able-tell-streams-apart)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44378-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I am wondering how wireshark is able to tell what frames/packets belong to which stream. It seems to be able to tell where one stream starts and ends even if more than one stream share a single connection.</p><p>For example if I send more than one HTTP connection using one single socket, wireshark is able to tell that there were two different HTTP requests/replies were exchanged.</p><p>Would this also apply to all other protocols, even it was a custom one (i.e. application-specific protocol)?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream follow_ssl_stream stream wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '15, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/6766ae900e081dbc1ecffa1162f60b3c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hebbo&#39;s gravatar image" /><p>hebbo<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hebbo has no accepted answers">0%</span></p></div></div><div id="comments-container-44378" class="comments-container"></div><div id="comment-tools-44378" class="comment-tools"></div><div class="clear"></div><div id="comment-44378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44379"></span>

<div id="answer-container-44379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44379-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is protocol specific, e.g. if you request multiple things first of all the reply needs to tell how long each thing is. Wireshark is just able to interpret those length indicators just like clients do. If you look at HTTP you'll see it giving a size in the headers with each content that is delivered.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '15, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-44379" class="comments-container"><span id="44380"></span><div id="comment-44380" class="comment"><div id="post-44380-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your time and quick response. I appreciate it.</p><p>I know a bit about HTTP, content length and others. But what if you have two requests coming at around same time and responses sent around same time. The two requests are large enough for the frames from two transactions to be mingled with each other. Would wireshark tell them apart too?</p><p>If you can give me some sort of formal specification that would be fine. I believe I know enough to understand it.</p><p>Thank you again.</p></div><div id="comment-44380-info" class="comment-info"><span class="comment-age">(22 Jul '15, 11:13)</span> hebbo</div></div><span id="44381"></span><div id="comment-44381" class="comment"><div id="post-44381-score" class="comment-score"></div><div class="comment-text"><p>the requests and responses within a single connection are serialized. You can only request a new item when the previous has been delivered.</p></div><div id="comment-44381-info" class="comment-info"><span class="comment-age">(22 Jul '15, 11:19)</span> Jasper ♦♦</div></div></div><div id="comment-tools-44379" class="comment-tools"></div><div class="clear"></div><div id="comment-44379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

