+++
type = "question"
title = "CDR app ID support"
description = '''Hi,  In the development version (1.11.2) CDR decoding for &quot;Data record format version: AppId 1 Rel 10.7.0&quot; does not decode properly. CDRs under AppId Rel 9.5.0 are decoded correctly. Is this a bug? or AppId 10.7.0 not supported? Thx Jean.-'''
date = "2013-11-29T12:53:00Z"
lastmod = "2013-11-30T19:30:00Z"
weight = 27575
keywords = [ "gtp", "prime", "cdr" ]
aliases = [ "/questions/27575" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [CDR app ID support](/questions/27575/cdr-app-id-support)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27575-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>In the development version (1.11.2) CDR decoding for "Data record format version: AppId 1 Rel 10.7.0" does not decode properly. CDRs under AppId Rel 9.5.0 are decoded correctly.</p><p>Is this a bug? or AppId 10.7.0 not supported?</p><p>Thx</p><p>Jean.-</p></div><div id="question-tags" class="tags-container tags">gtp prime cdr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '13, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/dae5978aca8b788c2880ad1232727a09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsarante&#39;s gravatar image" /><p>jsarante<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsarante has no accepted answers">0%</span></p></div></div><div id="comments-container-27575" class="comments-container"><span id="27578"></span><div id="comment-27578" class="comment"><div id="post-27578-score" class="comment-score"></div><div class="comment-text"><p>Does the current 1.10 version decode them correctly?</p></div><div id="comment-27578-info" class="comment-info"><span class="comment-age">(29 Nov '13, 18:52)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-27575" class="comment-tools"></div><div class="clear"></div><div id="comment-27575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27593"></span>

<div id="answer-container-27593" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27593-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the comments in Wireshark source files (the second line in wireshark-1.11.2/asn1/gprscdr/GPRSChargingDataTypesV9f0.asn), it looks like the latest version that's been written into Wireshark's code is for 3GPP TS 32.298 9.15.0, as of March 2013.</p><p>So, if you want you could write it yourself or ask the author of that one (cmaynard) if they're working on the later releases.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Nov '13, 19:30</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-27593" class="comments-container"><span id="27598"></span><div id="comment-27598" class="comment"><div id="post-27598-score" class="comment-score"></div><div class="comment-text"><p>Hi, It's actually me that is the author see packet-gprscdr-template.c and I'm not working on any update but given an example trace I would consider doing it.</p></div><div id="comment-27598-info" class="comment-info"><span class="comment-age">(01 Dec '13, 00:33)</span> Anders ♦</div></div><span id="27658"></span><div id="comment-27658" class="comment"><div id="post-27658-score" class="comment-score"></div><div class="comment-text"><p>I have updated the ASN1 code, you could try a buildbot build or build from trunk. Changes may be needed to apcket-gtp.c as well but to do those I'd like a trace to work with.</p></div><div id="comment-27658-info" class="comment-info"><span class="comment-age">(02 Dec '13, 03:27)</span> Anders ♦</div></div></div><div id="comment-tools-27593" class="comment-tools"></div><div class="clear"></div><div id="comment-27593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

