+++
type = "question"
title = "tcp syn/ack packet retransmission"
description = '''I am seeing this behavior on our network, i.e., the syn+ack packets being retransmitted even though an ack packet was received. Initially, I thought the ack packet was being lost but capturing on the server showed that the ack packet was received. Digging deeper I noticed that a web browser (172.16....'''
date = "2015-07-27T08:21:00Z"
lastmod = "2015-07-28T13:20:00Z"
weight = 44528
keywords = [ "syn+ack", "retransmissions", "tcp" ]
aliases = [ "/questions/44528" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp syn/ack packet retransmission](/questions/44528/tcp-synack-packet-retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44528-score" class="post-score" title="current number of votes">0</div><span id="post-44528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am seeing this behavior on our network, i.e., the syn+ack packets being retransmitted even though an ack packet was received. Initially, I thought the ack packet was being lost but capturing on the server showed that the ack packet was received. Digging deeper I noticed that a web browser (172.16.49.134) would open 6 simultaneous connections to the web server (172.16.1.39) and while one connection would receive data the other 5 would sit idle and exhibit the same behaviour as in the attached packet capture and eventually get closed.</p><p><a href="https://www.cloudshark.org/captures/36ce590618f0">https://www.cloudshark.org/captures/36ce590618f0</a></p><p>The server is running RedHat Linux: [<span class="__cf_email__" data-cfemail="ec9e838398ac84839f98828d8189">[email protected]</span> tmp]# uname -a Linux hostname 2.6.18-371.11.1.el5 #1 SMP Mon Jun 30 04:53:12 EDT 2014 i686 i686 i386 GNU/Linux</p><p>netstat -i doesn't show errors or dropped packets. Is this normal?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syn+ack" rel="tag" title="see questions tagged &#39;syn+ack&#39;">syn+ack</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '15, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/e7d1d3994349a9ea0554a6430dbe2ec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="naskop&#39;s gravatar image" /><p><span>naskop</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="naskop has no accepted answers">0%</span></p></div></div><div id="comments-container-44528" class="comments-container"></div><div id="comment-tools-44528" class="comment-tools"></div><div class="clear"></div><div id="comment-44528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44546"></span>

<div id="answer-container-44546" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44546-score" class="post-score" title="current number of votes">1</div><span id="post-44546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Everything has gone normal. But then the Client does not send application Data and for that kind of reason the server sends the syn,ack again, because he hadn´t anything more (Paket 4). And the client acknowledge this again(Paket 5). Afterthat the client closes the session with a normal session close (FIN), perhaps he really has nothng to send.</p><p>A similar question could be found here: <a href="https://ask.wireshark.org/questions/43648/spurious-retransmission-and-dup-ack">https://ask.wireshark.org/questions/43648/spurious-retransmission-and-dup-ack</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '15, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-44546" class="comments-container"><span id="44565"></span><div id="comment-44565" class="comment"><div id="post-44565-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the input Christian. I also found this link which explains the behavior: <a href="https://ask.wireshark.org/questions/33690/tcp-handshake-question">https://ask.wireshark.org/questions/33690/tcp-handshake-question</a> Any suggestions why the client would pause that long before making the GET request? I am seeing this also on sessions that do have actual data transferred.</p></div><div id="comment-44565-info" class="comment-info"><span class="comment-age">(28 Jul '15, 08:09)</span> <span class="comment-user userinfo">naskop</span></div></div><span id="44568"></span><div id="comment-44568" class="comment"><div id="post-44568-score" class="comment-score"></div><div class="comment-text"><p>First of allI think the link you posted in your comment describes another problem. Then I can see that the server sends the answer to a different mac address ( it is different from the source mac of the syn request) Could you provide a trace with a request inside?</p></div><div id="comment-44568-info" class="comment-info"><span class="comment-age">(28 Jul '15, 09:27)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44576"></span><div id="comment-44576" class="comment"><div id="post-44576-score" class="comment-score"></div><div class="comment-text"><p>I have sanitized the original capture and it also changed the devices MAC addresses. The server sends the frame to the gateway's vrrp virtual mac address</p></div><div id="comment-44576-info" class="comment-info"><span class="comment-age">(28 Jul '15, 13:14)</span> <span class="comment-user userinfo">naskop</span></div></div><span id="44577"></span><div id="comment-44577" class="comment"><div id="post-44577-score" class="comment-score"></div><div class="comment-text"><p>Ok. No then I just have the idea, that it could be application related. But as I told a trace with a request inside would be helpful.</p></div><div id="comment-44577-info" class="comment-info"><span class="comment-age">(28 Jul '15, 13:20)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-44546" class="comment-tools"></div><div class="clear"></div><div id="comment-44546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

