+++
type = "question"
title = "dissector debugging -- how to find the exact line of a &quot;malformed packet&quot; exception"
description = '''I&#x27;m developing a dissector for a custom protocol and have been getting &quot;Malformed Packet&quot; messages like the one shown below. From what I understand this is usually caused by overflowing a tvb. Is there any way to get some sort of stack trace so I can see exactly where my dissector/protocol is throwi...'''
date = "2011-06-28T16:51:00Z"
lastmod = "2011-06-29T18:44:00Z"
weight = 4797
keywords = [ "development", "exception", "dissector", "tvb" ]
aliases = [ "/questions/4797" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [dissector debugging -- how to find the exact line of a "malformed packet" exception](/questions/4797/dissector-debugging-how-to-find-the-exact-line-of-a-malformed-packet-exception)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4797-score" class="post-score" title="current number of votes">0</div><span id="post-4797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm developing a dissector for a custom protocol and have been getting "Malformed Packet" messages like the one shown below. From what I understand this is usually caused by overflowing a <code>tvb</code>. Is there any way to get some sort of stack trace so I can see exactly where my dissector/protocol is throwing the error?</p><pre><code>Expert Info (Error/Malformed): Malformed Packet (Exception occurred)
Message: Malformed Packet (Exception occurred)
Severity level: Error
Group: Malformed</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-exception" rel="tag" title="see questions tagged &#39;exception&#39;">exception</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tvb" rel="tag" title="see questions tagged &#39;tvb&#39;">tvb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '11, 16:51</strong></p><img src="https://secure.gravatar.com/avatar/38228d3d825564323a936d5f630aaba2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mitch_feaster&#39;s gravatar image" /><p><span>mitch_feaster</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mitch_feaster has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jun '11, 16:56</strong> </span></p></div></div><div id="comments-container-4797" class="comments-container"></div><div id="comment-tools-4797" class="comment-tools"></div><div class="clear"></div><div id="comment-4797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4816"></span>

<div id="answer-container-4816" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4816-score" class="post-score" title="current number of votes">3</div><span id="post-4816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mitch_feaster has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try stepping through execution of your dissector using a debugger. If you have a capture file and you want to narrow down the problem, use editcap (or Wireshark, I suppose) to "divide-and-conquer". Keep splitting the file in half until you isolate the offending packet. That may or may not make it obvious as to what part of your code is mis-behaving, but if not, it will still make stepping through execution in the debugger easier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 10:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '11, 18:44</strong> </span></p></div></div><div id="comments-container-4816" class="comments-container"><span id="4822"></span><div id="comment-4822" class="comment"><div id="post-4822-score" class="comment-score"></div><div class="comment-text"><p>Hmmm, well I already know the offending packets (I can even do a filter on "malformed" to find them) but those packets are decoding hundreds of messages, so using the debugger will be a bit of a pain... But it looks like that's my only option right now :). It would at least be nice if I could set a breakpoint in the exception handling code and then look at the stack trace from there but I can't quite pin down where that happens...</p></div><div id="comment-4822-info" class="comment-info"><span class="comment-age">(29 Jun '11, 13:43)</span> <span class="comment-user userinfo">mitch_feaster</span></div></div><span id="4824"></span><div id="comment-4824" class="comment"><div id="post-4824-score" class="comment-score"></div><div class="comment-text"><p>@mitch_feaster: So long as the error isn't dependent on a complete conversation, you could filter your capture so that only the malformed packets are displayed, then save only the displayed packets and debug using that file. That way, you could step with the debugger in a minimal subset. Probably not a totally optimal solution, but at least better than debugging with a full capture.</p></div><div id="comment-4824-info" class="comment-info"><span class="comment-age">(29 Jun '11, 15:08)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="4829"></span><div id="comment-4829" class="comment"><div id="post-4829-score" class="comment-score"></div><div class="comment-text"><p>@mitch_feaster: You might try setting a breakpoint in epan/dissectors/packet-frame.c's show_reported_bounds_error() function.</p></div><div id="comment-4829-info" class="comment-info"><span class="comment-age">(29 Jun '11, 18:44)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-4816" class="comment-tools"></div><div class="clear"></div><div id="comment-4816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4806"></span>

<div id="answer-container-4806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4806-score" class="post-score" title="current number of votes">0</div><span id="post-4806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try setting the environment variable <code>WIRESHARK_ABORT_ON_DISSECTOR_BUG</code> before running Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '11, 00:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4806" class="comments-container"><span id="4813"></span><div id="comment-4813" class="comment"><div id="post-4813-score" class="comment-score"></div><div class="comment-text"><p>Still nothing...</p></div><div id="comment-4813-info" class="comment-info"><span class="comment-age">(29 Jun '11, 09:39)</span> <span class="comment-user userinfo">mitch_feaster</span></div></div></div><div id="comment-tools-4806" class="comment-tools"></div><div class="clear"></div><div id="comment-4806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

