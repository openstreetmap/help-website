+++
type = "question"
title = "Libpcap won&#x27;t capture multiple interfaces simultaneously."
description = '''Hello.  I have an application which uses libpcap and captures the traffic on multiple interfaces.  I do have three interfaces eth0, eth1 and wlan0 .  When my interface eth1 is down, libpcap works on eth0 as expected. But with eth1 on , it never works. If I enable eth0 and eth1 both then capture on e...'''
date = "2013-01-18T01:43:00Z"
lastmod = "2013-03-01T15:39:00Z"
weight = 17767
keywords = [ "pcap" ]
aliases = [ "/questions/17767" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Libpcap won't capture multiple interfaces simultaneously.](/questions/17767/libpcap-wont-capture-multiple-interfaces-simultaneously)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17767-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I have an application which uses libpcap and captures the traffic on multiple interfaces. I do have three interfaces eth0, eth1 and wlan0 . When my interface eth1 is down, libpcap works on eth0 as expected. But with eth1 on , it never works. If I enable eth0 and eth1 both then capture on eth1 works and on eth0 interface it wont works.</p><p>Any idea, on how to overcome this problem ?</p><p>Best yash</p></div><div id="question-tags" class="tags-container tags">pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '13, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/5dc8192968061e7ff0475f55dc94802f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yash&#39;s gravatar image" /><p>yash<br />
<span class="score" title="2 reputation points">2</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yash has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jan '13, 02:10</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-17767" class="comments-container"><span id="17768"></span><div id="comment-17768" class="comment"><div id="post-17768-score" class="comment-score"></div><div class="comment-text"><p>Not really a Wireshark question. You may be better off asking on the mailing list for libpcap <a href="http://www.tcpdump.org/#mailing-lists">here</a>.</p></div><div id="comment-17768-info" class="comment-info"><span class="comment-age">(18 Jan '13, 01:49)</span> grahamb ♦</div></div></div><div id="comment-tools-17767" class="comment-tools"></div><div class="clear"></div><div id="comment-17767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19080"></span>

<div id="answer-container-19080" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19080-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As noted, this isn't really a Wireshark question, it's a libpcap question.</p><p>The mailing list for libpcap questions is tcpdump-workers; as per grahamb's comment, information on the tcpdump.org mailing lists can be found <a href="http://www.tcpdump.org/#mailing-lists">here</a>. (It's not a tcpdump question, either, but tcpdump-workers is, the name notwithstanding, a list for both tcpdump and libpcap.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 15:39</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19080" class="comments-container"></div><div id="comment-tools-19080" class="comment-tools"></div><div class="clear"></div><div id="comment-19080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

