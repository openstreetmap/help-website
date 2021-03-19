+++
type = "question"
title = "Help: wireshark crashes after adding preference code to my dissector"
description = '''I wanted to add some options in the preference window for my dissector. This is the code I have added to the &quot;proto_register&quot; function: module_t *dan_lte_sdk_module;  proto_dan_lte_sdk = proto_register_protocol (&quot;DAN LTE SDK Protocol&quot;, &quot;Dan LTE SDK&quot;, &quot;dan_lte_sdk&quot;);  register_init_routine(dan_defrag...'''
date = "2011-01-26T01:19:00Z"
lastmod = "2011-01-26T03:53:00Z"
weight = 1939
keywords = [ "dissector" ]
aliases = [ "/questions/1939" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Help: wireshark crashes after adding preference code to my dissector](/questions/1939/help-wireshark-crashes-after-adding-preference-code-to-my-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1939-score" class="post-score" title="current number of votes">0</div><span id="post-1939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to add some options in the preference window for my dissector. This is the code I have added to the "proto_register" function:</p><pre><code>module_t *dan_lte_sdk_module;

proto_dan_lte_sdk = proto_register_protocol (&quot;DAN LTE SDK Protocol&quot;, &quot;Dan LTE SDK&quot;, &quot;dan_lte_sdk&quot;);

register_init_routine(dan_defragment_init);

proto_register_field_array (proto_dan_lte_sdk, hf, array_length (hf));
proto_register_subtree_array (ett, array_length (ett));
register_dissector(&quot;dan_lte_sdk&quot;, dissect_dan_lte_sdk, proto_dan_lte_sdk);

dan_lte_sdk_module = prefs_register_protocol(proto_dan_lte_sdk, NULL);

prefs_register_bool_preference(dan_lte_sdk_module, &quot;Dissect_MAC_Payload&quot;,
                               &quot;Dissect MAC Layer from Data Payload&quot;,
                               &quot;In Uplink and Downlink data packets, dissect MAC heaser layer &quot;
                               &quot;Disabling MAC dissection will disable RLC dissection automaticly&quot;,
                               &amp;global_dan_lte_sdk_dissect_MAC);

prefs_register_bool_preference(dan_lte_sdk_module, &quot;Dissect_RLC_Payload&quot;,
                               &quot;Dissect RLC Layer from Data Payload&quot;,
                               &quot;In Uplink and Downlink data packets, dissect RLC heaser layer &quot;,
                               &amp;global_dan_lte_sdk_dissect_RLC);</code></pre><p>It works fine until I add those two (even one of them) "prefs_register_bool_preference" functions. What did I do wrong?</p><p>I get a "Runtime Error!" for wireshark.exe Removing those function fixes it back.</p><p>Thanks</p><p>Yosi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '11, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/8ab0d645ffb3d50a34f8ef582bb92061?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yosi&#39;s gravatar image" /><p><span>Yosi</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yosi has no accepted answers">0%</span></p></div></div><div id="comments-container-1939" class="comments-container"></div><div id="comment-tools-1939" class="comment-tools"></div><div class="clear"></div><div id="comment-1939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1940"></span>

<div id="answer-container-1940" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1940-score" class="post-score" title="current number of votes">1</div><span id="post-1940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Yosi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code> * Make sure that only lower-case ASCII letters, numbers,
 * underscores, and dots appear in the preference name.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '11, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1940" class="comments-container"></div><div id="comment-tools-1940" class="comment-tools"></div><div class="clear"></div><div id="comment-1940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

