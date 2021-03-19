+++
type = "question"
title = "Capture ALL incoming traffic and ONLY incoming traffic."
description = '''Hi  I have a set up with one switch and 4 hosts. I am capturing the traffic at Host interface. I am using below command to capture the traffic. tcpdump -w filename.pcap -i eth1 It shows all the incoming and outgoing packets. I am interested in seeing only the incoming packets. It uses multiple port ...'''
date = "2014-09-09T13:41:00Z"
lastmod = "2014-09-09T16:28:00Z"
weight = 36127
keywords = [ "filter", "incoming", "tcpdump", "tshark", "wireshark" ]
aliases = [ "/questions/36127" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture ALL incoming traffic and ONLY incoming traffic.](/questions/36127/capture-all-incoming-traffic-and-only-incoming-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36127-score" class="post-score" title="current number of votes">0</div><span id="post-36127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have a set up with one switch and 4 hosts. I am capturing the traffic at Host interface. I am using below command to capture the traffic.</p><p>tcpdump -w filename.pcap -i eth1</p><p>It shows all the incoming and outgoing packets. I am interested in seeing only the incoming packets. It uses multiple port numbers. How can i achieve this ?</p><p>Regards, Navaz</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-incoming" rel="tag" title="see questions tagged &#39;incoming&#39;">incoming</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '14, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/7ebc4294ff0928fd4def898edda41aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="navaz&#39;s gravatar image" /><p><span>navaz</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="navaz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Sep '14, 17:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-36127" class="comments-container"></div><div id="comment-tools-36127" class="comment-tools"></div><div class="clear"></div><div id="comment-36127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36132"></span>

<div id="answer-container-36132" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36132-score" class="post-score" title="current number of votes">0</div><span id="post-36132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After few searches i found this.</p><p>Outgoing from 192.168.0.1: tcpdump -i eth0 ip -X src host 192.168.0.1</p><p>Incoming to 192.168.0.1: tcpdump -i eth0 ip -X dst host 192.168.0.1</p><p>Thanks Navaz</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '14, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/7ebc4294ff0928fd4def898edda41aae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="navaz&#39;s gravatar image" /><p><span>navaz</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="navaz has no accepted answers">0%</span></p></div></div><div id="comments-container-36132" class="comments-container"></div><div id="comment-tools-36132" class="comment-tools"></div><div class="clear"></div><div id="comment-36132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

