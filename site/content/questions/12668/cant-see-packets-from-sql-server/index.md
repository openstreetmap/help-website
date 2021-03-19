+++
type = "question"
title = "Cant see packets from SQL Server"
description = '''Hello all, i have problem what i would like to do is to se packets between application and sql server. I use filter for Wireshark set to port 1433 and i cant see any of packets beetwen app and db even i do some queries etc. Could you tell me why it can be that situation please of help...'''
date = "2012-07-12T13:20:00Z"
lastmod = "2015-08-11T00:46:00Z"
weight = 12668
keywords = [ "sql", "server", "wireshark" ]
aliases = [ "/questions/12668" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cant see packets from SQL Server](/questions/12668/cant-see-packets-from-sql-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12668-score" class="post-score" title="current number of votes">0</div><span id="post-12668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>i have problem what i would like to do is to se packets between application and sql server. I use filter for Wireshark set to port 1433 and i cant see any of packets beetwen app and db even i do some queries etc. Could you tell me why it can be that situation please of help...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '12, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/34895c82dd58722a9e5f99fc7d8575d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nighttrain&#39;s gravatar image" /><p><span>nighttrain</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nighttrain has no accepted answers">0%</span></p></div></div><div id="comments-container-12668" class="comments-container"></div><div id="comment-tools-12668" class="comment-tools"></div><div class="clear"></div><div id="comment-12668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12669"></span>

<div id="answer-container-12669" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12669-score" class="post-score" title="current number of votes">1</div><span id="post-12669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are the application and SQLServer instance on the same machine? If so you may have difficulties due to the way loopback connections work on Windows. See the wiki <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback</a> page for more info.</p><p>If the app and SQLServer instance are on different machines then you should be able to capture the traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '12, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-12669" class="comments-container"><span id="12671"></span><div id="comment-12671" class="comment"><div id="post-12671-score" class="comment-score"></div><div class="comment-text"><p>Its on the same machine what should i do to get the packets?</p></div><div id="comment-12671-info" class="comment-info"><span class="comment-age">(12 Jul '12, 14:04)</span> <span class="comment-user userinfo">nighttrain</span></div></div><span id="12673"></span><div id="comment-12673" class="comment"><div id="post-12673-score" class="comment-score"></div><div class="comment-text"><p>I installed the Microsoft Loopback adapter succesfully but its set the ip for it: 169.254.152.239 and mask 255.255.0.0 in wireshark i cant see that interface how now could i use this?</p></div><div id="comment-12673-info" class="comment-info"><span class="comment-age">(12 Jul '12, 14:39)</span> <span class="comment-user userinfo">nighttrain</span></div></div><span id="12674"></span><div id="comment-12674" class="comment"><div id="post-12674-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answers" to comments as that's how this Q&amp;A site works.</p><p>Loopback capturing on Windows is hard. Try following some of the other info on the page I linked to. Your life will be much easier if you could just move the application to another machine.</p></div><div id="comment-12674-info" class="comment-info"><span class="comment-age">(12 Jul '12, 14:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="12678"></span><div id="comment-12678" class="comment"><div id="post-12678-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.netresec.com/?page=RawCap">RawCap</a> (mentioned in the <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">Loopback</a> wiki) works pretty well.</p></div><div id="comment-12678-info" class="comment-info"><span class="comment-age">(12 Jul '12, 19:49)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="44952"></span><div id="comment-44952" class="comment"><div id="post-44952-score" class="comment-score"></div><div class="comment-text"><p>is this still true for the latest version, 1.12.6?</p></div><div id="comment-44952-info" class="comment-info"><span class="comment-age">(10 Aug '15, 12:30)</span> <span class="comment-user userinfo">debuke</span></div></div><span id="44955"></span><div id="comment-44955" class="comment not_top_scorer"><div id="post-44955-score" class="comment-score"></div><div class="comment-text"><p>Yes, it's not a Wireshark issue, the issue is with the capturing mechanism WinPCap.</p></div><div id="comment-44955-info" class="comment-info"><span class="comment-age">(11 Aug '15, 00:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-12669" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-12669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

