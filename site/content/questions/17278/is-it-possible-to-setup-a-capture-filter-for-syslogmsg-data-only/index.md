+++
type = "question"
title = "Is it possible to setup a capture filter for syslog.msg data only"
description = '''I&#x27;m looking to capture packets that match only have syslog info matching the filter &quot;successful&quot;. Because of the number of packets coming to the device, I&#x27;m not looking for a display filter but a CAPTURE FILTER. I have the first part easy as &quot;port syslog&quot; but must missing the last part. In the displ...'''
date = "2012-12-27T12:39:00Z"
lastmod = "2012-12-27T14:36:00Z"
weight = 17278
keywords = [ "syslog", "capture-filter" ]
aliases = [ "/questions/17278" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to setup a capture filter for syslog.msg data only](/questions/17278/is-it-possible-to-setup-a-capture-filter-for-syslogmsg-data-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17278-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking to capture packets that match only have syslog info matching the filter "successful". Because of the number of packets coming to the device, I'm not looking for a display filter but a CAPTURE FILTER.</p><p>I have the first part easy as "port syslog" but must missing the last part. In the display filter I would use "syslog.msg contains "successful" but of course this will not work in the capture filter.</p><p>Any ideas would be helpful and thanks.</p></div><div id="question-tags" class="tags-container tags">syslog capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '12, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/e3d935d0277ac05a9fc833c07b809b8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sonicpepsi&#39;s gravatar image" /><p>sonicpepsi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sonicpepsi has no accepted answers">0%</span></p></div></div><div id="comments-container-17278" class="comments-container"></div><div id="comment-tools-17278" class="comment-tools"></div><div class="clear"></div><div id="comment-17278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17279"></span>

<div id="answer-container-17279" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17279-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You probably can't do what you want. Capture filters are much simpler than display filters and simply don't have the same functionality. There is no capture filter equivalent to "syslog.msg contains".</p><p>IF the string "successful" always appeared in exactly the same place in a frame, you could use byte offset filters to look for it, but my reading of RFC 5424, "The Syslog Protocol," is that syslog packets contain a number of variable length fields, and therefore subsequent fields won't always occur in exactly the same position within the frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '12, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-17279" class="comments-container"><span id="17281"></span><div id="comment-17281" class="comment"><div id="post-17281-score" class="comment-score"></div><div class="comment-text"><p>That's what I was thinking but didn't want to miss out in the event there was something I didn't see. Thanks for the response.</p></div><div id="comment-17281-info" class="comment-info"><span class="comment-age">(27 Dec '12, 14:09)</span> sonicpepsi</div></div></div><div id="comment-tools-17279" class="comment-tools"></div><div class="clear"></div><div id="comment-17279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17282"></span>

<div id="answer-container-17282" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17282-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm looking to capture packets that match only have syslog info matching the filter "successful".</p></blockquote><p>You can't do that with tcpdump or Wireshark, however ngrep would work that way.</p><blockquote><p><code>http://ngrep.sourceforge.net/</code><br />
</p></blockquote><p>call it like this:</p><blockquote><p><code>ngrep -O output.cap -s 0 -d eth0 'successful' 'port 514'</code><br />
</p></blockquote><p>At a high packet rate, you may miss some packets, due to overload issues.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '12, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Dec '12, 14:40</p></div></div><div id="comments-container-17282" class="comments-container"></div><div id="comment-tools-17282" class="comment-tools"></div><div class="clear"></div><div id="comment-17282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

