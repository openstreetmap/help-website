+++
type = "question"
title = "Convert large (60+ GB) Wireshark dataset to csv"
description = '''Hi, I am trying to convert a large Dataset to csv for analysis with statistic tools. My problem:  - Can&#x27;t open the dataset in Wireshark Windows - Program Crashes after 12+ hrs of loading  - Can&#x27;t convert via tshark because process is extreamly slow and crashed my computer after 20+ hrs I observed th...'''
date = "2017-06-07T14:29:00Z"
lastmod = "2017-06-07T14:41:00Z"
weight = 61848
keywords = [ "conversion" ]
aliases = [ "/questions/61848" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Convert large (60+ GB) Wireshark dataset to csv](/questions/61848/convert-large-60-gb-wireshark-dataset-to-csv)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61848-score" class="post-score" title="current number of votes">0</div><span id="post-61848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am trying to convert a large Dataset to csv for analysis with statistic tools. My problem: - Can't open the dataset in Wireshark Windows - Program Crashes after 12+ hrs of loading - Can't convert via tshark because process is extreamly slow and crashed my computer after 20+ hrs</p><p>I observed that using the tshark option the process does not use 100% of CPU and/or disk, though uses 100% of memory. Is there any "easy" form to convert?</p><p>thanks a lot in advanced</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversion" rel="tag" title="see questions tagged &#39;conversion&#39;">conversion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '17, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/181b1405e8a01bbe47e0233b262659b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kjeld&#39;s gravatar image" /><p><span>Kjeld</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kjeld has no accepted answers">0%</span></p></div></div><div id="comments-container-61848" class="comments-container"></div><div id="comment-tools-61848" class="comment-tools"></div><div class="clear"></div><div id="comment-61848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61849"></span>

<div id="answer-container-61849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61849-score" class="post-score" title="current number of votes">0</div><span id="post-61849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Both Wireshark and tshark are not made to handle this amount in a single file. The tracking of TCP sessions, protocol dependencies and symptoms eats up all the memory after a while.</p><p>Maybe you can run your CSV export from partial files? In that case you can use editcap (CLI tool installed with Wireshark) to cut the big file into smaller files using the -c parameter. If that's not possible you should tell us more about what kind of export you're trying to accomplish.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jun '17, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61849" class="comments-container"><span id="61850"></span><div id="comment-61850" class="comment"><div id="post-61850-score" class="comment-score"></div><div class="comment-text"><p>Great, thanks Jasper, will try that!</p></div><div id="comment-61850-info" class="comment-info"><span class="comment-age">(07 Jun '17, 14:41)</span> <span class="comment-user userinfo">Kjeld</span></div></div></div><div id="comment-tools-61849" class="comment-tools"></div><div class="clear"></div><div id="comment-61849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

