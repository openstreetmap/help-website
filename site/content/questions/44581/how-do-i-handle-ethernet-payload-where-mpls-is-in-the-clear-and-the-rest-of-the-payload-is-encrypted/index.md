+++
type = "question"
title = "How do I handle ethernet payload where MPLS is in the clear and the rest of the payload is encrypted?"
description = '''If I understand correctly, the MPLS dissector inspects the rest of the ethernet payload to determine what type it is. If it is encrypted or corrupted, it will randomly match various types which impacts my analysis.  I can not disable the MPLS dissector because I need to decode the MPLS header. Chang...'''
date = "2015-07-28T19:00:00Z"
lastmod = "2015-07-29T20:11:00Z"
weight = 44581
keywords = [ "encryption", "dissector", "mpls" ]
aliases = [ "/questions/44581" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I handle ethernet payload where MPLS is in the clear and the rest of the payload is encrypted?](/questions/44581/how-do-i-handle-ethernet-payload-where-mpls-is-in-the-clear-and-the-rest-of-the-payload-is-encrypted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44581-score" class="post-score" title="current number of votes">0</div><span id="post-44581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If I understand correctly, the MPLS dissector inspects the rest of the ethernet payload to determine what type it is. If it is encrypted or corrupted, it will randomly match various types which impacts my analysis.</p><ul><li>I can not disable the MPLS dissector because I need to decode the MPLS header.</li><li>Changing the default decoder for MPLS payload is inadequate because:</li><li>It's more of a 'last resort decoder' as it only applies after failing to match</li><li>There's no 'do not decode' option</li></ul><p>It seems like a 'do not decode MPLS payload at all' feature was over looked. So, does this sound like a feature request or have I overlooked a way of handling this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encryption" rel="tag" title="see questions tagged &#39;encryption&#39;">encryption</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-mpls" rel="tag" title="see questions tagged &#39;mpls&#39;">mpls</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '15, 19:00</strong></p><img src="https://secure.gravatar.com/avatar/8a5d8a0723a2ad109e237d90ec93b4e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Gangemi&#39;s gravatar image" /><p><span>Guy Gangemi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Gangemi has one accepted answer">100%</span></p></div></div><div id="comments-container-44581" class="comments-container"></div><div id="comment-tools-44581" class="comment-tools"></div><div class="clear"></div><div id="comment-44581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44615"></span>

<div id="answer-container-44615" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44615-score" class="post-score" title="current number of votes">0</div><span id="post-44615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Guy Gangemi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Going to Preferences &gt; Protocols &gt; MPLS and setting Default decoder won't work for reasons outlined above.</p><p>Decode as... &gt; Link won't work because the Ethertype is parsed from the payload which means it's effectively a random value.</p><p>Decode as... &gt; MPLS will work because, in my case, mpls.label is a constant value.</p><p>However, the inbuilt Data dissector isn't present in the list so I added one using LAU. The LAU file is quite simple:</p><pre><code>MPLS_DATA = Dissector.get(&quot;data&quot;)
mpls_table = DissectorTable.get(&quot;mpls.label&quot;)
mpls_table:add (4294967295, MPLS_DATA)</code></pre><p>I followed the Wireshark guide <a href="https://wiki.wireshark.org/Lua">here</a> to enable LAU.</p><p>Now I can find Data in the Decode as... &gt; MPLS list and selecting it results in the MPLS payload presented as generic data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '15, 20:11</strong></p><img src="https://secure.gravatar.com/avatar/8a5d8a0723a2ad109e237d90ec93b4e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Gangemi&#39;s gravatar image" /><p><span>Guy Gangemi</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Gangemi has one accepted answer">100%</span></p></div></div><div id="comments-container-44615" class="comments-container"></div><div id="comment-tools-44615" class="comment-tools"></div><div class="clear"></div><div id="comment-44615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

