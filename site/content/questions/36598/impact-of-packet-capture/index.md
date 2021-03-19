+++
type = "question"
title = "impact of packet capture"
description = '''We use wireshark for analyzing packet captures we collect with tcpdump and/or tshark on Linux systems. I have been trying to understand the impact of running tcpdump/tshark on packet flow of the host system, but I cannot seem to find much information on this. Can anyone explain how these tools inter...'''
date = "2014-09-25T06:45:00Z"
lastmod = "2014-10-20T05:40:00Z"
weight = 36598
keywords = [ "impact", "performance", "packet-capture", "tcpdump", "tshark" ]
aliases = [ "/questions/36598" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [impact of packet capture](/questions/36598/impact-of-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36598-score" class="post-score" title="current number of votes">0</div><span id="post-36598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We use wireshark for analyzing packet captures we collect with tcpdump and/or tshark on Linux systems. I have been trying to understand the impact of running tcpdump/tshark on packet flow of the host system, but I cannot seem to find much information on this. Can anyone explain how these tools interact with the host system and the impact on network activity?<br />
</p><p>Is any latency introduced into the session or risk of packets being dropped by the kernel due to the additional demands of copying incoming network data for the capture?</p><p>Thanks, Ryan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-impact" rel="tag" title="see questions tagged &#39;impact&#39;">impact</span> <span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '14, 06:45</strong></p><img src="https://secure.gravatar.com/avatar/ba1199f4d360c53a6cc8aa6aa5da37c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryber&#39;s gravatar image" /><p><span>ryber</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryber has one accepted answer">16%</span> </br></p></div></div><div id="comments-container-36598" class="comments-container"></div><div id="comment-tools-36598" class="comment-tools"></div><div class="clear"></div><div id="comment-36598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37194"></span>

<div id="answer-container-37194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37194-score" class="post-score" title="current number of votes">2</div><span id="post-37194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't have any numbers for you but for sure adding network capture adds work to the host. Some places where this would be the case:</p><ol><li>If running a capture turns on promiscuous mode then you'll be getting more traffic than usual (in modern switched networks there normally won't be much more). If you for some reason <strong>do</strong> end up getting a lot more traffic then this could affect latency and/or cause more packets to be dropped.</li><li>A monitored packet needs to be copied to 2 applications: the real network application and tcpdump/dumpshark. If you're on a RISC machine like SPARC such an extra copy can be quite expensive; on x86 it's much less of a problem. Unless your CPU usage is quite high this is unlikely to cause significant additional latency or packet drops.</li></ol><p>Of course all of the effects become bigger as traffic rates go up. So: if your traffic rate is not huge and/or your application is not super-critical, sure you can probably safely capture the traffic. Otherwise you might want to invest in a dedicated capture system (attached to a monitor port).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37194" class="comments-container"></div><div id="comment-tools-37194" class="comment-tools"></div><div class="clear"></div><div id="comment-37194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

