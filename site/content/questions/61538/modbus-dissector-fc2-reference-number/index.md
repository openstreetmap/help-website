+++
type = "question"
title = "Modbus dissector - FC2 reference number"
description = '''Hello, For the debugging it is very convinient, that it is possible to read the Modbus register number not only in the Query but also in the Response in case of FC3 (modbus.regnum16). Is it possible to read like this the FC2 reference number in the Response frame? For now I found, that the reference...'''
date = "2017-05-22T07:00:00Z"
lastmod = "2017-05-26T02:07:00Z"
weight = 61538
keywords = [ "modbus", "reference_num" ]
aliases = [ "/questions/61538" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Modbus dissector - FC2 reference number](/questions/61538/modbus-dissector-fc2-reference-number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61538-score" class="post-score" title="current number of votes">0</div><span id="post-61538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>For the debugging it is very convinient, that it is possible to read the Modbus register number not only in the Query but also in the Response in case of FC3 (modbus.regnum16). Is it possible to read like this the FC2 reference number in the Response frame? For now I found, that the reference number (modbus.reference_num) is visible only in Query of FC2. If there is no such function for now, is it possible that modbus community would make such extension of modbus dissector? That would make the use of it much comfortable and I guess more complete, because such feature is already available in case of FC3.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-reference_num" rel="tag" title="see questions tagged &#39;reference_num&#39;">reference_num</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '17, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/0d5c20b01de61cf351ec0b51c904a023?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jendker&#39;s gravatar image" /><p><span>Jendker</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jendker has no accepted answers">0%</span></p></div></div><div id="comments-container-61538" class="comments-container"></div><div id="comment-tools-61538" class="comment-tools"></div><div class="clear"></div><div id="comment-61538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61540"></span>

<div id="answer-container-61540" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61540-score" class="post-score" title="current number of votes">0</div><span id="post-61540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jendker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The dissection of the packed discrete inputs from FC2 could be improved, either by splitting each individual bit out in a manner similar to that for registers, or by displaying the address of the first bit in each byte. The former solution would be preferred as that would allow filtering based on the discret bit address.</p><p>To ask for this feature, please raise an entry on the Wireshark Bugzilla (if there isn't one already for this feature), marking it as an enhancement, and if at all possible, attach a capture file with the traffic of interest.</p><p>After that, post a comment back here with the number of the bugzilla entry for future reference.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '17, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61540" class="comments-container"><span id="61567"></span><div id="comment-61567" class="comment"><div id="post-61567-score" class="comment-score"></div><div class="comment-text"><p>Thank you <a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a>, the Bug ID is: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13734">13734</a></p><p>I am marking your answer as the accepted as soon as the enhancement is finished.</p></div><div id="comment-61567-info" class="comment-info"><span class="comment-age">(23 May '17, 01:58)</span> <span class="comment-user userinfo">Jendker</span></div></div><span id="61569"></span><div id="comment-61569" class="comment"><div id="post-61569-score" class="comment-score"></div><div class="comment-text"><blockquote>I am marking your answer as the accepted as soon as the enhancement is finished.</blockquote><p>That might be quite some time in the future when someone has the time and inclination to make such a change.</p></div><div id="comment-61569-info" class="comment-info"><span class="comment-age">(23 May '17, 02:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="61584"></span><div id="comment-61584" class="comment"><div id="post-61584-score" class="comment-score"></div><div class="comment-text"><p>Than there is no point in keeping this question still open, I am marking as answered.</p></div><div id="comment-61584-info" class="comment-info"><span class="comment-age">(23 May '17, 13:09)</span> <span class="comment-user userinfo">Jendker</span></div></div><span id="61636"></span><div id="comment-61636" class="comment"><div id="post-61636-score" class="comment-score"></div><div class="comment-text"><p>The future has arrived, I found some time last night to make this change.</p><p>If you can, please test a nightly build.</p></div><div id="comment-61636-info" class="comment-info"><span class="comment-age">(26 May '17, 02:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-61540" class="comment-tools"></div><div class="clear"></div><div id="comment-61540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

