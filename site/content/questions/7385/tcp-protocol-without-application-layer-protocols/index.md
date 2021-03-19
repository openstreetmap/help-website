+++
type = "question"
title = "TCP protocol without application layer protocols"
description = '''Hi I am new to networking and have a question about protocols. I analyze wireshark capture files, some are http some are ftp but some are plain TCP. For example; I started a video on youtube and all the stream data is shown as a plain TCP connection. My questions are;  Can we say application layer p...'''
date = "2011-11-11T15:51:00Z"
lastmod = "2011-11-12T13:23:00Z"
weight = 7385
keywords = [ "tcp" ]
aliases = [ "/questions/7385" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP protocol without application layer protocols](/questions/7385/tcp-protocol-without-application-layer-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7385-score" class="post-score" title="current number of votes">0</div><span id="post-7385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am new to networking and have a question about protocols.</p><p>I analyze wireshark capture files, some are http some are ftp but some are plain TCP.</p><p>For example; I started a video on youtube and all the stream data is shown as a plain TCP connection.</p><p>My questions are;</p><ul><li>Can we say application layer protocols are not mandatory in computer networking?</li><li>or is it because Wireshark doesn't know the protocol type, so it just shows TCP for the protocols that it doesn't know?</li><li>or it is what it is. Just plain tcp connection.</li></ul><p>I am just trying to understand what i must understand when i see TCP protocol name in the protocol column.</p><p>Thanks...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '11, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/f28df4e1d1ceb6f6a38657888457a740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sawque&#39;s gravatar image" /><p><span>sawque</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sawque has no accepted answers">0%</span></p></div></div><div id="comments-container-7385" class="comments-container"></div><div id="comment-tools-7385" class="comment-tools"></div><div class="clear"></div><div id="comment-7385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7389"></span>

<div id="answer-container-7389" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7389-score" class="post-score" title="current number of votes">2</div><span id="post-7389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As JK7 notes, Wireshark could show a packet with a protocol of "TCP" because it doesn't know what protocol is being used for the packet.</p><p>If the packet has no payload, such as an initial SYN packet with no data or an ACK packet with no data, Wireshark will show it as TCP as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '11, 18:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7389" class="comments-container"><span id="7390"></span><div id="comment-7390" class="comment"><div id="post-7390-score" class="comment-score"></div><div class="comment-text"><p>Thank you all.</p><p>OK. When I see TCP I must understand: either wireshark doesn't know what protocol is being used or if there is not a payload it can be SYN or ACK packet.</p><p>just one more question for to be sure.</p><p>So we can't say that TCP protocol can be without application layer protocol Right?(except sync, ack vs..)</p><p>We can say it for ARP (because ARP protocol's data doesn't contain any information related with above Layer -2, I means it ends at layer-2)</p><p>but if it is TCP, and also it has payloads, that means this payload(Like youtube video stream data) belongs to a protocol.</p><p>Thanks again</p></div><div id="comment-7390-info" class="comment-info"><span class="comment-age">(11 Nov '11, 18:51)</span> <span class="comment-user userinfo">sawque</span></div></div><span id="7391"></span><div id="comment-7391" class="comment"><div id="post-7391-score" class="comment-score">1</div><div class="comment-text"><p>Yes, transport-layer protocols such as TCP and UDP are not "top-layer" protocols like ARP; they exist to transport other protocols, so, other than packets containing only TCP-layer control information, such as those used to set up or tear down a connection, there has to be some form of protocol, even if it's a trivial protocol such as the data transfer protocol for FTP, in which the file being transferred is just streamed over the connection.</p></div><div id="comment-7391-info" class="comment-info"><span class="comment-age">(11 Nov '11, 19:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="7394"></span><div id="comment-7394" class="comment"><div id="post-7394-score" class="comment-score"></div><div class="comment-text"><p>Thank you Guy Harris;</p><p>I have some conclusions;</p><p>Can we say TCP and IP exist for other protocols but other protocols exist for themselves.</p><p>This is the differences between Tcp/IP and other protocols.</p><p>And this is why we call them tcp/ip protocol suites.</p><p>Are all these conclusions right?</p></div><div id="comment-7394-info" class="comment-info"><span class="comment-age">(12 Nov '11, 02:55)</span> <span class="comment-user userinfo">sawque</span></div></div><span id="7396"></span><div id="comment-7396" class="comment"><div id="post-7396-score" class="comment-score">1</div><div class="comment-text"><p>We can say that:</p><ul><li><p>there are protocols that exist solely to transport other protocols, such as TCP, IP, and SCTP, even if the other protocol is trivial, such as the "protocol" on FTP data connections;</p></li><li><p>there are protocols that do not transport other protocols, such as FTP;</p></li><li><p>there are protocols that can exist for themselves <em>and</em> transport other protocols, such as HTTP (which can be used for itself to fetch Web pages, and can also transport messages for higher-level protocols);</p></li><li><p>TCP and IP aren't the only protocols that exist solely to transport other protocols.</p></li></ul></div><div id="comment-7396-info" class="comment-info"><span class="comment-age">(12 Nov '11, 13:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-7389" class="comment-tools"></div><div class="clear"></div><div id="comment-7389-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7387"></span>

<div id="answer-container-7387" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7387-score" class="post-score" title="current number of votes">1</div><span id="post-7387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If wireshark doesn't know TCP based application layer protocol,it will simply display protocol as "TCP" with layer 7 (Data) info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '11, 17:04</strong></p><img src="https://secure.gravatar.com/avatar/01febacc45af8ecf743c4f575d428326?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JK7&#39;s gravatar image" /><p><span>JK7</span><br />
<span class="score" title="31 reputation points">31</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JK7 has no accepted answers">0%</span></p></div></div><div id="comments-container-7387" class="comments-container"></div><div id="comment-tools-7387" class="comment-tools"></div><div class="clear"></div><div id="comment-7387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

