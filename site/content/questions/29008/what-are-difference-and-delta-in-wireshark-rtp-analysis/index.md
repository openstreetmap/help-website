+++
type = "question"
title = "What are “Difference” and “Delta” in Wireshark RTP Analysis?"
description = '''I tried to find this in the documentation, but had no luck. I would love to dig the sources to find out, but I honestly don&#x27;t have the time. I tried to google this, but either people do not get any reply (like this one or that one) or they look at the sources and the epiphany they get prevents them ...'''
date = "2014-01-18T12:26:00Z"
lastmod = "2014-01-21T02:33:00Z"
weight = 29008
keywords = [ "graph", "rtp", "analysis" ]
aliases = [ "/questions/29008" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What are “Difference” and “Delta” in Wireshark RTP Analysis?](/questions/29008/what-are-difference-and-delta-in-wireshark-rtp-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29008-score" class="post-score" title="current number of votes">1</div><span id="post-29008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to find this in the documentation, but had no luck. I would love to dig the sources to find out, but I honestly don't have the time. I tried to google this, but either people do not get any reply (like this <a href="http://wireshark.org/lists/wireshark-users/200611/msg00169.html">one</a> or that <a href="http://wireshark.org/lists/wireshark-users/201003/msg00171.html">one</a>) or they look at the sources and the epiphany they get prevents them from sharing their newfound knowledge with the mere mortals we are (like <a href="http://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5498">here</a> or <a href="http://wireshark.org/lists/wireshark-users/201012/msg00035.html">there</a>).</p><p>Is the meaning behind "Difference" and "Delta" in Wireshark RTP analyses and graphs too much knowledge for the world to handle, or could we get a clear answer on that? (Also, do any of these relate to "Latency", and if not, is there a way to get the latency per packet from a capture?)</p><p>Edit: I'm using version 1.2.11.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '14, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/43c2f4173e7b15de81da4f84cf3b7579?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peniblec&#39;s gravatar image" /><p><span>Peniblec</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peniblec has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jan '14, 13:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29008" class="comments-container"></div><div id="comment-tools-29008" class="comment-tools"></div><div class="clear"></div><div id="comment-29008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29033"></span>

<div id="answer-container-29033" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29033-score" class="post-score" title="current number of votes">6</div><span id="post-29033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Peniblec has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, since I'm the one that committed the code I feel somewhat pressured to attempt to describe it ;)</p><p>To really understand the behaviour of RTP one has to be comfortable with the concept of timebases. With timebases I mean clocks running at different nodes and protocol levels of the networked system. Between nodes of an RTP session (I assume a point-to-point session here) there are several relevant timebases. There are the sender RTP timestamper and packet sender clock on the one end and RTP receiver and playout clock on the other. Note: these are not necessarily in sync.</p><p>Your Wireshark capture must be considered a point somewhere in between these nodes. It may be at the producer side (eg. in the gateway) or receiver side (eg. terminal), or somewhere in between (eg. intermediate network switch).</p><p>What the RTP nodes try to do at the session level is to convey realtime data (eg. speech) at a specified rate. They produce RTP packets with an agreed encoding and time interval (=size) and timestamp these frames. Then they hand them off to the network stack to be transmitted to the other node. When this packet actually appears on the network may depend on various factors, but will probably be with varying delay. Then it has to traverse the network. This may also be with varying delay. Then it enters the receiver node network stack which will deliver it to the receiving RTP endpoint, also with varying delay. So, the receiver has to cope with all that varying delay, and try to sync its timebase to the transmitter. As you can imagine from this description there is only a so much you can do with the receive timestamp. The RTP timestamps should be the ones the receiving RTP node should work with. As you can see it's complex enough, and I won't even discuss the playout clock.</p><p>Now that we're aware of the timing aspect of RTP we go back to the Wireshark RTP analysis' difference and delta.</p><p>Delta is the difference between arrival of this packet vs. the arrival of the previous packet. It's all at the network layer and reflects the packet arrival at the capture interface (where it's timestamped).</p><p>Difference tries to tell us something about the relationship between packet arrival and RTP timestamps. It's the (absolute) difference of the packet arrival at the capture interface (where it's timestamped) vs. the expected time of arrival of the packet at the capture interface based on the RTP timestamp.</p><p>So, Delta is nice from a networking perspective, but for the RTP receiver the Difference is much more relavant since it influences the depth of the jitter buffer is must maintain to provide an uninterrupted playout.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '14, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-29033" class="comments-container"><span id="29044"></span><div id="comment-29044" class="comment"><div id="post-29044-score" class="comment-score">1</div><div class="comment-text"><p>Okay, that did clear things up :) Sorry for the slight snark in the question, I was still recovering from the amount of people on the Internet who just assume that Delta and/or Difference are simply synonyms with Latency (i.e. time of arrival minus time of sending), since (I suppose) that's what they are looking for and they don't feel like digging too much (... I'm hardly one to talk, I guess).<br />
(I posted the same question on superuser, if you're interested)</p></div><div id="comment-29044-info" class="comment-info"><span class="comment-age">(20 Jan '14, 23:37)</span> <span class="comment-user userinfo">Peniblec</span></div></div><span id="29050"></span><div id="comment-29050" class="comment"><div id="post-29050-score" class="comment-score"></div><div class="comment-text"><p>Well done, <span>@Jaap</span>!</p></div><div id="comment-29050-info" class="comment-info"><span class="comment-age">(21 Jan '14, 02:33)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-29033" class="comment-tools"></div><div class="clear"></div><div id="comment-29033-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

