+++
type = "question"
title = "Mixing two rtp streams of a voip call"
description = '''I am trying to mix two rtp streams that I extracted from the pcap of a voip call (using rtpbreak). Problem is when I mix them ( sox -m) . The audio from the two streams are never in sync. But when I play the streams using wireshark, it is in sync. Procedure used  let the timestamp of the first packe...'''
date = "2014-12-10T19:12:00Z"
lastmod = "2014-12-10T19:12:00Z"
weight = 38521
keywords = [ "voipcalls", "wireshark", "rtp", "sync" ]
aliases = [ "/questions/38521" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mixing two rtp streams of a voip call](/questions/38521/mixing-two-rtp-streams-of-a-voip-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38521-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to mix two rtp streams that I extracted from the pcap of a voip call (using rtpbreak).</p><p>Problem is when I mix them ( sox -m) . The audio from the two streams are never in sync. But when I play the streams using wireshark, it is in sync.</p><p>Procedure used</p><ol><li>let the timestamp of the first packets of the 2 rtp streams(say A and B) be t1 and t2 (t1 &gt; t2).</li><li>pad (t1 - t2) amt of time at beginning of A to make stream C</li><li>mix B and C.</li></ol><p>It would be very helpful if someone could tell me how it is done in Wireshark. Thanks in advance</p></div><div id="question-tags" class="tags-container tags">voipcalls wireshark rtp sync</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '14, 19:12</strong></p><img src="https://secure.gravatar.com/avatar/b50929bbf0ce05d5c8984dc841f2a449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nightwatcher&#39;s gravatar image" /><p>nightwatcher<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nightwatcher has no accepted answers">0%</span></p></div></div><div id="comments-container-38521" class="comments-container"></div><div id="comment-tools-38521" class="comment-tools"></div><div class="clear"></div><div id="comment-38521-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

