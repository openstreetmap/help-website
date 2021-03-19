+++
type = "question"
title = "Tshark.exe is closing abnormally after some hours of execution."
description = '''Hi, i need to take USB trace for 7 days but after some hours of trace capture, the tshark exe is closing without any exception. please any one help me to solve this issue. Syntax: tshark.exe -i 3 -b filesize:10000 -b files:3 -w &amp;lt;usbtracefilename&amp;gt;. Thanks in Advance!!!!'''
date = "2017-05-31T07:33:00Z"
lastmod = "2017-05-31T10:34:00Z"
weight = 61712
keywords = [ "tshark" ]
aliases = [ "/questions/61712" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark.exe is closing abnormally after some hours of execution.](/questions/61712/tsharkexe-is-closing-abnormally-after-some-hours-of-execution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61712-score" class="post-score" title="current number of votes">0</div><span id="post-61712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i need to take USB trace for 7 days but after some hours of trace capture, the tshark exe is closing without any exception. please any one help me to solve this issue.</p><p><strong>Syntax:</strong> tshark.exe -i 3 -b filesize:10000 -b files:3 -w &lt;usbtracefilename&gt;.</p><p>Thanks in Advance!!!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '17, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/d2c9789a43b411fb047ce641badacaf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pramod&#39;s gravatar image" /><p><span>Pramod</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pramod has no accepted answers">0%</span></p></div></div><div id="comments-container-61712" class="comments-container"></div><div id="comment-tools-61712" class="comment-tools"></div><div class="clear"></div><div id="comment-61712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61713"></span>

<div id="answer-container-61713" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61713-score" class="post-score" title="current number of votes">1</div><span id="post-61713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pramod has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Probably an <a href="https://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory</a> error. Use dumpcap.exe for long-term captures.</p><p><strong>Edit</strong></p><p>Unfortunately dumpcap is (currently) unable to use USBpcap as a capture source, so this won't work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '17, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '17, 10:12</strong> </span></p></div></div><div id="comments-container-61713" class="comments-container"><span id="61714"></span><div id="comment-61714" class="comment"><div id="post-61714-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for the replay, can u please provide syntax for using dumpcap.exe</p><p>Thanks in Advance!!</p></div><div id="comment-61714-info" class="comment-info"><span class="comment-age">(31 May '17, 07:42)</span> <span class="comment-user userinfo">Pramod</span></div></div><span id="61715"></span><div id="comment-61715" class="comment"><div id="post-61715-score" class="comment-score"></div><div class="comment-text"><p>It should be the same. The man page is <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">here</a>, or use <code>dumpcap -?</code>.</p></div><div id="comment-61715-info" class="comment-info"><span class="comment-age">(31 May '17, 07:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="61716"></span><div id="comment-61716" class="comment"><div id="post-61716-score" class="comment-score"></div><div class="comment-text"><p>yes i tried Dumpcap.exe but it is not displaying USB interfaces.</p><p><strong>Please refer below screen shot</strong> <img src="https://osqa-ask.wireshark.org/upfiles/Dumpcap.PNG" alt="alt text" /></p><p>Thanks in Advance!!!</p></div><div id="comment-61716-info" class="comment-info"><span class="comment-age">(31 May '17, 08:40)</span> <span class="comment-user userinfo">Pramod</span></div></div><span id="61717"></span><div id="comment-61717" class="comment"><div id="post-61717-score" class="comment-score"></div><div class="comment-text"><p>I wasn't aware that dumpcap doesn't support USBpcap. Wireshark\tshark use the extcap mechanism for alternate capture sources such as USBpcap, unfortunately dumpcap doesn't support that.</p><p>I can't offer any solution in this case apart from debugging the issue in tshark, even then the problem might be in usbpcap.</p><p>You could also raise an issue on the USBPcap github site asking for support for ring buffers.</p></div><div id="comment-61717-info" class="comment-info"><span class="comment-age">(31 May '17, 10:09)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="61718"></span><div id="comment-61718" class="comment"><div id="post-61718-score" class="comment-score"></div><div class="comment-text"><p>You can try capturing the USB traffic with USBPcapCMD.exe as explained here: <a href="http://desowin.org/usbpcap/tour.html">http://desowin.org/usbpcap/tour.html</a> Then load the pcap in Wireshark (or if it is too big split it in chunks with editcap first).</p></div><div id="comment-61718-info" class="comment-info"><span class="comment-age">(31 May '17, 10:34)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-61713" class="comment-tools"></div><div class="clear"></div><div id="comment-61713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

