+++
type = "question"
title = "Can we define multiple criteria for our dissector plugin to be called ?"
description = '''I know that we have to give some criteria in proto_reg_handoff_PROTOABBREV function such as --   dissector_add(&quot;tcp.port&quot;, 3011, ns_nnm_msg_handle);   So here i want my dissector to be called also when tcp.port == 3008, so can i add just another line here such as --   dissector_add(&quot;tcp.port&quot;, 3008,...'''
date = "2012-08-12T09:40:00Z"
lastmod = "2012-08-12T19:41:00Z"
weight = 13566
keywords = [ "dissector", "plugin" ]
aliases = [ "/questions/13566" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can we define multiple criteria for our dissector plugin to be called ?](/questions/13566/can-we-define-multiple-criteria-for-our-dissector-plugin-to-be-called)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know that we have to give some criteria in proto_reg_handoff_PROTOABBREV function such as --</p><blockquote><blockquote><p>dissector_add("tcp.port", 3011, ns_nnm_msg_handle);</p></blockquote></blockquote><p>So here i want my dissector to be called also when tcp.port == 3008, so can i add just another line here such as --</p><blockquote><blockquote><p>dissector_add("tcp.port", 3008, ns_nnm_msg_handle);</p></blockquote></blockquote><p>Am i doing correct ? Any help is sincerely appreciated.</p></div><div id="question-tags" class="tags-container tags">dissector plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '12, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-13566" class="comments-container"></div><div id="comment-tools-13566" class="comment-tools"></div><div class="clear"></div><div id="comment-13566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13568"></span>

<div id="answer-container-13568" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13568-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can do that. Many dissectors do, whether it's registering in multiple dissector tables or registering with multiple keys in a single dissector table or both.</p><p>If your protocol can run over arbitrary ports, you might want to make a "range" preference, which lets the user specify a list of ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '12, 19:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-13568" class="comments-container"></div><div id="comment-tools-13568" class="comment-tools"></div><div class="clear"></div><div id="comment-13568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

