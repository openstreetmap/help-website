+++
type = "question"
title = "what determines the position of pointer of tree in main dissection function"
description = '''I have a very basic question.From what i understand , dissector_add determines criteria of wireshark calling my dissector. Now suppose if i have udp.port==7011 kind of filter , then i guess the pointer of &quot;tree&quot;(in dissect_proto) starts from udp packet ? Am i correct ? What will happen if i am using...'''
date = "2012-06-04T03:04:00Z"
lastmod = "2012-06-05T04:04:00Z"
weight = 11610
keywords = [ "plugin", "wireshark" ]
aliases = [ "/questions/11610" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [what determines the position of pointer of tree in main dissection function](/questions/11610/what-determines-the-position-of-pointer-of-tree-in-main-dissection-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11610-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a very basic question.From what i understand , dissector_add determines criteria of wireshark calling my dissector. Now suppose if i have udp.port==7011 kind of filter , then i guess the pointer of "tree"(in dissect_proto) starts from udp packet ? Am i correct ? What will happen if i am using heuristic dissector of "eth" ?</p></div><div id="question-tags" class="tags-container tags">plugin wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '12, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11610" class="comments-container"></div><div id="comment-tools-11610" class="comment-tools"></div><div class="clear"></div><div id="comment-11610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11656"></span>

<div id="answer-container-11656" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11656-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not sure where you're going with this, but the pointer 'tree' <em>may</em> point to a node to which your dissector can add proto items. You cannot make assumptions on where this 'tree' is rooted, nor do you have to. You get your data passed down to your dissector in the tvb, and you add your proto items to the proto tree. That's basically it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '12, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-11656" class="comments-container"><span id="11660"></span><div id="comment-11660" class="comment"><div id="post-11660-score" class="comment-score"></div><div class="comment-text"><p>Then how do i know where is correct place to add my proto items ?</p></div><div id="comment-11660-info" class="comment-info"><span class="comment-age">(05 Jun '12, 04:37)</span> yogeshg</div></div><span id="11663"></span><div id="comment-11663" class="comment"><div id="post-11663-score" class="comment-score"></div><div class="comment-text"><p>As Jaap said, you just add items to the passed in proto tree, nothing to think about.</p><p>Your dissector will be called at the right point in the frame dissection as set up by your call to dissector_add_xxx.</p><p>If you add a heuristic dissector to the UDP dissector with heur_dissector_add(), your dissector will be added to the chain of heuristic dissectors for UDP, and may get called if nothing in front of you in the chain handles the data.</p><p>If you add a dissector to the UDP dissector using dissector_add_uint() with a port preference of 7011, then it will only be called when UDP traffic appears on port 7011.</p><p>If you add a heuristic dissector to the eth" dissector your dissector will be added to the chain of heuristic dissectors for ethernet, and may get called if nothing in front of you in the chain handles the data.</p></div><div id="comment-11663-info" class="comment-info"><span class="comment-age">(05 Jun '12, 04:52)</span> grahamb ♦</div></div><span id="11665"></span><div id="comment-11665" class="comment"><div id="post-11665-score" class="comment-score"></div><div class="comment-text"><p>so basically , tree will automatically point at the start of the data which is relevant to my protocol because when we call for eg,</p><p>hb_tree = proto_item_add_subtree(ti, ett_hb); where hb is my protocol , hb_tree will contain all my protocol relevant info ? pls correct me if wrong , thanks for your patience :)</p></div><div id="comment-11665-info" class="comment-info"><span class="comment-age">(05 Jun '12, 05:05)</span> yogeshg</div></div><span id="11666"></span><div id="comment-11666" class="comment"><div id="post-11666-score" class="comment-score"></div><div class="comment-text"><p>The tree is where you hang your dissection items. The tvb* you are passed will contain the data for you to dissect, and offset 0 in it will contain the first byte of your protocol, the preceding dissectors having extracted their data payload into the tvb handed to you.</p></div><div id="comment-11666-info" class="comment-info"><span class="comment-age">(05 Jun '12, 05:13)</span> grahamb ♦</div></div></div><div id="comment-tools-11656" class="comment-tools"></div><div class="clear"></div><div id="comment-11656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

