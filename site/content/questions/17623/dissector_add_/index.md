+++
type = "question"
title = "dissector_add_"
description = '''I want to base the handoff call off the Data packet instead of using the below port exception. Thoughts?  void proto_reg_handoff_bppcp(void) {  dissector_handle_t bppcp_handle;  data_handle = find_dissector(&quot;data&quot;);  bppcp_handle = create_dissector_handle(dissect_bppcp, proto_bppcp);  dissector_add_...'''
date = "2013-01-11T13:04:00Z"
lastmod = "2013-01-11T13:15:00Z"
weight = 17623
keywords = [ "port", "handoff", "no" ]
aliases = [ "/questions/17623" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dissector\_add\_](/questions/17623/dissector_add_)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17623-score" class="post-score" title="current number of votes">0</div><span id="post-17623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to base the handoff call off the Data packet instead of using the below port exception.</p><p>Thoughts?<br />
</p><p>void proto_reg_handoff_bppcp(void) { dissector_handle_t bppcp_handle;</p><pre><code>    data_handle = find_dissector(&quot;data&quot;);
    bppcp_handle = create_dissector_handle(dissect_bppcp, proto_bppcp);
    dissector_add_uint(&quot;tcp.port&quot;, global_bppcp_port, bppcp_handle);</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-handoff" rel="tag" title="see questions tagged &#39;handoff&#39;">handoff</span> <span class="post-tag tag-link-no" rel="tag" title="see questions tagged &#39;no&#39;">no</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '13, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/1f51b148d3f1f063aa95114ceea3b70f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jballard1979&#39;s gravatar image" /><p><span>jballard1979</span><br />
<span class="score" title="20 reputation points">20</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jballard1979 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-17623" class="comments-container"></div><div id="comment-tools-17623" class="comment-tools"></div><div class="clear"></div><div id="comment-17623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17624"></span>

<div id="answer-container-17624" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17624-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17624-score" class="post-score" title="current number of votes">0</div><span id="post-17624-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>nevermind, I'll use the below! :)</p><p>heur_dissector_add</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '13, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/1f51b148d3f1f063aa95114ceea3b70f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jballard1979&#39;s gravatar image" /><p><span>jballard1979</span><br />
<span class="score" title="20 reputation points">20</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jballard1979 has no accepted answers">0%</span></p></div></div><div id="comments-container-17624" class="comments-container"></div><div id="comment-tools-17624" class="comment-tools"></div><div class="clear"></div><div id="comment-17624-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

