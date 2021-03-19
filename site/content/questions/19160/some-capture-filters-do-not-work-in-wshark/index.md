+++
type = "question"
title = "Some capture filters do not work in WShark!"
description = '''Hello, Some time ago I used the filter &quot;net&quot; for specific networks eg &quot;192.168.1.0/24 net&quot; and &quot;src&quot; for origin hosts, example : 192.168.1. 100, but none of these work for me now. Have they removed these filters? What is the alternative to these? Thanks in advance!'''
date = "2013-03-05T10:48:00Z"
lastmod = "2013-03-05T12:13:00Z"
weight = 19160
keywords = [ "capture", "capture-filter", "display-filter" ]
aliases = [ "/questions/19160" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Some capture filters do not work in WShark!](/questions/19160/some-capture-filters-do-not-work-in-wshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19160-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19160-score" class="post-score" title="current number of votes">0</div><span id="post-19160-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Some time ago I used the filter "net" for specific networks eg "192.168.1.0/24 net" and "src" for origin hosts, example : 192.168.1. 100, but none of these work for me now. Have they removed these filters? What is the alternative to these? Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '13, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/a334020eacdd8a7faf0f3e9d0d1cf678?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zig69&#39;s gravatar image" /><p><span>zig69</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zig69 has no accepted answers">0%</span></p></div></div><div id="comments-container-19160" class="comments-container"></div><div id="comment-tools-19160" class="comment-tools"></div><div class="clear"></div><div id="comment-19160-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19162"></span>

<div id="answer-container-19162" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19162-score" class="post-score" title="current number of votes">1</div><span id="post-19162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>These capture filter do work for me in 1.8.5 (Win XP)</p><blockquote><p><code>net 192.168.158.0/24</code><br />
<code>src 192.168.158.139</code><br />
</p></blockquote><p>So, what is your</p><ul><li>OS</li><li>OS version</li><li>Wireshark version</li></ul><p>where did you set that capture filter?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '13, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-19162" class="comments-container"><span id="19169"></span><div id="comment-19169" class="comment"><div id="post-19169-score" class="comment-score"></div><div class="comment-text"><p>OS:Windows XP OS version: Windows XP Service Pack 3 Wireshark version: 1.8.5</p><p>I set that capture filters in "filter" field in the main screen and It did not work.I did also from the field "capture file" in the option "show the capture options..." and did not work...</p></div><div id="comment-19169-info" class="comment-info"><span class="comment-age">(05 Mar '13, 11:39)</span> <span class="comment-user userinfo">zig69</span></div></div><span id="19170"></span><div id="comment-19170" class="comment"><div id="post-19170-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I set that capture filters in "filter" field in the main screen</p></blockquote><p>well, that's the <strong>display filter</strong> which has a totally different syntax.</p><blockquote><p>I did also from the field "capture file" in the option "show the capture options..." and did not work..</p></blockquote><p>Please see my answer for this question (where are the capture filters in 1.8.x.)</p><p><a href="http://ask.wireshark.org/questions/12452/where-are-the-capture-filter-options-in-wireshark-180">http://ask.wireshark.org/questions/12452/where-are-the-capture-filter-options-in-wireshark-180</a></p></div><div id="comment-19170-info" class="comment-info"><span class="comment-age">(05 Mar '13, 11:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="19172"></span><div id="comment-19172" class="comment"><div id="post-19172-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your valuable help.By the way, what is exactly the difference between Display and capture Filters?</p></div><div id="comment-19172-info" class="comment-info"><span class="comment-age">(05 Mar '13, 12:03)</span> <span class="comment-user userinfo">zig69</span></div></div><span id="19173"></span><div id="comment-19173" class="comment"><div id="post-19173-score" class="comment-score"></div><div class="comment-text"><p><a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a><br />
Capture filters are used <strong>during</strong> you capture data.</p><p><a href="http://wiki.wireshark.org/DisplayFilters">http://wiki.wireshark.org/DisplayFilters</a><br />
Display filters are used to analyze/filter the packets in Wireshark <strong>after</strong> your finished capturing.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-19173-info" class="comment-info"><span class="comment-age">(05 Mar '13, 12:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-19162" class="comment-tools"></div><div class="clear"></div><div id="comment-19162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

