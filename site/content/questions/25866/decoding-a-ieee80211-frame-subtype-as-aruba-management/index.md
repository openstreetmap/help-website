+++
type = "question"
title = "Decoding a IEEE802.11 Frame Subtype as Aruba Management"
description = '''Recently while decoding a IEEE802.11 frame using Wireshark I notice it being detected as an Aruba Management Frame.  As per IEEE standard Frame Subtype value 0x0f in 802.11 Frame is a reserved value. So why does wireshark decode it as Aruba Management. Am I missing something mentioned in the standar...'''
date = "2013-10-10T05:25:00Z"
lastmod = "2013-10-10T05:25:00Z"
weight = 25866
keywords = [ "subtype", "frame", "aruba" ]
aliases = [ "/questions/25866" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding a IEEE802.11 Frame Subtype as Aruba Management](/questions/25866/decoding-a-ieee80211-frame-subtype-as-aruba-management)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25866-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently while decoding a IEEE802.11 frame using Wireshark I notice it being detected as an Aruba Management Frame.</p><p>As per IEEE standard Frame Subtype value 0x0f in 802.11 Frame is a reserved value. So why does wireshark decode it as Aruba Management. Am I missing something mentioned in the standard.</p></div><div id="question-tags" class="tags-container tags">subtype frame aruba</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '13, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/09330db20e638b5d8ec974c7f62c905d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nikunj&#39;s gravatar image" /><p>Nikunj<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nikunj has no accepted answers">0%</span></p></div></div><div id="comments-container-25866" class="comments-container"><span id="25875"></span><div id="comment-25875" class="comment"><div id="post-25875-score" class="comment-score"></div><div class="comment-text"><p>Could you raise a bug report including the trace with the missinterpreted frame so we can take a look at it.</p></div><div id="comment-25875-info" class="comment-info"><span class="comment-age">(10 Oct '13, 06:32)</span> Anders ♦</div></div><span id="25881"></span><div id="comment-25881" class="comment"><div id="post-25881-score" class="comment-score"></div><div class="comment-text"><p>I don't think it is a misinterpretation. The dissector code simply defines subtype 0x0f as "Aruba Management" frame, whereas the OP believes this should not be the case, as subtype 0x0f if not used in the standard (I did not check). I guess, the developer of the dissector figured out, that Aruba is silently using that code for their own purposes and added that information to the dissector code.</p></div><div id="comment-25881-info" class="comment-info"><span class="comment-age">(10 Oct '13, 07:31)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25866" class="comment-tools"></div><div class="clear"></div><div id="comment-25866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

