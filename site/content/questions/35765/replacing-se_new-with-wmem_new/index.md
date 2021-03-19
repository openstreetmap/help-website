+++
type = "question"
title = "Replacing se_new() with wmem_new()"
description = '''I have a dissector that was working fine in the 1.10 series and made use of se_new() and &amp;lt;epan emem.h=&quot;&quot;&amp;gt;. This didn&#x27;t build in 1.12.0, I switched all calls to wmem_new(wmem_file_scope(), ). It build fine but blows up when I try to capture things. Examples below. check_key = se_new(gint) -&amp;gt;...'''
date = "2014-08-26T10:58:00Z"
lastmod = "2014-08-26T13:37:00Z"
weight = 35765
keywords = [ "se_new", "wmem_new" ]
aliases = [ "/questions/35765" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Replacing se\_new() with wmem\_new()](/questions/35765/replacing-se_new-with-wmem_new)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35765-score" class="post-score" title="current number of votes">0</div><span id="post-35765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a dissector that was working fine in the 1.10 series and made use of se_new() and &lt;epan emem.h=""&gt;.</p><p>This didn't build in 1.12.0, I switched all calls to wmem_new(wmem_file_scope(), ). It build fine but blows up when I try to capture things. Examples below.</p><p>check_key = se_new(gint) -&gt; check_key = wmem_new(wmem_file_scope(), gint)</p><p>p_add_proto_data(pinfo-&gt;fd, proto_frame, 0, request_info) -&gt; p_add_proto_data(wmem_file_scope(), pinfo-&gt;fd, proto_frame, 0, request_info);</p><p>p_remove_proto_data(pinfo-&gt;fd, proto_frame, 0) -&gt; p_remove_proto_data(wmem_file_scope(), pinfo-&gt;fd, proto_frame, 0)</p><p>I can't seem to find any documentation on wmwm_new(). I also have no idea when to use wmem_file_scope() vs wmem_packet_scope().</p><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-se_new" rel="tag" title="see questions tagged &#39;se_new&#39;">se_new</span> <span class="post-tag tag-link-wmem_new" rel="tag" title="see questions tagged &#39;wmem_new&#39;">wmem_new</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '14, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p><span>brwiese</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-35765" class="comments-container"></div><div id="comment-tools-35765" class="comment-tools"></div><div class="clear"></div><div id="comment-35765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35770"></span>

<div id="answer-container-35770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35770-score" class="post-score" title="current number of votes">1</div><span id="post-35770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like you are passing <code>pinfo-&gt;fd</code> to <code>p_add_proto_data()</code> and <code>p_remove_proto_data()</code>, when you should be simply passing <code>pinfo</code>. See <code>epan/frame_data.h</code>.</p><p>Also, <code>wmem_new()</code> is a macro defined in <code>epan/wmem/wmem_core.h</code>.</p><p>For help with wmem and memory pools, start with <code>doc/README.wmem</code>, and then have a look at the other README files where wmem is used, as well as Wireshark dissectors for more examples on its usage.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35770" class="comments-container"><span id="35776"></span><div id="comment-35776" class="comment"><div id="post-35776-score" class="comment-score"></div><div class="comment-text"><p>Thank you, the pinfo-&gt;fd seems to be the problem.</p><p>Sincerely, Brian</p></div><div id="comment-35776-info" class="comment-info"><span class="comment-age">(26 Aug '14, 13:37)</span> <span class="comment-user userinfo">brwiese</span></div></div></div><div id="comment-tools-35770" class="comment-tools"></div><div class="clear"></div><div id="comment-35770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

