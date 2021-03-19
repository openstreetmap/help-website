+++
type = "question"
title = "Wireshark Version Change in Linux Build"
description = '''Hi, I am building wireshark 2.2.4 in centOs. I used commands: make uninstall, ./autogen.sh, ./configure, make clean, make, make install. For some internal purpose I need to change the version 2.2.4 to 13.0.1 in Help&amp;gt;About Wireshark&amp;gt;wireshark. which set of files I need to change?'''
date = "2017-07-10T02:06:00Z"
lastmod = "2017-07-10T05:16:00Z"
weight = 62634
keywords = [ "gui", "version", "help" ]
aliases = [ "/questions/62634" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Version Change in Linux Build](/questions/62634/wireshark-version-change-in-linux-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62634-score" class="post-score" title="current number of votes">0</div><span id="post-62634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am building wireshark 2.2.4 in centOs. I used commands: make uninstall, ./autogen.sh, ./configure, make clean, make, make install. For some internal purpose I need to change the version 2.2.4 to 13.0.1 in Help&gt;About Wireshark&gt;wireshark. which set of files I need to change?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '17, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p><span>Abhisek</span><br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div></div><div id="comments-container-62634" class="comments-container"></div><div id="comment-tools-62634" class="comment-tools"></div><div class="clear"></div><div id="comment-62634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62635"></span>

<div id="answer-container-62635" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62635-score" class="post-score" title="current number of votes">0</div><span id="post-62635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Abhisek has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That would be in the top of configure.ac.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '17, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62635" class="comments-container"><span id="62637"></span><div id="comment-62637" class="comment"><div id="post-62637-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot man... I build by changing m4_define([version_major], [2]) m4_define([version_minor], [2]) m4_define([version_micro], [4]) to my desired version... I don't have enough reputation currently so please somebody select Japp answer as the correct answer.</p></div><div id="comment-62637-info" class="comment-info"><span class="comment-age">(10 Jul '17, 03:50)</span> <span class="comment-user userinfo">Abhisek</span></div></div><span id="62639"></span><div id="comment-62639" class="comment"><div id="post-62639-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-62639-info" class="comment-info"><span class="comment-age">(10 Jul '17, 04:12)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="62640"></span><div id="comment-62640" class="comment"><div id="post-62640-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-62640-info" class="comment-info"><span class="comment-age">(10 Jul '17, 04:12)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="62642"></span><div id="comment-62642" class="comment"><div id="post-62642-score" class="comment-score"></div><div class="comment-text"><p>To choose an answer as a correct one you do not need any reputation, the only person who can do so is the author of the question regardless how much reputation points they have. There are two icons, thumbs up and checkmark, and the right one to use is the checkmark one.</p></div><div id="comment-62642-info" class="comment-info"><span class="comment-age">(10 Jul '17, 04:34)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="62644"></span><div id="comment-62644" class="comment"><div id="post-62644-score" class="comment-score"></div><div class="comment-text"><p>Done......</p></div><div id="comment-62644-info" class="comment-info"><span class="comment-age">(10 Jul '17, 05:16)</span> <span class="comment-user userinfo">Abhisek</span></div></div></div><div id="comment-tools-62635" class="comment-tools"></div><div class="clear"></div><div id="comment-62635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

