+++
type = "question"
title = "How to best analyze two different captures"
description = '''I have two captures from each firewall for two sites connected by VPN tunnel. From the sending side host (site1) capture, Wireshark is reporting many TCP Zero Window and Update flags coming from the receiving side (site 2). Looking at the receiving (site2) capture, there are no TCP Zero Window and U...'''
date = "2013-10-03T15:32:00Z"
lastmod = "2013-10-03T22:54:00Z"
weight = 25611
keywords = [ "zero-window", "tcp" ]
aliases = [ "/questions/25611" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to best analyze two different captures](/questions/25611/how-to-best-analyze-two-different-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25611-score" class="post-score" title="current number of votes">0</div><span id="post-25611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two captures from each firewall for two sites connected by VPN tunnel. From the sending side host (site1) capture, Wireshark is reporting many TCP Zero Window and Update flags coming from the receiving side (site 2). Looking at the receiving (site2) capture, there are no TCP Zero Window and Update flags reported but only TCP retransmissions and Dup Ack. Having two sided captures, I would expect to see same TCP Zero Window and Update for the receiving side but that’s not the case.I would like advice on what’s the best way to analyze to rule out if it could be firewall issue or the client themselves.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zero-window" rel="tag" title="see questions tagged &#39;zero-window&#39;">zero-window</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '13, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p><span>ws2006</span><br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div></div><div id="comments-container-25611" class="comments-container"></div><div id="comment-tools-25611" class="comment-tools"></div><div class="clear"></div><div id="comment-25611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25617"></span>

<div id="answer-container-25617" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25617-score" class="post-score" title="current number of votes">1</div><span id="post-25617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like you're expecting the captures to show the same packets taken at the same time in two different locations, so first thing to do is to verify if that assumption is correct or if the packets aren't from the same connections. To do that I'd filter on the SYN packets only (tcp.flags=0x02) and compare the TCP initial sequence numbers. If you can't find a match you have some sort of proxying going on, which means that matching the sessions will be very difficult since the TCP connections are completely different. In that case you need to find out why this happens, and what kind of devices are involved (maybe some normal Proxy, maybe WAN accelerators etc.).</p><p>If you can find the same SYN packets on both sides you just go and filter on the session, and not by TCP stream number, because it may be different. Use a conversation filter instead, meaning that you filter on IP and port of both client and server. After that, you need to start comparing the single packets of the conversations to see what is different.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25617" class="comments-container"></div><div id="comment-tools-25617" class="comment-tools"></div><div class="clear"></div><div id="comment-25617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

