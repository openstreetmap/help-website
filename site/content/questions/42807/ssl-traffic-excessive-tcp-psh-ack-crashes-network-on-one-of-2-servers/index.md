+++
type = "question"
title = "SSL traffic excessive TCP PSH ACK crashes network on one of 2 servers"
description = '''What is the best way to filter traffic to see why a pair of servers which are built identical, one of them will cause the network to come to a screeching halt while the other one quietly does its job and works properly? SQL is running on them for an application. I have a capture of both of them, the...'''
date = "2015-06-01T10:44:00Z"
lastmod = "2015-06-01T15:09:00Z"
weight = 42807
keywords = [ "push", "ssl", "resets", "traffic", "high" ]
aliases = [ "/questions/42807" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSL traffic excessive TCP PSH ACK crashes network on one of 2 servers](/questions/42807/ssl-traffic-excessive-tcp-psh-ack-crashes-network-on-one-of-2-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42807-score" class="post-score" title="current number of votes">0</div><span id="post-42807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the best way to filter traffic to see why a pair of servers which are built identical, one of them will cause the network to come to a screeching halt while the other one quietly does its job and works properly? SQL is running on them for an application. I have a capture of both of them, the noisy ones expert info shows</p><p>ACKed segment that wasn't captured (common at capture start)1026 The transmission window is now completely full 154 TCP 'Previous segment not captured (common at capture start)' There are about 20 connection resets and 18 TCP zero window segment.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-push" rel="tag" title="see questions tagged &#39;push&#39;">push</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-resets" rel="tag" title="see questions tagged &#39;resets&#39;">resets</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-high" rel="tag" title="see questions tagged &#39;high&#39;">high</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '15, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/dfb8a08ccce532d92ead089aa98daf21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MacBee&#39;s gravatar image" /><p><span>MacBee</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MacBee has no accepted answers">0%</span></p></div></div><div id="comments-container-42807" class="comments-container"></div><div id="comment-tools-42807" class="comment-tools"></div><div class="clear"></div><div id="comment-42807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42809"></span>

<div id="answer-container-42809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42809-score" class="post-score" title="current number of votes">0</div><span id="post-42809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A server that brings "the network to a screeching halt"?! That sounds really strange, because servers should not have that much power over the network performance, and if they do something is really really going wrong.</p><p>Can you share your captures? Because your symptoms are not really telling much. "Previous segment not captured" could be packet loss, but they can also be dropped packets. Connection resets are normal as well these days and need closer investigation to see if they mean trouble. Zero Window is most interesting, as it points to a performance problem of the server that sends the Window size of zero.</p><p>Use <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> if you can share the capture, if not, see if you can sanitize it with <a href="https://www.tracewrangler.com">TraceWrangler</a> first.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42809" class="comments-container"><span id="42811"></span><div id="comment-42811" class="comment"><div id="post-42811-score" class="comment-score"></div><div class="comment-text"><p>I ran the tracewrangler on it but the file size is too large according to the cloudshark site..they are 50Megabyte and larger..</p><p>B</p></div><div id="comment-42811-info" class="comment-info"><span class="comment-age">(01 Jun '15, 11:52)</span> <span class="comment-user userinfo">MacBee</span></div></div><span id="42812"></span><div id="comment-42812" class="comment"><div id="post-42812-score" class="comment-score"></div><div class="comment-text"><p>Okay, then maybe you got access to something like Dropbox that doesn't restrict your file size?</p></div><div id="comment-42812-info" class="comment-info"><span class="comment-age">(01 Jun '15, 11:59)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42817"></span><div id="comment-42817" class="comment"><div id="post-42817-score" class="comment-score"></div><div class="comment-text"><p>Yes I do, if you send me your email address I will send you a link.</p><p>Bee</p></div><div id="comment-42817-info" class="comment-info"><span class="comment-age">(01 Jun '15, 13:18)</span> <span class="comment-user userinfo">MacBee</span></div></div><span id="42819"></span><div id="comment-42819" class="comment"><div id="post-42819-score" class="comment-score"></div><div class="comment-text"><p>Okay, send it to jasper [ät] packet-foo.com</p></div><div id="comment-42819-info" class="comment-info"><span class="comment-age">(01 Jun '15, 15:09)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-42809" class="comment-tools"></div><div class="clear"></div><div id="comment-42809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

