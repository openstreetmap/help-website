+++
type = "question"
title = "out-of-order packets"
description = '''Is there a way to display the payload data from a Wireshark trace so as to re-sequence it (to get rid of out-of-order errors). We need to determine exactly what the application sees AFTER the packets associated with a given TCP stream have been put into proper sequence. We could correlate the sequen...'''
date = "2011-06-21T09:51:00Z"
lastmod = "2011-06-21T14:07:00Z"
weight = 4647
keywords = [ "out-of-order" ]
aliases = [ "/questions/4647" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [out-of-order packets](/questions/4647/out-of-order-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4647-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to display the payload data from a Wireshark trace so as to re-sequence it (to get rid of out-of-order errors). We need to determine exactly what the application sees AFTER the packets associated with a given TCP stream have been put into proper sequence. We could correlate the sequence numbers manually, but were hoping for some automated way to accomplish what we need. Follow TCP stream apparently displays the data as it was seen on the network, not as the app process it once re-ordered.</p></div><div id="question-tags" class="tags-container tags">out-of-order</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '11, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/de310d5db6f9967a52b6b132c7ba7049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jowimi&#39;s gravatar image" /><p>jowimi<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jowimi has no accepted answers">0%</span></p></div></div><div id="comments-container-4647" class="comments-container"></div><div id="comment-tools-4647" class="comment-tools"></div><div class="clear"></div><div id="comment-4647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4652"></span>

<div id="answer-container-4652" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4652-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Follow TCP stream does just that, it reorders data according to sequence numbers and will put those in the output. The only reason for that to be messed up that I can imagine is when out-of-order packets are seen while both endpoints are sending data at the same time.</p><p>Are you able to share the tracefile to have a look whether Follow TCP stream is indeed behaving as expected (which it does not seem to do on your tracefile)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '11, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4652" class="comments-container"><span id="4654"></span><div id="comment-4654" class="comment"><div id="post-4654-score" class="comment-score"></div><div class="comment-text"><p>According to the Wireshark documentation at http://www.wireshark.org/docs/wsug_html/#ChAdvFollowTCPSection,</p><p>[The stream content is displayed in the same sequence as it appeared on the network. Traffic from A to B is marked in red, while traffic from B to A is marked in blue...]</p><p>The "same sequence as it appeared on the network" is somewhat misleading in that it implies that packets appear in received sequence, not in sequence number sequence. I'll assume you're correct.</p><p>Thanks much for your response.</p><p>P.S. I can't share the trace file as it contains live patient data</p></div><div id="comment-4654-info" class="comment-info"><span class="comment-age">(21 Jun '11, 15:23)</span> jowimi</div></div></div><div id="comment-tools-4652" class="comment-tools"></div><div class="clear"></div><div id="comment-4652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

