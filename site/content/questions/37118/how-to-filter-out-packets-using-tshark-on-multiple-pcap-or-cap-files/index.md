+++
type = "question"
title = "How to filter out packets using tshark on multiple pcap or cap files?"
description = '''Hi,  Is there a way to filter out packets using tshark on multiple pcap or cap files. I have tried with different variations but it has not worked, it only works when I explicitly specify the full file name. example: This will not work tshark -r 201410100*.cap -R &quot;diameter.Session-Id == &#92;&quot;what ever&#92;...'''
date = "2014-10-16T14:49:00Z"
lastmod = "2015-01-07T22:32:00Z"
weight = 37118
keywords = [ "tshark" ]
aliases = [ "/questions/37118" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter out packets using tshark on multiple pcap or cap files?](/questions/37118/how-to-filter-out-packets-using-tshark-on-multiple-pcap-or-cap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37118-score" class="post-score" title="current number of votes">0</div><span id="post-37118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Is there a way to filter out packets using tshark on multiple pcap or cap files.</p><p>I have tried with different variations but it has not worked, it only works when I explicitly specify the full file name.</p><p>example: This will not work<br />
tshark -r 201410100*.cap -R "diameter.Session-Id == \"what ever\"" -Tfields -E separator='|' -e frame.time</p><p>Thanks, Sunil</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '14, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/5062fe331d35d8cb304c944c61640383?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sunny&#39;s gravatar image" /><p><span>Sunny</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sunny has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37118" class="comments-container"></div><div id="comment-tools-37118" class="comment-tools"></div><div class="clear"></div><div id="comment-37118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37119"></span>

<div id="answer-container-37119" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37119-score" class="post-score" title="current number of votes">0</div><span id="post-37119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TShark doesn't support reading multiple capture files, so you can't run a single instance of TShark on multiple files. You'd have to run TShark separately once per file, or merge the captures into a single capture file using mergecap and run TShark on the merged file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '14, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37119" class="comments-container"></div><div id="comment-tools-37119" class="comment-tools"></div><div class="clear"></div><div id="comment-37119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38935"></span>

<div id="answer-container-38935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38935-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38935-score" class="post-score" title="current number of votes">0</div><span id="post-38935-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>for file in *.pcap;do echo "$file";tshark -n -r "$file" http.host == "keyword:443";done</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '15, 22:32</strong></p><img src="https://secure.gravatar.com/avatar/7aa04499f3f563d0098ede94c59a0589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bnx2&#39;s gravatar image" /><p><span>bnx2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bnx2 has no accepted answers">0%</span></p></div></div><div id="comments-container-38935" class="comments-container"></div><div id="comment-tools-38935" class="comment-tools"></div><div class="clear"></div><div id="comment-38935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

