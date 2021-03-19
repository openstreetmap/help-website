+++
type = "question"
title = "IEC 61850 MMS parser"
description = '''Hello All We need to develop code in order to parse IEC 61850 messages,including MMS. I understand that we can reduce the source code to what we need,  but it could take a lot of time to do it in accurate manner. What is a preferable way to build/receive such a parser? Thank you in advance Best Rega...'''
date = "2013-12-26T05:09:00Z"
lastmod = "2014-01-02T09:01:00Z"
weight = 28402
keywords = [ "iec", "61850" ]
aliases = [ "/questions/28402" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IEC 61850 MMS parser](/questions/28402/iec-61850-mms-parser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28402-score" class="post-score" title="current number of votes">0</div><span id="post-28402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All We need to develop code in order to parse IEC 61850 messages,including MMS. I understand that we can reduce the source code to what we need, but it could take a lot of time to do it in accurate manner. What is a preferable way to build/receive such a parser?</p><p>Thank you in advance Best Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iec" rel="tag" title="see questions tagged &#39;iec&#39;">iec</span> <span class="post-tag tag-link-61850" rel="tag" title="see questions tagged &#39;61850&#39;">61850</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '13, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/74895ae74172f131a9390fba5270e6d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ElenaB&#39;s gravatar image" /><p><span>ElenaB</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ElenaB has no accepted answers">0%</span></p></div></div><div id="comments-container-28402" class="comments-container"></div><div id="comment-tools-28402" class="comment-tools"></div><div class="clear"></div><div id="comment-28402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28406"></span>

<div id="answer-container-28406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28406-score" class="post-score" title="current number of votes">1</div><span id="post-28406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the answers to <a href="http://ask.wireshark.org/questions/23018/how-to-develop-my-own-traffic-data-analyzer-through-wireshark?page=1&amp;focusedAnswerId=23022#23022">this</a> question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Dec '13, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-28406" class="comments-container"><span id="28407"></span><div id="comment-28407" class="comment"><div id="post-28407-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your fast answer Probably i haven't make myself clear. We do not want to add new protocol, we would like to use iec6185 mms &amp; goose implementation which is already part of wireshark. We have our own networking and we have thinks to do with the parsed packet. So we need only the parsing part. What do you think?</p><p>Thank you in advance Elena</p></div><div id="comment-28407-info" class="comment-info"><span class="comment-age">(26 Dec '13, 07:22)</span> <span class="comment-user userinfo">ElenaB</span></div></div><span id="28411"></span><div id="comment-28411" class="comment"><div id="post-28411-score" class="comment-score"></div><div class="comment-text"><p>What kind of things do you have to do with the packets?</p></div><div id="comment-28411-info" class="comment-info"><span class="comment-age">(26 Dec '13, 08:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28526"></span><div id="comment-28526" class="comment"><div id="post-28526-score" class="comment-score"></div><div class="comment-text"><p>Don't forget that Wireshark's code is licensed under the GPL. So if you use any of its code then you must supply your source code to anyone you give your program to.</p></div><div id="comment-28526-info" class="comment-info"><span class="comment-age">(02 Jan '14, 09:01)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-28406" class="comment-tools"></div><div class="clear"></div><div id="comment-28406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

