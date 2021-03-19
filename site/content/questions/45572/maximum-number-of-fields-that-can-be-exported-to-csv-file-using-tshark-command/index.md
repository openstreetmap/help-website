+++
type = "question"
title = "Maximum number of fields that can be exported to CSV file using tshark command"
description = '''Hi all I was looking for a command line option to export fields within a message into a CSV file, i could find that it can be done using tshark command with some of the options. My question is as follows.  What is the maximum number of fields that can be exported to CSV file using -e option. (Becaus...'''
date = "2015-09-01T11:29:00Z"
lastmod = "2015-09-04T07:38:00Z"
weight = 45572
keywords = [ "tshark", "export-to-csv" ]
aliases = [ "/questions/45572" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Maximum number of fields that can be exported to CSV file using tshark command](/questions/45572/maximum-number-of-fields-that-can-be-exported-to-csv-file-using-tshark-command)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45572-score" class="post-score" title="current number of votes">0</div><span id="post-45572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I was looking for a command line option to export fields within a message into a CSV file, i could find that it can be done using tshark command with some of the options. My question is as follows.</p><ul><li>What is the maximum number of fields that can be exported to CSV file using -e option. (Because i have some of the messages which contains more than 100 fields).</li><li>Is there a way i can export all the fields of a message by default without specifying them using -e option. (as in most of my cases i need to export all the fields of a message, the command line becomes so big to maintain after adding all the fields).</li></ul><p>Thank you</p><p>Kiran Kumar G</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-export-to-csv" rel="tag" title="see questions tagged &#39;export-to-csv&#39;">export-to-csv</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '15, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p><span>Kiran Kumar G</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Sep '15, 13:29</strong> </span></p></div></div><div id="comments-container-45572" class="comments-container"></div><div id="comment-tools-45572" class="comment-tools"></div><div class="clear"></div><div id="comment-45572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45632"></span>

<div id="answer-container-45632" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45632-score" class="post-score" title="current number of votes">1</div><span id="post-45632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kiran Kumar G has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>What is the maximum number of fields that can be exported to CSV file using -e option.</em></p><p>There is no limit per se; however, there are limits as to how long the command-line can be, and this limit varies from platform to platform. For example, on Windows using <code>cmd.exe</code>, the following article describes the limits: <a href="https://support.microsoft.com/en-us/kb/830473">https://support.microsoft.com/en-us/kb/830473</a>.</p><p><em>Is there a way i can export all the fields of a message by default without specifying them using -e option.</em></p><p>Not that I know of.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Sep '15, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-45632" class="comments-container"></div><div id="comment-tools-45632" class="comment-tools"></div><div class="clear"></div><div id="comment-45632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

