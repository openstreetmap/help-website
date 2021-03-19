+++
type = "question"
title = "Protocol identification"
description = '''Is there a way to identify the protocol based on the captured data by wireshark?  Data from 7 multicast packets captured is shown below. p.#1 4c 45 49 00 00 ff 09 a3 00 1c 00 30 00 72 1c 16 b5 81 9d 47 ee 18 fb 40 b7 38 ef c5 95 a6 d3 34 00 06 00 00 00 00 00 03 00 00 00 0c 05 01 04 00 18 c1 35 08 06...'''
date = "2013-05-09T13:53:00Z"
lastmod = "2013-05-09T16:16:00Z"
weight = 21072
keywords = [ "udp", "protocol" ]
aliases = [ "/questions/21072" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Protocol identification](/questions/21072/protocol-identification)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to identify the protocol based on the captured data by wireshark? Data from 7 multicast packets captured is shown below.</p><pre><code>p.#1 4c 45 49 00 00 ff 09 a3 00 1c 00 30 00 72 1c 16 b5 81 9d 47 ee 18 fb 40 b7 38 ef c5 95 a6 d3 34 00 06 00 00 00 00 00 03 00 00 00 0c 05 01 04 00 18 c1 35 08 06 00 00 00 00 01 16 eb

p.#2 4c 45 49 05 00 ff 09 49 00 02 00 18 00 00 00 6f 00 2e b0 99 00 06 00 00 00 00 00 03 00 00 00 0c 08 00 00 00

p.#3 4c 45 49 00 00 ff 09 a4 00 1c 00 30 00 72 1c 16 b5 81 9d 47 ee 18 fb 40 b7 38 ef c5 95 a6 d3 34 00 06 00 00 00 00 00 03 00 00 00 0c 05 01 04 00 18 c1 35 08 06 00 00 00 00 01 16 eb

p.#4 4c 45 49 05 00 ff 09 4a 00 02 00 18 00 00 00 6f 00 2e b0 99 00 06 00 00 00 00 00 03 00 00 00 0c 08 00 00 00

p.#5 4c 45 49 00 00 ff 09 a5 00 1c 00 30 00 72 1c 16 b5 81 9d 47 ee 18 fb 40 b7 38 ef c5 95 a6 d3 34 00 06 00 00 00 00 00 03 00 00 00 0c 05 01 04 00 18 c1 35 08 06 00 00 00 00 01 16 eb

p.#6 4c 45 49 05 00 ff 09 4b 00 02 00 18 00 00 00 6f 00 2e b0 99 00 06 00 00 00 00 00 03 00 00 00 0c 08 00 00 00

p.#7 4c 45 49 00 00 ff 09 a6 00 1c 00 30 00 72 1c 16 b5 81 9d 47 ee 18 fb 40 b7 38 ef c5 95 a6 d3 34 00 06 00 00 00 00 00 03 00 00 00 0c 05 01 04 00 18 c1 35 08 06 00 00 00 00 01 16 eb</code></pre></div><div id="question-tags" class="tags-container tags">udp protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '13, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-21072" class="comments-container"><span id="21073"></span><div id="comment-21073" class="comment"><div id="post-21073-score" class="comment-score"></div><div class="comment-text"><blockquote><p>based on the captured data by wireshark?</p></blockquote><p>please post the capture file somewhere (google docs, dropbox, cloudshark).</p></div><div id="comment-21073-info" class="comment-info"><span class="comment-age">(09 May '13, 15:18)</span> Kurt Knochner ♦</div></div><span id="21074"></span><div id="comment-21074" class="comment"><div id="post-21074-score" class="comment-score"></div><div class="comment-text"><p><a href="http://cloudshark.org/captures/c90ed11d7b26">Link to Cloudshark</a></p></div><div id="comment-21074-info" class="comment-info"><span class="comment-age">(09 May '13, 15:47)</span> net_tech</div></div></div><div id="comment-tools-21072" class="comment-tools"></div><div class="clear"></div><div id="comment-21072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21075"></span>

<div id="answer-container-21075" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21075-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>UDP Port 2056 is sometimes used by a game called Civilization 4 (in multiplayer mode).</p><p>Is that game installed on the client (IP address 192.168.20.222)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '13, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-21075" class="comments-container"><span id="21076"></span><div id="comment-21076" class="comment"><div id="post-21076-score" class="comment-score"></div><div class="comment-text"><p>No, 192.168.20.222 is a Lutron <a href="http://www.lutron.com/en-US/Products/Pages/WholeHomeSystems/RadioRA2/Overview.aspx">RadioRa2</a> device, it multicasts over port 2056, which allows <a href="https://play.google.com/store/apps/details?id=com.lutron.lutronhomeplus&amp;feature=search_result#?t=W251bGwsMSwyLDEsImNvbS5sdXRyb24ubHV0cm9uaG9tZXBsdXMiXQ..">Lutron Home Control App</a> on an iPhone or Android device locate RadioRa2 on the network.</p></div><div id="comment-21076-info" class="comment-info"><span class="comment-age">(09 May '13, 17:46)</span> net_tech</div></div><span id="21083"></span><div id="comment-21083" class="comment"><div id="post-21083-score" class="comment-score"></div><div class="comment-text"><p>Well, then this is a proprietary protocol used by your Lutron device. See your other question regarding this:</p><blockquote><p><a href="http://ask.wireshark.org/questions/19042/dissect-traffic-between-lutron-radiora2-and-alarmcom">http://ask.wireshark.org/questions/19042/dissect-traffic-between-lutron-radiora2-and-alarmcom</a></p></blockquote></div><div id="comment-21083-info" class="comment-info"><span class="comment-age">(10 May '13, 02:28)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-21075" class="comment-tools"></div><div class="clear"></div><div id="comment-21075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

