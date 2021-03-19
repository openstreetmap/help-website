+++
type = "question"
title = "Identifying a distant network Packet loss"
description = '''Hi, I have access on the server side. My clients are facing packet loss when they connect to my server. How I calculate the packet loss is by counting the number of packets re-transmitted. Can someone tell me how can I identify which hop to the client has the packet loss? Any help in this case is hi...'''
date = "2015-03-31T18:37:00Z"
lastmod = "2015-04-01T09:48:00Z"
weight = 41072
keywords = [ "packetloss" ]
aliases = [ "/questions/41072" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Identifying a distant network Packet loss](/questions/41072/identifying-a-distant-network-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41072-score" class="post-score" title="current number of votes">0</div><span id="post-41072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have access on the server side. My clients are facing packet loss when they connect to my server.</p><p>How I calculate the packet loss is by counting the number of packets re-transmitted. Can someone tell me how can I identify which hop to the client has the packet loss?</p><p>Any help in this case is highly appreciated.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '15, 18:37</strong></p><img src="https://secure.gravatar.com/avatar/fa1e339a7494976f25c779d187cbfcaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sandy6933&#39;s gravatar image" /><p><span>sandy6933</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sandy6933 has no accepted answers">0%</span></p></div></div><div id="comments-container-41072" class="comments-container"></div><div id="comment-tools-41072" class="comment-tools"></div><div class="clear"></div><div id="comment-41072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41079"></span>

<div id="answer-container-41079" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41079-score" class="post-score" title="current number of votes">0</div><span id="post-41079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can someone tell me <strong>how can I identify which hop</strong> to the client has the packet loss?</p></blockquote><p>In most environments you can't.</p><p>Imagine this:</p><pre><code>Client -- R1 --- R2 ---* R3 ---* R4 --- R5 ---R6 -- Server</code></pre><p>If R3 or R4 is overloaded and drops a frame, it won't inform you in any way about the dropped frame, so there is no way to figure out if R3 or R4 (or any other router) dropped the frame, unless you are able to capture traffic in front and after the router, which is (probably) possible in an enterprise environment, but certainly impossible on the internet</p><pre><code>Client -- R1 --- R2 --- R3 --- R4 --- R5 ---R6 -- Server
                     |      |
                     |      |
                 capture  capture</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '15, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-41079" class="comments-container"><span id="41080"></span><div id="comment-41080" class="comment"><div id="post-41080-score" class="comment-score"></div><div class="comment-text"><p>well, if its <strong>his</strong> server and clients connecting to it I would assume it's his network, so he should be able to move the capture point until he sees original and retransmission (which would indicate where everything was still okay)</p></div><div id="comment-41080-info" class="comment-info"><span class="comment-age">(01 Apr '15, 01:19)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="41101"></span><div id="comment-41101" class="comment"><div id="post-41101-score" class="comment-score"></div><div class="comment-text"><p>the second scenario is for the case where it's his network.</p></div><div id="comment-41101-info" class="comment-info"><span class="comment-age">(01 Apr '15, 09:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-41079" class="comment-tools"></div><div class="clear"></div><div id="comment-41079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

