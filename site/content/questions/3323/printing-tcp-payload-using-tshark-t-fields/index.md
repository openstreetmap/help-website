+++
type = "question"
title = "Printing tcp payload using tshark -T fields?"
description = '''Hi all, I&#x27;m trying to print out the first 20 TCP payload bytes in tshark, but I want to print out several other fields so that I can pass the result to an analysis program I&#x27;m writing. Easiest way for me to parse the data is CSV, so I&#x27;m using tshark in -T fields mode with -E separator=, So I have ad...'''
date = "2011-04-04T09:13:00Z"
lastmod = "2011-04-16T13:14:00Z"
weight = 3323
keywords = [ "fields", "tshark", "tcp", "payload" ]
aliases = [ "/questions/3323" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Printing tcp payload using tshark -T fields?](/questions/3323/printing-tcp-payload-using-tshark-t-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3323-score" class="post-score" title="current number of votes">0</div><span id="post-3323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm trying to print out the first 20 TCP payload bytes in tshark, but I want to print out several other fields so that I can pass the result to an analysis program I'm writing. Easiest way for me to parse the data is CSV, so I'm using tshark in -T fields mode with -E separator=,</p><p>So I have additional options such as -e tcp.srcport -e tcp.stream -e tcp.flags.syn and so on. But as the last field, I can't find how to output the first 20 TCP payload bytes. I tried something like -e frame[54-73] but that didn't print anything out, neither did -e tcp[20-39] nor -e ip[54-73].</p><p>Any ideas?</p><p>Thanks,</p><p>--Rob</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '11, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/5335f2ecb2692cc80d041ee7d94c4198?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobB&#39;s gravatar image" /><p><span>RobB</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobB has no accepted answers">0%</span></p></div></div><div id="comments-container-3323" class="comments-container"><span id="3324"></span><div id="comment-3324" class="comment"><div id="post-3324-score" class="comment-score"></div><div class="comment-text"><p>I should also mention that -e data doesn't work: for TCP packets, it prints out nothing (even though I know there is data in there), and it only seems to print out data for things like IP fragments.</p></div><div id="comment-3324-info" class="comment-info"><span class="comment-age">(04 Apr '11, 09:23)</span> <span class="comment-user userinfo">RobB</span></div></div></div><div id="comment-tools-3323" class="comment-tools"></div><div class="clear"></div><div id="comment-3323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3534"></span>

<div id="answer-container-3534" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3534-score" class="post-score" title="current number of votes">1</div><span id="post-3534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Starting with Wireshark 1.4.5, available from the main <a href="http://www.wireshark.org/download.html">download</a> page, or with any development release starting from r36629, available from the <a href="http://www.wireshark.org/download/automated/">automated</a> download area, the TCP segment data is now filterable with "tcp.data". Unfortunately, you still won't be able to limit the amount of data with something like "tcp.data[0:20]".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '11, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3534" class="comments-container"></div><div id="comment-tools-3534" class="comment-tools"></div><div class="clear"></div><div id="comment-3534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

