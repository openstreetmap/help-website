+++
type = "question"
title = "MSSQL Keep-alive/RST Troubleshooting"
description = '''We have a billing package that uses MSSQL as it&#x27;s backend. On a physical machine, there are no issues with the software. In a VM on my system, the software will remain connected to the SQL server (looks like through keep-alives). In a wireshark trace, I can see the keep alive packets and the ACK pac...'''
date = "2016-09-22T12:38:00Z"
lastmod = "2016-09-25T05:56:00Z"
weight = 55758
keywords = [ "rst", "ack", "mssql", "keep-alive" ]
aliases = [ "/questions/55758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MSSQL Keep-alive/RST Troubleshooting](/questions/55758/mssql-keep-aliverst-troubleshooting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55758-score" class="post-score" title="current number of votes">0</div><span id="post-55758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a billing package that uses MSSQL as it's backend. On a physical machine, there are no issues with the software. In a VM on my system, the software will remain connected to the SQL server (looks like through keep-alives). In a wireshark trace, I can see the keep alive packets and the ACK packets back. Eventually, it looks like the server sends RST packets to the client and that is what breaks the connection and causes the software to stop working (gives a bunch of errors and crashes). What I am trying to determine is why is only this VM affected and if it is software (VMWare, the network driver, etc) or is it my host (no issues running anything on the host). If I can upload the capture somewhere, I would be happy to provide. Thanks for any help that can be offered.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-mssql" rel="tag" title="see questions tagged &#39;mssql&#39;">mssql</span> <span class="post-tag tag-link-keep-alive" rel="tag" title="see questions tagged &#39;keep-alive&#39;">keep-alive</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '16, 12:38</strong></p><img src="https://secure.gravatar.com/avatar/994c03d60b24fdb85343c17923e4e124?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmcwhirter&#39;s gravatar image" /><p><span>bmcwhirter</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmcwhirter has no accepted answers">0%</span></p></div></div><div id="comments-container-55758" class="comments-container"><span id="55773"></span><div id="comment-55773" class="comment"><div id="post-55773-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-55773-info" class="comment-info"><span class="comment-age">(23 Sep '16, 02:07)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="55775"></span><div id="comment-55775" class="comment"><div id="post-55775-score" class="comment-score"></div><div class="comment-text"><p>I've been trying to create an account on CloudShark since I posted this question. Their main site works but when I confirm my email address, the page takes forever to load then says that CloudShark is unavailable. I'll keep trying.</p></div><div id="comment-55775-info" class="comment-info"><span class="comment-age">(23 Sep '16, 06:29)</span> <span class="comment-user userinfo">bmcwhirter</span></div></div><span id="55776"></span><div id="comment-55776" class="comment"><div id="post-55776-score" class="comment-score"></div><div class="comment-text"><p>Finally got it uploaded. Is this what you need? <a href="https://www.cloudshark.org/captures/6e68c2d61fa7">https://www.cloudshark.org/captures/6e68c2d61fa7</a></p><p>.19 is the MSSQL server and .96 is the client VM.</p></div><div id="comment-55776-info" class="comment-info"><span class="comment-age">(23 Sep '16, 08:10)</span> <span class="comment-user userinfo">bmcwhirter</span></div></div></div><div id="comment-tools-55758" class="comment-tools"></div><div class="clear"></div><div id="comment-55758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55810"></span>

<div id="answer-container-55810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55810-score" class="post-score" title="current number of votes">0</div><span id="post-55810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, the teardown packet (via RST) is coming from the server, so it's not the physical or virtual client that aborts the connection. The RST looks to me like a connection abort (RST is sometimes also used as a "normal" shutdown of a connection) - the question is, what did the client do to annoy the server that much?</p><p>What is odd is how frequently the client uses Keep-Alives - one per 30 seconds is quite normal, but you see that it often fires a series of packets in a few microseconds (especially right before the RSTs).</p><p>This is what I would do:</p><ol><li>Take a capture of a working setup to compare the behavior between the two setups. What does the client do differently?</li><li>Take a capture at the server (if you can) to check if the same packets are seen on both ends - sometimes, firewalls and other middle boxes may be responsible for this kind of thing, e.g. when they suspect malicious behavior (which the rapid fire keep-alives may be considered as)</li></ol><p>Also, try to capture with a dedicated capture device/laptop, and NOT on the end system (client or server). Here's why: <a href="https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '16, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '16, 05:56</strong> </span></p></div></div><div id="comments-container-55810" class="comments-container"></div><div id="comment-tools-55810" class="comment-tools"></div><div class="clear"></div><div id="comment-55810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

