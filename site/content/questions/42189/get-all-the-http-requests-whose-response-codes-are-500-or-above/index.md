+++
type = "question"
title = "get all the HTTP requests whose response codes are 500 or above."
description = '''Would like to get all the HTTP requests whose response codes are 500 or above. I tried the following but it only gave me the responses. http.response.code &amp;gt;= 500  Any ideas? Thanks.'''
date = "2015-05-07T08:47:00Z"
lastmod = "2015-05-07T11:52:00Z"
weight = 42189
keywords = [ "wireshark" ]
aliases = [ "/questions/42189" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [get all the HTTP requests whose response codes are 500 or above.](/questions/42189/get-all-the-http-requests-whose-response-codes-are-500-or-above)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42189-score" class="post-score" title="current number of votes">0</div><span id="post-42189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Would like to get all the HTTP requests whose response codes are 500 or above. I tried the following but it only gave me the responses.</p><pre><code>http.response.code &gt;= 500</code></pre><p>Any ideas? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '15, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-42189" class="comments-container"></div><div id="comment-tools-42189" class="comment-tools"></div><div class="clear"></div><div id="comment-42189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42190"></span>

<div id="answer-container-42190" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42190-score" class="post-score" title="current number of votes">1</div><span id="post-42190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Normally, you can't filter packets (HTTP requests) based on an attribute of different packets (HTTP responses). However, in in the case of HTTP, if the response is present in the trace, Wireshark will put a field (http.response_in) in the request listing the packet that has the response. If the response is not present in the trace, Wireshark does not insert the http.response_in field. We can use the <em>Ignore Packet</em> function and the presence or absence of the http.response_in field to find the requests that we want.</p><p>To show only requests whose response codes are 500 or above:</p><ol><li>Apply a display filter of "http.response.code &lt; 500" These are the responses to the requests that we <em>don't want</em>.</li><li>Select "Edit &gt; Ignore All Displayed Packets"</li><li>Apply a display filter of "http.response_in"</li></ol><p>You will now see only the requests whose responses are present in the trace and that had a response code of 500 or higher. If you want to see both the requests and their responses, change the display filter in step 3 to "http.response_in || http.response.code".</p><p>Remember to select "Edit &gt; Unignore All Packets" when you're done. Wireshark treats ignored packets as if they are not present, and they will not match any display filters, nor will they be included in any graphs.</p><p>Variations of this technnique can be used with any request/response protocol where Wireshark calculates and provides links between the requests and responses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '15, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-42190" class="comments-container"><span id="42191"></span><div id="comment-42191" class="comment"><div id="post-42191-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@Jim Aragon</span> for this workaround! Wish there are stateful filtering rules that one can apply.</p></div><div id="comment-42191-info" class="comment-info"><span class="comment-age">(07 May '15, 11:52)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-42190" class="comment-tools"></div><div class="clear"></div><div id="comment-42190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

