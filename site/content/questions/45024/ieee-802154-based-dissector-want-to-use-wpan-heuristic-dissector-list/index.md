+++
type = "question"
title = "IEEE 802.15.4-based dissector, want to use wpan heuristic dissector list"
description = '''Hi, I am building a dissector that is based on the IEEE 802.15.4 dissector. I want it to throw data to the same sub-dissectors that the original dissector does, but since those sub-dissectors do not register into my heuristic table, I am not sure how to do that. I am using 1.12.6 and I see that the ...'''
date = "2015-08-12T15:17:00Z"
lastmod = "2015-08-12T15:17:00Z"
weight = 45024
keywords = [ "802.15.4" ]
aliases = [ "/questions/45024" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IEEE 802.15.4-based dissector, want to use wpan heuristic dissector list](/questions/45024/ieee-802154-based-dissector-want-to-use-wpan-heuristic-dissector-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45024-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am building a dissector that is based on the IEEE 802.15.4 dissector. I want it to throw data to the same sub-dissectors that the original dissector does, but since those sub-dissectors do not register into my heuristic table, I am not sure how to do that. I am using 1.12.6 and I see that the method find_heur_dissector_list is implemented in packet.c, but not packet.h, and I don't want to add and recompile the dll because then I think it won't work with the stable release anymore, because libwireshark.dll will be different.</p><p>Any ideas on how I could get it to throw to one of the entries in the wpan heuristic table?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">802.15.4</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/8f99f97ead483c8f43cf63e9b3d17f7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="j-demars&#39;s gravatar image" /><p>j-demars<br />
<span class="score" title="41 reputation points">41</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="j-demars has no accepted answers">0%</span></p></div></div><div id="comments-container-45024" class="comments-container"><span id="45046"></span><div id="comment-45046" class="comment"><div id="post-45046-score" class="comment-score"></div><div class="comment-text"><p>Hi, It seems to exist in the development tree epan/packet.h:WS_DLL_PUBLIC heur_dissector_list_t find_heur_dissector_list(const char *name);</p><p>so perhaps you could use one of the development releases.</p></div><div id="comment-45046-info" class="comment-info"><span class="comment-age">(13 Aug '15, 01:37)</span> Anders ♦</div></div></div><div id="comment-tools-45024" class="comment-tools"></div><div class="clear"></div><div id="comment-45024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

