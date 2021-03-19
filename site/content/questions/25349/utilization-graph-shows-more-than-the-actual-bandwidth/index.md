+++
type = "question"
title = "Utilization graph shows more than the actual bandwidth"
description = '''I have a total of T1 link that i was trying to analyze how bandwidth is been used by different applications. What I can see the default graph show a big line, suggesting how the total traffic was when the trace took. Ideally that line should be less than 1.54 Mbps - T1 speed. But i do see spikes abo...'''
date = "2013-09-29T18:37:00Z"
lastmod = "2013-09-30T15:14:00Z"
weight = 25349
keywords = [ "graphs", "utilization", "wireshark" ]
aliases = [ "/questions/25349" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Utilization graph shows more than the actual bandwidth](/questions/25349/utilization-graph-shows-more-than-the-actual-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25349-score" class="post-score" title="current number of votes">0</div><span id="post-25349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a total of T1 link that i was trying to analyze how bandwidth is been used by different applications. What I can see the default graph show a big line, suggesting how the total traffic was when the trace took. Ideally that line should be less than 1.54 Mbps - T1 speed. But i do see spikes above 1.54. What does it mean ? ..is it a burst in traffic.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graphs" rel="tag" title="see questions tagged &#39;graphs&#39;">graphs</span> <span class="post-tag tag-link-utilization" rel="tag" title="see questions tagged &#39;utilization&#39;">utilization</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '13, 18:37</strong></p><img src="https://secure.gravatar.com/avatar/adfa43f849103e9c0bbbbd91e819760e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pappu&#39;s gravatar image" /><p><span>pappu</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pappu has no accepted answers">0%</span></p></div></div><div id="comments-container-25349" class="comments-container"></div><div id="comment-tools-25349" class="comment-tools"></div><div class="clear"></div><div id="comment-25349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25420"></span>

<div id="answer-container-25420" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25420-score" class="post-score" title="current number of votes">1</div><span id="post-25420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you are not capturing on the T1 interface, but on an ethernet interface in the path between the end-systems and the router that connects to the T1 interface.</p><p>Since the ethernet interface has a higher bandwidth, there can bursts with a higher bandwidth due to buffering on the router.</p><p>If I was wrong in my assumption, please supply more details on where you did your capture and how you created your graph.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25420" class="comments-container"><span id="25424"></span><div id="comment-25424" class="comment"><div id="post-25424-score" class="comment-score"></div><div class="comment-text"><p>Hi SYN-bit. These T1 lands on a router after which I have a span port which is a Gig port which goes to my monitoring tool where I am taking this trace.<br />
</p><p>if you can elaborate more or have any good article that I can read that will be very helpful.</p></div><div id="comment-25424-info" class="comment-info"><span class="comment-age">(30 Sep '13, 14:57)</span> <span class="comment-user userinfo">pappu</span></div></div><span id="25428"></span><div id="comment-25428" class="comment"><div id="post-25428-score" class="comment-score"></div><div class="comment-text"><p>Imagine sending 10000 bytes over the T1 from a system on the internal network. Those 10000 bytes can be sent to the router at 1 Gbit/s. The router will buffer all 10000 bytes and will send the data at 1.54 Mbit/s on the T1. As you capture on the 1 Gbit/s interface, you will see the data being sent at 1 Gbit/s, even though on the T1 it is sent at 1.54 Mbit/s.</p><p>Of course you can not send data to the router at 1 Gbit/s for a long period, as the buffers will fill up and packets will be dropped. The TCP protocol has mechanisms built in to prevent that from happening by adjusting the rate at which data is sent. But still in small intervals there will be higher bandwidths visible.</p></div><div id="comment-25428-info" class="comment-info"><span class="comment-age">(30 Sep '13, 15:14)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-25420" class="comment-tools"></div><div class="clear"></div><div id="comment-25420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25352"></span>

<div id="answer-container-25352" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25352-score" class="post-score" title="current number of votes">0</div><span id="post-25352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By default IO graphs calculate the bandwidth (Bits/tick if you chose that) in <strong>both</strong> directions (inbound and outbound). So, if you want to check only your inbound utilization, you should use a display filter in the IO graphs and choose the local network for IP destination.</p><blockquote><p>ip.dst eq 192.168.1.0/24<br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '13, 19:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-25352" class="comments-container"><span id="25396"></span><div id="comment-25396" class="comment"><div id="post-25396-score" class="comment-score"></div><div class="comment-text"><p>Thank You Kurt, I have been using the ip.src and ip.dst filters. But still I see a spike in utilization that would go above the normal bandwidth.</p><p>The big green spike that you see is the spike above the normal 1.5 Mbps of the actual T1 bandwidth.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_-bandwidth_small.png" alt="alt text" /></p></div><div id="comment-25396-info" class="comment-info"><span class="comment-age">(30 Sep '13, 09:06)</span> <span class="comment-user userinfo">pappu</span></div></div><span id="25397"></span><div id="comment-25397" class="comment"><div id="post-25397-score" class="comment-score"></div><div class="comment-text"><p>can you please add a screenshot of the IO graph settings?</p></div><div id="comment-25397-info" class="comment-info"><span class="comment-age">(30 Sep '13, 10:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="25427"></span><div id="comment-25427" class="comment"><div id="post-25427-score" class="comment-score"></div><div class="comment-text"><p>do you see frames larger than 1500 bytes? If so, your interface might support TCP offloading and Wiresharks calculation for the throughput will get corrupted by the large frames, as it thinks there are far more bits/s than are there in reality (several real frames in on large frame that wireshark sees)</p></div><div id="comment-25427-info" class="comment-info"><span class="comment-age">(30 Sep '13, 15:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25352" class="comment-tools"></div><div class="clear"></div><div id="comment-25352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

