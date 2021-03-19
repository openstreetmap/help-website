+++
type = "question"
title = "Wireshark Change time UTC"
description = '''Can someone help me to change UTC -3 times from my wireshark? '''
date = "2017-06-26T17:23:00Z"
lastmod = "2017-06-27T10:02:00Z"
weight = 62310
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/62310" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Change time UTC](/questions/62310/wireshark-change-time-utc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62310-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone help me to change UTC -3 times from my wireshark?</p></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '17, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/a95becaa9162bc901663cdd569efda99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorgeMiguelr210&#39;s gravatar image" /><p>JorgeMiguelr210<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorgeMiguelr210 has no accepted answers">0%</span></p></div></div><div id="comments-container-62310" class="comments-container"><span id="62316"></span><div id="comment-62316" class="comment"><div id="post-62316-score" class="comment-score"></div><div class="comment-text"><p>So is that "change the time stamps for the packets in the file" or is that "change the time stamps in the <em>names</em> of capture files"? From "I want my pcap file save the logs with the date and time of my local machine", it sounds as if you mean the time stamps in the <em>file name</em> rather than in the <em>packets</em>.</p></div><div id="comment-62316-info" class="comment-info"><span class="comment-age">(26 Jun '17, 18:40)</span> Guy Harris ♦♦</div></div><span id="62329"></span><div id="comment-62329" class="comment"><div id="post-62329-score" class="comment-score"></div><div class="comment-text"><p>Change the time stamps for the packets in the file</p></div><div id="comment-62329-info" class="comment-info"><span class="comment-age">(27 Jun '17, 05:56)</span> JorgeMiguelr210</div></div></div><div id="comment-tools-62310" class="comment-tools"></div><div class="clear"></div><div id="comment-62310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62331"></span>

<div id="answer-container-62331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62331-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to change timestamps in a capture file have a look at the <code>-t</code> option of the <a href="https://www.wireshark.org/docs/man-pages/editcap.html">editcap</a> command line tool.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '17, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62331" class="comments-container"></div><div id="comment-tools-62331" class="comment-tools"></div><div class="clear"></div><div id="comment-62331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62339"></span>

<div id="answer-container-62339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62339-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Time stamps in pcap and pcapng files are stored as UTC (seconds and fractions of a second since January 1, 1970, 00:00:00 UTC, although leap seconds are usually not counted). Programs that read those files call routines to convert that to local time.</p><p>So if your machine isn't in the UTC-3 time zone, but you want to display the time stamps as UTC-3, you'd have to either shift the time stamps by the difference between UTC-3 and the time zone your machine is set for (which means that somebody <em>else</em> reading the capture file would, by default, see the time stamps incorrectly if they're in a different time zone), as per Jaap's suggestion, or you'd have to change the time zone setting of your machine, or you'd have to change the time zone for the instance Wireshark that's reading the file.</p><p>On most UN*Xes, you can change the time zone for a particular program by running it from the command line and setting the <code>TZ</code> environment variable to the appropriate value, for example <code>TZ=Europe/London wireshark {filename}</code> if you want the time stamps to display as time in the UK.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '17, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-62339" class="comments-container"></div><div id="comment-tools-62339" class="comment-tools"></div><div class="clear"></div><div id="comment-62339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

