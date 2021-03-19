+++
type = "question"
title = "Why am I seeing &quot;TCP Window Full&quot; on upload?"
description = '''What would be some of the reasons that I am seeing TCP Window Full flag in Wireshark?  I am performing an upload to my server, and the flag is seen on the packets that the user is sending to the server. '''
date = "2012-07-05T16:57:00Z"
lastmod = "2013-09-10T04:19:00Z"
weight = 12474
keywords = [ "tcp" ]
aliases = [ "/questions/12474" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I seeing "TCP Window Full" on upload?](/questions/12474/why-am-i-seeing-tcp-window-full-on-upload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12474-score" class="post-score" title="current number of votes">0</div><span id="post-12474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What would be some of the reasons that I am seeing <em>TCP Window Full</em> flag in Wireshark? I am performing an upload to my server, and the flag is seen on the packets that the user is sending to the server.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '12, 16:57</strong></p><img src="https://secure.gravatar.com/avatar/7217b1ac7da15eb25ea2cd9c9067dd2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shpakster&#39;s gravatar image" /><p><span>shpakster</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shpakster has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jul '12, 22:20</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-12474" class="comments-container"></div><div id="comment-tools-12474" class="comment-tools"></div><div class="clear"></div><div id="comment-12474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12475"></span>

<div id="answer-container-12475" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12475-score" class="post-score" title="current number of votes">1</div><span id="post-12475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is not really a flag, it's a diagnosis made by Wireshark's TCP expert. It means that Wireshark has seen as many bytes being sent as the receiver signaled to be able to receive before the sender needs to stop and wait for an acknowledgement.</p><p>Depending on how long the acknowledge takes a Window Full situation can slow down data transfers more or less drastically because the sender just can't continue until the ACK comes in. The usual solution to this is to increase the servers receive window size (if possible at all) to allow more data to travel towards the receiver at the same time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '12, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-12475" class="comments-container"><span id="12492"></span><div id="comment-12492" class="comment"><div id="post-12492-score" class="comment-score"></div><div class="comment-text"><p>The server is a Windows 2008 server and window scaling is enabled. Is there anything else that can be done?</p></div><div id="comment-12492-info" class="comment-info"><span class="comment-age">(06 Jul '12, 15:24)</span> <span class="comment-user userinfo">shpakster</span></div></div><span id="24496"></span><div id="comment-24496" class="comment"><div id="post-24496-score" class="comment-score"></div><div class="comment-text"><p>why would this happen? The receiver tells the sender the n-bytes that it can receive, then the sender should just send the n-bytes and no more. I don't understand under what situation would the sender send more data than the window advertised by the receiver. Please help!</p></div><div id="comment-24496-info" class="comment-info"><span class="comment-age">(09 Sep '13, 21:50)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="24521"></span><div id="comment-24521" class="comment"><div id="post-24521-score" class="comment-score"></div><div class="comment-text"><p>The sender NEVER it allowed to send more data than allowed by the reciever specified through recieve window.</p></div><div id="comment-24521-info" class="comment-info"><span class="comment-age">(10 Sep '13, 04:19)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-12475" class="comment-tools"></div><div class="clear"></div><div id="comment-12475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12493"></span>

<div id="answer-container-12493" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12493-score" class="post-score" title="current number of votes">1</div><span id="post-12493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jasper said, the usual solution is to increase the receive window size. The fact that window scaling is in use does not mean that the window size is as large as possible. For example, I'm looking at a trace file right now where both systems advertise a window scale factor of 8 (multiply by 256), but then they only use a window size of value of 256. A window size value of 256 multiplied by the window scaling factor multiplier of 256 gives an actual window size of 65,536 bytes. We could have a window size that large without window scaling. So check the actual receive window size.</p><p>Also, you might check for a lot of lost packets / retransmissions from the server to the client. It's possible that Wireshark and the client think the receiver's window is full because ACKs are getting lost on the way back.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '12, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-12493" class="comments-container"></div><div id="comment-tools-12493" class="comment-tools"></div><div class="clear"></div><div id="comment-12493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

