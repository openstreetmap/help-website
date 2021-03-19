+++
type = "question"
title = "can bus (j1939) frames without datas wrong interpreted"
description = '''Hello everybody, I&#x27;m sending a 1st frame with 0xDEADBEEF on datas on a virtual can bus (vcan0) And the second time there is the same without these datas. But wireshark(2.0.2) is interpreting the 2nd frame malformed... Any Idea ?   Thanks in advance.'''
date = "2016-04-13T09:08:00Z"
lastmod = "2016-04-25T23:39:00Z"
weight = 51641
keywords = [ "bus", "data", "can", "malformed", "j1939" ]
aliases = [ "/questions/51641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [can bus (j1939) frames without datas wrong interpreted](/questions/51641/can-bus-j1939-frames-without-datas-wrong-interpreted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51641-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody,</p><p>I'm sending a 1st frame with 0xDEADBEEF on datas on a virtual can bus (vcan0) And the second time there is the same without these datas.</p><p>But wireshark(2.0.2) is interpreting the 2nd frame malformed... Any Idea ? <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_du_2016-04-13_17:53:08.png" alt="alt text" /> Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">bus data can malformed j1939</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '16, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/177e55c0d5e8a290e016f63356e5f9fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lamoule74&#39;s gravatar image" /><p>lamoule74<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lamoule74 has 2 accepted answers">66%</span></p></img></div></div><div id="comments-container-51641" class="comments-container"><span id="51643"></span><div id="comment-51643" class="comment"><div id="post-51643-score" class="comment-score"></div><div class="comment-text"><p>This may be a bug, or actual invalid data. Looking at the code, the J1939 dissector expects the CAN Identifier to be &lt; 0x20000000 and 0xDEADBEEF isn't. This means the J1939 dissector should refuse to dissect the frame, but that doesn't appear to be happening for you.</p><p>Can you share that capture file somewhere publicly?</p></div><div id="comment-51643-info" class="comment-info"><span class="comment-age">(13 Apr '16, 09:57)</span> grahamb ♦</div></div><span id="51645"></span><div id="comment-51645" class="comment"><div id="post-51645-score" class="comment-score">1</div><div class="comment-text"><p>@grahamb, 0xdeadbeef was the payload of the properly dissected packet, not the CAN ID of the "malformed" one. @lamoule74's real question is why a CAN frame with Frame-Length 0 and, consistently with that, no actual data is reported as a malformed one.</p><p>@lamoule74, I don't know whether the CAN specification permits void frames or not; depending on that, the "malformed packet" tag may be just (if void CAN frames are forbidden) or a dissector bug (if void CAN frames are permitted). As you venture to forge CAN frames, I'd guess you know enough of the specification so you should be able to decide whether to <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">file a Wireshark bug</a> or to fix your CAN frame generator. Note that the <code>Remote Transmission Request</code> flag may be relevant too, i.e. void frames may only be permitted if this flag is set.</p></div><div id="comment-51645-info" class="comment-info"><span class="comment-age">(13 Apr '16, 11:27)</span> sindy</div></div><span id="51650"></span><div id="comment-51650" class="comment"><div id="post-51650-score" class="comment-score"></div><div class="comment-text"><p>@sindy, good spot, so the id is 0x0c011201 and the J1939 dissector will try to dissect the 0 byte data frame. I'm in the same boat as you, I don't know if that's permitted.</p></div><div id="comment-51650-info" class="comment-info"><span class="comment-age">(13 Apr '16, 13:59)</span> grahamb ♦</div></div></div><div id="comment-tools-51641" class="comment-tools"></div><div class="clear"></div><div id="comment-51641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51945"></span>

<div id="answer-container-51945" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51945-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hey everyone, the bug has been fixed by the team, that's perfect : <a href="https://code.wireshark.org/review/#/c/15110/">https://code.wireshark.org/review/#/c/15110/</a></p><p>How do I apply this on my wireshark version now ? May I have to apply a patch or checkout the src then recompile them ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '16, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/177e55c0d5e8a290e016f63356e5f9fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lamoule74&#39;s gravatar image" /><p>lamoule74<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lamoule74 has 2 accepted answers">66%</span></p></div></div><div id="comments-container-51945" class="comments-container"><span id="51946"></span><div id="comment-51946" class="comment"><div id="post-51946-score" class="comment-score">1</div><div class="comment-text"><p>That depends on your OS. The change has been backported to 2.0, so any of the <a href="https://www.wireshark.org/download/automated/">automated builds</a> of 2.0.4rc0-x-... where x &gt;= 6 than will have the fix.</p><p>If you have built Wireshark yourself, you'll have to check out the source that includes the commit 23086b3a.</p></div><div id="comment-51946-info" class="comment-info"><span class="comment-age">(25 Apr '16, 23:50)</span> grahamb ♦</div></div><span id="51952"></span><div id="comment-51952" class="comment"><div id="post-51952-score" class="comment-score"></div><div class="comment-text"><p>OK, I recompiled the stuff; emtpy frames are no linger recognized as malformed !</p><p>:D</p></div><div id="comment-51952-info" class="comment-info"><span class="comment-age">(26 Apr '16, 01:59)</span> lamoule74</div></div></div><div id="comment-tools-51945" class="comment-tools"></div><div class="clear"></div><div id="comment-51945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

