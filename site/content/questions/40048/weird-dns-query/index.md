+++
type = "question"
title = "Weird DNS Query"
description = '''Hi, Can someone explain why do i get the field Length before the field Transaction ID in this DNS queries ? The query type is TKEY . Can you provide a RFC or something similar ? Because according to the structure of the DNS it should start with the Transaction ID . '''
date = "2015-02-24T08:33:00Z"
lastmod = "2015-02-24T08:46:00Z"
weight = 40048
keywords = [ "dns" ]
aliases = [ "/questions/40048" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Weird DNS Query](/questions/40048/weird-dns-query)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40048-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Can someone explain why do i get the field Length before the field Transaction ID in this DNS queries ?<br />
The query type is TKEY .<br />
Can you provide a RFC or something similar ?<br />
Because according to the structure of the DNS it should start with the Transaction ID .</p><p><img src="https://osqa-ask.wireshark.org/upfiles/weird_dns.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '15, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/cce50cb41e08f84235b3bffa81b24e94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saeedh&#39;s gravatar image" /><p>saeedh<br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saeedh has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-40048" class="comments-container"></div><div id="comment-tools-40048" class="comment-tools"></div><div class="clear"></div><div id="comment-40048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40049"></span>

<div id="answer-container-40049" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40049-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's because it's DNS over TCP, and since the DNS content may be (and is, in your case) spread over multiple segments, the protocol needs to announce how many bytes there are in total for reassembly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '15, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-40049" class="comments-container"><span id="40050"></span><div id="comment-40050" class="comment"><div id="post-40050-score" class="comment-score"></div><div class="comment-text"><p>so the only change is because its over tcp ? meaning can i get now all dns variants that i would normally get in udp but with the addition of those two bytes ? are those bytes a must in dns over tcp ?</p></div><div id="comment-40050-info" class="comment-info"><span class="comment-age">(24 Feb '15, 09:05)</span> saeedh</div></div><span id="40051"></span><div id="comment-40051" class="comment"><div id="post-40051-score" class="comment-score"></div><div class="comment-text"><p>Yes, see <a href="https://www.ietf.org/rfc/rfc1035.txt">RFC 1035</a> sect 4.2.2 TCP usage:</p><blockquote>The message is prefixed with a two byte length field which gives the message length, excluding the two byte length field. This length field allows the low-level processing to assemble a complete message before beginning to parse it.</blockquote></div><div id="comment-40051-info" class="comment-info"><span class="comment-age">(24 Feb '15, 09:10)</span> grahamb ♦</div></div><span id="40053"></span><div id="comment-40053" class="comment"><div id="post-40053-score" class="comment-score"></div><div class="comment-text"><p>yes, you get those two bytes only for TCP, and every time. They are a must.</p></div><div id="comment-40053-info" class="comment-info"><span class="comment-age">(24 Feb '15, 09:10)</span> Jasper ♦♦</div></div></div><div id="comment-tools-40049" class="comment-tools"></div><div class="clear"></div><div id="comment-40049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

