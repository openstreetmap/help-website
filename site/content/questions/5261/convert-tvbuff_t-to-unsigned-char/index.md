+++
type = "question"
title = "Convert tvbuff_t* to unsigned char*"
description = '''Is there a nice clean way to convert tvbuff_t to an unsigned char? I am using an external library for some decryption and it accepts the unsigned char*. I was looking through the Wireshark source code but only came up with: struct tvbuff; typedef struct tvbuff tvbuff_t;  Which doesn&#x27;t give me enough...'''
date = "2011-07-26T08:16:00Z"
lastmod = "2011-07-27T01:55:00Z"
weight = 5261
keywords = [ "development" ]
aliases = [ "/questions/5261" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Convert tvbuff\_t\* to unsigned char\*](/questions/5261/convert-tvbuff_t-to-unsigned-char)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5261-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5261-score" class="post-score" title="current number of votes">0</div><span id="post-5261-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a nice clean way to convert tvbuff_t <em>to an unsigned char</em>? I am using an external library for some decryption and it accepts the unsigned char*. I was looking through the Wireshark source code but only came up with:</p><pre><code>struct tvbuff;
typedef struct tvbuff tvbuff_t;</code></pre><p>Which doesn't give me enough information to be able to convert, that is unless I can simply do a byte for byte conversion?<br />
</p><p>Thank you for your time, Brandon</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p><span>officialhopsof</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jul '11, 11:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5261" class="comments-container"><span id="5263"></span><div id="comment-5263" class="comment"><div id="post-5263-score" class="comment-score"></div><div class="comment-text"><p>Oh, also, I do not need the header information, I simply need the actual message data.</p></div><div id="comment-5263-info" class="comment-info"><span class="comment-age">(26 Jul '11, 08:47)</span> <span class="comment-user userinfo">officialhopsof</span></div></div></div><div id="comment-tools-5261" class="comment-tools"></div><div class="clear"></div><div id="comment-5261-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5266"></span>

<div id="answer-container-5266" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5266-score" class="post-score" title="current number of votes">5</div><span id="post-5266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See README.developer section 1.4.2 "Extracting data from packets".</p><p>Note the caveats around using functions such as <code>tvb_get_ptr()</code> though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5266" class="comments-container"><span id="5274"></span><div id="comment-5274" class="comment"><div id="post-5274-score" class="comment-score"></div><div class="comment-text"><p>Found it! Thanks!</p></div><div id="comment-5274-info" class="comment-info"><span class="comment-age">(26 Jul '11, 12:24)</span> <span class="comment-user userinfo">officialhopsof</span></div></div><span id="5300"></span><div id="comment-5300" class="comment"><div id="post-5300-score" class="comment-score">2</div><div class="comment-text"><p>If this is the correct answer please click the tick so it shows as the accepted answer.</p></div><div id="comment-5300-info" class="comment-info"><span class="comment-age">(27 Jul '11, 01:55)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-5266" class="comment-tools"></div><div class="clear"></div><div id="comment-5266-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

