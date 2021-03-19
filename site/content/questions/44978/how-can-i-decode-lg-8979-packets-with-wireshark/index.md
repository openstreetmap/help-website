+++
type = "question"
title = "How can I decode LG 8979 packets with Wireshark?"
description = '''I have a capture which shows communication between a LG 8979 server and client pair operating via TCP. Can someone help me with decoding the packets as LG 8979 protocol? Now I see the capture with TCP and Telnet packets.'''
date = "2015-08-11T17:33:00Z"
lastmod = "2015-08-12T15:28:00Z"
weight = 44978
keywords = [ "protocol" ]
aliases = [ "/questions/44978" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I decode LG 8979 packets with Wireshark?](/questions/44978/how-can-i-decode-lg-8979-packets-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44978-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44978-score" class="post-score" title="current number of votes">0</div><span id="post-44978-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture which shows communication between a LG 8979 server and client pair operating via TCP. Can someone help me with decoding the packets as LG 8979 protocol? Now I see the capture with TCP and Telnet packets.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '15, 17:33</strong></p><img src="https://secure.gravatar.com/avatar/4ab73a34da850f82895af222e6cc85fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swetharvss&#39;s gravatar image" /><p><span>swetharvss</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swetharvss has no accepted answers">0%</span></p></div></div><div id="comments-container-44978" class="comments-container"></div><div id="comment-tools-44978" class="comment-tools"></div><div class="clear"></div><div id="comment-44978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45025"></span>

<div id="answer-container-45025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45025-score" class="post-score" title="current number of votes">0</div><span id="post-45025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First, you will need to run Wireshark 1.12 or later, as earlier versions don't support dissecting that protocol.</p><p>Then, you will need to change the "L&amp;G 8979 Protocol Port" preference for the L&amp;G 8979 protocol to the port number being used, or select one of the packets in the TCP connection and use "Decode As" to specify that it should be decoded as L&amp;G 8979.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Aug '15, 15:29</strong> </span></p></div></div><div id="comments-container-45025" class="comments-container"></div><div id="comment-tools-45025" class="comment-tools"></div><div class="clear"></div><div id="comment-45025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

