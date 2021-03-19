+++
type = "question"
title = "Where can I find SCTP Data Chunk in Dissector Table?"
description = '''Dear all! I would like to write a chained dissector for SCTP Data Chunk but I don&#x27;t know how can I reach it in the Dissector Table. I know I can do this with SCTP like this: first: ether_table = DissectorTable.get (&quot;ethertype&quot;) original_dissector = ether_table:get_dissector(0x84) then in the definit...'''
date = "2013-08-08T06:31:00Z"
lastmod = "2013-08-08T08:41:00Z"
weight = 23643
keywords = [ "chained-dissector", "sctp", "data-chunk" ]
aliases = [ "/questions/23643" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where can I find SCTP Data Chunk in Dissector Table?](/questions/23643/where-can-i-find-sctp-data-chunk-in-dissector-table)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23643-score" class="post-score" title="current number of votes">0</div><span id="post-23643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all!</p><p>I would like to write a chained dissector for SCTP Data Chunk but I don't know how can I reach it in the Dissector Table. I know I can do this with SCTP like this:</p><p>first: <code>ether_table = DissectorTable.get ("ethertype") original_dissector = ether_table:get_dissector(0x84)</code></p><p>then in the definition my dissector:</p><p><code>original_dissector:call( buffer, pinfo, tree )</code></p><p>finally:</p><p><code>ether_table:add (0x84, mydiss)</code></p><p>But I cannot dissect an SCTP Data Chunk in a way like this. The Data Chunk looks in wireshark like a different protocol with its own grey trail and treeview. The payload protocol identifier of sctp finds out the real protocol of the data chunk.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-chained-dissector" rel="tag" title="see questions tagged &#39;chained-dissector&#39;">chained-dissector</span> <span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-data-chunk" rel="tag" title="see questions tagged &#39;data-chunk&#39;">data-chunk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '13, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/2942e21b1a69a461cfc2e72172fc748d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="torinos&#39;s gravatar image" /><p><span>torinos</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="torinos has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '13, 08:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-23643" class="comments-container"></div><div id="comment-tools-23643" class="comment-tools"></div><div class="clear"></div><div id="comment-23643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23656"></span>

<div id="answer-container-23656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23656-score" class="post-score" title="current number of votes">0</div><span id="post-23656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The SCTP dissector has 2 dissector tables: "sctp.port" (which allows you to grab packets for a particular port) and "sctp.ppi" (which allows you to grab packets for a particular Payload Protocol Identifier). So I think you'd call DissectorTable.get("sctp.port") and then the rest would be about the same (I guess, I don't use Lua).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-23656" class="comments-container"></div><div id="comment-tools-23656" class="comment-tools"></div><div class="clear"></div><div id="comment-23656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

