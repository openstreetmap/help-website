+++
type = "question"
title = "Rate limit causes excess retransmissions and duplicate acks"
description = '''We recently had a customer complaining that performance from their remote site to our home office here was bad. Investigation with Iperf and Wireshark showed a massive number of retrans and dupe acks. In chasing the circuit back to the home office we found out that the circuit provider had put a rat...'''
date = "2011-04-01T08:19:00Z"
lastmod = "2011-04-01T11:09:00Z"
weight = 3275
keywords = [ "rate", "limit", "retransmissions" ]
aliases = [ "/questions/3275" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Rate limit causes excess retransmissions and duplicate acks](/questions/3275/rate-limit-causes-excess-retransmissions-and-duplicate-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3275-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We recently had a customer complaining that performance from their remote site to our home office here was bad. Investigation with Iperf and Wireshark showed a massive number of retrans and dupe acks. In chasing the circuit back to the home office we found out that the circuit provider had put a rate limit of 15 Mbps on their Foundry router in between us. When they took off the limit the circuit tested clean.</p><p>I've heard of some network devices simply dropping the packets when the limit is reached which, I guess, is why we saw this result. I have a hard time believing that all rate limit devices are this crude. Are there other methods or is this pretty much what I'm going to see in terms of symptoms?</p></div><div id="question-tags" class="tags-container tags">rate limit retransmissions</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '11, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/e9731598241220667226ea8b75584a70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dribniff&#39;s gravatar image" /><p>dribniff<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dribniff has no accepted answers">0%</span></p></div></div><div id="comments-container-3275" class="comments-container"><span id="3279"></span><div id="comment-3279" class="comment"><div id="post-3279-score" class="comment-score"></div><div class="comment-text"><p>Well, most devices do drop packets. How you drop those packets is important. Just tail dropping can cause issues like this. Some type of early detection coupled with dropping would be better. If you limit the throughput to 15Mbps, do you see packet drops?</p></div><div id="comment-3279-info" class="comment-info"><span class="comment-age">(01 Apr '11, 17:51)</span> hansangb</div></div><span id="3321"></span><div id="comment-3321" class="comment"><div id="post-3321-score" class="comment-score"></div><div class="comment-text"><p>More like 8-10 Mbps. We're getting a lot better with Iperf than we ever were before. By limiting the rate we're able to see a clean capture. This sounds like the old days where to kept bumping the MTU around until you got a clean, full stream of data.</p><p>In this case, the three hops thru provider layer two devices cleanly allowed up to 80M on the 100m circuit until we hit the router (we backtracked with Iperf) The problem is we're trying to consolidate the remote servers back here and all that user traffic easily runs over 50m aggregate. The provider grinned and said "buy more"</p></div><div id="comment-3321-info" class="comment-info"><span class="comment-age">(04 Apr '11, 06:12)</span> dribniff</div></div></div><div id="comment-tools-3275" class="comment-tools"></div><div class="clear"></div><div id="comment-3275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3276"></span>

<div id="answer-container-3276" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3276-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can't speak for "real" routers, but FreeBSD's traffic shaper (see the <a href="http://www.freebsd.org/cgi/man.cgi?query=ipfw&amp;apropos=0&amp;sektion=0&amp;manpath=FreeBSD+8.2-stable&amp;format=html#TRAFFIC_SHAPER_(DUMMYNET)_CONFIGURATION">ipfw</a> man page) allows you to limit traffic to a given speed but it also allows you to control the queue size of the "pipe" (see the 'bandwidth' and 'queue' parameters). I would (possibly naively) think that "real" routers would have similar mechanisms.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '11, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-3276" class="comments-container"><span id="3322"></span><div id="comment-3322" class="comment"><div id="post-3322-score" class="comment-score"></div><div class="comment-text"><p>So here's the question that came up in our group: If you can't control the provider and you can't buy more bandwidth are you better to turn the users down to 10 Mbps at their workstations and push the throttling back to the computer? Of course this depends on the ratio of local versus remote (to the user), but when you're trying to move all of the servers back...</p><p>In the Cisco IOS when QoS is invoked I see the word "drop" at the end of the command. They mean that literally, don't they?</p></div><div id="comment-3322-info" class="comment-info"><span class="comment-age">(04 Apr '11, 06:21)</span> dribniff</div></div><span id="3328"></span><div id="comment-3328" class="comment"><div id="post-3328-score" class="comment-score">1</div><div class="comment-text"><p>You can also rate limit yourself. If the carrier is using a pure taildrop scenario, you may have better luck smoothing it out using your own router. The drop counter is literal, but you can rate limit things that you don't care about, you can use WRED so you can be more intelligent in your drops etc. But keep in mind that your carrier may already be doing this. Using a tool like iperf may not truly give you a real world handling of packet loss (i.e. it may look worse during testing than it really is in reality) good luck</p></div><div id="comment-3328-info" class="comment-info"><span class="comment-age">(04 Apr '11, 11:06)</span> hansangb</div></div><span id="3339"></span><div id="comment-3339" class="comment"><div id="post-3339-score" class="comment-score"></div><div class="comment-text"><p>I agree with Hansangb - controlling yourself at your edge is the best option. What is the latency between the two sites? By dropping the packets your provider is likely causing TCP to go through a slowstart. If the latency between your sites is great the recovery from slowstart can take longer, which greatly degrades performance. If you can keep your traffic slightly below the providers imposed limit you'll make out better in the long run.</p></div><div id="comment-3339-info" class="comment-info"><span class="comment-age">(05 Apr '11, 05:17)</span> GeonJay</div></div></div><div id="comment-tools-3276" class="comment-tools"></div><div class="clear"></div><div id="comment-3276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

