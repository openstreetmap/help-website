+++
type = "question"
title = "How to obtain informations from a dissector inside a sub-dissector ?"
description = '''I&#x27;m writting a dissector for the modludp64 protocol. It&#x27;s work, this is cool and I release it in few days. But before I want to add some features. To distinguish messages, I need to know if the destination ip address is unicast or multicast, but I don&#x27;t know how to retreive this informations. Someon...'''
date = "2011-03-20T14:15:00Z"
lastmod = "2011-03-21T06:11:00Z"
weight = 2953
keywords = [ "development", "dissector", "sub-dissector" ]
aliases = [ "/questions/2953" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to obtain informations from a dissector inside a sub-dissector ?](/questions/2953/how-to-obtain-informations-from-a-dissector-inside-a-sub-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2953-score" class="post-score" title="current number of votes">0</div><span id="post-2953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writting a dissector for the modludp64 protocol. It's work, this is cool and I release it in few days. But before I want to add some features. To distinguish messages, I need to know if the destination ip address is unicast or multicast, but I don't know how to retreive this informations.</p><p>Someone can help me.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-sub-dissector" rel="tag" title="see questions tagged &#39;sub-dissector&#39;">sub-dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '11, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/a8e5c9438725b82bdee34d32a2068b80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chronidev&#39;s gravatar image" /><p><span>chronidev</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chronidev has no accepted answers">0%</span></p></div></div><div id="comments-container-2953" class="comments-container"></div><div id="comment-tools-2953" class="comment-tools"></div><div class="clear"></div><div id="comment-2953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2965"></span>

<div id="answer-container-2965" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2965-score" class="post-score" title="current number of votes">0</div><span id="post-2965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This should result in TRUE for multicast addresses (untested YMMV).</p><p><code>((pinfo-&gt;net_dst.type == AT_IPv4) &amp;&amp; (((*(guint8 *)(pinfo-&gt;net_dst.data) &amp; 0xF0) == 0xE0)) || ((pinfo-&gt;net_dst.type == AT_IPv6) &amp;&amp; ((*(guint8 *)(pinfo-&gt;net_dst.data) == 0xFF))))</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2965" class="comments-container"></div><div id="comment-tools-2965" class="comment-tools"></div><div class="clear"></div><div id="comment-2965-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

