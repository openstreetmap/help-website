+++
type = "question"
title = "throughput measurement, graph"
description = '''Hi,  Im currently working on my Bachelor theses, and have a problem. The goal is to show differences among TCP variants. As far as know, the biggest difference is based on Congestion Avoidance, which Id like to demonstrate by unplugging one site of the communication and than take a look at how quick...'''
date = "2013-03-18T07:14:00Z"
lastmod = "2013-03-18T13:31:00Z"
weight = 19617
keywords = [ "control", "throughput", "tcp", "congestion" ]
aliases = [ "/questions/19617" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [throughput measurement, graph](/questions/19617/throughput-measurement-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19617-score" class="post-score" title="current number of votes">0</div><span id="post-19617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I<code>m currently working on my Bachelor theses, and have a problem. The goal is to show differences among TCP variants. As far as know, the biggest difference is based on Congestion Avoidance, which I</code>d like to demonstrate by unplugging one site of the communication and than take a look at how quickly those different TCP types can recover from that "disconnection". To determine that, i need a very exact output (graph) that would show that. IS IT POSSIBLE IN WIRESHARK?</p><p>Thank you very much in advance,</p><p>Radim Havlicek</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-control" rel="tag" title="see questions tagged &#39;control&#39;">control</span> <span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-congestion" rel="tag" title="see questions tagged &#39;congestion&#39;">congestion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Mar '13, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/198f364985a629d7dd0991bc6a838e21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="radim0574&#39;s gravatar image" /><p><span>radim0574</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="radim0574 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Mar '13, 09:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19617" class="comments-container"></div><div id="comment-tools-19617" class="comment-tools"></div><div class="clear"></div><div id="comment-19617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19618"></span>

<div id="answer-container-19618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19618-score" class="post-score" title="current number of votes">1</div><span id="post-19618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, Have you looked at the different TCP stream graphs? Especially the tcptrace variant? (See: "Statistics -&gt; TCP StreamGraph -&gt; Time-Sequence Graph (tcptrace)")</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '13, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19618" class="comments-container"><span id="19626"></span><div id="comment-19626" class="comment"><div id="post-19626-score" class="comment-score"></div><div class="comment-text"><p>thank you for your answer. Yes, i did but than doesn`t provide all i need, which is:exact time (yes), bandwidth (yes), current RTT (no), congestion window (no). I need to determine where exactly the connection is back (which packet), and when exactly does the throughput gets into the same level as it was before the disconnection.</p><p>Radim</p></div><div id="comment-19626-info" class="comment-info"><span class="comment-age">(18 Mar '13, 13:31)</span> <span class="comment-user userinfo">radim0574</span></div></div></div><div id="comment-tools-19618" class="comment-tools"></div><div class="clear"></div><div id="comment-19618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19625"></span>

<div id="answer-container-19625" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19625-score" class="post-score" title="current number of votes">0</div><span id="post-19625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would also make use of the Statistics:Flow Graph which represents the details and direction of the TCP packets as they flow between the hosts.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Mar '13, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-19625" class="comments-container"></div><div id="comment-tools-19625" class="comment-tools"></div><div class="clear"></div><div id="comment-19625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

