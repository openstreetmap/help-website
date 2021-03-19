+++
type = "question"
title = "Heuristic dissector works with 1.6.x but not with 1.8.x"
description = '''I&#x27;ve developed a very simple heuristic dissector for a proprietary protocol using Wireshark 1.6.8. It works flawlessly and the heuristics identify the payload on top of TCP. The same sources compile fine with Wireshark 1.8.4 but Wireshark appears to be unable to identify the payload. The frames are ...'''
date = "2012-12-17T07:02:00Z"
lastmod = "2012-12-18T01:10:00Z"
weight = 16973
keywords = [ "heuristic", "dissector", "wireshark" ]
aliases = [ "/questions/16973" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Heuristic dissector works with 1.6.x but not with 1.8.x](/questions/16973/heuristic-dissector-works-with-16x-but-not-with-18x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16973-score" class="post-score" title="current number of votes">0</div><span id="post-16973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've developed a very simple heuristic dissector for a proprietary protocol using Wireshark 1.6.8. It works flawlessly and the heuristics identify the payload on top of TCP.</p><p>The same sources compile fine with Wireshark 1.8.4 but Wireshark appears to be unable to identify the payload. The frames are identified if and only if I force it with 'Dissect as..'.</p><p>I've added some <em>printf</em> to the dissector function and they never show up unless I use "Dissect as...". I've also checked that "Analyze / Enabled Protocols" has my protocol enabled.</p><p>What could be the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-heuristic" rel="tag" title="see questions tagged &#39;heuristic&#39;">heuristic</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/6a068406cf7a70fd69b6376a75dd176a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rafa&#39;s gravatar image" /><p><span>Rafa</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rafa has no accepted answers">0%</span></p></div></div><div id="comments-container-16973" class="comments-container"></div><div id="comment-tools-16973" class="comment-tools"></div><div class="clear"></div><div id="comment-16973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16974"></span>

<div id="answer-container-16974" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16974-score" class="post-score" title="current number of votes">2</div><span id="post-16974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rafa has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What are the frames in question actually identified as ?</p><p>A different protocol (which is also identified heuristically) ?</p><p>If so, does disabling that protocol help ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '12, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-16974" class="comments-container"><span id="16975"></span><div id="comment-16975" class="comment"><div id="post-16975-score" class="comment-score"></div><div class="comment-text"><p>They are identified as TCP and I have the heuristic dissector chained to TCP: heur_dissector_add("tcp", dissect_blah_heur, proto_blah);</p></div><div id="comment-16975-info" class="comment-info"><span class="comment-age">(17 Dec '12, 07:22)</span> <span class="comment-user userinfo">Rafa</span></div></div><span id="17006"></span><div id="comment-17006" class="comment"><div id="post-17006-score" class="comment-score">2</div><div class="comment-text"><p>In theory, heuristic dissectors chained to TCP are called in turn until one indicates that it can dissect the data.</p><p>If your dissector is not being called, then either some other heuristic dissector has grabbed the frame or the frame has been grabbed by a dissector based on the TCP port being used.</p><p>Since "Decode As" works, it seems to me that another dissector must have grabbed the frame.</p><p>In either case I would have expected that that dissector would show as being over TCP in the details pane.</p><p>What happens if you set the "Try heuristic sub-dissectors first" TCP preference ?</p></div><div id="comment-17006-info" class="comment-info"><span class="comment-age">(17 Dec '12, 19:02)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="17013"></span><div id="comment-17013" class="comment"><div id="post-17013-score" class="comment-score"></div><div class="comment-text"><p>Thank you, that was the problem. That preference was set in Wireshark 1.6 but not in 1.8 although this is the first time I have played with the TCP preferences.</p></div><div id="comment-17013-info" class="comment-info"><span class="comment-age">(18 Dec '12, 01:10)</span> <span class="comment-user userinfo">Rafa</span></div></div></div><div id="comment-tools-16974" class="comment-tools"></div><div class="clear"></div><div id="comment-16974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

