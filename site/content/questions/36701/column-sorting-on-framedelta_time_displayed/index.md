+++
type = "question"
title = "Column Sorting on frame.delta_time_displayed"
description = '''Hello, I have been searching for the last 60 minutes (30 of them here), so forgive me if I missed it, but this is driving me nuts.. I am currently working through the &quot;Troubleshooting with wireshark&quot; book from Laura Chapell (excellent stuff BTW, always good to start again) but I am currently having ...'''
date = "2014-09-29T12:46:00Z"
lastmod = "2014-09-29T14:14:00Z"
weight = 36701
keywords = [ "sorting" ]
aliases = [ "/questions/36701" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Column Sorting on frame.delta\_time\_displayed](/questions/36701/column-sorting-on-framedelta_time_displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36701-score" class="post-score" title="current number of votes">0</div><span id="post-36701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have been searching for the last 60 minutes (30 of them here), so forgive me if I missed it, but this is driving me nuts..</p><p>I am currently working through the "Troubleshooting with wireshark" book from Laura Chapell (excellent stuff BTW, always good to start again) but I am currently having difficulty with something technically trivial imho :/</p><p>I added a Custom Column for frame.time_delta_displayed, all good. I changed my time format to ms (which only seems to actually affect the original Time column??) But now when I sort on the column by clicking twice, it only sorts the whole numbers, anything after the decimal doesn't seem to interest it??</p><p>i.e 5.223137000 4.000378000 1.000000000 0.000154000 0.003407000</p><p>Can someone tell me how I: A: Get my custom time fields to also display ms ( I assume I am going file editing somewhere but can't find it yet) b: How I can then get the columns to sort properly.. In the book they are okay, just not on my pc..(I found a semi related question with an answer about the sorting gtk being used not doing certain things??)</p><p>latest version 1.12.1, tried this on Windows 7, Ubuntu/Mint</p><p>Thx Darren</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sorting" rel="tag" title="see questions tagged &#39;sorting&#39;">sorting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '14, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-36701" class="comments-container"></div><div id="comment-tools-36701" class="comment-tools"></div><div class="clear"></div><div id="comment-36701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36708"></span>

<div id="answer-container-36708" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36708-score" class="post-score" title="current number of votes">1</div><span id="post-36708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DarrenWright has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The sorting problem (at least for tcp.time_delta) is a known bug: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8964">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8964</a><br />
I assume the <code>frame.time_delta_displayed</code> has the same root cause.</p><p>The modifiable granularity of the time stamps seems to apply to non-custom columns only. So you might want to use the following column settings to achieve this.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/columns.PNG" alt="alt text" /></p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '14, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-36708" class="comments-container"><span id="36710"></span><div id="comment-36710" class="comment"><div id="post-36710-score" class="comment-score"></div><div class="comment-text"><p>Thx, thought I was going mad.</p><p>The Delta Time was what I wanted :D sometimes we can really overcomplicate the simplest of things. As I see this is the FRAME Delta, I assume there is currently no built in TCP delta?</p><p>As for the bug, I just looked into it, it sems to affect all custom columns, if I take a built in column it works fine.</p><p>Ah well,you can't have everything all the time. Thanks for the help, it's good. (and yes: location Germany. This bug is annyoing as hell.. CSV files have the same thing as here a ; is used instead of a ,)</p></div><div id="comment-36710-info" class="comment-info"><span class="comment-age">(29 Sep '14, 14:03)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="36711"></span><div id="comment-36711" class="comment"><div id="post-36711-score" class="comment-score"></div><div class="comment-text"><p>If the answer on this question answered your question, please Accept it (by clicking the checkmark) so the question won't show up in the list of unanswered questions.</p><p>Thanks</p></div><div id="comment-36711-info" class="comment-info"><span class="comment-age">(29 Sep '14, 14:14)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-36708" class="comment-tools"></div><div class="clear"></div><div id="comment-36708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

