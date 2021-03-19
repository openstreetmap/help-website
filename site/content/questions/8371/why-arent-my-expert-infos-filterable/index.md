+++
type = "question"
title = "Why aren&#x27;t my expert-infos filterable?"
description = '''I have a plugin dissector which may attach expert info to a packet as shown below: if(EXPERT_CONDITION(p_item)) {  expert_add_info_format(pinfo, p_item, PI_PROTOCOL, PI_WARN, &quot;expert warning&quot;); }  Here, EXPERT_CONDITION is a macro that examines the data in p_item (equivalent to the code given in my ...'''
date = "2012-01-13T07:55:00Z"
lastmod = "2012-01-13T17:18:00Z"
weight = 8371
keywords = [ "filter", "development", "expert-info", "dissector", "display-filter" ]
aliases = [ "/questions/8371" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why aren't my expert-infos filterable?](/questions/8371/why-arent-my-expert-infos-filterable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8371-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a plugin dissector which may attach expert info to a packet as shown below:</p><pre><code>if(EXPERT_CONDITION(p_item))
{
    expert_add_info_format(pinfo, p_item, PI_PROTOCOL, PI_WARN, &quot;expert warning&quot;);
}</code></pre><p>Here, <code>EXPERT_CONDITION</code> is a macro that examines the data in <code>p_item</code> (equivalent to the code given in my answer <a href="http://ask.wireshark.org/questions/7225/how-can-i-examine-the-actual-value-of-a-proto_item?page=1#7330">here</a>). I have captures where this expert info is visible in the tree, but no other expert info is present in the packet. In these captures, if I put <code>expert</code> in the filter pane, these marked packets do not show up. If I look in the <code>Expert Infos</code> dialog, I see <code>Warnings: 0 (0)</code>.</p><p>Because of this I can't filter on packets in my protocol with an expert info that is specific to my protocol. How can I change my code so that the expert-info marked packets of my protocol are correctly filterable?</p></div><div id="question-tags" class="tags-container tags">filter development expert-info dissector display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '12, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8371" class="comments-container"></div><div id="comment-tools-8371" class="comment-tools"></div><div class="clear"></div><div id="comment-8371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8380"></span>

<div id="answer-container-8380" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8380-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you calling expert_add_info_format() from within an <code>if (tree) {}</code> block, perhaps? This needs to be called whether the <code>tree</code> is <code>NULL</code> or not. The <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer?revision=39587&amp;view=markup">README.developer</a> document doesn't explicitly mention the expert infos, but the following excerpt does apply to expert infos as well:</p><pre><code>   Note, however, that you must fill in column information, create
   conversations, reassemble packets, build any other persistent state
   needed for dissection, and call subdissectors regardless of whether
   &quot;tree&quot; is NULL or not.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '12, 17:18</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8380" class="comments-container"><span id="8438"></span><div id="comment-8438" class="comment"><div id="post-8438-score" class="comment-score"></div><div class="comment-text"><p>This is the problem. I checked by rearranging a small portion of my dissector so the expert logic for one specific case would be run regardless of the <code>tree</code>. As expected, the filter <code>expert</code> correctly displays those packets, but still misses other marked packets that depend on <code>tree</code>.</p></div><div id="comment-8438-info" class="comment-info"><span class="comment-age">(17 Jan '12, 08:32)</span> multipleinte...</div></div></div><div id="comment-tools-8380" class="comment-tools"></div><div class="clear"></div><div id="comment-8380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

