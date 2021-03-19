+++
type = "question"
title = "Can a heuristic dissector be applied to the entire TCP connection?"
description = '''I have a TCP session consisting of multiple packets. When I select any one of them and say &quot;Decode as...&quot; for my dissector, the dissector is properly applied to all packets in the entire session. I can write a heuristic detector for my dissector that will match only the first packet in the sequence....'''
date = "2013-05-23T07:53:00Z"
lastmod = "2013-05-23T08:34:00Z"
weight = 21412
keywords = [ "heuristic", "heur-dissect", "dissector", "heur_dissector_add" ]
aliases = [ "/questions/21412" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can a heuristic dissector be applied to the entire TCP connection?](/questions/21412/can-a-heuristic-dissector-be-applied-to-the-entire-tcp-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21412-score" class="post-score" title="current number of votes">0</div><span id="post-21412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a TCP session consisting of multiple packets. When I select any one of them and say "Decode as..." for my dissector, the dissector is properly applied to all packets in the entire session.</p><p>I can write a heuristic detector for my dissector that will match only the first packet in the sequence. However, when I do this, only the first packet is decoded by my dissector, and the remaining packets don't get dissected. Is it possible to tell the heuristic to apply the same dissector to all packets in the same TCP session?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-heuristic" rel="tag" title="see questions tagged &#39;heuristic&#39;">heuristic</span> <span class="post-tag tag-link-heur-dissect" rel="tag" title="see questions tagged &#39;heur-dissect&#39;">heur-dissect</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-heur_dissector_add" rel="tag" title="see questions tagged &#39;heur_dissector_add&#39;">heur_dissector_add</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '13, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/3dcd36f51cf45ba2e5cfd351cbcf7127?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LouisDx&#39;s gravatar image" /><p><span>LouisDx</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LouisDx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '13, 07:53</strong> </span></p></div></div><div id="comments-container-21412" class="comments-container"></div><div id="comment-tools-21412" class="comment-tools"></div><div class="clear"></div><div id="comment-21412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21413"></span>

<div id="answer-container-21413" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21413-score" class="post-score" title="current number of votes">1</div><span id="post-21413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LouisDx has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>once your heuristic kicks in you can set up a conversation and define your dissector as the conversation dissector. See conversation.h for the API and search the sources for examples (packet-sip, maybe).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '13, 08:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-21413" class="comments-container"><span id="21414"></span><div id="comment-21414" class="comment"><div id="post-21414-score" class="comment-score"></div><div class="comment-text"><p>That sounds promising -- thanks!</p></div><div id="comment-21414-info" class="comment-info"><span class="comment-age">(23 May '13, 08:06)</span> <span class="comment-user userinfo">LouisDx</span></div></div><span id="21417"></span><div id="comment-21417" class="comment"><div id="post-21417-score" class="comment-score"></div><div class="comment-text"><p>It worked, perfect!</p></div><div id="comment-21417-info" class="comment-info"><span class="comment-age">(23 May '13, 08:34)</span> <span class="comment-user userinfo">LouisDx</span></div></div></div><div id="comment-tools-21413" class="comment-tools"></div><div class="clear"></div><div id="comment-21413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

