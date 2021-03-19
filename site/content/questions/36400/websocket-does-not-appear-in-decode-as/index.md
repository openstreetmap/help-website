+++
type = "question"
title = "websocket does not appear in Decode As"
description = '''Hi, I&#x27;ve got a recording of web socket communication. I know for sure that web sockets are used, there is not HTTP CONNECT stage, however, it is done in a different way (which I yet have to find). Wireshark does not recognize the web socket packets as such, showing them as TCP only. When I try to ma...'''
date = "2014-09-17T05:09:00Z"
lastmod = "2014-09-17T11:57:00Z"
weight = 36400
keywords = [ "websockets" ]
aliases = [ "/questions/36400" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [websocket does not appear in Decode As](/questions/36400/websocket-does-not-appear-in-decode-as)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36400-score" class="post-score" title="current number of votes">0</div><span id="post-36400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've got a recording of web socket communication. I know for sure that web sockets are used, there is not HTTP CONNECT stage, however, it is done in a different way (which I yet have to find). Wireshark does not recognize the web socket packets as such, showing them as TCP only. When I try to manually force it to switch to websocket via Decode As - the websocket is just not there!I'm using the latestversion on both Windows and OS X. Please advise!</p><p>Moshe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-websockets" rel="tag" title="see questions tagged &#39;websockets&#39;">websockets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '14, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/260a26dfe025a1368a7c600a483e79a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moshek&#39;s gravatar image" /><p><span>moshek</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moshek has no accepted answers">0%</span></p></div></div><div id="comments-container-36400" class="comments-container"></div><div id="comment-tools-36400" class="comment-tools"></div><div class="clear"></div><div id="comment-36400-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36413"></span>

<div id="answer-container-36413" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36413-score" class="post-score" title="current number of votes">0</div><span id="post-36413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is simply not doable for now as the websocket dissector does not register itself as part of the Decode As list. Having it would require to modify the packet-websocket.c file and recompile.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '14, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-36413" class="comments-container"></div><div id="comment-tools-36413" class="comment-tools"></div><div class="clear"></div><div id="comment-36413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36414"></span>

<div id="answer-container-36414" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36414-score" class="post-score" title="current number of votes">0</div><span id="post-36414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I achieved my goal by registering my lua dissector that just forwarded the call to websocket. It kind of worked, but turned out that the traffic was not a valid web socket :-(</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '14, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/260a26dfe025a1368a7c600a483e79a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moshek&#39;s gravatar image" /><p><span>moshek</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moshek has no accepted answers">0%</span></p></div></div><div id="comments-container-36414" class="comments-container"></div><div id="comment-tools-36414" class="comment-tools"></div><div class="clear"></div><div id="comment-36414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

