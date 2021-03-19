+++
type = "question"
title = "Is there any better way to dump data? (http)"
description = '''I&#x27;m using tshark to get html pages out of a capture file, and checking how many of those contain a specific element. Currently I&#x27;m using the following params: tshark.exe -r test.pcap -o &quot;tcp.desegment_tcp_streams:TRUE&quot; -R &quot;tcp.stream==13 and http&quot; -T pdml &amp;gt; test.session13.pdml  and get the html d...'''
date = "2010-12-21T05:56:00Z"
lastmod = "2010-12-22T02:47:00Z"
weight = 1431
keywords = [ "http", "data", "tshark" ]
aliases = [ "/questions/1431" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there any better way to dump data? (http)](/questions/1431/is-there-any-better-way-to-dump-data-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1431-score" class="post-score" title="current number of votes">0</div><span id="post-1431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using tshark to get html pages out of a capture file, and checking how many of those contain a specific element. Currently I'm using the following params:</p><pre><code>tshark.exe -r test.pcap -o &quot;tcp.desegment_tcp_streams:TRUE&quot;  -R &quot;tcp.stream==13 and http&quot; -T pdml &gt; test.session13.pdml</code></pre><p>and get the html documents themselves inside a <code>data-text-lines</code> element spread over many <code>field</code> elements in the output pdml. Which means that I need to concatenate the data in those elements to get the whole html back together. That's not a great problem, I just wonder, is there a better way to do so? Meaning, letting tshark itself output the complete html?</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '10, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/9b7b5e633f7836289c2fc6c3934bffaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r0u1i&#39;s gravatar image" /><p><span>r0u1i</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r0u1i has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Dec '10, 06:14</strong> </span></p></div></div><div id="comments-container-1431" class="comments-container"></div><div id="comment-tools-1431" class="comment-tools"></div><div class="clear"></div><div id="comment-1431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1432"></span>

<div id="answer-container-1432" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1432-score" class="post-score" title="current number of votes">1</div><span id="post-1432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="r0u1i has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about:</p><pre><code>tshark.exe -r test.pcap -o &quot;tcp.desegment_tcp_streams:TRUE&quot; -R &quot;http contains &lt;string&gt;&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '10, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1432" class="comments-container"><span id="1433"></span><div id="comment-1433" class="comment"><div id="post-1433-score" class="comment-score"></div><div class="comment-text"><p>It's more complicated than that, it's really a validation rule (the location of javascript references). So I need to get the plain HTMLs out.</p></div><div id="comment-1433-info" class="comment-info"><span class="comment-age">(21 Dec '10, 06:14)</span> <span class="comment-user userinfo">r0u1i</span></div></div><span id="1434"></span><div id="comment-1434" class="comment"><div id="post-1434-score" class="comment-score"></div><div class="comment-text"><p>Then you might want to take a look at tcpflow</p><p>(http://www.circlemud.org/~jelson/software/tcpflow/)</p></div><div id="comment-1434-info" class="comment-info"><span class="comment-age">(21 Dec '10, 06:18)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="1450"></span><div id="comment-1450" class="comment"><div id="post-1450-score" class="comment-score"></div><div class="comment-text"><p>I'm accepting it as 'NO, there's no better way in tshark' :)</p></div><div id="comment-1450-info" class="comment-info"><span class="comment-age">(22 Dec '10, 02:47)</span> <span class="comment-user userinfo">r0u1i</span></div></div></div><div id="comment-tools-1432" class="comment-tools"></div><div class="clear"></div><div id="comment-1432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

