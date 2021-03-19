+++
type = "question"
title = "Why is receive window limited from Linux client?"
description = '''Capture: https://www.cloudshark.org/captures/1d1eeadf0ad5 Configuration: Client (Linux 2.6.32-431.30.1.el6.x86_64) --&amp;gt; HTTP GET --&amp;gt; Server (Linux 3.16.6-203.fc20.x86_64) The receive window sent by 10.20.30.254 is no more than 14848; however, the client is configured with: $ sudo sysctl -a | gr...'''
date = "2014-10-29T22:37:00Z"
lastmod = "2014-10-30T08:16:00Z"
weight = 37448
keywords = [ "tcpwindowsize", "linux" ]
aliases = [ "/questions/37448" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why is receive window limited from Linux client?](/questions/37448/why-is-receive-window-limited-from-linux-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37448-score" class="post-score" title="current number of votes">0</div><span id="post-37448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Capture: <a href="https://www.cloudshark.org/captures/1d1eeadf0ad5">https://www.cloudshark.org/captures/1d1eeadf0ad5</a></p><p>Configuration: Client (Linux 2.6.32-431.30.1.el6.x86_64) --&gt; HTTP GET --&gt; Server (Linux 3.16.6-203.fc20.x86_64)</p><p>The receive window sent by 10.20.30.254 is no more than 14848; however, the client is configured with:</p><pre><code>$ sudo sysctl -a | grep rmem
net.core.rmem_max = 2097152
net.core.rmem_default = 1048576
net.ipv4.tcp_rmem = 1048510 1048510 16777216</code></pre><p>The request is made with <code>wget "http://10.20.30.120:9080/silly_webapp/Silly?fn=output&amp;bytes=131072"</code> and strace does not show any usage of SO_RCVBUF:</p><pre><code>socket(PF_INET, SOCK_STREAM, IPPROTO_IP) = 4
connect(4, {sa_family=AF_INET, sin_port=htons(9080), sin_addr=inet_addr(&quot;10.20.30.120&quot;)}, 16) = 0
select(5, NULL, [4], NULL, {900, 0})    = 1 (out [4], left {899, 999994})
write(4, &quot;GET /silly_webapp/Silly?fn=outpu&quot;..., 156) = 156</code></pre><p>Why isn't the initially advertised receive window larger? (I'm investigating an issue where a large response is being delayed and this is the first symptom I noticed.)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '14, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/22c069d7e35bcdeae3046090e5c307e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kgibm&#39;s gravatar image" /><p><span>kgibm</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kgibm has no accepted answers">0%</span></p></div></div><div id="comments-container-37448" class="comments-container"></div><div id="comment-tools-37448" class="comment-tools"></div><div class="clear"></div><div id="comment-37448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37449"></span>

<div id="answer-container-37449" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37449-score" class="post-score" title="current number of votes">2</div><span id="post-37449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kgibm has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is the first offering of the windowsize after the 3-way handshake. It allows for 10 full sized MSS segments. The windowsize will/should open up as the session goes on - if it ever does...<br />
I would say this is a good/common practice to shield the receiving TCP from a mis-behaving sender that does not follow the slowstart algorithm.<br />
Regards Matthias</p><p>Just found this link <a href="http://tools.ietf.org/html/draft-ietf-tcpm-initcwnd-00">http://tools.ietf.org/html/draft-ietf-tcpm-initcwnd-00</a> explaining the 10 MSS .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '14, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Oct '14, 00:00</strong> </span></p></div></div><div id="comments-container-37449" class="comments-container"><span id="37450"></span><div id="comment-37450" class="comment"><div id="post-37450-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I have a different packet capture (which I can't share) where a Linux client advertises a window size of 131328 in the first offering - how is that possible? Is it possible to change the 10 value?</p></div><div id="comment-37450-info" class="comment-info"><span class="comment-age">(29 Oct '14, 23:03)</span> <span class="comment-user userinfo">kgibm</span></div></div><span id="37451"></span><div id="comment-37451" class="comment"><div id="post-37451-score" class="comment-score"></div><div class="comment-text"><p>I should add that the final use case will be a completely internal network with controlled software, so a mis-behaving sender is not a concern and we want to maximize throughput.</p></div><div id="comment-37451-info" class="comment-info"><span class="comment-age">(29 Oct '14, 23:04)</span> <span class="comment-user userinfo">kgibm</span></div></div><span id="37454"></span><div id="comment-37454" class="comment"><div id="post-37454-score" class="comment-score"></div><div class="comment-text"><p>The other linux client offering 131328 is also running RHEL?</p></div><div id="comment-37454-info" class="comment-info"><span class="comment-age">(30 Oct '14, 00:01)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="37459"></span><div id="comment-37459" class="comment"><div id="post-37459-score" class="comment-score"></div><div class="comment-text"><p>Good question, it looks like it is actually Windows 7. Does that have a different first offering size? Or maybe the MSS is bigger (e.g. jumbo frames)?</p></div><div id="comment-37459-info" class="comment-info"><span class="comment-age">(30 Oct '14, 06:54)</span> <span class="comment-user userinfo">kgibm</span></div></div><span id="37461"></span><div id="comment-37461" class="comment"><div id="post-37461-score" class="comment-score"></div><div class="comment-text"><p>Regarding the link you added, are you sure that's about the receiver intial window and not the sender's congestion window?</p></div><div id="comment-37461-info" class="comment-info"><span class="comment-age">(30 Oct '14, 07:07)</span> <span class="comment-user userinfo">kgibm</span></div></div><span id="37466"></span><div id="comment-37466" class="comment not_top_scorer"><div id="post-37466-score" class="comment-score"></div><div class="comment-text"><p>The change specified in this document affects the value of the initial window. So I interpret as being the receiver's initial windowsize.</p><p>Windows and Linux use different TCP stacks and thus operate differently.</p></div><div id="comment-37466-info" class="comment-info"><span class="comment-age">(30 Oct '14, 08:00)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="37468"></span><div id="comment-37468" class="comment not_top_scorer"><div id="post-37468-score" class="comment-score"></div><div class="comment-text"><p>Thanks Matthias!</p></div><div id="comment-37468-info" class="comment-info"><span class="comment-age">(30 Oct '14, 08:16)</span> <span class="comment-user userinfo">kgibm</span></div></div></div><div id="comment-tools-37449" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-37449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

