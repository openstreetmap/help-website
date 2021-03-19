+++
type = "question"
title = "Display all streams with a matching URI"
description = '''Hi, I am trying to find a way to display all HTTP requests AND the relevant responses that match a specific URI, say /images/*, from a capture file. I appreciate that I can match the request packet with http.request.uri, but is it possible to also select the packets related to the responses? Regards'''
date = "2010-10-27T01:47:00Z"
lastmod = "2010-11-04T04:45:00Z"
weight = 701
keywords = [ "request", "http", "response", "uri" ]
aliases = [ "/questions/701" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display all streams with a matching URI](/questions/701/display-all-streams-with-a-matching-uri)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-701-score" class="post-score" title="current number of votes">0</div><span id="post-701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to find a way to display all HTTP requests AND the relevant responses that match a specific URI, say /images/*, from a capture file.</p><p>I appreciate that I can match the request packet with http.request.uri, but is it possible to also select the packets related to the responses?</p><p>Regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-request" rel="tag" title="see questions tagged &#39;request&#39;">request</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span> <span class="post-tag tag-link-uri" rel="tag" title="see questions tagged &#39;uri&#39;">uri</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '10, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/98e0bec6d3458b20a073ba107b54de9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rtector&#39;s gravatar image" /><p><span>rtector</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rtector has no accepted answers">0%</span></p></div></div><div id="comments-container-701" class="comments-container"></div><div id="comment-tools-701" class="comment-tools"></div><div class="clear"></div><div id="comment-701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="734"></span>

<div id="answer-container-734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-734-score" class="post-score" title="current number of votes">1</div><span id="post-734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark by itself is not capable of doing that. You might be able to achieve this by using <a href="http://wiki.wireshark.org/Mate">MATE</a> or <a href="http://wiki.wireshark.org/Lua">LUA</a>.</p><p>However, there is another way, you can use tshark to create a new file that contains only the HTTP requests/responses that you are interested in. Have a look at <a href="http://www.cacetech.com/sharkfest.10/A-6_Blok%20HANDS-ON%20LAB%20-%20Using%20Wireshark%20Command%20Line%20Tools%20and%20Scripting.zip">the presentation I gave at Sharkfest</a> to see how this can be done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '10, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-734" class="comments-container"></div><div id="comment-tools-734" class="comment-tools"></div><div class="clear"></div><div id="comment-734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="716"></span>

<div id="answer-container-716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-716-score" class="post-score" title="current number of votes">0</div><span id="post-716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hmm... that is tough because you'd need to find a value in the response packet that ties it to the request packet - such as the name of the file embedded in the file that is being sent.</p><p>Since that isn't usually what happens, your best bet may be to find the packet of interest using the filter you defined and then right-click on the packet, Follow TCP Stream - you'll see all the requested URIs and responses for that connection though.</p><p>If you are trying to reassemble those requested URIs, try File &gt; Export &gt; Objects &gt; HTTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '10, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-716" class="comments-container"><span id="817"></span><div id="comment-817" class="comment"><div id="post-817-score" class="comment-score"></div><div class="comment-text"><p>Hi. Thank you for your answer but unfortunately the requests are pipelined (reverse proxy to server farm) and so the TCP stream is not much use. Additionally, I needed to do this on a large scale :)</p><p>Regards</p></div><div id="comment-817-info" class="comment-info"><span class="comment-age">(04 Nov '10, 04:45)</span> <span class="comment-user userinfo">rtector</span></div></div></div><div id="comment-tools-716" class="comment-tools"></div><div class="clear"></div><div id="comment-716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

