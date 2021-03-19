+++
type = "question"
title = "Time Shift feature"
description = '''Do you know some bug with Time Shift feature? When I right-click on the first packet in the trace file, I choose Time Shift... and write -0.000235 it does not work (uoy can user Reload button on the toolbar). I can use only full second for example +3.0. Miliseconds, and other, do not work. It is nor...'''
date = "2013-10-16T13:48:00Z"
lastmod = "2013-10-17T03:06:00Z"
weight = 26084
keywords = [ "time_shift", "features" ]
aliases = [ "/questions/26084" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Time Shift feature](/questions/26084/time-shift-feature)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26084-score" class="post-score" title="current number of votes">1</div><span id="post-26084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Do you know some bug with Time Shift feature? When I right-click on the first packet in the trace file, I choose Time Shift... and write -0.000235 it does not work (uoy can user Reload button on the toolbar). I can use only full second for example +3.0. Miliseconds, and other, do not work. It is normal? Or I should set something more?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-time_shift" rel="tag" title="see questions tagged &#39;time_shift&#39;">time_shift</span> <span class="post-tag tag-link-features" rel="tag" title="see questions tagged &#39;features&#39;">features</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '13, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/28071bd7cf93e424c03dec9086ffa60f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net16&#39;s gravatar image" /><p><span>net16</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net16 has no accepted answers">0%</span></p></div></div><div id="comments-container-26084" class="comments-container"></div><div id="comment-tools-26084" class="comment-tools"></div><div class="clear"></div><div id="comment-26084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26114"></span>

<div id="answer-container-26114" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26114-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26114-score" class="post-score" title="current number of votes">3</div><span id="post-26114-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="net16 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I use 1.10.2 too. When I write -0.000100, I receive "Offset is zero." error.</p></blockquote><p>I have the same effect on my system. <strong>However</strong> if I use a comma instead of a dot, it works. I run a <strong>german localized</strong> Windows.</p><p>Works (comma): +/- 0,00001<br />
Does not work (dot): +/- 0.00001</p><p>I don't know if this is intended localized behavior of Wireshark or a bug.</p><p><strong>++ UPDATE ++</strong></p><p>I tend to say it is (kind of) a bug, as the help text in the "Time Shift" windows only mentions a dot, even on a localized windows. However, that behavior is the same since 1.8.0 !?! So, maybe it is intended localized behavior, but then the help text needs to be adjusted for a localized windows as well.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '13, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Oct '13, 03:26</strong> </span></p></div></div><div id="comments-container-26114" class="comments-container"><span id="26117"></span><div id="comment-26117" class="comment"><div id="post-26117-score" class="comment-score"></div><div class="comment-text"><p>Yes, a comma works. Thank you very much again.</p></div><div id="comment-26117-info" class="comment-info"><span class="comment-age">(17 Oct '13, 03:04)</span> <span class="comment-user userinfo">net16</span></div></div><span id="26119"></span><div id="comment-26119" class="comment"><div id="post-26119-score" class="comment-score"></div><div class="comment-text"><p>You're welcome:</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-26119-info" class="comment-info"><span class="comment-age">(17 Oct '13, 03:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26114" class="comment-tools"></div><div class="clear"></div><div id="comment-26114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26087"></span>

<div id="answer-container-26087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26087-score" class="post-score" title="current number of votes">1</div><span id="post-26087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Which time-shift option did you use? I assume the pre-selected one on top? This makes <strong>all</strong> packets shift in time, which means the relative time won't change (as the time stamp of the first packet is also shifted).</p><p>Could you look into the frame section for the absolute timestamp and check whether it has changed?</p><p>BTW it is indeed possible to do changes in microseconds...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '13, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-26087" class="comments-container"><span id="26088"></span><div id="comment-26088" class="comment"><div id="post-26088-score" class="comment-score"></div><div class="comment-text"><p>Thank you SYN-bit. I use first option and anything does not change: time in Time column and [Time shift for this packet: 0.000000000 seconds] (in frame section). If I use 2, 3 seconds then it changes. But if I use 0.something it does not work.</p><p>The smallest Tick interval is 0.001s (in Statistics-&gt;IO Graph). It is possible to take data to CSV in smaller intervals? It is needed to analising on microsecond field.</p></div><div id="comment-26088-info" class="comment-info"><span class="comment-age">(16 Oct '13, 14:30)</span> <span class="comment-user userinfo">net16</span></div></div><span id="26089"></span><div id="comment-26089" class="comment"><div id="post-26089-score" class="comment-score">1</div><div class="comment-text"><p>Which version of wireshark are you using? I just tried myself with 1.10.2 and timeshifting does work for -0.000100.</p><p>In IO graphs, it is not possible to use a smaller interval without changing the source code. (it's better to start a new question for uhmmm... new questions :-))</p></div><div id="comment-26089-info" class="comment-info"><span class="comment-age">(16 Oct '13, 15:13)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="26111"></span><div id="comment-26111" class="comment"><div id="post-26111-score" class="comment-score"></div><div class="comment-text"><p>I use 1.10.2 too. When I write -0.000100, I receive "Offset is zero." error. But if I write -1.000100 Arrival Time has decreased about 1 s (and [Time shift for this packet: -1.000000000 seconds]). Notice that it decreases with 1s, not 1.000100s. Value has been rounded to integer value. I have checked on different files and packets. What is the problem?? I have SVN Rev 51934 from/trunk-1.10.</p></div><div id="comment-26111-info" class="comment-info"><span class="comment-age">(17 Oct '13, 02:31)</span> <span class="comment-user userinfo">net16</span></div></div></div><div id="comment-tools-26087" class="comment-tools"></div><div class="clear"></div><div id="comment-26087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

