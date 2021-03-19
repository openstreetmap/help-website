+++
type = "question"
title = "NBSS and smb2 in mid-tcp package"
description = '''Hi. When NBSS session or session smb occurs in the middle of the TCP packet, I can not see them properly in wireshark. How do I can see the analysis of these protocols, if they are in the middle of the tcp packet? I tried to do it using the menu &quot;Decode as...&quot;, but nothing happened.!'''
date = "2016-05-26T05:30:00Z"
lastmod = "2016-06-06T06:00:00Z"
weight = 52957
keywords = [ "and", "smb2", "nbss" ]
aliases = [ "/questions/52957" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NBSS and smb2 in mid-tcp package](/questions/52957/nbss-and-smb2-in-mid-tcp-package)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52957-score" class="post-score" title="current number of votes">0</div><span id="post-52957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. When NBSS session or session smb occurs in the middle of the TCP packet, I can not see them properly in wireshark.<img src="http://image.openlan.ru/images/73087889424015887072.png" alt="alt text" /> How do I can see the analysis of these protocols, if they are in the middle of the tcp packet? I tried to do it using the menu "Decode as...", but nothing happened.!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-and" rel="tag" title="see questions tagged &#39;and&#39;">and</span> <span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span> <span class="post-tag tag-link-nbss" rel="tag" title="see questions tagged &#39;nbss&#39;">nbss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '16, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/ca21b8a48942dbed19628ffdda42121e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barabashka&#39;s gravatar image" /><p><span>barabashka</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barabashka has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52957" class="comments-container"><span id="52958"></span><div id="comment-52958" class="comment"><div id="post-52958-score" class="comment-score"></div><div class="comment-text"><p>Working from a screenshot is prohibitively difficult. Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-52958-info" class="comment-info"><span class="comment-age">(26 May '16, 05:57)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="53220"></span><div id="comment-53220" class="comment"><div id="post-53220-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the long silence;) Here is the link <a href="https://www.cloudshark.org/captures/8319b97b6296">https://www.cloudshark.org/captures/8319b97b6296</a> I Thank you for your attention to this issue</p></div><div id="comment-53220-info" class="comment-info"><span class="comment-age">(06 Jun '16, 01:56)</span> <span class="comment-user userinfo">barabashka</span></div></div><span id="53236"></span><div id="comment-53236" class="comment"><div id="post-53236-score" class="comment-score"></div><div class="comment-text"><p><span>@barabashka</span></p><p>I moved your "answer" to a comment under the question when you posted it and then deleted the 2nd "answer" as it was a duplicate.</p><p>Please read the site FAQ for more information.</p></div><div id="comment-53236-info" class="comment-info"><span class="comment-age">(06 Jun '16, 06:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-52957" class="comment-tools"></div><div class="clear"></div><div id="comment-52957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52976"></span>

<div id="answer-container-52976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52976-score" class="post-score" title="current number of votes">0</div><span id="post-52976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>can see the analysis of these protocols, if they are in the middle of the tcp packet?</p></blockquote><p>Currently, no. Wireshark would have to scan through the packet to find the beginning of the SMB2 message (which actually beings with the "NetBIOS SS" data - Wireshark <em>really</em> should be labeling port 445 traffic as SMB, not NBSS, as SMB-over-TCP uses something similar to, but simpler than, NBSS), show the data before it as continuation data, and show the SMB2 message. It currently doesn't do that.</p><p>It'd be a <em>lot</em> easier to test and implement it if we had a capture file, just as Jaap suggested.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '16, 15:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-52976" class="comments-container"></div><div id="comment-tools-52976" class="comment-tools"></div><div class="clear"></div><div id="comment-52976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

