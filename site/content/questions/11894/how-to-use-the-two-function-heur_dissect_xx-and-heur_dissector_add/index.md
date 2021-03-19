+++
type = "question"
title = "how to use the two function: heur_dissect_XX() and heur_dissector_add()？"
description = '''The two function just in the packet-umts-fp.c. The protocol is &quot;fp&quot;.but i don&#x27;t know how to use it. When I select a packet,then dissect as,there is no &quot;fp&quot; to select.why? Hope the master give advice or comments please!'''
date = "2012-06-14T01:06:00Z"
lastmod = "2012-06-14T05:17:00Z"
weight = 11894
keywords = [ "fp", "heur-dissect", "umts-fp" ]
aliases = [ "/questions/11894" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to use the two function: heur\_dissect\_XX() and heur\_dissector\_add()？](/questions/11894/how-to-use-the-two-function-heur_dissect_xx-and-heur_dissector_add)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11894-score" class="post-score" title="current number of votes">0</div><span id="post-11894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The two function just in the packet-umts-fp.c. The protocol is "fp".but i don't know how to use it. When I select a packet,then dissect as,there is no "fp" to select.why?</p><p>Hope the master give advice or comments please!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fp" rel="tag" title="see questions tagged &#39;fp&#39;">fp</span> <span class="post-tag tag-link-heur-dissect" rel="tag" title="see questions tagged &#39;heur-dissect&#39;">heur-dissect</span> <span class="post-tag tag-link-umts-fp" rel="tag" title="see questions tagged &#39;umts-fp&#39;">umts-fp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '12, 01:06</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-11894" class="comments-container"></div><div id="comment-tools-11894" class="comment-tools"></div><div class="clear"></div><div id="comment-11894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11897"></span>

<div id="answer-container-11897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11897-score" class="post-score" title="current number of votes">0</div><span id="post-11897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, Look in doc/README.heuristic to get some information on heuristics. if you want to register and UDP dissector to be able to use "decode as" use dissector_add_handle("udp.port", fp_handle); In this particular case that will probably do you no good as you need the fp_info struct (packet-umts_fp.h filled in and stored in per_packet_data for the FP dissector to be able to dissect the packet. It might be possible to designa heuristic to find FP packets making use of the CRC to at least dissect control signals, from there it might be possible to do more. regards Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '12, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-11897" class="comments-container"></div><div id="comment-tools-11897" class="comment-tools"></div><div class="clear"></div><div id="comment-11897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

