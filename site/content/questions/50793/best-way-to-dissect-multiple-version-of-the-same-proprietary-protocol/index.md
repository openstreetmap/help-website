+++
type = "question"
title = "Best way to dissect multiple version of the same proprietary protocol ?"
description = '''Hi, Our project often updates our proprietary protocol, we&#x27;ll call the protocol: ZEPROTO. Our softwares use a single version of ZEPROTO, examples:  software_01 uses ZEPROTO v01 software_02 uses ZEPROTO v02, ... During development, we use ZEPROTO vTrunk.  All versions use the same ports to communicat...'''
date = "2016-03-10T05:48:00Z"
lastmod = "2016-03-10T07:44:00Z"
weight = 50793
keywords = [ "version", "multiple", "dll" ]
aliases = [ "/questions/50793" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Best way to dissect multiple version of the same proprietary protocol ?](/questions/50793/best-way-to-dissect-multiple-version-of-the-same-proprietary-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50793-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Our project often updates our proprietary protocol, we'll call the protocol: <em>ZEPROTO</em>. Our softwares use a single version of ZEPROTO, examples:</p><ul><li><strong>software_01</strong> uses <strong>ZEPROTO v01</strong></li><li><strong>software_02</strong> uses <strong>ZEPROTO v02</strong>, ...</li><li>During development, we use <strong>ZEPROTO vTrunk</strong>.</li></ul><p>All versions use the same ports to communicate and are not necessarily backward compatible. Until now, we didn't have anything specific in the packet which could tell the version of the packet itself. We've added this feature recently, example:</p><ul><li>At the beginning of the packet : 0x00 0x05 0x20 0x01 0xNN ... 0xMM means that the version of ZEPROTO is v5.2.1 followed other data.</li></ul><p>Since we don't have the version bytes in previous version of ZEPROTO and there is no specific pattern allowing us to distinguish a version from data, we can't decode properly.</p><p>Now (thank you if you've read until here), what can I do ?</p><ul><li>Can I have as many DLL for the same protocol but with different version ?</li><li>Can I have a single DLL but with many dissectors or other things that I could disable/enable from the protocol Menu ?</li></ul><p>What's the best ?</p></div><div id="question-tags" class="tags-container tags">version multiple dll</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '16, 05:48</strong></p><img src="https://secure.gravatar.com/avatar/46ef36ddea155cb13d6344c0c1731b7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_michel&#39;s gravatar image" /><p>_michel<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_michel has no accepted answers">0%</span></p></div></div><div id="comments-container-50793" class="comments-container"></div><div id="comment-tools-50793" class="comment-tools"></div><div class="clear"></div><div id="comment-50793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50798"></span>

<div id="answer-container-50798" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50798-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably easiest to have a single DLL with a protocol preference to manually select the version of protocol to decode the data as. One option for the preference could be "automatic", for use where the protocol has the version in the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '16, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50798" class="comments-container"><span id="50800"></span><div id="comment-50800" class="comment"><div id="post-50800-score" class="comment-score"></div><div class="comment-text"><p>well, that's the problem. For old versions, without the version 4 bytes, there is a chance that the data bytes look like version bytes.</p></div><div id="comment-50800-info" class="comment-info"><span class="comment-age">(10 Mar '16, 09:06)</span> _michel</div></div><span id="50801"></span><div id="comment-50801" class="comment"><div id="post-50801-score" class="comment-score"></div><div class="comment-text"><p>So the user will have to manually set the preference to "old version xxx". Hopefully the users will know what version they are expecting to see.</p><p>If there are truly no heuristics available to determine the different protocol versions, then it will have to be done via a manual preference setting.</p><p>Using different dissectors means instead of a preference setting the user will have to manually chose "Decode As ..." and the required version. IMHO though, creating different dissectors for a protocol that is likely to have lots in common between the versions is a lot more work.</p></div><div id="comment-50801-info" class="comment-info"><span class="comment-age">(10 Mar '16, 09:30)</span> grahamb ♦</div></div></div><div id="comment-tools-50798" class="comment-tools"></div><div class="clear"></div><div id="comment-50798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

