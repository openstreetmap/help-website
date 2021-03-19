+++
type = "question"
title = "Unable to decode TCAP/GSM_MAP/GSM_SMS protocol layers..showing upto SCCP"
description = '''Hi All, Not able to see the decoded trace after SCCP. Its showing as only data after SCCP. Please guide me to see decoded layers of TCAP/GSM_MAP/GSM_SMS protocol. Is there any setting change required Regards, Arpit'''
date = "2014-04-10T23:47:00Z"
lastmod = "2014-04-11T17:32:00Z"
weight = 31747
keywords = [ "tcap" ]
aliases = [ "/questions/31747" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to decode TCAP/GSM\_MAP/GSM\_SMS protocol layers..showing upto SCCP](/questions/31747/unable-to-decode-tcapgsm_mapgsm_sms-protocol-layersshowing-upto-sccp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31747-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Not able to see the decoded trace after SCCP. Its showing as only data after SCCP. Please guide me to see decoded layers of TCAP/GSM_MAP/GSM_SMS protocol.</p><p>Is there any setting change required</p><p>Regards, Arpit</p></div><div id="question-tags" class="tags-container tags">tcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '14, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/8a4d7bafe5171216533cd4c9b6936f04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arpit&#39;s gravatar image" /><p>Arpit<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arpit has no accepted answers">0%</span></p></div></div><div id="comments-container-31747" class="comments-container"></div><div id="comment-tools-31747" class="comment-tools"></div><div class="clear"></div><div id="comment-31747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31748"></span>

<div id="answer-container-31748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31748-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check tat your GSM MAP ssn preferences matches the ssn used in SCCP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '14, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-31748" class="comments-container"><span id="31816"></span><div id="comment-31816" class="comment"><div id="post-31816-score" class="comment-score"></div><div class="comment-text"><p>Its already configured SSN value as 0-8 in GSM MAP.</p><p>We have used SSN 8 at called GT in SCCP, but in opened trace in wire-shark, I am unable to find any SSN value.</p><p>Most of all packet is showing with as SSN not present:--</p><p>{.... ..0. = SubSystem Number Indicator: SSN not present (0x00)}</p><p>And for some packet, SSN field value appearing in wire-shark trace as:---</p><p>"Expert Info (Warn/Protocol): Message is routed on SSN, but SSN is not present"</p><p>Please guide.</p><p>Regard, Arpit</p></div><div id="comment-31816-info" class="comment-info"><span class="comment-age">(14 Apr '14, 23:12)</span> Arpit</div></div></div><div id="comment-tools-31748" class="comment-tools"></div><div class="clear"></div><div id="comment-31748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31764"></span>

<div id="answer-container-31764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31764-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the Wireshark GUI, go to Edit &gt; Preferences &gt; Protocols &gt; GSM MAP, and make sure that the called SSN in your SCCP header is included in the list of SSNs to map to this protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '14, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-31764" class="comments-container"><span id="31817"></span><div id="comment-31817" class="comment"><div id="post-31817-score" class="comment-score"></div><div class="comment-text"><p>Its already configured SSN value as 0-8 in GSM MAP.</p><p>We have used SSN 8 at called GT in SCCP, but in opened trace in wire-shark, I am unable to find any SSN value.</p><p>Most of all packet is showing with as SSN not present:--</p><p>{.... ..0. = SubSystem Number Indicator: SSN not present (0x00)}</p><p>And for some packet, SSN field value appearing in wire-shark trace as:---</p><p>"Expert Info (Warn/Protocol): Message is routed on SSN, but SSN is not present"</p><p>Please guide.</p><p>Regard, Arpit</p></div><div id="comment-31817-info" class="comment-info"><span class="comment-age">(14 Apr '14, 23:12)</span> Arpit</div></div><span id="31821"></span><div id="comment-31821" class="comment"><div id="post-31821-score" class="comment-score"></div><div class="comment-text"><p>Try fiddling with the SCCP preferenses and "Users table", for more help you'll need to publish the trace somewhere so we can have a look at it.</p></div><div id="comment-31821-info" class="comment-info"><span class="comment-age">(15 Apr '14, 00:44)</span> Anders ♦</div></div><span id="31855"></span><div id="comment-31855" class="comment"><div id="post-31855-score" class="comment-score"></div><div class="comment-text"><p>I've seen it show 'Message is routed on SSN but SSN is not present" when the MTP3 layer was incorrectly decoding. Under MTP3 preferences, make sure it's set correctly to ITU, ANSI, etc.</p><p>If it still doesn't work, please upload here and post the URL: <a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a></p></div><div id="comment-31855-info" class="comment-info"><span class="comment-age">(15 Apr '14, 15:27)</span> Quadratic</div></div></div><div id="comment-tools-31764" class="comment-tools"></div><div class="clear"></div><div id="comment-31764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

