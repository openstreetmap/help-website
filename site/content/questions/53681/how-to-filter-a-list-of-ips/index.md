+++
type = "question"
title = "How to filter a list of IP&#x27;s"
description = '''Hi, I need to filter a bigger number of not range-connected IP-Adresses. So I have to write them all down, but I do not find a working syntax. I tried this: Not Equal.ip.dst==191.168.232.139.90, 77.234.45.65, 5.45.58.148, 212.4.153.167, 52.71.81.247, 104.102.22.121 It does not work. Seperating the A...'''
date = "2016-06-27T23:05:00Z"
lastmod = "2016-06-29T12:32:00Z"
weight = 53681
keywords = [ "filter", "ip", "list" ]
aliases = [ "/questions/53681" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter a list of IP's](/questions/53681/how-to-filter-a-list-of-ips)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53681-score" class="post-score" title="current number of votes">0</div><span id="post-53681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need to filter a bigger number of not range-connected IP-Adresses. So I have to write them all down, but I do not find a working syntax.</p><p>I tried this:</p><p>Not Equal.ip.dst==191.168.232.139.90, 77.234.45.65, 5.45.58.148, 212.4.153.167, 52.71.81.247, 104.102.22.121</p><p>It does not work. Seperating the Adresses with "and" or "or" instead of commata does also not Work.</p><p>The Filter Line always stays red. How can I do this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '16, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/638247299493c279d676cc7c45f90d03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ellevader&#39;s gravatar image" /><p><span>Ellevader</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ellevader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jun '16, 02:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53681" class="comments-container"></div><div id="comment-tools-53681" class="comment-tools"></div><div class="clear"></div><div id="comment-53681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53684"></span>

<div id="answer-container-53684" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53684-score" class="post-score" title="current number of votes">0</div><span id="post-53684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you looking for something like this? ! (ip.dst==191.168.232.139 or ip.dst== 77.234.45.65 or ip.dst== 5.45.58.148 or ip.dst== 212.4.153.167 or ip.dst== 52.71.81.247 or ip.dst== 104.102.22.121)</p><p>Your first IP address is wrong (5 octets) and it is not possible to have a list of addresses, this is why your search did not work. If you want to remove frames to and from those addresses you want to use ip.addr instead of ip.dst</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '16, 23:46</strong></p><img src="https://secure.gravatar.com/avatar/f2fbd92409ebe39b42fcededc798db95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ae4baifee4&#39;s gravatar image" /><p><span>ae4baifee4</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ae4baifee4 has no accepted answers">0%</span></p></div></div><div id="comments-container-53684" class="comments-container"><span id="53732"></span><div id="comment-53732" class="comment"><div id="post-53732-score" class="comment-score"></div><div class="comment-text"><p>THX ae4baifee4! It absolutely works.</p><p>Hi Jaap, I'm an absolute beginner on this subject and did not understand too much so far, seems I have to renew my fundamentals of knowlegde about boolean expressions in general first :(</p><p>This really helps me much at a Problem I have to solve asap.</p><p>Thanks again!</p></div><div id="comment-53732-info" class="comment-info"><span class="comment-age">(29 Jun '16, 10:21)</span> <span class="comment-user userinfo">Ellevader</span></div></div><span id="53733"></span><div id="comment-53733" class="comment"><div id="post-53733-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p><p>Yes, Wireshark is a power tool, for power users.</p></div><div id="comment-53733-info" class="comment-info"><span class="comment-age">(29 Jun '16, 12:32)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-53684" class="comment-tools"></div><div class="clear"></div><div id="comment-53684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53691"></span>

<div id="answer-container-53691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53691-score" class="post-score" title="current number of votes">0</div><span id="post-53691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should read this documentation:</p><ul><li><a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html">Users Guide</a></li><li><a href="https://wiki.wireshark.org/DisplayFilters">Wiki</a></li></ul><p>for more background of how Display Filters work and how to compose the expressions you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '16, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53691" class="comments-container"></div><div id="comment-tools-53691" class="comment-tools"></div><div class="clear"></div><div id="comment-53691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

