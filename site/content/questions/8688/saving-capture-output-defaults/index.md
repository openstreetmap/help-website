+++
type = "question"
title = "Saving Capture Output Defaults"
description = '''I am using Wireshark to monitorall traffic on a switch for our VOIP supplier, and writing to multiple files, creating a new file every 10 minutes. Every time I restart Wireshark I have to add new settings - Is there any way I can save these settings so that it always restarts and makes the minute ou...'''
date = "2012-01-30T03:16:00Z"
lastmod = "2012-01-30T08:36:00Z"
weight = 8688
keywords = [ "capture-defaults" ]
aliases = [ "/questions/8688" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Saving Capture Output Defaults](/questions/8688/saving-capture-output-defaults)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8688-score" class="post-score" title="current number of votes">0</div><span id="post-8688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark to monitorall traffic on a switch for our VOIP supplier, and writing to multiple files, creating a new file every 10 minutes. Every time I restart Wireshark I have to add new settings - Is there any way I can save these settings so that it always restarts and makes the minute output files. Looking at help, I guess a batch file might do it - what is the syntax, or can I copy the syntax of my edited job to drop into a batch fle.</p><p>Any pointers would be much appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-defaults" rel="tag" title="see questions tagged &#39;capture-defaults&#39;">capture-defaults</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '12, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/31ee5e050f9d633ec206e3624c91200c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithy&#39;s gravatar image" /><p><span>keithy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithy has no accepted answers">0%</span></p></div></div><div id="comments-container-8688" class="comments-container"></div><div id="comment-tools-8688" class="comment-tools"></div><div class="clear"></div><div id="comment-8688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8691"></span>

<div id="answer-container-8691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8691-score" class="post-score" title="current number of votes">0</div><span id="post-8691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Look into using dumpcap instead. Using a cmd file it could look like this:</p><p><code>"C:Program FilesWiresharkdumpcap.exe" -i 2 -f "not tcp port 3389 and  not tcp port 80" -w "net1.cap" -b duration:600 -b files:200 </code></p><p>Look at the <a href="http://www.wireshark.org/docs/wsug_html_chunked/AppToolsdumpcap.html">user's guide</a> for the exact parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '12, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8691" class="comments-container"><span id="8703"></span><div id="comment-8703" class="comment"><div id="post-8703-score" class="comment-score"></div><div class="comment-text"><p>Thank you for such a prompt response - will get onto it !</p></div><div id="comment-8703-info" class="comment-info"><span class="comment-age">(30 Jan '12, 08:36)</span> <span class="comment-user userinfo">keithy</span></div></div></div><div id="comment-tools-8691" class="comment-tools"></div><div class="clear"></div><div id="comment-8691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

