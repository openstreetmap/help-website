+++
type = "question"
title = "Tshark HTPP Jitter Statistics Capabilities Question"
description = '''Hello, My question is simply what are the capabilities of specifically tshark or even wireshark for the ability to analyze pcap files finding jitter? I have seen various posts for VOIP or RTP jitter but none for HTTP. Also, I was also wondering how most people capture latency within a pcap file usin...'''
date = "2015-08-28T07:42:00Z"
lastmod = "2015-08-31T13:14:00Z"
weight = 45464
keywords = [ "jitter", "tshark" ]
aliases = [ "/questions/45464" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark HTPP Jitter Statistics Capabilities Question](/questions/45464/tshark-htpp-jitter-statistics-capabilities-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45464-score" class="post-score" title="current number of votes">0</div><span id="post-45464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>My question is simply what are the capabilities of specifically tshark or even wireshark for the ability to analyze pcap files finding jitter? I have seen various posts for VOIP or RTP jitter but none for HTTP. Also, I was also wondering how most people capture latency within a pcap file using the TCP protocol. So far my solution to that problem has been finding the difference in time between next TCP sequence data packets coming from the HTTP server.</p><p>Thanks in advance for any comments or advice,</p><p>Joe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jitter" rel="tag" title="see questions tagged &#39;jitter&#39;">jitter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '15, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/17c3f2c7628cf18f00d2d2136dbc3560?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danjoemart&#39;s gravatar image" /><p><span>danjoemart</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danjoemart has no accepted answers">0%</span></p></div></div><div id="comments-container-45464" class="comments-container"><span id="45466"></span><div id="comment-45466" class="comment"><div id="post-45466-score" class="comment-score"></div><div class="comment-text"><p>well, there is no (common) definition for <strong>jitter</strong> in HTTP, so what is <strong>your definition</strong>? Based on that, we might be able to suggest something.</p></div><div id="comment-45466-info" class="comment-info"><span class="comment-age">(28 Aug '15, 07:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45476"></span><div id="comment-45476" class="comment"><div id="post-45476-score" class="comment-score"></div><div class="comment-text"><p>Well, I have been googling around since I wrote this post a couple hours ago and I found this filter "tcp.analysis.ack_rtt". Basically, I am just trying to do some kind of analysis on "general network rtt" so I have some kind of idea of the network latency. From there I was hoping I could get some idea of what the jitter is so perhaps I could add a "http" filter. Without googling what jitter means my idea of jitter is the fluctuation of network latency on a stream over time.</p><p>Basically the whole point of what I am doing is I am trying to measure network latency for video traffic which flows over http under extreme network load. In my tests I am saturating the network with Iperf UDP traffic and I am trying to figure out how I can view how the cameras are behaving. One very important statistic I am trying to find is jitter and latency. Hope that helps. I think I am getting closer to an answer now.</p><p>Thanks again,</p><p>Joe</p></div><div id="comment-45476-info" class="comment-info"><span class="comment-age">(28 Aug '15, 09:07)</span> <span class="comment-user userinfo">danjoemart</span></div></div></div><div id="comment-tools-45464" class="comment-tools"></div><div class="clear"></div><div id="comment-45464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45479"></span>

<div id="answer-container-45479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45479-score" class="post-score" title="current number of votes">0</div><span id="post-45479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>my idea of jitter is the fluctuation of network latency on a stream over time.</p></blockquote><p>O.K. if you want to measure latency, you'll have to do that at two points in parallel, with high precision clocks. One in front of the sender and one in front of the receiver. Then compare both capture files to calculate the delta of the frame timestamps and create a graph or something based on that information.</p><p>It's easy for Wireshark to calculate jitter for RTP, because there are timestamps in the RTP payload, which can be used.</p><p>Unfortunately, you don't have timestamps in (regular) TCP frames, so the only thing you can do is what I described above. Unfortunately (again), there is no support whatsoever for that in Wireshark/tshark, so you'll have to use a script (Perl/Python/<a href="http://www.muppetlabs.com/~breadbox/bf/">Brainfuck</a>/Whatever), to parse the output of tshark and to do the calculation of frame time delta.</p><p>See my answer to a totally different question for an idea how you could use tshark and Perl for your task.</p><blockquote><p><a href="https://ask.wireshark.org/questions/45349/how-to-print-field-labels-with-values/45477">https://ask.wireshark.org/questions/45349/how-to-print-field-labels-with-values/45477</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '15, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-45479" class="comments-container"><span id="45553"></span><div id="comment-45553" class="comment"><div id="post-45553-score" class="comment-score"></div><div class="comment-text"><p>Hey Kurt,</p><p>Thanks for your help and the information you provided does seem to make sense as it does seem like what you said is the correct way to setup your environment to get very accurate data with precision.<br />
</p><p>However, my tests have already completed and I cannot redo it. I only have my result pcap data.</p><p>My main question for you is, how reliable and accurate would the data be if I used the tcp.analysis.ack_rtt filter? I already have a script that goes through my pcap files and extracts those time differences and the data to me seems like it provides a good sense as to what the latency looks like. It would be nice to have a second opinion.</p><p>Thanks in advance, Joe</p></div><div id="comment-45553-info" class="comment-info"><span class="comment-age">(31 Aug '15, 13:14)</span> <span class="comment-user userinfo">danjoemart</span></div></div></div><div id="comment-tools-45479" class="comment-tools"></div><div class="clear"></div><div id="comment-45479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

