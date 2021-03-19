+++
type = "question"
title = "Tcp Window Size and acknowledgment"
description = '''I read a lot of things about these and I am very confused. If you help me I will be very glad. My questions are: 1-) Does TCP protocol send acknowledgment for every TCP segment or depends on window size?  Because in that link: http://www.firewall.cx/networking-topics/protocols/tcp/130-protocols-tcp-...'''
date = "2011-11-14T15:34:00Z"
lastmod = "2011-11-15T10:54:00Z"
weight = 7428
keywords = [ "window", "tcp", "size" ]
aliases = [ "/questions/7428" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tcp Window Size and acknowledgment](/questions/7428/tcp-window-size-and-acknowledgment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7428-score" class="post-score" title="current number of votes">0</div><span id="post-7428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I read a lot of things about these and I am very confused.</p><p>If you help me I will be very glad.</p><p>My questions are:</p><p>1-) Does TCP protocol send acknowledgment for every TCP segment or depends on window size?</p><p>Because in that link: http://www.firewall.cx/networking-topics/protocols/tcp/130-protocols-tcp-overview.html</p><p><img src="http://www.firewall.cx/images/stories/tcp-quick-overview-6.gif" alt="alt text" /></p><p>It shows because of windows size, it sends one acknowledgment for 3 packets.</p><p>But in that animation: http://www.youtube.com/watch?v=9BuaeEjIeQI&amp;feature=related</p><p>It seems that TCP protocol sends acknowledgment packet for every TCP segment.</p><p>Is Acknowledgment datagram per TCP datagram or per window?</p><p>2-) I downloaded http://media.packetlife.net/media/blog/attachments/424/TCP_example.cap; and I am trying to understand the window size value but I am confused.</p><p>The article says: "Window size is used by the receiver to indicate to the sender the amount of data that it is able to accept. When the amount of data transmitted is equal to the current Window value, the sender will expect a new Window value from the receiver, along with an acknowledgement for the Window just received."</p><p><img src="http://s12.postimage.org/a18k7vz71/Untitled.jpg" alt="alt text" /></p><p>Yes, in the sample .cap; window size is increased for every step but the amount of data that is transmitted is 1514 byte and it is constant. Why is that so?</p><p>Thanks...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '11, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/f28df4e1d1ceb6f6a38657888457a740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sawque&#39;s gravatar image" /><p><span>sawque</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sawque has no accepted answers">0%</span></p></img></div></div><div id="comments-container-7428" class="comments-container"></div><div id="comment-tools-7428" class="comment-tools"></div><div class="clear"></div><div id="comment-7428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7433"></span>

<div id="answer-container-7433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7433-score" class="post-score" title="current number of votes">1</div><span id="post-7433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Part of the confusion is that the first web site you referred to, http://www.firewall.cx/networking-topics/protocols/tcp/130-protocols-tcp-overview.html, is using confusing and incorrect terms. The title of the first graphic you posted says "Window Size = 3." On his web site, the author says "In the above example, we have a window size equal to 3, which means that host B can send 3 data segments to host A before expecting an ACK back." That is not correct. The window size is the amount of data, in bytes, that the receiver can accept. You would not see a window size of 3 bytes unless the receiver was overloaded and unable to keep up with the sender.</p><p>There are lots of good explanations of TCP on the web. I'd Google and find a better one.</p><p>Acknowledgement is per datagram, but because of a feature called Delayed ACK, you might see one acknowledgement for every two datagrams.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '11, 18:24</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></img></div></div><div id="comments-container-7433" class="comments-container"><span id="7437"></span><div id="comment-7437" class="comment"><div id="post-7437-score" class="comment-score">1</div><div class="comment-text"><p>You might even see ACKs after 8,9,10 whatever segments, which is absolutely OK as well - delayed ACK simply states, that the reciever of data does not acknowledge every incoming segment for performance reasons. The exact behaviour depends solely on the Operating System in place which is why on most (MS based) systems there is an ACK for every 2nd incoming segment</p></div><div id="comment-7437-info" class="comment-info"><span class="comment-age">(15 Nov '11, 02:41)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="7450"></span><div id="comment-7450" class="comment"><div id="post-7450-score" class="comment-score"></div><div class="comment-text"><p>You are correct that you might see ACKs less often than every other segment, depending on the implementation. RFC 1122 says that "...in a stream of full sized segments there SHOULD be an ACK for at least every second segment." The use of "SHOULD" means that the implementation can ignore that recommendation if there is good reason to do so.</p></div><div id="comment-7450-info" class="comment-info"><span class="comment-age">(15 Nov '11, 10:54)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-7433" class="comment-tools"></div><div class="clear"></div><div id="comment-7433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

