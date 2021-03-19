+++
type = "question"
title = "tshark memory consumption increasing continuously"
description = '''Hi, I written an application in C Language which uses tshark to apply the display filter. Application sends PDUs to tshark over stdin and receive filtered PDUs over stdout. I am using following command while launching tshark in child process tshark -r - -R &quot;Filter Expression&quot; -w - -q -s0 This applic...'''
date = "2013-05-05T02:30:00Z"
lastmod = "2013-05-06T20:13:00Z"
weight = 20954
keywords = [ "memory_leak", "out-of-memory", "tshark" ]
aliases = [ "/questions/20954" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark memory consumption increasing continuously](/questions/20954/tshark-memory-consumption-increasing-continuously)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20954-score" class="post-score" title="current number of votes">0</div><span id="post-20954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I written an application in C Language which uses tshark to apply the display filter. Application sends PDUs to tshark over stdin and receive filtered PDUs over stdout. I am using following command while launching tshark in child process</p><p>tshark -r - -R "Filter Expression" -w - -q -s0</p><p>This application runs continuously which send around 4000 PDUs/sec to thsark for filtering.</p><p>But the memory consumption of tshark is continuously increasing. After 10-12 hours, tshark was using 2.2 GB of memory. I have to kill tshark and restart to free-up memory usage.</p><p>I gone through <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a> wiki page.</p><p>Is there any way to restrict the memory consumption of tshark??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-memory_leak" rel="tag" title="see questions tagged &#39;memory_leak&#39;">memory_leak</span> <span class="post-tag tag-link-out-of-memory" rel="tag" title="see questions tagged &#39;out-of-memory&#39;">out-of-memory</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '13, 02:30</strong></p><img src="https://secure.gravatar.com/avatar/a273217076451fb71206e452cf39243e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="friends&#39;s gravatar image" /><p><span>friends</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="friends has no accepted answers">0%</span></p></div></div><div id="comments-container-20954" class="comments-container"></div><div id="comment-tools-20954" class="comment-tools"></div><div class="clear"></div><div id="comment-20954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20955"></span>

<div id="answer-container-20955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20955-score" class="post-score" title="current number of votes">1</div><span id="post-20955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark and tshark keep state of past connections to be able to dissect future packets properly. There is no mechanism in Wireshark or Tshark that flushes the state information. In Wireshark it is needed to be able to dissect a packet properly when it will be clicked on and even though tsharks one-pass design might make it possible to flush stale data, it uses the same engine as Wireshark.</p><p>Are you depending on display filters? What are you filtering on? Can capture (BPF) filters be used?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '13, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20955" class="comments-container"><span id="20999"></span><div id="comment-20999" class="comment"><div id="post-20999-score" class="comment-score"></div><div class="comment-text"><p>Yes, I need display filters. I need filtering of many fields of gsm_map layer (for example, msisdn). Capture filter does not provide all those filtering capability.</p></div><div id="comment-20999-info" class="comment-info"><span class="comment-age">(06 May '13, 20:13)</span> <span class="comment-user userinfo">friends</span></div></div></div><div id="comment-tools-20955" class="comment-tools"></div><div class="clear"></div><div id="comment-20955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

