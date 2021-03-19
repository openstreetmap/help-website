+++
type = "question"
title = "Verification of counters in a particular range in a packet capture"
description = '''I have got counters based on 2 sec interval.    I need to verify that the count should be in range 1200 to 1600. Is there any way we can do it without parsing whole output?   If for any particular time interval, the count doesn&#x27;t fall into matching range, some error/warning message should get printe...'''
date = "2013-10-16T03:52:00Z"
lastmod = "2013-10-16T07:31:00Z"
weight = 26051
keywords = [ "libwireshark", "wireshark", "counters" ]
aliases = [ "/questions/26051" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Verification of counters in a particular range in a packet capture](/questions/26051/verification-of-counters-in-a-particular-range-in-a-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26051-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have got counters based on 2 sec interval.</p><ul><li><p>I need to verify that the count should be in range 1200 to 1600. Is there any way we can do it without parsing whole output?</p></li><li><p>If for any particular time interval, the count doesn't fall into matching range, some error/warning message should get printed.</p></li><li><p>Is there any method to get average for this counters?</p></li></ul><pre><code># tshark -r q4-mme.pcap -qz io,stat,2,&quot;COUNT(frame.time)frame.time&quot;
===================================================================
IO Statistics
Interval: 2.000 secs
Column #0: COUNT(frame.time)frame.time
                |   Column #0
Time            |          COUNT
000.000-002.000              1241
002.000-004.000              1272
004.000-006.000              1315
006.000-008.000              1371
008.000-010.000              1195
010.000-012.000              1299
012.000-014.000              1305
014.000-016.000              1391
016.000-018.000              1463
018.000-020.000              1454
020.000-022.000              1392
022.000-024.000              1438
024.000-026.000              1362
026.000-028.000              1491
028.000-030.000              1392
030.000-032.000              1422
032.000-034.000              1425
034.000-036.000              1486
036.000-038.000              1449
038.000-040.000              1487
040.000-042.000              1402
042.000-044.000              1420
044.000-046.000              1330
046.000-048.000              1458
048.000-050.000              1420
050.000-052.000               144
===================================================================</code></pre><p>Total number of time intervals is not static (it will vary).</p><p>Please let me know how can I achieve the desired results.</p></div><div id="question-tags" class="tags-container tags">libwireshark wireshark counters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '13, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/963f2abedc2aff60ceae201a8f231d42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="npatel&#39;s gravatar image" /><p>npatel<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="npatel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '14, 22:37</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-26051" class="comments-container"></div><div id="comment-tools-26051" class="comment-tools"></div><div class="clear"></div><div id="comment-26051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26070"></span>

<div id="answer-container-26070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26070-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Please let me know how can I achieve the desired results.</p></blockquote><p>By parsing the output and by checking if your defined conditions do match.</p><blockquote><p>Is there any way we can do it without parsing whole output?</p></blockquote><p>No. Who should do it if not you !?! ;-))</p><p>The be more precise: There is no built-in mechanism in Wireshark/tshark that will do it for you automatically.</p><p>Instead of using tshark, you could create the same with an IO Graph and then check 'visually' (look at the graph) if the COUNT() value exceeds a certain limit.</p><blockquote><p>If for any particular time interval, the count doesn't fall into matching range, some error/warning message should get printed.</p></blockquote><p>As mentioned, there is no automatism in Wireshark/tshark to generate alerts if a traffic pattern meets a certain condition (although that would be a cool feature in Wireshark!). So, it's up to you to parse the tshark output with a script and then generate whatever alert you need.</p><blockquote><p>Is there any method to get average for this counters?</p></blockquote><p>Either do it yourself in a script or feed the tshark output into a spreadsheet software and calculate the average there.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '13, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '13, 07:44</p></div></div><div id="comments-container-26070" class="comments-container"></div><div id="comment-tools-26070" class="comment-tools"></div><div class="clear"></div><div id="comment-26070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

