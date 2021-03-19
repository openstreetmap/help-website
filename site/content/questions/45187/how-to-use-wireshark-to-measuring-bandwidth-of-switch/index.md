+++
type = "question"
title = "How to use wireshark to measuring  bandwidth of switch?"
description = '''i want to monitor bandwidth of switch, can i use wireshark to do it?'''
date = "2015-08-18T01:31:00Z"
lastmod = "2015-08-20T03:56:00Z"
weight = 45187
keywords = [ "bandwidth" ]
aliases = [ "/questions/45187" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use wireshark to measuring bandwidth of switch?](/questions/45187/how-to-use-wireshark-to-measuring-bandwidth-of-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45187-score" class="post-score" title="current number of votes">0</div><span id="post-45187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to monitor bandwidth of switch, can i use wireshark to do it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '15, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/70c1fb6b4249368eec5cd18cfe7aa122?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nghiepnv&#39;s gravatar image" /><p><span>nghiepnv</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nghiepnv has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Aug '15, 05:00</strong> </span></p></div></div><div id="comments-container-45187" class="comments-container"><span id="45190"></span><div id="comment-45190" class="comment"><div id="post-45190-score" class="comment-score">1</div><div class="comment-text"><p>can you please define what you mean by <strong>monitor bandwidth of switch</strong>?</p><p>Please try to be as precise as possible. Maybe a few words about the reason why you want to do that, would also help to understand what you are trying to do.</p></div><div id="comment-45190-info" class="comment-info"><span class="comment-age">(18 Aug '15, 03:10)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45193"></span><div id="comment-45193" class="comment"><div id="post-45193-score" class="comment-score"></div><div class="comment-text"><p>Thank for replay sory! my english is very bad, i mistake between measuring and monitor !!! I want measuring bandwidth at each port of the switch.</p></div><div id="comment-45193-info" class="comment-info"><span class="comment-age">(18 Aug '15, 03:18)</span> <span class="comment-user userinfo">nghiepnv</span></div></div><span id="45218"></span><div id="comment-45218" class="comment"><div id="post-45218-score" class="comment-score"></div><div class="comment-text"><p>you are probably want to use an SNMP Manager to poll the interface statistics of the switch.</p></div><div id="comment-45218-info" class="comment-info"><span class="comment-age">(18 Aug '15, 16:05)</span> <span class="comment-user userinfo">NiCe85</span></div></div><span id="45250"></span><div id="comment-45250" class="comment"><div id="post-45250-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I want measuring bandwidth at each port of the switch.</p></blockquote><p>measure the bandwidth of what?</p><p>Again: If you want any help, you should add as much information as possible, so we can understand what you are trying to do.</p></div><div id="comment-45250-info" class="comment-info"><span class="comment-age">(19 Aug '15, 13:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45254"></span><div id="comment-45254" class="comment"><div id="post-45254-score" class="comment-score"></div><div class="comment-text"><p>i have a server, client will connect to it. I have about 50 client simultaneous working. I want measuring bandwidth at each port of the switch. You can find the technology on my company' website <a href="http://viegrid.com/vi-vn/gi%E1%BA%A3iph%C3%A1pv%C3%A0c%C3%B4ngngh%E1%BB%87/gi%E1%BA%A3iph%C3%A1p/gi%E1%BA%A3iph%C3%A1ph%E1%BA%A1t%E1%BA%A7ng/b%E1%BB%99gi%E1%BA%A3iph%C3%A1pvazurdanhhi%E1%BB%87usaokhu%C3%AA2015.aspx">Viegrid</a> , it name is V-AZUR. I want comparing my old switch vs switch cisco.</p></div><div id="comment-45254-info" class="comment-info"><span class="comment-age">(19 Aug '15, 18:52)</span> <span class="comment-user userinfo">nghiepnv</span></div></div></div><div id="comment-tools-45187" class="comment-tools"></div><div class="clear"></div><div id="comment-45187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45264"></span>

<div id="answer-container-45264" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45264-score" class="post-score" title="current number of votes">0</div><span id="post-45264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want comparing my old switch vs switch cisco.</p></blockquote><p>O.K. so, you want to compare the <strong>forwarding performance</strong> of your switch. While you can do that with Wireshark (and a lot of work), I won't recommend that, because you would have to capture the traffic with TAPs at ALL interface of the switch in parallel and you also need a lot of clients and servers. These kind of tests are usually done with very expensive testing equipment (Breakingpoint, etc.).</p><blockquote><p>i have a server, client will connect to it. I have about 50 client simultaneous working</p></blockquote><p><strong>However</strong>: you are saying, that you have only <strong>ONE</strong> server and 50 clients. So, the limit is the switch interface connected to the server. No matter which switch you are using, the forwarding capacity won't be the problem compared to the limits of the single attached switch interface to the server, so the proposed test does not make any sense. You won't test the switch. You will only test the performance of the server or the limit of the link (1 Gbit/s, 10 Gbit/s).</p><p>But maybe I'm totally misunderstanding your question. If so, please add more details.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '15, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45264" class="comments-container"></div><div id="comment-tools-45264" class="comment-tools"></div><div class="clear"></div><div id="comment-45264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

