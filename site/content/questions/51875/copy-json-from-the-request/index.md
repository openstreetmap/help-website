+++
type = "question"
title = "Copy json from the request"
description = '''I&#x27;m trying to copy json from a POST&#x27;ed request. I can see the json in two different formats, but none of them easily copyable. Any suggestions how to get the json out of request in a simple way?    '''
date = "2016-04-22T08:27:00Z"
lastmod = "2016-04-26T00:56:00Z"
weight = 51875
keywords = [ "json", "copy", "request", "copying" ]
aliases = [ "/questions/51875" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Copy json from the request](/questions/51875/copy-json-from-the-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51875-score" class="post-score" title="current number of votes">0</div><span id="post-51875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to copy json from a POST'ed request. I can see the json in two different formats, but none of them easily copyable.</p><p>Any suggestions how to get the json out of request in a simple way?</p><p><img src="http://i63.tinypic.com/6o390w.png" alt="json place " /></p><p><img src="http://i67.tinypic.com/2ef3tyr.png" alt="json place 2" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-copy" rel="tag" title="see questions tagged &#39;copy&#39;">copy</span> <span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-copying" rel="tag" title="see questions tagged &#39;copying&#39;">copying</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '16, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/f7efa95364507635a0021a1231eb6b65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aleksander&#39;s gravatar image" /><p><span>Aleksander</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aleksander has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51875" class="comments-container"></div><div id="comment-tools-51875" class="comment-tools"></div><div class="clear"></div><div id="comment-51875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51878"></span>

<div id="answer-container-51878" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51878-score" class="post-score" title="current number of votes">2</div><span id="post-51878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Right click the Javascript Object Notation entry in the packet list, select "Export Packet Bytes...", enter a suitable filename, e.g json.txt and then click Save.</p><p>For the first packet in the json sample capture <a href="http://www.pcapr.net/view/tyson.key/2010/4/6/4/json-small.pcap.html">here</a>, I got this output:</p><pre><code>[{&quot;C&quot;:&quot;VIS&quot;,&quot;D&quot;:{&quot;u&quot;:[{&quot;i&quot;:270729761,&quot;c&quot;:7143451,&quot;p&quot;:2187,&quot;pp&quot;:10849}, &quot;i&quot;:270746145,&quot;c&quot;:7143452,&quot;pp&quot;:10849,&quot;ps&quot;:0,&quot;pe&quot;:0}]}}]</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '16, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-51878" class="comments-container"><span id="51939"></span><div id="comment-51939" class="comment"><div id="post-51939-score" class="comment-score"></div><div class="comment-text"><p>Took me a while to find the "Export Packet Bytes Bytes" option. But found and it worked like a charm. Thanks!</p></div><div id="comment-51939-info" class="comment-info"><span class="comment-age">(25 Apr '16, 14:13)</span> <span class="comment-user userinfo">Aleksander</span></div></div><span id="51950"></span><div id="comment-51950" class="comment"><div id="post-51950-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-51950-info" class="comment-info"><span class="comment-age">(26 Apr '16, 00:56)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-51878" class="comment-tools"></div><div class="clear"></div><div id="comment-51878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

