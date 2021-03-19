+++
type = "question"
title = "Wireshark crashes when saving capture file"
description = '''I just installed Wire Shark on my desktop and laptop. After capturing some traffic I go to save to a file and the application closes without any error messages. This is the behavior on both machines. Hopefully I&#x27;m just an idiot and didn&#x27;t set something up right... Thanks in advance! Here is the &#x27;Abo...'''
date = "2016-04-28T15:17:00Z"
lastmod = "2016-04-29T10:17:00Z"
weight = 52063
keywords = [ "wireshark_crashed", "capture-file" ]
aliases = [ "/questions/52063" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark crashes when saving capture file](/questions/52063/wireshark-crashes-when-saving-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52063-score" class="post-score" title="current number of votes">0</div><span id="post-52063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just installed Wire Shark on my desktop and laptop.</p><p>After capturing some traffic I go to save to a file and the application closes without any error messages. This is the behavior on both machines. Hopefully I'm just an idiot and didn't set something up right...</p><p>Thanks in advance!</p><p>Here is the 'About Wireshark' info:</p><p>Version 2.0.3 (v2.0.3-0-geed34f0 from master-2.0) ~ ~ Running on 64-bit Windows 7 Service Pack 1, build 7601, with locale C, with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980), based on libpcap version 1.0 branch 1_0_rel0b (20091008), with GnuTLS 3.2.15, with Gcrypt 1.6.2, without AirPcap. Intel(R) Core(TM) i7-6700 CPU @ 3.40GHz (with SSE4.2), with 16282MB of physical memory.</p><p>Built using Microsoft Visual C++ 12.0 build 40629</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark_crashed" rel="tag" title="see questions tagged &#39;wireshark_crashed&#39;">wireshark_crashed</span> <span class="post-tag tag-link-capture-file" rel="tag" title="see questions tagged &#39;capture-file&#39;">capture-file</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '16, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/6888b7719e9f79f120e8f972cd948d5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deanvolsen&#39;s gravatar image" /><p><span>deanvolsen</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deanvolsen has no accepted answers">0%</span></p></div></div><div id="comments-container-52063" class="comments-container"></div><div id="comment-tools-52063" class="comment-tools"></div><div class="clear"></div><div id="comment-52063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52072"></span>

<div id="answer-container-52072" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52072-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52072-score" class="post-score" title="current number of votes">2</div><span id="post-52072-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By any chance are you using a Dell with their 'Dell Backup and Recovery' software installed? If yes, it is most probably the culprit. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12036">bug 12036</a> for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '16, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-52072" class="comments-container"><span id="52085"></span><div id="comment-52085" class="comment"><div id="post-52085-score" class="comment-score"></div><div class="comment-text"><p>Thanks everyone. It was the 'Dell Backup and Recovery' bug...</p><p>I removed the software and now it's working properly.</p><p>Thanks again</p></div><div id="comment-52085-info" class="comment-info"><span class="comment-age">(29 Apr '16, 10:17)</span> <span class="comment-user userinfo">deanvolsen</span></div></div></div><div id="comment-tools-52072" class="comment-tools"></div><div class="clear"></div><div id="comment-52072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52065"></span>

<div id="answer-container-52065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52065-score" class="post-score" title="current number of votes">0</div><span id="post-52065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Hopefully I'm just an idiot and didn't set something up right...</p></blockquote><p>Or maybe Wireshark has a bug, which is the most likely case.</p><p>Please file a bug report on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>. Give as many details as you can - for example, did it just happen once or does it happen every time? Does "without any error messages" mean that Windows doesn't pop up a dialog indicating that the program had an error?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '16, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-52065" class="comments-container"></div><div id="comment-tools-52065" class="comment-tools"></div><div class="clear"></div><div id="comment-52065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

