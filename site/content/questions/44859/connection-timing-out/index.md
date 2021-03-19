+++
type = "question"
title = "Connection timing out"
description = '''I&#x27;m investigating an intermittent problem involving the transfer of data. An internal client application sends data to a server accessible over the internet. The communication uses SSL. Recently, the transfer of data has started to fail. Application logs show a &#x27;connection time out&#x27; message. Applica...'''
date = "2015-08-05T02:17:00Z"
lastmod = "2015-08-06T04:55:00Z"
weight = 44859
keywords = [ "ssl", "timeout" ]
aliases = [ "/questions/44859" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Connection timing out](/questions/44859/connection-timing-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44859-score" class="post-score" title="current number of votes">0</div><span id="post-44859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm investigating an intermittent problem involving the transfer of data. An internal client application sends data to a server accessible over the internet. The communication uses SSL.</p><p>Recently, the transfer of data has started to fail. Application logs show a 'connection time out' message. Application providers say it's not a software fault. All other internet bound services are operating without issues and this is an isolated issue.</p><p>Questions:</p><ol><li>What would you look out for in a WireShark capture? Are there any specific filters etc that would be useful in this scenario?</li><li>A firewall capture taken during a failed transfer, shows a RST near the end of the capture, from the server 30secs after the previous packet in that conversation. I suspect the timer is controlled by a time out setting in the application but what I don't understand is if thats the case, why would the RST be sent from the remote server and not the client where the application is hosted?</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '15, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/7ed8c3ce35fb8f90f49428398992b223?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brad_101&#39;s gravatar image" /><p><span>Brad_101</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brad_101 has no accepted answers">0%</span></p></div></div><div id="comments-container-44859" class="comments-container"></div><div id="comment-tools-44859" class="comment-tools"></div><div class="clear"></div><div id="comment-44859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44880"></span>

<div id="answer-container-44880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44880-score" class="post-score" title="current number of votes">0</div><span id="post-44880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Without seeing a capture it's a lot of guesswork but here is my try.</p><ol><li>I would start looking whether the TLS handshake was successful and real data transfer was going on.<br />
An indication is that the tcp payload starts with 17030x Filter: <code>tcp[12,20:2]==50:1703||tcp[12,32:2]==80:1703</code></li><li>If the firewall trace shows a RESET coming from the server exactly 30 seconds after the previous packet then it is likely a timer at the server that is causing the connectin to be closed. But maybe the RST does not really come from the server but from a device in between. Check the ip.ttl of the reset and see if it matches the server's TTLs from previous packets.</li></ol><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '15, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div></div><div id="comments-container-44880" class="comments-container"><span id="44886"></span><div id="comment-44886" class="comment"><div id="post-44886-score" class="comment-score"></div><div class="comment-text"><p>Thanks Matthias.</p><p>Here are two seperate traces captured from firewall during a successful data transfer and during an unsuccessful transfer.</p><p>The failure trace is different to the caputre I was referring too previously so the 30 sec time out is different (looks like it's higher in this case).</p><p>Success trace = <a href="https://drive.google.com/file/d/0BxWWq7ozi-PFZnc2eEFSZnh6blU/view?usp=sharing">https://drive.google.com/file/d/0BxWWq7ozi-PFZnc2eEFSZnh6blU/view?usp=sharing</a> Failure trace = <a href="https://drive.google.com/file/d/0BxWWq7ozi-PFUW4yeUZUcGlBZFU/view?usp=sharing">https://drive.google.com/file/d/0BxWWq7ozi-PFUW4yeUZUcGlBZFU/view?usp=sharing</a></p><p>The TTL on the RST is different to the TTL in previous packets.</p><p>For what reason would another device send the RST? Is that normal?</p></div><div id="comment-44886-info" class="comment-info"><span class="comment-age">(05 Aug '15, 13:21)</span> <span class="comment-user userinfo">Brad_101</span></div></div><span id="44889"></span><div id="comment-44889" class="comment"><div id="post-44889-score" class="comment-score"></div><div class="comment-text"><p>The failing trace shows that your firewall resets the connection because the server didn't send a syn_ack within 30 seconds.</p><p>So the real problem is that the server does not accept your 4th tcp connection (tcp.stream==3). It -might- be because your client application didn't close the 3rd connection (tcp.stream==2) as it did with tcp.stream=0 of tcp.stream==1.</p></div><div id="comment-44889-info" class="comment-info"><span class="comment-age">(05 Aug '15, 14:14)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="44904"></span><div id="comment-44904" class="comment"><div id="post-44904-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response Matthias.</p><p>How do you know that it's the firewall resetting the connection? Is it assumed it's that device because the server hasn't sent a SYN_ACK?</p><p>From looking at the success trace, it seems the client didn't send a FIN for streams 5 &amp; 6 either.<br />
</p><p>Does that change your thoughts in response to your comment in the second paragraph?</p></div><div id="comment-44904-info" class="comment-info"><span class="comment-age">(06 Aug '15, 03:46)</span> <span class="comment-user userinfo">Brad_101</span></div></div><span id="44905"></span><div id="comment-44905" class="comment"><div id="post-44905-score" class="comment-score"></div><div class="comment-text"><p>"How do I know it's the FW sending the RST?" I don't know, I guess from the TTL 64 which is a well known initial ttl value (for linux based systems) - and it would make sense if a firewall resets a connection that never fully established after a certain amount of time.</p><p>In the success case the server actively terminates the connections after 15 seconds. I don't know the application protocol so I cannot comment on whether it is good behaviour by the client to keep sessions open if they're no longer needed. And the success case doesn't show another new session attempt while the sessions are still in FINWAIT2 state.</p><p>But there are many possibilities why the server doesn't respond to your syn requests.</p></div><div id="comment-44905-info" class="comment-info"><span class="comment-age">(06 Aug '15, 04:55)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-44880" class="comment-tools"></div><div class="clear"></div><div id="comment-44880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

