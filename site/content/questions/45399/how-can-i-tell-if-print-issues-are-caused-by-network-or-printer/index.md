+++
type = "question"
title = "How can I tell if print issues are caused by network or printer"
description = '''We have about 8 HP (AIO) printers at the office who have printing issues from time to time. Prints are really slow, and sometimes even fail. In such case the printer seems to receive a printjob, but fails to print in the end. All printers are fairly new (2 months) I made a packetcapture of a failed ...'''
date = "2015-08-27T05:37:00Z"
lastmod = "2015-08-27T11:35:00Z"
weight = 45399
keywords = [ "windows", "zero-window" ]
aliases = [ "/questions/45399" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I tell if print issues are caused by network or printer](/questions/45399/how-can-i-tell-if-print-issues-are-caused-by-network-or-printer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45399-score" class="post-score" title="current number of votes">0</div><span id="post-45399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have about 8 HP (AIO) printers at the office who have printing issues from time to time. Prints are really slow, and sometimes even fail. In such case the printer seems to receive a printjob, but fails to print in the end.</p><p>All printers are fairly new (2 months)</p><p>I made a packetcapture of a failed print that didnt came out.</p><p>See: <a href="http://s18.postimg.org/84me57oeh/wireshark_print_issues.png">http://s18.postimg.org/84me57oeh/wireshark_print_issues.png</a></p><p>I`m wondering how I can tell this issue is on the printers end or on the network. We have a PFsense router in place and all MTU sizes are default.</p><p>Looking forward to some pointers :)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-zero-window" rel="tag" title="see questions tagged &#39;zero-window&#39;">zero-window</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '15, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/79992d08cfb74cb377fa78e6e71643fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jortie&#39;s gravatar image" /><p><span>jortie</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jortie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '15, 05:38</strong> </span></p></div></div><div id="comments-container-45399" class="comments-container"><span id="45405"></span><div id="comment-45405" class="comment"><div id="post-45405-score" class="comment-score"></div><div class="comment-text"><p>You might want to start posting the capture file on cloudshark and define which IP address is what node.</p></div><div id="comment-45405-info" class="comment-info"><span class="comment-age">(27 Aug '15, 09:00)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="45407"></span><div id="comment-45407" class="comment"><div id="post-45407-score" class="comment-score"></div><div class="comment-text"><p>192.168.100.5 is the printer. The other one is the client. <a href="https://www.cloudshark.org/captures/10f1058e0f93">https://www.cloudshark.org/captures/10f1058e0f93</a></p></div><div id="comment-45407-info" class="comment-info"><span class="comment-age">(27 Aug '15, 09:02)</span> <span class="comment-user userinfo">jortie</span></div></div></div><div id="comment-tools-45399" class="comment-tools"></div><div class="clear"></div><div id="comment-45399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45410"></span>

<div id="answer-container-45410" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45410-score" class="post-score" title="current number of votes">0</div><span id="post-45410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jortie has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So the receive window at the printer is full ( zero window in packet #22). And after the client is probing the zero window but the printer always answers with a zero window size.</p><p>So the initial window of this printer is with 17500 (Frame#2; Field: Calculated Window Size in TCP Header) really low. Have you talked to HP?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '15, 12:45</strong> </span></p></div></div><div id="comments-container-45410" class="comments-container"><span id="45411"></span><div id="comment-45411" class="comment"><div id="post-45411-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much. I havent talked to HP because I wanted to be sure first if the network might be to blame. Can we reliably say this is a printer issue?</p></div><div id="comment-45411-info" class="comment-info"><span class="comment-age">(27 Aug '15, 10:46)</span> <span class="comment-user userinfo">jortie</span></div></div><span id="45412"></span><div id="comment-45412" class="comment"><div id="post-45412-score" class="comment-score"></div><div class="comment-text"><p>It could be the printer, the firmware of the printer, not enough RAM at the printer, or the file itsself could not be printed.</p><p>But if there is no Layer4 device between the client and the printer, than we can reliably say it is not the network.</p></div><div id="comment-45412-info" class="comment-info"><span class="comment-age">(27 Aug '15, 11:35)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-45410" class="comment-tools"></div><div class="clear"></div><div id="comment-45410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

