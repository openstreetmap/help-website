+++
type = "question"
title = "Capture all network traffic to single ip address"
description = '''Hi I&#x27;ve just started using wireshark and don&#x27;t know what i&#x27;m doing!! I need to capture all traffic on our LAN going to a single ip address so that I can find individual pc&#x27;s. As soon as I have the ip addresses I can do a lookup in DNS. Is this possible and if so how using the Wireshark GUI? Thanks'''
date = "2012-06-28T07:47:00Z"
lastmod = "2012-06-28T13:45:00Z"
weight = 12274
keywords = [ "capture-filter" ]
aliases = [ "/questions/12274" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture all network traffic to single ip address](/questions/12274/capture-all-network-traffic-to-single-ip-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12274-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I've just started using wireshark and don't know what i'm doing!! I need to capture all traffic on our LAN going to a single ip address so that I can find individual pc's. As soon as I have the ip addresses I can do a lookup in DNS. Is this possible and if so how using the Wireshark GUI?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '12, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/c160b8d4d634984a852546919917b489?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xenolith5&#39;s gravatar image" /><p>xenolith5<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xenolith5 has no accepted answers">0%</span></p></div></div><div id="comments-container-12274" class="comments-container"></div><div id="comment-tools-12274" class="comment-tools"></div><div class="clear"></div><div id="comment-12274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12281"></span>

<div id="answer-container-12281" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12281-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://wiki.wireshark.org/DisplayFilters">http://wiki.wireshark.org/DisplayFilters</a></p><p>If I understand correctly, you can use the filter bar at the top of the Wireshark GUI to search for packets travelling to or from a particular ip address.</p><p>Given an ip address xxx.xxx.xxx.xxx , you would input into the filter:</p><pre><code>       ip.src==xxx.xxx.xxx.xxx and ip.dest==xxx.xxx.xxx.xxx</code></pre><p>You should get all packets that are travelling to and from that ip address/computer!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '12, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/40b1f396144af1f57dd3b8a211387e6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ian&#39;s gravatar image" /><p>Ian<br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ian has no accepted answers">0%</span></p></div></div><div id="comments-container-12281" class="comments-container"></div><div id="comment-tools-12281" class="comment-tools"></div><div class="clear"></div><div id="comment-12281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12287"></span>

<div id="answer-container-12287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12287-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture all traffic going to IPv4 address XXX.XXX.XXX.XXX, use Capture -&gt; Options to start the capture, and specify a capture filter of <code>dst host XXX.XXX.XXX.XXX</code>.</p><p>If you want to capture all traffic going to <em>and coming from</em> that address, use <code>host XXX.XXX.XXX.XXX</code> instead; <code>dst host XXX.XXX.XXX.XXX</code> will <em>NOT</em> capture any traffic coming <em>from</em> that machine.</p><p>If, however, you want to do a <em>single</em> capture and then look at it to find out traffic coming from multiple <em>different</em> PCs, capture without a capture filter and then use display filters for each of the machines, as Ian suggested.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '12, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12287" class="comments-container"><span id="12301"></span><div id="comment-12301" class="comment"><div id="post-12301-score" class="comment-score"></div><div class="comment-text"><p>Thanks Ian and Guy, when I try both options I only see traffic from my interface not all lan traffic. In the capture options there is a tick next to promiscuous mode which I thought allowed all packets through. Is this due to routers and switches?</p><p>Gavin</p></div><div id="comment-12301-info" class="comment-info"><span class="comment-age">(29 Jun '12, 00:52)</span> xenolith5</div></div><span id="12319"></span><div id="comment-12319" class="comment"><div id="post-12319-score" class="comment-score"></div><div class="comment-text"><p>Generally, Wireshark can interpret when packets go from a device to a switch/router, but depending on your setup (what device is plugged into which switch, and where is that switch plugged into), you may run into issues where the packets being analyzed by Wireshark appear to only be coming from the switch in between. What is your setup currently?</p></div><div id="comment-12319-info" class="comment-info"><span class="comment-age">(29 Jun '12, 08:37)</span> Ian</div></div></div><div id="comment-tools-12287" class="comment-tools"></div><div class="clear"></div><div id="comment-12287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

