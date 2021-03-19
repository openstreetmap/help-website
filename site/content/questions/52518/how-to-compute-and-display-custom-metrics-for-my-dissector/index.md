+++
type = "question"
title = "How to compute and display custom metrics for my dissector"
description = '''Hello, I am developping a custom dissector that shall compute the maximum delay between several pdu (e.g max delay between &quot;keep alive&quot; pdus). To provide the &quot;raw data&quot; I add this kind of code : foo_tap = register_tap(&quot;foo&quot;); (in proto_registerxxx) and  tap_queue_packet(foo_tap, pinfo, &amp;amp;foo_info...'''
date = "2016-05-13T09:05:00Z"
lastmod = "2016-07-19T09:36:00Z"
weight = 52518
keywords = [ "tap", "statistic" ]
aliases = [ "/questions/52518" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to compute and display custom metrics for my dissector](/questions/52518/how-to-compute-and-display-custom-metrics-for-my-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52518-score" class="post-score" title="current number of votes">0</div><span id="post-52518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am developping a custom dissector that shall compute the maximum delay between several pdu (e.g max delay between "keep alive" pdus).</p><p>To provide the "raw data" I add this kind of code :</p><p><code>foo_tap = register_tap("foo");</code> (in proto_registerxxx)</p><p>and</p><p><code>tap_queue_packet(foo_tap, pinfo, &amp;foo_info);</code> (after dissecting packet)</p><p>To use my dissector as the tap listener, I added this code :</p><p><code>register_tap_listener("foo", NULL, NULL, 0, foostat_reset, foostat_packet, foostat_draw);</code> (in proto reg handoff)</p><p>I also added the three functions <code>foostat_reset, foostat_packet and foostat_draw</code>.</p><p>===</p><p>Now I have a few questions (I did not managed to find any example in the README.xxx):</p><ol><li>How can I display my metrics ?</li><li>How can I keep all this code in the same dll ?</li><li>foostat_packet is called only when my display filter contains foo. If I do not have a foo filter, it is not called, even if I receive a foo pdu. Is this normal ?</li></ol><p>Thank you !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-statistic" rel="tag" title="see questions tagged &#39;statistic&#39;">statistic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '16, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/dfd728dcc858e4bb45f3ea8804fe9ba1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hpa&#39;s gravatar image" /><p><span>hpa</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hpa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 May '16, 09:08</strong> </span></p></div></div><div id="comments-container-52518" class="comments-container"></div><div id="comment-tools-52518" class="comment-tools"></div><div class="clear"></div><div id="comment-52518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54164"></span>

<div id="answer-container-54164" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54164-score" class="post-score" title="current number of votes">0</div><span id="post-54164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>"I did not managed to find any example in the README.xxx"</em></p><p>Have you read <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.tapping;h=56b7a4ba1c573fa1460fbd47272ff457da7c5df8;hb=HEAD"><code>doc/README.tapping</code></a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '16, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jul '16, 09:37</strong> </span></p></div></div><div id="comments-container-54164" class="comments-container"></div><div id="comment-tools-54164" class="comment-tools"></div><div class="clear"></div><div id="comment-54164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

