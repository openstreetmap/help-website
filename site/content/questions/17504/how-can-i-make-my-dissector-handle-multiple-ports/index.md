+++
type = "question"
title = "How can I make my dissector handle multiple ports?"
description = '''My Dissector will use multiple ports across our network. How can I define them? packet-bppcp.c dissector_add_uint(&quot;tcp.port&quot;, BPPCP_PORT, bppcp_handle);  packet-bppcp.h #define BPPCP_PORT 26810 /* 4006 4181 4192 45634 7003 9010 9020 */ '''
date = "2013-01-07T09:44:00Z"
lastmod = "2013-01-07T11:32:00Z"
weight = 17504
keywords = [ "multi_ports" ]
aliases = [ "/questions/17504" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I make my dissector handle multiple ports?](/questions/17504/how-can-i-make-my-dissector-handle-multiple-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17504-score" class="post-score" title="current number of votes">0</div><span id="post-17504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My Dissector will use multiple ports across our network. How can I define them?</p><pre><code>packet-bppcp.c
dissector_add_uint(&quot;tcp.port&quot;, BPPCP_PORT, bppcp_handle);

packet-bppcp.h
#define BPPCP_PORT  26810 /* 4006 4181 4192 45634 7003 9010 9020 */</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-multi_ports" rel="tag" title="see questions tagged &#39;multi_ports&#39;">multi_ports</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '13, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/1f51b148d3f1f063aa95114ceea3b70f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jballard1979&#39;s gravatar image" /><p><span>jballard1979</span><br />
<span class="score" title="20 reputation points">20</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jballard1979 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jan '13, 11:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-17504" class="comments-container"></div><div id="comment-tools-17504" class="comment-tools"></div><div class="clear"></div><div id="comment-17504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17505"></span>

<div id="answer-container-17505" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17505-score" class="post-score" title="current number of votes">2</div><span id="post-17505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jballard1979 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the HTTP dissector for an example:</p><pre><code>#define TCP_DEFAULT_RANGE &quot;80,3128,3132,5985,8080,8088,11371,1900,2869,2710&quot;
[...]
range_convert_str(&amp;global_http_tcp_range, TCP_DEFAULT_RANGE, 65535);
http_tcp_range = range_empty();
prefs_register_range_preference(http_module, &quot;tcp.port&quot;, &quot;TCP Ports&quot;,
                &quot;TCP Ports range&quot;,
                &amp;global_http_tcp_range, 65535);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '13, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17505" class="comments-container"><span id="17516"></span><div id="comment-17516" class="comment"><div id="post-17516-score" class="comment-score"></div><div class="comment-text"><p>Implemented using example above.</p><p>Thanks boss.</p></div><div id="comment-17516-info" class="comment-info"><span class="comment-age">(07 Jan '13, 10:57)</span> <span class="comment-user userinfo">jballard1979</span></div></div><span id="17525"></span><div id="comment-17525" class="comment"><div id="post-17525-score" class="comment-score"></div><div class="comment-text"><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-17525-info" class="comment-info"><span class="comment-age">(07 Jan '13, 11:32)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17505" class="comment-tools"></div><div class="clear"></div><div id="comment-17505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

