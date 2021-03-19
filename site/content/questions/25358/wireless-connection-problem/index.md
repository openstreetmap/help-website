+++
type = "question"
title = "Wireless Connection Problem"
description = '''Sir I have data dongle(wireless device) to provide wireless internet on my laptop. Can I use wireshark to see the data packet going and coming through my laptop via this data dongle. I tried but in Interface in wireshark it doesnot display wireless connection. Please guide me to see wireless connect...'''
date = "2013-09-29T23:58:00Z"
lastmod = "2013-10-01T04:05:00Z"
weight = 25358
keywords = [ "captureproblems" ]
aliases = [ "/questions/25358" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless Connection Problem](/questions/25358/wireless-connection-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25358-score" class="post-score" title="current number of votes">0</div><span id="post-25358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sir I have data dongle(wireless device) to provide wireless internet on my laptop. Can I use wireshark to see the data packet going and coming through my laptop via this data dongle. I tried but in Interface in wireshark it doesnot display wireless connection. Please guide me to see wireless connection in wireshark.</p><p>Piyush Sharma</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-captureproblems" rel="tag" title="see questions tagged &#39;captureproblems&#39;">captureproblems</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '13, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/80e562b282574c4a2a06ee968f80fb6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PEEYUSH&#39;s gravatar image" /><p><span>PEEYUSH</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PEEYUSH has no accepted answers">0%</span></p></div></div><div id="comments-container-25358" class="comments-container"></div><div id="comment-tools-25358" class="comment-tools"></div><div class="clear"></div><div id="comment-25358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25426"></span>

<div id="answer-container-25426" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25426-score" class="post-score" title="current number of votes">0</div><span id="post-25426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Sir I have data dongle(wireless device) to provide wireless internet on my laptop.<br />
tried but in Interface in wireshark it doesnot display wireless connection.</p></blockquote><p>There are two possibilities (or more ;-))</p><ol><li>You inserted the USB device after you booted the PC and/or started Wireshark (depends on the way you installed WinPcap)</li><li>The USB device driver creates a PPP interface</li></ol><p><strong>Regarding Nr. 1:</strong><br />
</p><p>In that case WinPcap, the library and system service used by Wireshark, does not know about the new interface. Please restart the NPF service while the device is connected to your system.</p><p>As administrator (elevated DOS box) run</p><blockquote><p>sc stop npf<br />
sc start npf<br />
dumpcap -D -M<br />
</p></blockquote><p>Do you see the interface in the list of interfaces, that dumpcap printed?</p><p>If <strong>yes</strong>: Problem solved.<br />
If <strong>no</strong>: goto 2.</p><p>See also a similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/16299/capture-packets-with-zte-hspa-modem-mf195">http://ask.wireshark.org/questions/16299/capture-packets-with-zte-hspa-modem-mf195</a><br />
</p></blockquote><p><strong>Regarding Nr. 2:</strong><br />
</p><p>WinPcap does not support PPP interfaces, and thus you cannot capture data with Wireshark on that interface.</p><blockquote><p><a href="http://www.winpcap.org/misc/faq.htm#Q-5">http://www.winpcap.org/misc/faq.htm#Q-5</a></p></blockquote><p>You can try Microsoft Network Monitor.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 15:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-25426" class="comments-container"><span id="25440"></span><div id="comment-25440" class="comment"><div id="post-25440-score" class="comment-score"></div><div class="comment-text"><p>MS Network Monitor has been recently superseded by Message Analyzer. I haven't checked to see if MS are still making Network Monitor available.</p></div><div id="comment-25440-info" class="comment-info"><span class="comment-age">(01 Oct '13, 01:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="25442"></span><div id="comment-25442" class="comment"><div id="post-25442-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the hint. Network Monitor is still there, and there is no real reason to remove that tool. We will see. Do you work with Message Analyzer? What do you think about it?</p></div><div id="comment-25442-info" class="comment-info"><span class="comment-age">(01 Oct '13, 01:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="25444"></span><div id="comment-25444" class="comment"><div id="post-25444-score" class="comment-score"></div><div class="comment-text"><p>I fired up the beta for about 15 seconds, and was repulsed by the UI. Haven't looked at it since.</p></div><div id="comment-25444-info" class="comment-info"><span class="comment-age">(01 Oct '13, 02:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="25451"></span><div id="comment-25451" class="comment"><div id="post-25451-score" class="comment-score"></div><div class="comment-text"><blockquote><p>for about 15 seconds</p></blockquote><p>duh... <strong>that's</strong> long ;-))</p><p>Well, according to the title of his blog entry, that guy from Microsoft thinks network capture is (already) dead</p><blockquote><p><a href="http://blogs.technet.com/b/messageanalyzer/archive/2013/03/04/network-capture-is-dead.aspx">http://blogs.technet.com/b/messageanalyzer/archive/2013/03/04/network-capture-is-dead.aspx</a></p></blockquote><p>I won't go that far, but there are (will be) some challenges for network capturing. See my <a href="http://ask.wireshark.org/questions/23800/nsa-sniffing-and-encryption">NSA/crypto question</a>.</p></div><div id="comment-25451-info" class="comment-info"><span class="comment-age">(01 Oct '13, 03:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="25459"></span><div id="comment-25459" class="comment"><div id="post-25459-score" class="comment-score"></div><div class="comment-text"><p>Kind of misleading headline considering MA will still capture from NDIS amongst many other sources.</p></div><div id="comment-25459-info" class="comment-info"><span class="comment-age">(01 Oct '13, 04:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-25426" class="comment-tools"></div><div class="clear"></div><div id="comment-25426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

