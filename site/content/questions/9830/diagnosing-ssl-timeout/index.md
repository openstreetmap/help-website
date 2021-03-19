+++
type = "question"
title = "Diagnosing SSL timeout"
description = '''I&#x27;m attempting to use a PayPal listener plugin in WordPress and am hung up on an SSL timeout. Searches to date have yielded nothing on topic and the plugin developer is effectively offline. I thought perhaps I&#x27;d learn something by performing a packet trace. Unfortunately I don&#x27;t quite know what to l...'''
date = "2012-03-28T20:36:00Z"
lastmod = "2012-03-29T08:18:00Z"
weight = 9830
keywords = [ "ssl", "paypal", "ipn", "timeout" ]
aliases = [ "/questions/9830" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Diagnosing SSL timeout](/questions/9830/diagnosing-ssl-timeout)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9830-score" class="post-score" title="current number of votes">0</div><span id="post-9830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm attempting to use a PayPal listener plugin in WordPress and am hung up on an SSL timeout. Searches to date have yielded nothing on topic and the plugin developer is effectively offline. I thought perhaps I'd learn something by performing a packet trace. Unfortunately I don't quite know what to look for. Any suggestions on how best to proceed are welcome. Thanks.</p><p>George</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-paypal" rel="tag" title="see questions tagged &#39;paypal&#39;">paypal</span> <span class="post-tag tag-link-ipn" rel="tag" title="see questions tagged &#39;ipn&#39;">ipn</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '12, 20:36</strong></p><img src="https://secure.gravatar.com/avatar/97bb1df7d515458e46518b675b92cf68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeoB&#39;s gravatar image" /><p><span>GeoB</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeoB has no accepted answers">0%</span></p></div></div><div id="comments-container-9830" class="comments-container"><span id="9838"></span><div id="comment-9838" class="comment"><div id="post-9838-score" class="comment-score"></div><div class="comment-text"><p>In a trace of the conversation I see the IPN POST from PayPal, a DNS query for sandbox, then a RST after about 4 seconds. This does not appear consistent with code that says timeout =&gt; 30 seconds (and sslverify =&gt; false). Or do I misunderstand what I see? g</p></div><div id="comment-9838-info" class="comment-info"><span class="comment-age">(29 Mar '12, 08:18)</span> <span class="comment-user userinfo">GeoB</span></div></div></div><div id="comment-tools-9830" class="comment-tools"></div><div class="clear"></div><div id="comment-9830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

