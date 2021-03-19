+++
type = "question"
title = "Wireshark crash"
description = '''Hi What is the meaning of wireshark crash?? does it mean that wireshark stopped and can&#x27;t save the captured data, or it means the software itself is carshed and it doesn&#x27;t work any more? what are the common mistakes that cause the crash other than running wireshark for along time (Briefly). Thanks'''
date = "2012-12-05T04:10:00Z"
lastmod = "2012-12-05T05:20:00Z"
weight = 16582
keywords = [ "wireshark" ]
aliases = [ "/questions/16582" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark crash](/questions/16582/wireshark-crash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16582-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16582-score" class="post-score" title="current number of votes">0</div><span id="post-16582-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi What is the meaning of wireshark crash?? does it mean that wireshark stopped and can't save the captured data, or it means the software itself is carshed and it doesn't work any more? what are the common mistakes that cause the crash other than running wireshark for along time (Briefly). Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p><span>Leena</span><br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div></div><div id="comments-container-16582" class="comments-container"></div><div id="comment-tools-16582" class="comment-tools"></div><div class="clear"></div><div id="comment-16582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16584"></span>

<div id="answer-container-16584" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16584-score" class="post-score" title="current number of votes">1</div><span id="post-16584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leena has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark crash normaly refers to the application having an unrecoverable error and being terminated by the OS. The most common reasons beeing SW bugs or out-of-memory (out-of-memory may be caused by a bug). If this happens during capturing the temporary capture file can be recoverd from the temp directory up to the point of the crash or close to. No user action other than capturing enough data to cause out-of-memory should crash Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-16584" class="comments-container"><span id="16585"></span><div id="comment-16585" class="comment"><div id="post-16585-score" class="comment-score"></div><div class="comment-text"><p>does it mean that if a crash takes place I should download and install wireshark again</p></div><div id="comment-16585-info" class="comment-info"><span class="comment-age">(05 Dec '12, 04:26)</span> <span class="comment-user userinfo">Leena</span></div></div><span id="16586"></span><div id="comment-16586" class="comment"><div id="post-16586-score" class="comment-score">1</div><div class="comment-text"><p>no, it means that you captured too much data in a single take. Just restart Wireshark and capture less data, or capture data into multiple files (see the capture options dialog).</p></div><div id="comment-16586-info" class="comment-info"><span class="comment-age">(05 Dec '12, 04:50)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="16590"></span><div id="comment-16590" class="comment"><div id="post-16590-score" class="comment-score"></div><div class="comment-text"><p>Thanks alot everybody</p></div><div id="comment-16590-info" class="comment-info"><span class="comment-age">(05 Dec '12, 05:20)</span> <span class="comment-user userinfo">Leena</span></div></div></div><div id="comment-tools-16584" class="comment-tools"></div><div class="clear"></div><div id="comment-16584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

