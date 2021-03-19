+++
type = "question"
title = "Use sub-dissector in dissector"
description = '''Hi, I work on a dissector which decode a UDP based protocol. For each UDP packets I have a moludp64 packet which can contain one or more message blocks. Each message block is encode in another protocol, and I will implement these others protocols. What is the best way to make this happen? Is it my m...'''
date = "2011-03-22T03:23:00Z"
lastmod = "2011-03-22T16:33:00Z"
weight = 3014
keywords = [ "development", "dissector", "sub-dissector" ]
aliases = [ "/questions/3014" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use sub-dissector in dissector](/questions/3014/use-sub-dissector-in-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3014-score" class="post-score" title="current number of votes">0</div><span id="post-3014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I work on a dissector which decode a UDP based protocol. For each UDP packets I have a moludp64 packet which can contain one or more message blocks. Each message block is encode in another protocol, and I will implement these others protocols. What is the best way to make this happen? Is it my moludp64 dissector which must be calling the others dissectors?</p><p>Thanks for you help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-sub-dissector" rel="tag" title="see questions tagged &#39;sub-dissector&#39;">sub-dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '11, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/a8e5c9438725b82bdee34d32a2068b80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chronidev&#39;s gravatar image" /><p><span>chronidev</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chronidev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '11, 07:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-3014" class="comments-container"></div><div id="comment-tools-3014" class="comment-tools"></div><div class="clear"></div><div id="comment-3014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3020"></span>

<div id="answer-container-3020" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3020-score" class="post-score" title="current number of votes">0</div><span id="post-3020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="chronidev has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The best way is to create a subdissector table. This table can be indexed by a number or string, and can be used by you moludp64 dissector to call subdissectors. These subdissectors have to register themselves with this table, for a particular number or string in order to get called.</p><p>This is a basic de-multiplexing schema used at all (transport) protocol layers. For instance the same happens from the IP dissector to the UDP, TCP, SCTP dissector, based on protocol ID. And from TCP dissector to the HTTP, TELNET, FTP dissector, based on port number. Have a look at <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-udp.c">packet-udp.c</a> for example.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '11, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3020" class="comments-container"><span id="3034"></span><div id="comment-3034" class="comment"><div id="post-3034-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap, it's very interresting.</p></div><div id="comment-3034-info" class="comment-info"><span class="comment-age">(22 Mar '11, 16:33)</span> <span class="comment-user userinfo">chronidev</span></div></div></div><div id="comment-tools-3020" class="comment-tools"></div><div class="clear"></div><div id="comment-3020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

