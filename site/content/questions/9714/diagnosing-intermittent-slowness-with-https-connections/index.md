+++
type = "question"
title = "Diagnosing intermittent slowness with HTTPS connections"
description = '''I have a Java-based client that uses HTTPS to talk -- over the Internet -- with an Apache web server. When this client is run behind my firewall, some HTTP requests (about 5% of them) take far too long to complete (e.g. 15 seconds instead of the normal 20 milliseconds). Some requests, like ~750 KB f...'''
date = "2012-03-22T17:08:00Z"
lastmod = "2012-03-28T13:02:00Z"
weight = 9714
keywords = [ "wireshark", "troubleshooting", "help" ]
aliases = [ "/questions/9714" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Diagnosing intermittent slowness with HTTPS connections](/questions/9714/diagnosing-intermittent-slowness-with-https-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9714-score" class="post-score" title="current number of votes">0</div><span id="post-9714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Java-based client that uses HTTPS to talk -- over the Internet -- with an Apache web server. When this client is run behind my firewall, some HTTP requests (about 5% of them) take far too long to complete (e.g. 15 seconds instead of the normal 20 milliseconds). Some requests, like ~750 KB file uploads, seemingly never complete.</p><p>When the firewall is bypassed, everything works fine.<br />
</p><p>It's usually HTTP POST/PUT messages with large (32k+) payloads in the message body that encounter trouble, but sometimes small messages with no payload have problems. I am trying to use Wireshark to understand the pathology of the problem, but I am relatively inexperienced with debugging SSL/TLS. I am able to decrypt the communication, but all that has allowed me to do is isolate a conversation which had trouble:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/capture.png" alt="alt text" /></p><p>I'm not quite sure how to proceed here. What should I look for? Are the Unknown Records of concern? What's triggering the retransmissions? Do I need to do a simultaneous packet capture at the firewall as well? Any advice or insight is appreciated. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '12, 17:08</strong></p><img src="https://secure.gravatar.com/avatar/7410fa097cd2feb76730c6843f631121?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20Clark&#39;s gravatar image" /><p><span>Mike Clark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike Clark has one accepted answer">100%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Apr '12, 08:58</strong> </span></p></div></div><div id="comments-container-9714" class="comments-container"></div><div id="comment-tools-9714" class="comment-tools"></div><div class="clear"></div><div id="comment-9714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9825"></span>

<div id="answer-container-9825" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9825-score" class="post-score" title="current number of votes">0</div><span id="post-9825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mike Clark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It turned out to be a <a href="http://en.wikipedia.org/wiki/Duplex_mismatch">duplex mismatch</a> between our firewall's NIC and a router's NIC. The firewall NIC was set to autonegotiate, and the router's NIC was set to full duplex. After setting both to full duplex, the problem went away.</p><p>Because one of the key symptoms for diagnosing duplex mismatch is packet loss, it was important to take a capture at both ends of the conversation to see which packets were arriving and which weren't. After analyzing packet captures from both ends of the conversation, I found that the captured behavior matched very closely with Wikipedia's description of the TCP symptoms of duplex mismatch:</p><blockquote><p>The lost packets force the TCP protocol to perform error recovery, but the initial (streamlined) recovery attempts fail because the retransmitted packets are lost in exactly the same way as the original packets. Eventually, the TCP transmission window becomes full and the TCP protocol refuses to transmit any further data until the previously-transmitted data is acknowledged. This, in turn, will quiesce the new traffic over the connection, leaving only the retransmissions and acknowledgments. Since the retransmission timer grows progressively longer between attempts, eventually a retransmission will occur when there is no reverse traffic on the connection, and the acknowledgment are finally received. This will restart the TCP traffic, which in turn immediately causes lost packets as streaming resumes.</p></blockquote><p>As mentioned in the article, a key TCP symptom that indicates duplex mismatch is the TCP connection devolving into almost entirely delayed retransmissions and ACKs, resulting in a TCP connection that is "alive" and "active" but transmitting data at an incredibly slow rate.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '12, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/7410fa097cd2feb76730c6843f631121?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20Clark&#39;s gravatar image" /><p><span>Mike Clark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike Clark has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Mar '12, 16:49</strong> </span></p></div></div><div id="comments-container-9825" class="comments-container"></div><div id="comment-tools-9825" class="comment-tools"></div><div class="clear"></div><div id="comment-9825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

