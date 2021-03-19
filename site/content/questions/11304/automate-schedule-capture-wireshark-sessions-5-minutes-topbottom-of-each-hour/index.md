+++
type = "question"
title = "Automate / Schedule Capture WireShark sessions? (5 minutes top/bottom of each hour)"
description = '''Hello, I&#x27;ve been asked to capture data for my Ceton InfiniTV PCI CableCard tuner card. The error I&#x27;m trying to capture happens at the start of TV Recordings. The problem is, the error is very intermittent. I can&#x27;t leave WireShark in capture mode for more then 5 or 10 minutes, or they data captured w...'''
date = "2012-05-24T02:34:00Z"
lastmod = "2012-05-24T03:27:00Z"
weight = 11304
keywords = [ "shedule", "automatically" ]
aliases = [ "/questions/11304" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Automate / Schedule Capture WireShark sessions? (5 minutes top/bottom of each hour)](/questions/11304/automate-schedule-capture-wireshark-sessions-5-minutes-topbottom-of-each-hour)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11304-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I've been asked to capture data for my Ceton InfiniTV PCI CableCard tuner card. The error I'm trying to capture happens at the start of TV Recordings. The problem is, the error is very intermittent. I can't leave WireShark in capture mode for more then 5 or 10 minutes, or they data captured will be WAY too big!<br />
</p><p>Is there a way to schedule WireShark to capture data for 5 minutes at the top and bottom of each other? That way I can set it and forget it until the error happens.</p><p>I'm getting frustrated trying to manually capture it. As you can imagine with Murphy's Law, the days I don't capture I get the error, and the days I spend all day trying to capture I get nothing.</p><p>So again, can I use Scheduled Tasks in Windows 7 or something? If so how? Can I have the data be captured and saved anywhere else other than C: ? My C: is s smaller SD drive. I could let the capture run longer if I have it going to D: or a network share.</p></div><div id="question-tags" class="tags-container tags">shedule automatically</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '12, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/e7d77c44c0202c720bf8f66673432c85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JazJon&#39;s gravatar image" /><p>JazJon<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JazJon has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-11304" class="comments-container"></div><div id="comment-tools-11304" class="comment-tools"></div><div class="clear"></div><div id="comment-11304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11305"></span>

<div id="answer-container-11305" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11305-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should look into using dumpcap. That will capture the traffic and write it directly to disk without using up a whole lot of memory trying to interpret the capture. You can then load the captures using Wireshark and examine them. Dumpcap can save the packets to any part of your filesystem and can filter out irrelevant packets and rotate the output files over time or size so that they aren't too big and painful to work with in Wireshark.</p><p>Look at the man page for dumpcap <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">here</a>. You should particularly investigate the filters to minimise the traffic you capture to the items of interest, the snaplen to limit the size of each packet stored on disk, and the ring buffer options to use multiple files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '12, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11305" class="comments-container"><span id="11316"></span><div id="comment-11316" class="comment"><div id="post-11316-score" class="comment-score"></div><div class="comment-text"><p>I found a solution that works for now. (so I can capture 24/7) See below :)</p><hr /><p>Posted on: 24 May 2012 12:26 PM Hi Jon, One trick that might be helpful to you is to set up Wireshark to capture with a circular buffer (so it only saves, for instance, the last 500MB of data) - that way you can just stop the capture once the issue occurs.</p><p>Thank you, Ceton Support</p><hr /><p>Jon User</p><p>Posted on: 24 May 2012 01:02 PM</p><p>Thanks I found what you suggested under WireShark Capture Options.</p><p>I assigned a capture file to E:\WireShark my unused 500MB drive. I add the circular capture option going to my It's set to write up to 220MB per file and only keep a maximum of 2 files.</p><p>I have WireShark running 24/7 now and will stop/save the capture 60 seconds after I notice the error message popup live. (will need to catch one live of course)</p><p>Stand by</p></div><div id="comment-11316-info" class="comment-info"><span class="comment-age">(24 May '12, 13:03)</span> JazJon</div></div><span id="11317"></span><div id="comment-11317" class="comment"><div id="post-11317-score" class="comment-score"></div><div class="comment-text"><p>You'll probably run out of memory running Wireshark 24/7. Even though Wireshark switches files, it's still accumulating state.</p></div><div id="comment-11317-info" class="comment-info"><span class="comment-age">(24 May '12, 13:23)</span> grahamb ♦</div></div></div><div id="comment-tools-11305" class="comment-tools"></div><div class="clear"></div><div id="comment-11305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

