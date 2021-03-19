+++
type = "question"
title = "no packets captured"
description = '''I am running wireshark on windows 7. I have an alpha usb wireless adapter. I have acrylic running and it sees various wifi traffic. So clearly, the wireless adapter is working and sees wireless traffic.  With wireshark, I get nothing. I used this exact same computer and wireless adapter last year wi...'''
date = "2016-05-05T09:04:00Z"
lastmod = "2016-05-11T18:49:00Z"
weight = 52250
keywords = [ "wireless", "capture", "802.11", "windows", "packet" ]
aliases = [ "/questions/52250" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [no packets captured](/questions/52250/no-packets-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52250-score" class="post-score" title="current number of votes">0</div><span id="post-52250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running wireshark on windows 7. I have an alpha usb wireless adapter. I have acrylic running and it sees various wifi traffic. So clearly, the wireless adapter is working and sees wireless traffic.<br />
</p><p>With wireshark, I get nothing.</p><p>I used this exact same computer and wireless adapter last year with wireshark and I captured 802.11 packets. I know acrylic has updated since then and so has wireshark. Is it because of those updates that I can't do this anymore? Or is there something else that I am forgetting to do?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '16, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/efddbf0ae6e0c4b1cd182c684814c087?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rlwhiterose&#39;s gravatar image" /><p><span>rlwhiterose</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rlwhiterose has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-52250" class="comments-container"></div><div id="comment-tools-52250" class="comment-tools"></div><div class="clear"></div><div id="comment-52250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52350"></span>

<div id="answer-container-52350" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52350-score" class="post-score" title="current number of votes">0</div><span id="post-52350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Are you explicitly selecting the interface when you capture, or just using Start capture button?</p><p>Assuming you're on 2.0.1 or higher, I would go under capture options</p><li>make sure you have the wireless interface selected with no filter.</li><li>Look at the little "Traffic" line graph to confirm that packets are showing up on the interfaces you expect.<p>You could consider re-installing WinPcap if you're not seeing the interfaces/traffic you expect in the options menu.</p></li></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '16, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/3f2f87a6a68e4c51c3851c20b6c56a1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CMH_Tim&#39;s gravatar image" /><p><span>CMH_Tim</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CMH_Tim has no accepted answers">0%</span></p></div></div><div id="comments-container-52350" class="comments-container"><span id="52351"></span><div id="comment-52351" class="comment"><div id="post-52351-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. I am selecting the interface and the litte "Traffic" line graph shows nothing going on at all. I don't have a filter on.</p><p>I bet you are right that I should re-install WinPcap. But instead I just gave up on windows and went back to Linux.</p></div><div id="comment-52351-info" class="comment-info"><span class="comment-age">(09 May '16, 09:12)</span> <span class="comment-user userinfo">rlwhiterose</span></div></div></div><div id="comment-tools-52350" class="comment-tools"></div><div class="clear"></div><div id="comment-52350-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52456"></span>

<div id="answer-container-52456" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52456-score" class="post-score" title="current number of votes">0</div><span id="post-52456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi. You could try to use latest Npcap 0.07 R3: <a href="https://github.com/nmap/npcap/releases">https://github.com/nmap/npcap/releases</a>.</p><p>Npcap supports to capture 802.11 packets on ordinary wireless adapter (the one shipped with your computer)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '16, 18:49</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p><span>Yang Luo</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-52456" class="comments-container"></div><div id="comment-tools-52456" class="comment-tools"></div><div class="clear"></div><div id="comment-52456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

