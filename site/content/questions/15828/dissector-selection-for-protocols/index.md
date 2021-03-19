+++
type = "question"
title = "Dissector selection for protocols"
description = '''Hello, community, I read the developer documentation about writing own plugins for Wireshark. However, there is still one thing I did not understand. Heuristic dissectors use some heuristics to see whether the packet in question is of the protocol they can dissect. But how do normal dissectors know?...'''
date = "2012-11-12T07:58:00Z"
lastmod = "2012-11-13T00:57:00Z"
weight = 15828
keywords = [ "selection", "header", "dissector", "determine" ]
aliases = [ "/questions/15828" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector selection for protocols](/questions/15828/dissector-selection-for-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15828-score" class="post-score" title="current number of votes">0</div><span id="post-15828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, community, I read the developer documentation about writing own plugins for Wireshark. However, there is still one thing I did not understand. Heuristic dissectors use some heuristics to see whether the packet in question is of the protocol they can dissect. But how do normal dissectors know? As far as I understood, they register on the special protocol header, but the exact procedure is not clear for me... Could anybody give a short explanation?</p><p>Best regards Ewgenij</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-header" rel="tag" title="see questions tagged &#39;header&#39;">header</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-determine" rel="tag" title="see questions tagged &#39;determine&#39;">determine</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '12, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/74ba4ba7a26d5efda01b6ae18bbe48e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewgenijkkg&#39;s gravatar image" /><p><span>Ewgenijkkg</span><br />
<span class="score" title="66 reputation points">66</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewgenijkkg has 3 accepted answers">60%</span></p></div></div><div id="comments-container-15828" class="comments-container"></div><div id="comment-tools-15828" class="comment-tools"></div><div class="clear"></div><div id="comment-15828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15829"></span>

<div id="answer-container-15829" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15829-score" class="post-score" title="current number of votes">1</div><span id="post-15829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ewgenijkkg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depends on how the protocol works but it is common that the lower protocol has a dissector table in which the next protocol can register, see "internals-&gt;dissector tables" The Ethernet dissector has a table for etherypes where dissectors can register. If there is a dissector for the ethertype in question that will be called. If it's IP the IP dissector will be called, IP has a protocol field so that is used as a dissector table. If the next protocol is UDP the UDP dissector has a udp.port table and will cal the dissector registered for that port etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-15829" class="comments-container"><span id="15848"></span><div id="comment-15848" class="comment"><div id="post-15848-score" class="comment-score"></div><div class="comment-text"><p>Ah, Ok, I understand. Thank you. And what about this "see "internals-&gt;dissector tables""? Where can I find it? :)</p></div><div id="comment-15848-info" class="comment-info"><span class="comment-age">(13 Nov '12, 00:24)</span> <span class="comment-user userinfo">Ewgenijkkg</span></div></div><span id="15849"></span><div id="comment-15849" class="comment"><div id="post-15849-score" class="comment-score"></div><div class="comment-text"><p>Main menubar, next to help</p></div><div id="comment-15849-info" class="comment-info"><span class="comment-age">(13 Nov '12, 00:27)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="15851"></span><div id="comment-15851" class="comment"><div id="post-15851-score" class="comment-score"></div><div class="comment-text"><p>OK, thank you a lot!</p></div><div id="comment-15851-info" class="comment-info"><span class="comment-age">(13 Nov '12, 00:57)</span> <span class="comment-user userinfo">Ewgenijkkg</span></div></div></div><div id="comment-tools-15829" class="comment-tools"></div><div class="clear"></div><div id="comment-15829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

