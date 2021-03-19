+++
type = "question"
title = "Telnet is not passing for specific IP"
description = '''Hi there I&#x27;m having a time reader device connect to the network which works fine unless for specific IP addresses it doen&#x27;t alow telnet but it still relply to the ping. The out put shows my laptop IP address 10.6.80.135 and the problem is with IP address 10.6.80.120 While the IP address 10.6.80.83 i...'''
date = "2014-02-03T00:46:00Z"
lastmod = "2014-02-03T07:16:00Z"
weight = 29386
keywords = [ "ping", "telnet" ]
aliases = [ "/questions/29386" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Telnet is not passing for specific IP](/questions/29386/telnet-is-not-passing-for-specific-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29386-score" class="post-score" title="current number of votes">0</div><span id="post-29386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there I'm having a time reader device connect to the network which works fine unless for specific IP addresses it doen't alow telnet but it still relply to the ping. The out put shows my laptop IP address 10.6.80.135 and the problem is with IP address 10.6.80.120</p><p>While the IP address 10.6.80.83 is working fine.</p><pre><code>78  22.937534000    10.6.80.135 10.6.5.118  TCP 54  49439 &gt; http [RST, ACK] Seq=1 Ack=1 Win=0 Len=0
83  23.578853000    10.6.80.135 10.6.80.120 TCP 66  49443 &gt; http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
86  24.092328000    10.6.80.120 10.6.80.135 TCP 60  http &gt; 49443 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-telnet" rel="tag" title="see questions tagged &#39;telnet&#39;">telnet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '14, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/c14df72726dbf82188a94047f8cc95ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharif&#39;s gravatar image" /><p><span>sharif</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharif has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '14, 02:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29386" class="comments-container"></div><div id="comment-tools-29386" class="comment-tools"></div><div class="clear"></div><div id="comment-29386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29388"></span>

<div id="answer-container-29388" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29388-score" class="post-score" title="current number of votes">0</div><span id="post-29388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like there is either no telnet server running (or it is listening on a different port) or there is a filter (ACL) that blocks connection requests to the telnet port.</p><p>Do you see a SYN-ACK in the capture file?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '14, 01:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '14, 01:06</strong> </span></p></div></div><div id="comments-container-29388" class="comments-container"><span id="29389"></span><div id="comment-29389" class="comment"><div id="post-29389-score" class="comment-score"></div><div class="comment-text"><p>In fact it does telnet but when you change the IP address</p><pre><code>78 22.937534000 10.6.80.135 10.6.5.118 TCP 54 49439 &gt; http [RST, ACK] Seq=1 Ack=1 Win=0 Len=0 
83 23.578853000 10.6.80.135 10.6.80.120 TCP 66 49443 &gt; http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1 
86 24.092328000 10.6.80.120 10.6.80.135 TCP 60 http &gt; 49443 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre></div><div id="comment-29389-info" class="comment-info"><span class="comment-age">(03 Feb '14, 02:01)</span> <span class="comment-user userinfo">sharif</span></div></div><span id="29390"></span><div id="comment-29390" class="comment"><div id="post-29390-score" class="comment-score"></div><div class="comment-text"><p>Two things</p><ul><li>you are talking about telnet, but the capture shows http as destination port!?!</li><li>if you get a RESET (frame 86) after a SYN (frame 83), there is either no server software listening on that port (most likely), or there is a filter on the system (ACL, Firewall) that blocks the connection.</li></ul><p>OR</p><ul><li>there is another system on the network with the same IP. Please check if the MAC address for 10.6.80.120 makes sense (in the capture file), meaning if it is really the MAC address of the device.</li></ul></div><div id="comment-29390-info" class="comment-info"><span class="comment-age">(03 Feb '14, 02:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29391"></span><div id="comment-29391" class="comment"><div id="post-29391-score" class="comment-score"></div><div class="comment-text"><p>Yes I'm trying to telnet port 80</p></div><div id="comment-29391-info" class="comment-info"><span class="comment-age">(03 Feb '14, 02:48)</span> <span class="comment-user userinfo">sharif</span></div></div><span id="29395"></span><div id="comment-29395" class="comment"><div id="post-29395-score" class="comment-score"></div><div class="comment-text"><p>O.K. see my comment above, regarding the three possible problems.</p></div><div id="comment-29395-info" class="comment-info"><span class="comment-age">(03 Feb '14, 07:16)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29388" class="comment-tools"></div><div class="clear"></div><div id="comment-29388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

