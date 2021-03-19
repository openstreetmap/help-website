+++
type = "question"
title = "TvbRange:uint() does not handle %d byte integers"
description = '''I am writing a wireshark dissector in lua,set &quot;buf={} buf=buffer(0,size):uint()&quot;,and run wireshark,error occurred:&quot;TvbRange:uint() does not handle %d byte integers&quot;.'''
date = "2015-04-27T03:20:00Z"
lastmod = "2015-04-27T17:55:00Z"
weight = 41878
keywords = [ "lua", "tvbrange", "dissector" ]
aliases = [ "/questions/41878" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TvbRange:uint() does not handle %d byte integers](/questions/41878/tvbrangeuint-does-not-handle-d-byte-integers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41878-score" class="post-score" title="current number of votes">0</div><span id="post-41878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a wireshark dissector in lua,set "buf={} buf=buffer(0,size):uint()",and run wireshark,error occurred:"TvbRange:uint() does not handle %d byte integers".</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tvbrange" rel="tag" title="see questions tagged &#39;tvbrange&#39;">tvbrange</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '15, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/d4eab55adb51186bd1e0e5c981d1496b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qife&#39;s gravatar image" /><p><span>qife</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qife has no accepted answers">0%</span></p></div></div><div id="comments-container-41878" class="comments-container"></div><div id="comment-tools-41878" class="comment-tools"></div><div class="clear"></div><div id="comment-41878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41879"></span>

<div id="answer-container-41879" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41879-score" class="post-score" title="current number of votes">0</div><span id="post-41879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at Pascal's answer here<br />
</p><p><a href="http://ask.wireshark.org/questions/41614/converting-userdata-to-number">http://ask.wireshark.org/questions/41614/converting-userdata-to-number</a></p><p>Specifically reference to lua uint() function</p><p>11.8.3.3. tvbrange:uint()</p><p>Get a Big Endian (network order) unsigned integer from a TvbRange. The range must be 1, 2, 3 or 4 octets long. Returns</p><p>The unsigned integer value.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '15, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-41879" class="comments-container"><span id="41903"></span><div id="comment-41903" class="comment"><div id="post-41903-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I have read the docs,but I can't understand the function uint().Could you give me an example.</p></div><div id="comment-41903-info" class="comment-info"><span class="comment-age">(27 Apr '15, 17:55)</span> <span class="comment-user userinfo">qife</span></div></div></div><div id="comment-tools-41879" class="comment-tools"></div><div class="clear"></div><div id="comment-41879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

