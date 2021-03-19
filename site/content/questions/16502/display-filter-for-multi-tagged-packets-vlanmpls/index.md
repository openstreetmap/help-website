+++
type = "question"
title = "display filter for multi-tagged packets (vlan/mpls)?"
description = '''as far as i can see there is no way to distinguish multiple vlan (and mpls) tags with a display filter. e.g. in a double-tagged frame both vlan-ids are named &quot;vlan.id&quot; and i can not set a specific filter for the second tag. is there a way to do this, like &quot;vlan[2].id&quot; maybe? i know i can use somethi...'''
date = "2012-12-03T08:14:00Z"
lastmod = "2012-12-03T08:35:00Z"
weight = 16502
keywords = [ "diplay-filter", "mpls", "vlan" ]
aliases = [ "/questions/16502" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [display filter for multi-tagged packets (vlan/mpls)?](/questions/16502/display-filter-for-multi-tagged-packets-vlanmpls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16502-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>as far as i can see there is no way to distinguish multiple vlan (and mpls) tags with a display filter. e.g. in a double-tagged frame both vlan-ids are named "vlan.id" and i can not set a specific filter for the second tag. is there a way to do this, like "vlan[2].id" maybe? i know i can use something like "frame[18:04]==00:78:81:00" but if i want to check if the cfi-bit in the second tag is set i have to use "frame[18]&amp;0x16" instead of something more readable like "vlan[2].cfi == 1".</p></div><div id="question-tags" class="tags-container tags">diplay-filter mpls vlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '12, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/b4cfed4f94ec9b26a8b4c89e056d7a26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scathaig&#39;s gravatar image" /><p>scathaig<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scathaig has no accepted answers">0%</span></p></div></div><div id="comments-container-16502" class="comments-container"></div><div id="comment-tools-16502" class="comment-tools"></div><div class="clear"></div><div id="comment-16502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16503"></span>

<div id="answer-container-16503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16503-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at the answer of SYN-bit for the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/16140/wireshark-capture-displays-inner-ip-when-traffic-is-ipinip</code><br />
</p></blockquote><p>I have not tried it, but the same should work for a VLAN tag. That's not a display filter as you need it, but at least you can view the various tags in tshark and then filter the output with other tools (grep, etc.).</p><p>Another option would (possibly) be a display filter macro:</p><blockquote><p><code>http://www.wireshark.org/docs/wsug_html_chunked/ChDisplayFilterMacrosSection.html?</code><br />
</p></blockquote><p>Define your macro like this:</p><blockquote><p><code>vlan2_cfi_set -&gt; (frame[18]&amp;0x16)</code></p></blockquote><p>then use the macro in a display filter:</p><blockquote><p><code>ip.addr eq 1.2.3.4 and ${vlan2_cfi_set}</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '12, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Dec '12, 09:19</p></div></div><div id="comments-container-16503" class="comments-container"></div><div id="comment-tools-16503" class="comment-tools"></div><div class="clear"></div><div id="comment-16503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

