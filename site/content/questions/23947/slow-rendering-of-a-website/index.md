+++
type = "question"
title = "Slow rendering of a website"
description = '''The following trace shows the capture of IE trying to load cnn.com. From frame 49 onwards things look fine. I cannot see any tell tale signs of problems. There are some retransmits that popup along the way but nothing that help identify the problem outright. What other areas could I focus on here? h...'''
date = "2013-08-22T04:26:00Z"
lastmod = "2013-08-22T05:17:00Z"
weight = 23947
keywords = [ "latency" ]
aliases = [ "/questions/23947" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slow rendering of a website](/questions/23947/slow-rendering-of-a-website)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23947-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The following trace shows the capture of IE trying to load cnn.com. From frame 49 onwards things look fine. I cannot see any tell tale signs of problems. There are some retransmits that popup along the way but nothing that help identify the problem outright. What other areas could I focus on here?</p><p><a href="http://www.cloudshark.org/captures/3bfe4764f3f4">http://www.cloudshark.org/captures/3bfe4764f3f4</a></p></div><div id="question-tags" class="tags-container tags">latency</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '13, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/3e8f9f4373a1fe12ae4be7f9b995707c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wireshark12&#39;s gravatar image" /><p>wireshark12<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wireshark12 has no accepted answers">0%</span></p></div></div><div id="comments-container-23947" class="comments-container"></div><div id="comment-tools-23947" class="comment-tools"></div><div class="clear"></div><div id="comment-23947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23951"></span>

<div id="answer-container-23951" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23951-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Oh, "some retransmits" is a very polite description. I see almost 10% of all packets require retrasnmission with up to 10 seconds RTO. <img src="https://osqa-ask.wireshark.org/upfiles/Selection_048.png" alt="alt text" /></p><p>Also, there are many HTTP Timeout responses indicating that the server(s) didn't get your data in time. <code>http.response.code == 408</code></p><p><code>tcp.srcport==54264 and tcp.len gt 0</code> shows that even small packets don't make it with out excessive retransmissions.</p><p>So, somewhere somewhat eats your packets...<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '13, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Aug '13, 05:37</p></div></div><div id="comments-container-23951" class="comments-container"><span id="23952"></span><div id="comment-23952" class="comment"><div id="post-23952-score" class="comment-score"></div><div class="comment-text"><p>Thank you. What are the tell tale signs for the re-transmit reasons?</p></div><div id="comment-23952-info" class="comment-info"><span class="comment-age">(22 Aug '13, 05:25)</span> wireshark12</div></div><span id="23954"></span><div id="comment-23954" class="comment"><div id="post-23954-score" class="comment-score"></div><div class="comment-text"><p>My apologies - I should rephrase my question - Is there anything else I could look for to see what's 'eating' the packets or does that require looking at the packets at those junctions?</p></div><div id="comment-23954-info" class="comment-info"><span class="comment-age">(22 Aug '13, 05:45)</span> wireshark12</div></div><span id="23956"></span><div id="comment-23956" class="comment"><div id="post-23956-score" class="comment-score"></div><div class="comment-text"><p>Well, assuming that the rest of the world can browse CNN well I assume that the culprit is close to you. Are you using your iPhone as a hotspot here?</p></div><div id="comment-23956-info" class="comment-info"><span class="comment-age">(22 Aug '13, 05:56)</span> mrEEde</div></div><span id="23957"></span><div id="comment-23957" class="comment"><div id="post-23957-score" class="comment-score"></div><div class="comment-text"><p>LOL. Yes, I am using my iPhone as a hotspot. I am also with Verizon. As I type this, I'm thinking that this might be a case of throttling?</p></div><div id="comment-23957-info" class="comment-info"><span class="comment-age">(22 Aug '13, 06:14)</span> wireshark12</div></div><span id="23964"></span><div id="comment-23964" class="comment"><div id="post-23964-score" class="comment-score"></div><div class="comment-text"><p>That's what it is, you probably have exceeded your limit so they slow you down</p></div><div id="comment-23964-info" class="comment-info"><span class="comment-age">(22 Aug '13, 08:08)</span> mrEEde</div></div></div><div id="comment-tools-23951" class="comment-tools"></div><div class="clear"></div><div id="comment-23951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

