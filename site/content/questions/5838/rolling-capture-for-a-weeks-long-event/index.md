+++
type = "question"
title = "Rolling Capture for a week&#x27;s long event"
description = '''Is there a way to truncate the capture log to say 4 or 6 hours? I need to diagnose a problem that happens randomly every 4-14 days, and would like to have a capture of the data happening at the moment of the event without crushing the computer running Wireshark for 14 days straight...'''
date = "2011-08-24T06:47:00Z"
lastmod = "2011-08-24T07:45:00Z"
weight = 5838
keywords = [ "rolling", "capture", "log" ]
aliases = [ "/questions/5838" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Rolling Capture for a week's long event](/questions/5838/rolling-capture-for-a-weeks-long-event)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5838-score" class="post-score" title="current number of votes">1</div><span id="post-5838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to truncate the capture log to say 4 or 6 hours? I need to diagnose a problem that happens randomly every 4-14 days, and would like to have a capture of the data happening at the moment of the event without crushing the computer running Wireshark for 14 days straight...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rolling" rel="tag" title="see questions tagged &#39;rolling&#39;">rolling</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-log" rel="tag" title="see questions tagged &#39;log&#39;">log</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '11, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/7984cfa1f056f7fa3c7b46b7fc3f7b10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cshep70&#39;s gravatar image" /><p><span>cshep70</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cshep70 has no accepted answers">0%</span></p></div></div><div id="comments-container-5838" class="comments-container"></div><div id="comment-tools-5838" class="comment-tools"></div><div class="clear"></div><div id="comment-5838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5840"></span>

<div id="answer-container-5840" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5840-score" class="post-score" title="current number of votes">4</div><span id="post-5840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use dumpcap (included with Wireshark) for that purpose. I have kept dumpcap running for months in that manner. The clue is to make use of the ringbuffer functionality. You will want to use something like:</p><pre><code>dumpcap -i &lt;interface&gt; -w &lt;file.cap&gt; -b filesize:32768 -b files:128</code></pre><p>This will create a 4GB ringbuffer (128 files of 32MB). This way you will never run out of disk space and keep only the last 4GB of capture data until the problem occurs and the dumpcap command is stopped (by ctrl+C).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '11, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5840" class="comments-container"><span id="5842"></span><div id="comment-5842" class="comment"><div id="post-5842-score" class="comment-score"></div><div class="comment-text"><p>Much Obliged! That's what I had been looking for.</p></div><div id="comment-5842-info" class="comment-info"><span class="comment-age">(24 Aug '11, 07:45)</span> <span class="comment-user userinfo">cshep70</span></div></div></div><div id="comment-tools-5840" class="comment-tools"></div><div class="clear"></div><div id="comment-5840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

