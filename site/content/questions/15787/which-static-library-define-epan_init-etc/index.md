+++
type = "question"
title = "which static library define epan_init, etc?"
description = '''which wireshark static library on linux define   epan_init, proto_item_fill_label, g_sprintf, g_assertion_message_expr, register_all_protocol_handoffs, register_all_protocols, frame_data_set_before_dissect, g_malloc0  thank you very much.'''
date = "2012-11-10T00:09:00Z"
lastmod = "2012-11-10T17:19:00Z"
weight = 15787
keywords = [ "epan_init" ]
aliases = [ "/questions/15787" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [which static library define epan\_init, etc?](/questions/15787/which-static-library-define-epan_init-etc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15787-score" class="post-score" title="current number of votes">0</div><span id="post-15787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>which wireshark static library on linux define</p><ul><li>epan_init,</li><li>proto_item_fill_label,</li><li>g_sprintf,</li><li>g_assertion_message_expr,</li><li>register_all_protocol_handoffs,</li><li>register_all_protocols,</li><li>frame_data_set_before_dissect,</li><li>g_malloc0</li></ul><p>thank you very much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-epan_init" rel="tag" title="see questions tagged &#39;epan_init&#39;">epan_init</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '12, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p><span>ylda_ljm0620</span><br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Nov '12, 06:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-15787" class="comments-container"></div><div id="comment-tools-15787" class="comment-tools"></div><div class="clear"></div><div id="comment-15787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15790"></span>

<div id="answer-container-15790" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15790-score" class="post-score" title="current number of votes">1</div><span id="post-15790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Whether a library is static or dynamic depends on how it's built, not what it defines.</p><p>The libraries that define those functions are:</p><ul><li><code>epan_init</code> - libwireshark</li><li><code>proto_item_fill_label</code> - libwireshark</li><li><code>g_sprintf</code> - glib</li><li><code>g_assertion_message_expr</code> - glib</li><li><code>register_all_protocol_handoffs</code> - libwireshark</li><li><code>register_all_protocols</code> - libwireshark</li><li><code>frame_data_set_before_dissect</code> - libwireshark</li><li><code>g_malloc0</code> - glib</li></ul><p>Whether the machine you're using has static versions of either of those libraries depends on how the libraries were built and, if GLib and Wireshark are provided as packages for your system, whether static versions of the libraries are provided in any of those packages and, if so, whether they're provided in a separate package and whether that package is installed on your machine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '12, 17:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15790" class="comments-container"></div><div id="comment-tools-15790" class="comment-tools"></div><div class="clear"></div><div id="comment-15790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

