+++
type = "question"
title = "Dissector for PORT 80"
description = '''I need a dissector for tcp Port 80 and the first Data Byte like Hex 03. Only then. If is not is Hex03 the normaly dissector run. I use Wireshark Version 1.6.5 Thanks Ralf'''
date = "2012-03-25T23:33:00Z"
lastmod = "2012-03-26T09:38:00Z"
weight = 9754
keywords = [ "development", "dissector" ]
aliases = [ "/questions/9754" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector for PORT 80](/questions/9754/dissector-for-port-80)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9754-score" class="post-score" title="current number of votes">0</div><span id="post-9754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need a dissector for tcp Port 80 and the first Data Byte like Hex 03. Only then. If is not is Hex03 the normaly dissector run.</p><p>I use Wireshark Version 1.6.5</p><p>Thanks Ralf</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '12, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/7a210690d78d254d6109a7e335f135a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ralf%20Kruppa&#39;s gravatar image" /><p><span>Ralf Kruppa</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ralf Kruppa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>26 Mar '12, 05:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span></p></div></div><div id="comments-container-9754" class="comments-container"></div><div id="comment-tools-9754" class="comment-tools"></div><div class="clear"></div><div id="comment-9754-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9763"></span>

<div id="answer-container-9763" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9763-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9763-score" class="post-score" title="current number of votes">1</div><span id="post-9763-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Create your dissector as an heuristic dissector and check the TCP preference "Try heuristic sub-dissectors first"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '12, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-9763" class="comments-container"><span id="9764"></span><div id="comment-9764" class="comment"><div id="post-9764-score" class="comment-score"></div><div class="comment-text"><p>I use an LUA Datei und at the moment i use this:</p><hr /><p>-- Zuweisung der TCP-Tabelle http_table = DissectorTable.get("http.port") -- Zuweisung der zu überwachenden Ports http_table:add(0080,MY_proto)</p><hr /><p>So i get all Packts of Port 80. I neet only the Packets where the first Byte of the TCP Date ist HEX 03.</p><p>Thanks Ralf</p></div><div id="comment-9764-info" class="comment-info"><span class="comment-age">(26 Mar '12, 04:24)</span> <span class="comment-user userinfo">Ralf Kruppa</span></div></div><span id="9769"></span><div id="comment-9769" class="comment"><div id="post-9769-score" class="comment-score"></div><div class="comment-text"><p>So you dissector should check the first byte it is given, and if it is 0x03 process the data. If it isn't then return FALSE indicating that your dissector didn't handle the message.</p><p>See README.heuristic in the doc subdirectory of the source tree for all the essential details.</p></div><div id="comment-9769-info" class="comment-info"><span class="comment-age">(26 Mar '12, 09:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-9763" class="comment-tools"></div><div class="clear"></div><div id="comment-9763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

