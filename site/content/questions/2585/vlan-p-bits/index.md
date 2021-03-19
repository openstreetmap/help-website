+++
type = "question"
title = "VLAN P-bits"
description = '''How to check VLAN P-bits in a wireshark log?'''
date = "2011-02-28T07:34:00Z"
lastmod = "2011-02-28T07:52:00Z"
weight = 2585
keywords = [ "vlan-pbits" ]
aliases = [ "/questions/2585" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [VLAN P-bits](/questions/2585/vlan-p-bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2585-score" class="post-score" title="current number of votes">0</div><span id="post-2585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to check VLAN P-bits in a wireshark log?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vlan-pbits" rel="tag" title="see questions tagged &#39;vlan-pbits&#39;">vlan-pbits</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '11, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/25af1b236e2b74f6f291a95f864b722f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shfarooq&#39;s gravatar image" /><p><span>shfarooq</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shfarooq has no accepted answers">0%</span></p></div></div><div id="comments-container-2585" class="comments-container"></div><div id="comment-tools-2585" class="comment-tools"></div><div class="clear"></div><div id="comment-2585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2586"></span>

<div id="answer-container-2586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2586-score" class="post-score" title="current number of votes">0</div><span id="post-2586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If by "Wireshark Log" you mean, a "Packet capture file" and by "Check" you mean "Display" you can display this field with a custom column. Depending on the version of wireshark you need to use the field "vlan.priority" for versions up to 1.4.x and "eth.vlan.pri" for version 1.5.0 and higher.</p><p>In version 1.4.0 and higher you can rightclick on the VLAN priority field in the packet details pane and choose "Apply as column" to create the new column automatically.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '11, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2586" class="comments-container"></div><div id="comment-tools-2586" class="comment-tools"></div><div class="clear"></div><div id="comment-2586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

