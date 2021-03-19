+++
type = "question"
title = "what does &quot;packets dropped&quot; really mean ?"
description = '''hi experts - I am running a capture with dumpcap and rawshark on a very busy machine. I usually get a report like &quot;Packets: 100847 Packets dropped: 1124898&quot; from dumpcap (when I am killing it after 100,000 packets).  dumpcap process is configured to capture on:   one of 8 interfaces tcp port 80  (ex...'''
date = "2011-02-02T01:40:00Z"
lastmod = "2011-02-02T18:49:00Z"
weight = 2095
keywords = [ "packets", "dumpcap", "dropped" ]
aliases = [ "/questions/2095" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [what does "packets dropped" really mean ?](/questions/2095/what-does-packets-dropped-really-mean)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2095-score" class="post-score" title="current number of votes">3</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>hi experts -</p><p>I am running a capture with dumpcap and rawshark on a very busy machine. I usually get a report like "Packets: 100847 Packets dropped: 1124898" from dumpcap (when I am killing it after 100,000 packets).</p><p>dumpcap process is configured to capture on:</p><ol><li>one of 8 interfaces</li><li>tcp port 80</li></ol><p>(example:/root/monitor/wireshark-1.4.2/.libs/dumpcap -w- -f tcp port 80 -i eth4)</p><p>does the "packet dropped" count include packets from :</p><ol><li>other interfaces</li><li>non tcp / non port 80 ,</li></ol><p><strong>or is it just packets dropped to dumpcap not being able to capture fast enough ?</strong> is there a general way to check the reason for dropped packets ?</p><p>thanks - Yoav.</p></div><div id="question-tags" class="tags-container tags">packets dumpcap dropped</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '11, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/7eff7b23646c5be465e00815aabcf9b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yoav&#39;s gravatar image" /><p>yoav<br />
<span class="score" title="86 reputation points">86</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yoav has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Feb '11, 01:44</p></div></div><div id="comments-container-2095" class="comments-container"></div><div id="comment-tools-2095" class="comment-tools"></div><div class="clear"></div><div id="comment-2095-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2120"></span>

<div id="answer-container-2120" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2120-score" class="post-score" title="current number of votes">7</div></div></td><td><div class="item-right"><div class="answer-body"><p>It means "packets dropped because they came in too fast for dumpcap to save"; the packet capture mechanisms that libpcap/WinPcap use (dumpcap, like tcpdump and many other packet-capture programs, uses libpcap/WinPcap) have a buffer into which packets received from the network are dumped, and if that buffer isn't emptied fast enough by the application, packets that arrive will be discarded. That's what the mechanisms count as dropped packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '11, 18:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2120" class="comments-container"></div><div id="comment-tools-2120" class="comment-tools"></div><div class="clear"></div><div id="comment-2120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

