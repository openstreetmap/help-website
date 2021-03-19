+++
type = "question"
title = "Not capturing in promiscuous mode in Windows 7 x64"
description = '''It appears that setting promiscuous mode in windows 7 enterprise x64, is not really setting promiscuous mode at all. I am trying to capture raw ethernet packets, ie not TCP/IP or any other format, it is debugging information. I have it directly connected, no switches. All drivers, winpcpap, and wire...'''
date = "2013-12-19T09:45:00Z"
lastmod = "2013-12-19T11:49:00Z"
weight = 28294
keywords = [ "winpcap", "promiscuous", "windows7" ]
aliases = [ "/questions/28294" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not capturing in promiscuous mode in Windows 7 x64](/questions/28294/not-capturing-in-promiscuous-mode-in-windows-7-x64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28294-score" class="post-score" title="current number of votes">0</div><span id="post-28294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It appears that setting promiscuous mode in windows 7 enterprise x64, is not really setting promiscuous mode at all. I am trying to capture raw ethernet packets, ie not TCP/IP or any other format, it is debugging information. I have it directly connected, no switches. All drivers, winpcpap, and wireshark are up to date. When I start the capture, if I look at the "Local Area Connection Status" I can see the bytes being received. If I use my old XP machine it captures them just fine. If I use "Microsoft Network Monitor" it captures them just fine. I also tried Windump, and it doesn't capture them either. Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '13, 09:45</strong></p><img src="https://secure.gravatar.com/avatar/7d0fe40baa3434251e9cee2e7f91869b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BenWhite&#39;s gravatar image" /><p><span>BenWhite</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BenWhite has no accepted answers">0%</span></p></div></div><div id="comments-container-28294" class="comments-container"><span id="28295"></span><div id="comment-28295" class="comment"><div id="post-28295-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark are you using? Which version of WinPcap are you using?</p></div><div id="comment-28295-info" class="comment-info"><span class="comment-age">(19 Dec '13, 10:20)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="28297"></span><div id="comment-28297" class="comment"><div id="post-28297-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 1.10.4 and also tried 1.5.1 WinPcap 4.1.3 also tried 4.1.? and 4.2.? (don't remember exact older versions.)</p></div><div id="comment-28297-info" class="comment-info"><span class="comment-age">(19 Dec '13, 11:02)</span> <span class="comment-user userinfo">BenWhite</span></div></div></div><div id="comment-tools-28294" class="comment-tools"></div><div class="clear"></div><div id="comment-28294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28298"></span>

<div id="answer-container-28298" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28298-score" class="post-score" title="current number of votes">0</div><span id="post-28298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I started shutting down all unneeded services. I found that the "McAfee Host Intrusion Prevention Service" was the culprit. Upon further investigation, it was filtering out my raw ether packets since they were "Non-IP Protocol."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '13, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/7d0fe40baa3434251e9cee2e7f91869b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BenWhite&#39;s gravatar image" /><p><span>BenWhite</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BenWhite has no accepted answers">0%</span></p></div></div><div id="comments-container-28298" class="comments-container"></div><div id="comment-tools-28298" class="comment-tools"></div><div class="clear"></div><div id="comment-28298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

