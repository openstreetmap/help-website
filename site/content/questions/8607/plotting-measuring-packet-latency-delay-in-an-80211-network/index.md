+++
type = "question"
title = "Plotting (/measuring) packet latency (delay) in an 802.11 network."
description = '''Hi all, I am trying to plot/measure packet latency (delay) in a 802.11 network using wireshark and I would like to know how people are doing this. Up unitl now, my settings in the I/O Graph are: Units: Advanced Filter: empty, AVG(*): frame.time_delta_displayed As I am relatively new to wireshark I a...'''
date = "2012-01-25T11:08:00Z"
lastmod = "2012-04-16T16:16:00Z"
weight = 8607
keywords = [ "delay", "latency", "802.11" ]
aliases = [ "/questions/8607" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Plotting (/measuring) packet latency (delay) in an 802.11 network.](/questions/8607/plotting-measuring-packet-latency-delay-in-an-80211-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8607-score" class="post-score" title="current number of votes">0</div><span id="post-8607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am trying to plot/measure packet latency (delay) in a 802.11 network using wireshark and I would like to know how people are doing this.</p><p>Up unitl now, my settings in the I/O Graph are: Units: Advanced Filter: empty, AVG(*): frame.time_delta_displayed</p><p>As I am relatively new to wireshark I am not sure whether this is correct, or not.</p><p>Also, as far as I can tell from a previous post, I am NOT supposed to use MAC timestamp filter (wlan.mactime). However, I am not sure if Host timestamp (wlan.hosttime) would be useful. Where do I find more info on this filter? To add to my ignorance, I am not excacly sure whether(/how) I CAN plot wlan.hosttime on the I/O Graph.</p><p>I would like to think I have done a thourough google/wireshark search, but I must have missed something. I am relatively new to wireshark, so please forgive my ignorance.</p><p>The 802.11 traffic was captured with an AirPcap Tx USB adapter and Wireshark Version 1.6.1 (SVN Rev 38096 from /trunk-1.6) running on a Windoze XP SP3 PC.</p><p>Any ideas, or links to sites, books, etc.. would be more than welcome.</p><p>Thanks</p><p>Alex</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '12, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/18440914e73da9d5280d0404ad6cf9a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="almost_linear&#39;s gravatar image" /><p><span>almost_linear</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="almost_linear has no accepted answers">0%</span></p></div></div><div id="comments-container-8607" class="comments-container"><span id="8608"></span><div id="comment-8608" class="comment"><div id="post-8608-score" class="comment-score"></div><div class="comment-text"><p>Let's start with a basic question: What are you actually trying to measure ? delay/latency between what and what ?</p></div><div id="comment-8608-info" class="comment-info"><span class="comment-age">(25 Jan '12, 11:17)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="8609"></span><div id="comment-8609" class="comment"><div id="post-8609-score" class="comment-score"></div><div class="comment-text"><p>Hi Bill,</p><p>I can see how my question is not clear, probably becasue I have gaps in my knowledge.</p><p>What I would like to find out is how long it takes a data packet transmitted from a station, to be received and acknowldeged from an access point.</p><p>Hope this is more clear.</p><p>Thanks Alex</p></div><div id="comment-8609-info" class="comment-info"><span class="comment-age">(25 Jan '12, 11:43)</span> <span class="comment-user userinfo">almost_linear</span></div></div></div><div id="comment-tools-8607" class="comment-tools"></div><div class="clear"></div><div id="comment-8607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10202"></span>

<div id="answer-container-10202" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10202-score" class="post-score" title="current number of votes">0</div><span id="post-10202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Bill, I know this is not a very timely answer, but here it goes: You can measure latency in a network, or the delay from client to a server using ping.<br />
</p><p>From your Windows machine click on Start. Then type in cmd to launch the black "DOS command" window. At the &gt; type in something like &gt;ping <a href="http://amazon.com">amazon.com</a><br />
Your computer will launch ping and then you will get a reply something like this:</p><p>Reply from 72.21.221.176: bytes=32 time&lt; 15ms TTL=128 Reply from 72.21.221.176: bytes=32 time&lt; 10ms TTL=128 Reply from 72.21.221.176: bytes=32 time&lt; 10ms TTL=128 Reply from 72.21.221.176: bytes=32 time&lt; 10ms TTL=128</p><p>Ping statistics for 72.21.221.176: Packets: Sent = 4, Received =4, Lost = 0 (0% loss), Approximate round trip in milli-seconds: Minimum = 10ms, Maximum = 15ms, Average = 11ms</p><p>This may not always work. One reason may be that the DNS server is not translating URLs to IP addresses properly. The other reason is that firewalls or other filtering is preventing ping from working.</p><p>This should get you started. Konrad</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/ad404df93f33762ef82765f1d910a789?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Konrad&#39;s gravatar image" /><p><span>Konrad</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Konrad has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '12, 16:17</strong> </span></p></div></div><div id="comments-container-10202" class="comments-container"></div><div id="comment-tools-10202" class="comment-tools"></div><div class="clear"></div><div id="comment-10202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

