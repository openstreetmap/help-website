+++
type = "question"
title = "p-bits numbering"
description = '''I am using Wireshark version 1.10.1 and I&#x27;ve got a p-bit column set up by using Custom -&amp;gt; vlan.priority. This gives me the priority bit in the column but they are spelled out, for example &quot;Best Effort&quot; and &quot;Voice&quot;, but I only want the p-bit numbers 0-7 displayed in the column as it had done in pr...'''
date = "2013-08-23T18:53:00Z"
lastmod = "2013-08-24T01:08:00Z"
weight = 23990
keywords = [ "column", "resolved", "vlan", "priority" ]
aliases = [ "/questions/23990" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [p-bits numbering](/questions/23990/p-bits-numbering)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23990-score" class="post-score" title="current number of votes">0</div><span id="post-23990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark version 1.10.1 and I've got a p-bit column set up by using Custom -&gt; vlan.priority. This gives me the priority bit in the column but they are spelled out, for example "Best Effort" and "Voice", but I only want the p-bit numbers 0-7 displayed in the column as it had done in previous versions of wireshark, by using the option L2 COS value (802.1p). This now just yields a blank value in the column. Is there some way I can have the vlan.priority option convert the values to numbers instead of text?</p><p>The packet display in 1.10.1 are also a much lighter blue than the last version I had, 1.6.1 - how can I adjust that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span> <span class="post-tag tag-link-resolved" rel="tag" title="see questions tagged &#39;resolved&#39;">resolved</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span> <span class="post-tag tag-link-priority" rel="tag" title="see questions tagged &#39;priority&#39;">priority</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Aug '13, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/b3bd2fc506c49e5b95e4bdd2e93f4589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharkwire1&#39;s gravatar image" /><p><span>Sharkwire1</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharkwire1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '13, 01:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23990" class="comments-container"></div><div id="comment-tools-23990" class="comment-tools"></div><div class="clear"></div><div id="comment-23990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23994"></span>

<div id="answer-container-23994" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23994-score" class="post-score" title="current number of votes">1</div><span id="post-23994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Once you have set up the column, you can "right-click" on the column header and "deselect" the option "Show Resolved".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-23994" class="comments-container"></div><div id="comment-tools-23994" class="comment-tools"></div><div class="clear"></div><div id="comment-23994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

