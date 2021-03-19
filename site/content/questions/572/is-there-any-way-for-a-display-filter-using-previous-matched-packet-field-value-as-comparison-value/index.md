+++
type = "question"
title = "is there any way for a display filter using previous matched packet field value as comparison value?"
description = '''Hi, Experts: for smpp protocol, I just want wireshark to display smpp submit request only with specific Dest term id, and the related server response. the related server response has smpp sequence id related. so how I can realize this display filter? Regards Zenith'''
date = "2010-10-20T21:15:00Z"
lastmod = "2010-10-20T21:15:00Z"
weight = 572
keywords = [ "display-filter" ]
aliases = [ "/questions/572" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [is there any way for a display filter using previous matched packet field value as comparison value?](/questions/572/is-there-any-way-for-a-display-filter-using-previous-matched-packet-field-value-as-comparison-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-572-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Experts:</p><p>for smpp protocol, I just want wireshark to display smpp submit request only with specific Dest term id, and the related server response. the related server response has smpp sequence id related.</p><p>so how I can realize this display filter?</p><p>Regards Zenith</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '10, 21:15</strong></p><img src="https://secure.gravatar.com/avatar/9eeeb74a813612d95f2e6de3c3205bb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zenith&#39;s gravatar image" /><p>zenith<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zenith has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Oct '10, 18:18</p></div></div><div id="comments-container-572" class="comments-container"><span id="573"></span><div id="comment-573" class="comment"><div id="post-573-score" class="comment-score">1</div><div class="comment-text"><p>Have you tried filtering on (smpp.command_id == 0x00000004) || (smpp.command_id == 0x80000004)? That gives you Submit_sm Requests and responses as a first hit.</p><p>Regarding the specifics: What exactly do you mean with "Dest term id" ? When looking at a sample trace for smpp i only see an entry for "Recipient address".</p></div><div id="comment-573-info" class="comment-info"><span class="comment-age">(21 Oct '10, 00:54)</span> Landi</div></div><span id="576"></span><div id="comment-576" class="comment"><div id="post-576-score" class="comment-score"></div><div class="comment-text"><p>Actually, I only want wireshark to display the specific submit request and accurately with it's own response, not all responses. I don't know wireshark can do automatcially using the previously matched packets's smpp msg sequence_id to filter again, and combine the two scan and show the result. it's something like regular expression's back reference.</p><p>let me imagine the following syntax for display filter improvement.</p><p>function point: 1.group matching<br />
using comma to split next matching within the group, it could be &gt;2 messages in the group.</p><p>(smpp.destination_addr contains "9703" ,smpp.sequence_number == &amp;smpp.sequence_number)</p><p>2.back reference &amp; is the previous matched packets, once &amp; used, and it should be released immediately. and group matching start over again for next matching group.</p><p>and more thinking, currently wireshark do not have the global variables can be defined to use in display filter. to link higher application level packets, if there are global variables that can be used to set some correlation id/key information in it, and reused in later when filtering,then two totally different underly protocols can be linked together. I want to call this service level filtering mechanism.</p></div><div id="comment-576-info" class="comment-info"><span class="comment-age">(21 Oct '10, 11:12)</span> zenith</div></div></div><div id="comment-tools-572" class="comment-tools"></div><div class="clear"></div><div id="comment-572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

