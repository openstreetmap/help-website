+++
type = "question"
title = "Definitions of the structures used in the code"
description = '''Hello everyone, Is there some list of all data types (structures) definitions that are defined by the developers?  For example, the definition of the structure conversations___table I found in the file conversations_table.h.  For now, I need the definitions for the structures: -conv___id_t -nstime_t...'''
date = "2012-09-12T08:58:00Z"
lastmod = "2012-09-13T04:55:00Z"
weight = 14210
keywords = [ "source-code", "definitions", "structures", "definition" ]
aliases = [ "/questions/14210" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Definitions of the structures used in the code](/questions/14210/definitions-of-the-structures-used-in-the-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14210-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone,</p><p>Is there some list of all data types (structures) definitions that are defined by the developers? For example, the definition of the structure <strong>conversations___table</strong> I found in the file <strong>conversations_table.h</strong>.</p><p>For now, I need the definitions for the structures:</p><p>-conv___id_t</p><p>-nstime_t</p><p>-SAT_E</p><p>-address</p><p>-ptype</p><p>Thank you in advance.</p><p>Best regards,</p><p>Kiril</p></div><div id="question-tags" class="tags-container tags">source-code definitions structures definition</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '12, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/755cc43ee92b9171108d1438724f5e06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bluzerot&#39;s gravatar image" /><p>bluzerot<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bluzerot has no accepted answers">0%</span></p></div></div><div id="comments-container-14210" class="comments-container"></div><div id="comment-tools-14210" class="comment-tools"></div><div class="clear"></div><div id="comment-14210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14229"></span>

<div id="answer-container-14229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14229-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The source code is where the answer is. Look into using tools like cscope to find them easily.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '12, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14229" class="comments-container"><span id="14230"></span><div id="comment-14230" class="comment"><div id="post-14230-score" class="comment-score"></div><div class="comment-text"><p>Even simply doing grep helps or see which headers are included by the file using them and look trough those.</p></div><div id="comment-14230-info" class="comment-info"><span class="comment-age">(13 Sep '12, 05:06)</span> Anders ♦</div></div><span id="14231"></span><div id="comment-14231" class="comment"><div id="post-14231-score" class="comment-score"></div><div class="comment-text"><p>I have the following alias:</p><pre><code>alias srcfgrep=&#39;fgrep -Ril --include &quot;*.[ch]&quot; --exclude &quot;*svn*&quot; &#39;</code></pre><p>which helps a lot in finding files in which certain strings occur.</p><p>Usage:</p><pre><code>[email protected]:~/Wireshark/trunk$ srcfgrep find_or_create_conversation *
asn1/h225/packet-h225-template.c
asn1/ldap/packet-ldap-template.c
asn1/ros/packet-ros-template.c
epan/conversation.c
epan/conversation.h
epan/dissectors/packet-adwin.c
epan/dissectors/packet-afp.c
[...]
[email protected]:~/Wireshark/trunk$</code></pre><p>Which helps me a lot in finding my way through the code :-)</p></div><div id="comment-14231-info" class="comment-info"><span class="comment-age">(13 Sep '12, 05:27)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-14229" class="comment-tools"></div><div class="clear"></div><div id="comment-14229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

