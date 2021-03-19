+++
type = "question"
title = "TCP Retransmission Issue"
description = '''We keep seeing lots of &quot;TCP Re-transmission&quot;, &quot;TCP DUP Ack&quot; &amp;amp; &quot;&quot; in Wireshark. It appears to us that EVERY TIME the client is sending a request followed by a re-transmission almost immediately. Are we doing any thing wrong on the client side? or even on the server side? Is there any timer we cou...'''
date = "2017-02-13T11:53:00Z"
lastmod = "2017-02-13T13:03:00Z"
weight = 59381
keywords = [ "dup", "ack", "fast", "tcp", "re-transmission" ]
aliases = [ "/questions/59381" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Retransmission Issue](/questions/59381/tcp-retransmission-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59381-score" class="post-score" title="current number of votes">0</div><span id="post-59381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We keep seeing lots of "TCP Re-transmission", "TCP DUP Ack" &amp; "<img src="https://osqa-ask.wireshark.org/upfiles/TCP_Re-transmission_Issue.PNG" alt="TCP Fast Re-transmission" />" in Wireshark. It appears to us that EVERY TIME the client is sending a request followed by a re-transmission almost immediately. Are we doing any thing wrong on the client side? or even on the server side? Is there any timer we could properly adjust to prevent the inappropriate re-transmission?</p><p>Pls. see attached. The client is 10.10.10.70 and the server is 192.168.1.52</p><p>Any help clearing this issue is appreciated.<br />
</p><p>Thank you,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup" rel="tag" title="see questions tagged &#39;dup&#39;">dup</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-fast" rel="tag" title="see questions tagged &#39;fast&#39;">fast</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-re-transmission" rel="tag" title="see questions tagged &#39;re-transmission&#39;">re-transmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '17, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/331b3ed2fb21864d41705b7b188041bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khojal&#39;s gravatar image" /><p><span>Khojal</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khojal has no accepted answers">0%</span> </br></p></img></div></div><div id="comments-container-59381" class="comments-container"></div><div id="comment-tools-59381" class="comment-tools"></div><div class="clear"></div><div id="comment-59381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59382"></span>

<div id="answer-container-59382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59382-score" class="post-score" title="current number of votes">1</div><span id="post-59382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like you captured duplicate packets. Please check out this blog post:</p><p><a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '17, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-59382" class="comments-container"></div><div id="comment-tools-59382" class="comment-tools"></div><div class="clear"></div><div id="comment-59382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59383"></span>

<div id="answer-container-59383" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59383-score" class="post-score" title="current number of votes">1</div><span id="post-59383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Seems like you have captured all frames twice. Please try <code>editcap -D</code> which comes within the wireshark packege, to eleminate the 'red herings'.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '17, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-59383" class="comments-container"><span id="59385"></span><div id="comment-59385" class="comment"><div id="post-59385-score" class="comment-score"></div><div class="comment-text"><p>You right. Thank you Jasper and Christian. That was very helpful.Some how we were capturing twice; however, after we adjusted the capture, we now only see the TCP retransmission issue EVERY TIME the client is requesting a "GetMenuWithPermissions". The server starts to send a<img src="https://osqa-ask.wireshark.org/upfiles/TCP_Re-transmission_Issue_2.PNG" alt="alt text" /> retransmission after about 10 Milli-seconds is it doesn't get an "ACK" from the client? Are we doing any thing wrong from the client or from the server? do we need to adjust any timer for the server re-transmission. Again this issue happens only when the client wants to get "GetMenuWithPermission". Please see attached screen capture.</p><p>Thank you</p></div><div id="comment-59385-info" class="comment-info"><span class="comment-age">(13 Feb '17, 12:55)</span> <span class="comment-user userinfo">Khojal</span></div></div><span id="59386"></span><div id="comment-59386" class="comment"><div id="post-59386-score" class="comment-score">1</div><div class="comment-text"><p>Your capture technique is still not 100% accurate - you have packets way too big, over 4k for the "200 OK"... I recommend not capturing locally on any device involved, but use a SPAN port or TAP instead. Otherwise you'll still be chasing ghosts.</p></div><div id="comment-59386-info" class="comment-info"><span class="comment-age">(13 Feb '17, 13:03)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-59383" class="comment-tools"></div><div class="clear"></div><div id="comment-59383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

