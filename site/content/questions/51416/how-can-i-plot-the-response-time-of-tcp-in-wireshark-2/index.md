+++
type = "question"
title = "How can I plot the response time of TCP in Wireshark 2?"
description = '''I&#x27;m trying to plot a graph using the I/O Graph function in Wireshark 2.0.1 but I can&#x27;t figure out how to set it up. I have tried to plot the graph using tcp.analysis.ack_rtt but I can&#x27;t figure out how to do it correctly. The Y-axis values gets very big and I can&#x27;t seem to display something else than...'''
date = "2016-04-05T07:56:00Z"
lastmod = "2016-04-05T11:14:00Z"
weight = 51416
keywords = [ "plot", "tcp", "iograph" ]
aliases = [ "/questions/51416" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I plot the response time of TCP in Wireshark 2?](/questions/51416/how-can-i-plot-the-response-time-of-tcp-in-wireshark-2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51416-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to plot a graph using the I/O Graph function in Wireshark 2.0.1 but I can't figure out how to set it up. I have tried to plot the graph using tcp.analysis.ack_rtt but I can't figure out how to do it correctly. The Y-axis values gets very big and I can't seem to display something else than time on the X axis.</p><p>This is my current try: <a href="http://i.imgur.com/MKGTRn2.png">http://i.imgur.com/MKGTRn2.png</a></p><p>I can't seem to figure it out. Please help!</p><p>Thankful for advice</p></div><div id="question-tags" class="tags-container tags">plot tcp iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '16, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/8d6d2b081f367d8f0530178508774b2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inz&#39;s gravatar image" /><p>inz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inz has no accepted answers">0%</span></p></div></div><div id="comments-container-51416" class="comments-container"></div><div id="comment-tools-51416" class="comment-tools"></div><div class="clear"></div><div id="comment-51416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51422"></span>

<div id="answer-container-51422" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51422-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't display something other than time on the X axis. You're plotting how values change over time. What else would you want there?</p><p>Your graph is correct. (Well, except that you have "avg" in the graph title, which implies "average," but you selected MAX as the calculation type instead of AVG. Assuming you really do want maximum, you've done it correctly.)</p><p>Yes, the Y-axis values get very large. I did this for one of my capture files, and it appears that the Y-axis values were in microseconds.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '16, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51422" class="comments-container"><span id="51423"></span><div id="comment-51423" class="comment"><div id="post-51423-score" class="comment-score"></div><div class="comment-text"><p>I think I saw someone have packets on the X axis or something like that. Anyway I think mostly that the big values on the Y axis is the problem, I just disregarded the idea of the graph being correct because of those.</p></div><div id="comment-51423-info" class="comment-info"><span class="comment-age">(05 Apr '16, 11:35)</span> inz</div></div><span id="51424"></span><div id="comment-51424" class="comment"><div id="post-51424-score" class="comment-score"></div><div class="comment-text"><p>It would be nice if Wireshark used seconds or milliseconds instead.</p></div><div id="comment-51424-info" class="comment-info"><span class="comment-age">(05 Apr '16, 12:43)</span> Jim Aragon</div></div><span id="51439"></span><div id="comment-51439" class="comment"><div id="post-51439-score" class="comment-score"></div><div class="comment-text"><p>You could try to use the logarithm view, if the values have a huge range.</p><p>For changing the x value, I think you have to export the trace as a csv file and play around in excel.</p></div><div id="comment-51439-info" class="comment-info"><span class="comment-age">(06 Apr '16, 10:19)</span> Christian_R</div></div></div><div id="comment-tools-51422" class="comment-tools"></div><div class="clear"></div><div id="comment-51422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

