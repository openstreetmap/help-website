+++
type = "question"
title = "GLib-CRITICAL segmentation fault with wireshark"
description = '''After I made some changes to my plugin-dissector code (I added somme Libgcrypt related code), I get a segmentation fault. I got it even before Wireshark executes any of the libgcrypt code that I added. The error says: (lt-wireshark:4944): GLib-CRITICAL : g_hash_table_lookup: assertion `hash_table !=...'''
date = "2015-02-26T19:50:00Z"
lastmod = "2015-02-26T23:23:00Z"
weight = 40112
keywords = [ "glib", "fault", "segmentation", "wireshark" ]
aliases = [ "/questions/40112" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [GLib-CRITICAL segmentation fault with wireshark](/questions/40112/glib-critical-segmentation-fault-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40112-score" class="post-score" title="current number of votes">0</div><span id="post-40112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After I made some changes to my plugin-dissector code (I added somme Libgcrypt related code), I get a segmentation fault. I got it even before Wireshark executes any of the libgcrypt code that I added. The error says: <strong>(lt-wireshark:4944): GLib-CRITICAL</strong> : g_hash_table_lookup: assertion `hash_table != NULL' failed Segmentation fault (core dumped)**</p><p>I'd like to know What went wrong? or How can I figure out what went wrong in this case? or what could such error mean?</p><p>Thanks. Flora</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-glib" rel="tag" title="see questions tagged &#39;glib&#39;">glib</span> <span class="post-tag tag-link-fault" rel="tag" title="see questions tagged &#39;fault&#39;">fault</span> <span class="post-tag tag-link-segmentation" rel="tag" title="see questions tagged &#39;segmentation&#39;">segmentation</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '15, 19:50</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-40112" class="comments-container"></div><div id="comment-tools-40112" class="comment-tools"></div><div class="clear"></div><div id="comment-40112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40113"></span>

<div id="answer-container-40113" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40113-score" class="post-score" title="current number of votes">1</div><span id="post-40113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This error means that you are trying to do a lookup on a NULL hash table pointer (so the hash table has not been initialized before the lookup). Ensure to create the hash table before.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '15, 23:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-40113" class="comments-container"></div><div id="comment-tools-40113" class="comment-tools"></div><div class="clear"></div><div id="comment-40113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

