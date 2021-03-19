+++
type = "question"
title = "Http Put request capture filter"
description = '''Hello I am looking to capture only PUT requests on my web server. I have seen a filter for GET requests and honestly haven&#x27;t been able to decipher it down so I can adjust it for my need. the filter i found was:  tcp[((tcp[12:1] &amp;amp; 0xf0) &amp;gt;&amp;gt; 2):4] = 0x47455420 and I tried to adjust it to:  tc...'''
date = "2015-08-05T14:06:00Z"
lastmod = "2015-08-10T08:04:00Z"
weight = 44888
keywords = [ "capture-filter" ]
aliases = [ "/questions/44888" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Http Put request capture filter](/questions/44888/http-put-request-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44888-score" class="post-score" title="current number of votes">0</div><span id="post-44888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I am looking to capture only PUT requests on my web server. I have seen a filter for GET requests and honestly haven't been able to decipher it down so I can adjust it for my need. the filter i found was: tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420</p><p>and I tried to adjust it to: tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x50555420</p><p>which didn't work because I believe the offset is different between GET and PUT requests. ANy help is appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '15, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/533b45923ef9621ff92e431027c913c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deesarmy&#39;s gravatar image" /><p><span>Deesarmy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deesarmy has no accepted answers">0%</span></p></div></div><div id="comments-container-44888" class="comments-container"><span id="44892"></span><div id="comment-44892" class="comment"><div id="post-44892-score" class="comment-score"></div><div class="comment-text"><p>What about this filter:<br />
http.request.method==PUT<br />
</p><p>Is this you need or do you need something more special?</p></div><div id="comment-44892-info" class="comment-info"><span class="comment-age">(05 Aug '15, 14:40)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="44893"></span><div id="comment-44893" class="comment"><div id="post-44893-score" class="comment-score"></div><div class="comment-text"><p>There is high levels of traffic on this server so I'm trying to build it into a capture filter. The method above would work for display filters which will work but the syntax for capture filtering is a bit different. I appreciate the reaponse though.</p></div><div id="comment-44893-info" class="comment-info"><span class="comment-age">(05 Aug '15, 14:59)</span> <span class="comment-user userinfo">Deesarmy</span></div></div><span id="44894"></span><div id="comment-44894" class="comment"><div id="post-44894-score" class="comment-score"></div><div class="comment-text"><p>Sorry did not read the word capture in your question.</p></div><div id="comment-44894-info" class="comment-info"><span class="comment-age">(05 Aug '15, 15:05)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-44888" class="comment-tools"></div><div class="clear"></div><div id="comment-44888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44944"></span>

<div id="answer-container-44944" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44944-score" class="post-score" title="current number of votes">1</div><span id="post-44944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a tool to generate capture filters based on strings.</p><blockquote><p><a href="https://www.wireshark.org/tools/string-cf.html">https://www.wireshark.org/tools/string-cf.html</a></p></blockquote><p><strong>PUT /test</strong> would translate to:</p><pre><code>tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x50555420 &amp;&amp; tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) + 4:4] = 0x2f746573 &amp;&amp; tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2) + 8:2] = 0x7420</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Aug '15, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-44944" class="comments-container"></div><div id="comment-tools-44944" class="comment-tools"></div><div class="clear"></div><div id="comment-44944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

