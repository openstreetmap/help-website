+++
type = "question"
title = "Wireshark UDP Stream not readable"
description = '''Hello everybody. I captured this stream from the software GrandMA2 onPc. It is the MA-Net2. What do I have to do to make everything readable, so that I know how the protocol works? Thank you very much! http://www.file-upload.net/download-11214052/mystream.pcapng.html LER'''
date = "2016-01-15T10:46:00Z"
lastmod = "2016-01-19T07:41:00Z"
weight = 49258
keywords = [ "decode", "udp", "stream", "encoder" ]
aliases = [ "/questions/49258" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark UDP Stream not readable](/questions/49258/wireshark-udp-stream-not-readable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49258-score" class="post-score" title="current number of votes">0</div><span id="post-49258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody.</p><p>I captured this stream from the software GrandMA2 onPc. It is the MA-Net2. What do I have to do to make everything readable, so that I know how the protocol works?</p><p>Thank you very much!</p><p><a href="http://www.file-upload.net/download-11214052/mystream.pcapng.html">http://www.file-upload.net/download-11214052/mystream.pcapng.html</a></p><p>LER</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-encoder" rel="tag" title="see questions tagged &#39;encoder&#39;">encoder</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '16, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/6b2e83814eda1d2a368069a1d4f1e837?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lreu&#39;s gravatar image" /><p><span>lreu</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lreu has no accepted answers">0%</span></p></div></div><div id="comments-container-49258" class="comments-container"></div><div id="comment-tools-49258" class="comment-tools"></div><div class="clear"></div><div id="comment-49258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49259"></span>

<div id="answer-container-49259" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49259-score" class="post-score" title="current number of votes">0</div><span id="post-49259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFAICT, someone would need to build a dissector for the protocol. To do that, one would either need documentation from the protocol manufacture or manually reverse engineer the protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '16, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/d2ddaa4ccb4e58c470c0eb3bc39005e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DJX&#39;s gravatar image" /><p><span>DJX</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DJX has no accepted answers">0%</span></p></div></div><div id="comments-container-49259" class="comments-container"><span id="49261"></span><div id="comment-49261" class="comment"><div id="post-49261-score" class="comment-score"></div><div class="comment-text"><p>Yeah, but there isn't any documentation about that specific protocol :(</p></div><div id="comment-49261-info" class="comment-info"><span class="comment-age">(15 Jan '16, 11:51)</span> <span class="comment-user userinfo">lreu</span></div></div><span id="49271"></span><div id="comment-49271" class="comment"><div id="post-49271-score" class="comment-score"></div><div class="comment-text"><p>Welcome to the world of closed source protocols. :)</p></div><div id="comment-49271-info" class="comment-info"><span class="comment-age">(16 Jan '16, 05:51)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="49375"></span><div id="comment-49375" class="comment"><div id="post-49375-score" class="comment-score"></div><div class="comment-text"><p>Please ask the vendor (malighting), they might have a dissector for (internal) troubleshooting of their own protocol which is just not available freely.</p></div><div id="comment-49375-info" class="comment-info"><span class="comment-age">(19 Jan '16, 07:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-49259" class="comment-tools"></div><div class="clear"></div><div id="comment-49259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

