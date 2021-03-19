+++
type = "question"
title = "wireshark timestamp accuracy"
description = '''I am trying to measure packet processing performance of a server. The server process  is running on a linux system and it is connected to an ethernet switch. A windows  machine connected to the sniffer port and running wireshark to capture the packet.  When I captured the packet at 1 packet/sec rate...'''
date = "2011-01-29T12:13:00Z"
lastmod = "2011-02-13T07:44:00Z"
weight = 2010
keywords = [ "timestamp", "accuracy" ]
aliases = [ "/questions/2010" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark timestamp accuracy](/questions/2010/wireshark-timestamp-accuracy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2010-score" class="post-score" title="current number of votes">0</div><span id="post-2010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to measure packet processing performance of a server. The server process is running on a linux system and it is connected to an ethernet switch. A windows machine connected to the sniffer port and running wireshark to capture the packet.</p><p>When I captured the packet at 1 packet/sec rate, using wireshark running on windows, the response time obtained is at around 400 micro seconds. However, when wireshark is run on the Linux machine itself, the response time obtained is around 200 microseconds.</p><p>Why is there a such a big difference in the time reported by wireshark in the two systems? Note, that i am calculating the difference in the time when wireshark sees the incoming and outgoing packet. The switch is gigabit ethernet switch and the 2 systems are connected via gigabit ethernet.</p><p>Is wireshark timestamp accurate enough for measuring times in the 100 microsecond range ?</p><p>any other light-weight tools to collect more accurate timestamps on a system, without impacting performance of the system itself ??</p><p>Thanks Ramesh</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-accuracy" rel="tag" title="see questions tagged &#39;accuracy&#39;">accuracy</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '11, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/2fd3f495998c7891a4cc725c573ee03a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ramekris&#39;s gravatar image" /><p><span>ramekris</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ramekris has no accepted answers">0%</span></p></div></div><div id="comments-container-2010" class="comments-container"></div><div id="comment-tools-2010" class="comment-tools"></div><div class="clear"></div><div id="comment-2010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="2015"></span>

<div id="answer-container-2015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2015-score" class="post-score" title="current number of votes">1</div><span id="post-2015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Does <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvTimestamps.html#id4927553">this</a> help you understand? It basically states you're dependent on the platform you capture on, and the place in the network you capture.</p><p>Light weight tools? Not really, there's timestamping network hardware for that, like <a href="http://www.cacetech.com/products/turbocap.html">this</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '11, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '11, 11:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-2015" class="comments-container"></div><div id="comment-tools-2015" class="comment-tools"></div><div class="clear"></div><div id="comment-2015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2082"></span>

<div id="answer-container-2082" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2082-score" class="post-score" title="current number of votes">1</div><span id="post-2082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here's my 2 cents.</p><p>I sometimes work on market trading platforms, and sometimes on micro algorithmic trading platforms. They make money via millions of transactions performed in sub seconds. They (the business folks that run this platform) are always asking us to give them the finest possible resolution when it comes to providing performance data. This allows them to track variable latency in the data coming from the feed source, variable latency as it traverses the network, and finally variability in response time from the trading grid itself. I won't go into the craziness of attempting to archive and analyze microsecond sampled performance data from hundreds of disparate systems. What I will tell you is that Cisco themselves won't rely on sub-100 microsecond data that comes from their systems. The variability of the bus clock at such fine increments is enough to sway the data. If you're capturing on a highend router you can possibly trust the ticks to 100µs. If you're capturing on a Cat switch I wouldn't trust the ticks at less than 1ms. If it's a regular ol' PC then I would also not rely on less than 1ms. Virtualized systems are a joke with it comes to bus tick regularity.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '11, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-2082" class="comments-container"></div><div id="comment-tools-2082" class="comment-tools"></div><div class="clear"></div><div id="comment-2082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2017"></span>

<div id="answer-container-2017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2017-score" class="post-score" title="current number of votes">0</div><span id="post-2017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The difference is actually not very big, it's only a couple of hundred microseconds.</p><p>If you capture on the server you see a delta time between incoming and outgoing frame of 200 microseconds, which is the actual local response time of the service.</p><p>If you capture with a monitor session on a switch you have to add forwarding delay of the switch for both directions, which is typically around 100 microseconds for switches operating in Store and Foreward mode. So that would explain why you have 200 microseconds plus 2 times 100 microseconds when capturing on the switch instead of on the server itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '11, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2017" class="comments-container"><span id="2020"></span><div id="comment-2020" class="comment"><div id="post-2020-score" class="comment-score"></div><div class="comment-text"><p>The switch delay should have been the same for incoming and outgoing frame, and I am calculating the difference in timestamps, it would eliminate the switch delay.</p><p>How much is the delay from the time packet in received at the driver till the wireshark stamps it (for incomfing), and the delay from when wireshark stamps outgoing packet till it is put on the wire ? Would that be in the order of 100 microseconds ?</p></div><div id="comment-2020-info" class="comment-info"><span class="comment-age">(30 Jan '11, 06:09)</span> <span class="comment-user userinfo">ramekris</span></div></div><span id="2023"></span><div id="comment-2023" class="comment"><div id="post-2023-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure how fast Wireshark picks up and timestamps a frame but I guess it is a lot faster than 100 microseconds.</p></div><div id="comment-2023-info" class="comment-info"><span class="comment-age">(30 Jan '11, 14:05)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="2025"></span><div id="comment-2025" class="comment"><div id="post-2025-score" class="comment-score"></div><div class="comment-text"><p>As <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvTimestamps.html#id4927553">the reference Jaap gave</a> indicates, Wireshark <em>doesn't</em> timestamp frames - on almost all platforms (the only significant exception I know of is HP-UX), even libpcap doesn't do so, it just uses timestamps supplied by the OS.</p><p>The delay between the arrival of the last bit of the packet at the network adapter, and the time stamping in the networking stack, is <em>probably</em> less than 100 microseconds. Time stamps might have a multi-millisecond precision, however.</p></div><div id="comment-2025-info" class="comment-info"><span class="comment-age">(30 Jan '11, 16:57)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-2017" class="comment-tools"></div><div class="clear"></div><div id="comment-2017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2298"></span>

<div id="answer-container-2298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2298-score" class="post-score" title="current number of votes">0</div><span id="post-2298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I confess I don't understand the issue. Why do you care about individual packet processing times. Surely you care more about how many packets you process in a time interval. Remember that in any real operation there are likely to be multiple processes reading and writing to the wire. So there is a queue of stuff waiting to go in or out. Do the measurements with a million packets, and calculate average and standard deviation.<br />
</p><p>If you want to find times take at different stages, perhaps start with timing a million icmp echo packets to 127.0.0.1, then to the other server's IP, then to whatever process you have running on the server.<br />
</p><p>Then repeat the tests with 2, 4, 8, 16 clients all pounding on the server. And repeat with 2, 4, 8 16 processes on the server. I think you will find that turnaround for an individual packet is small, and that the standard deviations are large enough that it's no longer safe to assume a normal distribution. Poisson maybe?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/ed2ddfe3ce5e547c20fafa0c82b3e970?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SGBotsford&#39;s gravatar image" /><p><span>SGBotsford</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SGBotsford has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-2298" class="comments-container"></div><div id="comment-tools-2298" class="comment-tools"></div><div class="clear"></div><div id="comment-2298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

