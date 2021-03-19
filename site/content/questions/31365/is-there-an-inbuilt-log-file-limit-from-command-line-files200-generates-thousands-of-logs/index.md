+++
type = "question"
title = "Is there an inbuilt Log File limit from command line. files:200 generates thousands of logs."
description = '''Hi,  Is there an inbuilt Log File limit from command line. files:200 generates thousands of logs. At 200, i get many thousands of log files. I stopped them at 20,000 manually. &quot;C:&#92;Program Files&#92;Wireshark&#92;Wireshark.exe&quot; -i &quot;Local Area Connection&quot; -k -w &quot;C:&#92;SOE&#92;Logs&#92;NetCap.pcapng&quot; -N &quot;mntC&quot; -t ad -b f...'''
date = "2014-04-01T21:45:00Z"
lastmod = "2014-04-02T13:25:00Z"
weight = 31365
keywords = [ "command", "limit", "log", "file", "line." ]
aliases = [ "/questions/31365" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there an inbuilt Log File limit from command line. files:200 generates thousands of logs.](/questions/31365/is-there-an-inbuilt-log-file-limit-from-command-line-files200-generates-thousands-of-logs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31365-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31365-score" class="post-score" title="current number of votes">0</div><span id="post-31365-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is there an inbuilt Log File limit from command line. files:200 generates thousands of logs.</p><p>At 200, i get many thousands of log files. I stopped them at 20,000 manually.</p><p>"C:\Program Files\Wireshark\Wireshark.exe" -i "Local Area Connection" -k -w "C:\SOE\Logs\NetCap.pcapng" -N "mntC" -t ad -b filesize:10000 -b files:200</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-command" rel="tag" title="see questions tagged &#39;command&#39;">command</span> <span class="post-tag tag-link-limit" rel="tag" title="see questions tagged &#39;limit&#39;">limit</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-line." rel="tag" title="see questions tagged &#39;line.&#39;">line.</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 21:45</strong></p><img src="https://secure.gravatar.com/avatar/c95b60dcb8f2b864bdcd9bb2bfed3e78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="timekeeper5150&#39;s gravatar image" /><p><span>timekeeper5150</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="timekeeper5150 has no accepted answers">0%</span></p></div></div><div id="comments-container-31365" class="comments-container"></div><div id="comment-tools-31365" class="comment-tools"></div><div class="clear"></div><div id="comment-31365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31430"></span>

<div id="answer-container-31430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31430-score" class="post-score" title="current number of votes">0</div><span id="post-31430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I remember we had this 'problem' here, but I can't find the question for it. So, here are some questions in return.</p><ul><li>What is your OS version?</li><li>What is you Wireshark version?</li><li><p>Is there any security software on the PC that might prevent Wireshark from deleted the old ring buffer files? If so, did you try to disable that software?</p></li><li><p>did you try to capture with dumpcap instead of Wireshark</p></li></ul><blockquote><p>dumpcap -i "Local Area Connection" -w "C:\SOE\Logs\NetCap.pcapng" -b filesize:10000 -b files:200</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31430" class="comments-container"></div><div id="comment-tools-31430" class="comment-tools"></div><div class="clear"></div><div id="comment-31430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

