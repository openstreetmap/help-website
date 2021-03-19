+++
type = "question"
title = "LDAP dissector"
description = ''''''
date = "2015-11-24T03:45:00Z"
lastmod = "2015-11-24T04:06:00Z"
weight = 47918
keywords = [ "ldap" ]
aliases = [ "/questions/47918" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LDAP dissector](/questions/47918/ldap-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47918-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark-expert_info-LDAP_errors1.tiff" alt="I may have a rather stupid question here, but what makes Wireshark &quot;decide&quot; if e.g. ldap traffic is indeed ldap traffic? Is it because of the used tcp port 389, or is there more intelligence in this decision? The issue I&#39;m facing is that I can see ldap errors to/from a server that is built by an external company, and they claim that the server is not using ldap at all... The server just opens tcp sessions with random tcp ports... (I&#39;&#39; m running latest version of wireshark 1.12.8) Thanks for your help!" /></p></div><div id="question-tags" class="tags-container tags">ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '15, 03:45</strong></p><img src="https://secure.gravatar.com/avatar/4fc43c83d14e6cb53bf36dd8013dbcf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="profke&#39;s gravatar image" /><p>profke<br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="profke has no accepted answers">0%</span></p></img></div></div><div id="comments-container-47918" class="comments-container"></div><div id="comment-tools-47918" class="comment-tools"></div><div class="clear"></div><div id="comment-47918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47921"></span>

<div id="answer-container-47921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47921-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark dissectors for a particular protocol can be called to dissect packets for a number of reasons:</p><ul><li>The dissector has registered to be called for packets on a particular port, e.g. tcp/389 for LDAP, usually via a preferences setting for the dissector.</li><li>The dissector has registered as a "heuristic" dissector and has determined, possibly incorrectly, that the packets it has been handed are indeed of the expected protocol type.</li><li>The dissector registers has a handler for a particular "type" of data, e.g. "text/plain" and the dissector for a another protocol has determined that the data is of the specified type.</li><li>The user has made a "Decode As .. " setting to decode all packets on a particular Link Type\Network Type\Transport Port as the specified protocol.</li><li>Other ways I've forgotten or didn't even know about.</li></ul><p>In summary, yes a dissector can be called for packets that are not of the correct type and various forms of oddness will ensue depending on how the dissector is coded.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '15, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '15, 09:13</p></div></div><div id="comments-container-47921" class="comments-container"><span id="47924"></span><div id="comment-47924" class="comment"><div id="post-47924-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham, there are no special decode settings, all is default. But if I see successfull bind responses, I guess then it is really ldap, not some other traffic using the same tcp port as ldap's default one? I'd like to show you some screen shots, but don't know how-to...</p></div><div id="comment-47924-info" class="comment-info"><span class="comment-age">(24 Nov '15, 04:24)</span> profke</div></div><span id="47925"></span><div id="comment-47925" class="comment"><div id="post-47925-score" class="comment-score"></div><div class="comment-text"><p>Analysis by screenshot is ... painful.</p><p>You can share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc.</p></div><div id="comment-47925-info" class="comment-info"><span class="comment-age">(24 Nov '15, 04:36)</span> grahamb ♦</div></div><span id="48005"></span><div id="comment-48005" class="comment"><div id="post-48005-score" class="comment-score"></div><div class="comment-text"><p>Yes, agree, but I can't share the pcap files. Meanwhile things are clear now; the traffic is indeed LDAP. Thx for your help.</p></div><div id="comment-48005-info" class="comment-info"><span class="comment-age">(26 Nov '15, 07:34)</span> profke</div></div><span id="48010"></span><div id="comment-48010" class="comment"><div id="post-48010-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-48010-info" class="comment-info"><span class="comment-age">(26 Nov '15, 09:13)</span> grahamb ♦</div></div></div><div id="comment-tools-47921" class="comment-tools"></div><div class="clear"></div><div id="comment-47921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

