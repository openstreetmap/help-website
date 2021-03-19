+++
type = "question"
title = "5 second delay in transmitting.."
description = '''Hi We have been troubleshooting download speed issues for a client of ours. they are using Windows Server 2003 (with Window scaling &amp;amp; Selective ACK turned on). &amp;amp; the client is either Windows XP or Windows 7. We have been carrying out tests by running a test script that downloads a file from ...'''
date = "2011-07-01T07:45:00Z"
lastmod = "2011-07-01T11:32:00Z"
weight = 4883
keywords = [ "delay", "window", "size" ]
aliases = [ "/questions/4883" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [5 second delay in transmitting..](/questions/4883/5-second-delay-in-transmitting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4883-score" class="post-score" title="current number of votes">0</div><span id="post-4883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>We have been troubleshooting download speed issues for a client of ours. they are using Windows Server 2003 (with Window scaling &amp; Selective ACK turned on). &amp; the client is either Windows XP or Windows 7.</p><p>We have been carrying out tests by running a test script that downloads a file from one of our Web Servers multiple times &amp; we note the time taken to download the file each time.</p><p>We have also captured the traffic on the Server &amp; the client during this testing. We can see in the captures that every so often the sending Server waits for approx 5 seconds before continuing to send data.</p><p>Can anyone explain why this would be? Also, if the Receiver announces a TCP Window Size of Zero, apparently the sender should send a very small packet to prompt the receiver to re-announce the Window size. how long does it wait before sending this packet?</p><p>Many thanks Ian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-size" rel="tag" title="see questions tagged &#39;size&#39;">size</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '11, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/4dfdb30f4297c840a2cd7b3b6754fe34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ipittam&#39;s gravatar image" /><p><span>ipittam</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ipittam has no accepted answers">0%</span></p></div></div><div id="comments-container-4883" class="comments-container"></div><div id="comment-tools-4883" class="comment-tools"></div><div class="clear"></div><div id="comment-4883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4885"></span>

<div id="answer-container-4885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4885-score" class="post-score" title="current number of votes">0</div><span id="post-4885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ian,</p><p>My understanding is that when a NIC announces TCP Windows Size of Zero then the recieve buffer is full and it can no longer accept data. The sending computer then sends windows probes to see when the recieve buffer can accept more data. The recieve computer sends a tcp windows update to receive more data. You could identify more of what is happening as the buffer fills up and releases using the filter: "tcp.window_size &lt; == 65535"</p><p>By using the Time Display of View Packets Since Last Captured Packet, you can see the time between window zero condition and the tcp window update.</p><p>You could also create an Advanced I/O graph of avg(*)tcp.len to depict the payload size. Or another graph which depicts the tcp.len and tcp.window_size to see the window zero condition and the tcp window update.</p><p>Hope this is somewhat helpful,</p><p>John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '11, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-4885" class="comments-container"></div><div id="comment-tools-4885" class="comment-tools"></div><div class="clear"></div><div id="comment-4885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4888"></span>

<div id="answer-container-4888" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4888-score" class="post-score" title="current number of votes">0</div><span id="post-4888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do the 5-second pauses correspond with Zero Window announcements from the client? If so, the server is pausing because the client can't keep up. If not, then it's something on the server. Could the server be overloaded?</p><p>Per RFC 1122, The first Zero Window Probe should be sent when the zero window condition has existed for the retransmission timeout period. The transmitting host should increase the interval between successive zero window probes exponentially. Usually, you'll see the interval between zero window probes doubling with each probe. As always, the exact details are somewhat implementation dependent.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '11, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-4888" class="comments-container"></div><div id="comment-tools-4888" class="comment-tools"></div><div class="clear"></div><div id="comment-4888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

