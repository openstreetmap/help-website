+++
type = "question"
title = "Decode TP4(COTP) inside CLNP"
description = '''Why there is no way to force wireshark to decode perfectly normal TP4 transport layer (it&#x27;s called COTP in wireshark terms) packets inside CLNP network layer? All I see is &quot;Data&quot; and there is no way to &quot;Decode as&quot; or apply any other dissector. On wireshark wiki it states: &quot;CLNP: COTP uses CLNP as it...'''
date = "2011-12-19T04:10:00Z"
lastmod = "2011-12-19T07:20:00Z"
weight = 8037
keywords = [ "tp4", "cotp", "clnp" ]
aliases = [ "/questions/8037" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decode TP4(COTP) inside CLNP](/questions/8037/decode-tp4cotp-inside-clnp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8037-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why there is no way to force wireshark to decode perfectly normal TP4 transport layer (it's called COTP in wireshark terms) packets inside CLNP network layer? All I see is "Data" and there is no way to "Decode as" or apply any other dissector. On wireshark wiki it states: "CLNP: COTP uses CLNP as its underlying network protocol." And yes, this is the case.</p><p>Example (don't see how to attach actual pcap):</p><pre><code>15:14:34.065889 CLNP, length 65
Data PDU, hlen: 60, v: 1, lifetime: 2.5s, Segment PDU length: 65, checksum: 0x0000(unverified)
Flags [Segmentation permitted]
source address (length 20): 39.356f.0000.0001.0000.0001.0001.0000.0011.0000.00
dest   address (length 20): 39.356f.0000.0001.0000.0001.0001.0000.0022.9685.00
Data Unit ID: 0x64c0, Segment Offset: 0, Total PDU Length: 65
  Priority Option #205, length 1, value: 0x0
  undecoded non-header data, length 5
  0x0000:  0465 8d8e 15</code></pre></div><div id="question-tags" class="tags-container tags">tp4 cotp clnp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '11, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/080873e10c10150278129c73d221706b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Constantine%20P&#39;s gravatar image" /><p>Constantine P<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Constantine P has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Dec '11, 04:14</p></div></div><div id="comments-container-8037" class="comments-container"><span id="35098"></span><div id="comment-35098" class="comment"><div id="post-35098-score" class="comment-score"></div><div class="comment-text"><p>how did u manage to generate tp4 traffic , i can't find any application that uses this protocol , well ... i found atn linux implementation but i couldn't compile it , may i ask for your help on how to generate tp4 traffic ?</p></div><div id="comment-35098-info" class="comment-info"><span class="comment-age">(03 Aug '14, 02:52)</span> saeedh</div></div></div><div id="comment-tools-8037" class="comment-tools"></div><div class="clear"></div><div id="comment-8037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8040"></span>

<div id="answer-container-8040" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8040-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OMG, thanks god we have source code:</p><p><code>static gboolean always_decode_transport = FALSE;</code></p><p>And I this leads to option inside CLNP protocol preferences that says:</p><p>"Always try to decode NSDU as transport PDUs"</p><p>Check it and it works! I really wonder why it's not checked by default, people use CLNP for something else?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '11, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/080873e10c10150278129c73d221706b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Constantine%20P&#39;s gravatar image" /><p>Constantine P<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Constantine P has no accepted answers">0%</span></p></div></div><div id="comments-container-8040" class="comments-container"></div><div id="comment-tools-8040" class="comment-tools"></div><div class="clear"></div><div id="comment-8040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

