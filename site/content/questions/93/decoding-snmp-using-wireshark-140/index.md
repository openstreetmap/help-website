+++
type = "question"
title = "Decoding SNMP using Wireshark 1.4.0"
description = '''I need to decode snmp OIDs in Wireshark, but when I Enable it under Name  resolution I receive this error message: Stopped processing module SNMPv2-SMI due to error(s) to prevent  potential crash in libsmi. Module&#x27;s conformance level: 1. See details at: http://bugs.debian.org/cgi-bin/bugreport.cgi?b...'''
date = "2010-09-15T12:02:00Z"
lastmod = "2010-09-16T00:19:00Z"
weight = 93
keywords = [ "snmp", "libsmi" ]
aliases = [ "/questions/93" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding SNMP using Wireshark 1.4.0](/questions/93/decoding-snmp-using-wireshark-140)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-93-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to decode snmp OIDs in Wireshark, but when I Enable it under Name resolution I receive this error message:</p><p>Stopped processing module SNMPv2-SMI due to error(s) to prevent potential crash in libsmi. Module's conformance level: 1. See details at: http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=560325</p><p>Is there something I am doing wrong ?</p><p>I am running wireshark 1.4.0 (SVN Rev 34005 from /trunk-1.4) under Vista.</p></div><div id="question-tags" class="tags-container tags">snmp libsmi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '10, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/3316014cff31ccb73779aa1214f3ca39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Glenn%20Andrews&#39;s gravatar image" /><p>Glenn Andrews<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Glenn Andrews has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 17 Sep '10, 11:30</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-93" class="comments-container"></div><div id="comment-tools-93" class="comment-tools"></div><div class="clear"></div><div id="comment-93-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="111"></span>

<div id="answer-container-111" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-111-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Glen,</p><p>according to the bug you've mentioned the lib which will be used for decoding the SNMP OIDs has some problems if the dependencies are not satisfied. One option could be to decode the OID by hand and verify if all needed MIB files to do this are on you system. This might be hard in case your not familiar with reading MIBs. The other option is upload a trace or post a hexdump of the packet, so that there is a chance to reproduce the problem.</p><p>regards Oliver</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 13:42</strong></p><img src="https://secure.gravatar.com/avatar/ea89a7136cee2bff4cc1ddbaf5e1b676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oliver&#39;s gravatar image" /><p>Oliver<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oliver has no accepted answers">0%</span></p></div></div><div id="comments-container-111" class="comments-container"></div><div id="comment-tools-111" class="comment-tools"></div><div class="clear"></div><div id="comment-111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="124"></span>

<div id="answer-container-124" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-124-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Oliver, the thing is I havent even loaded a capture at the point when this message appears. I tried replacing the SNMPv2-SMI file with another one and the same message occurs.</p><p>Glenn</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 16:07</strong></p><img src="https://secure.gravatar.com/avatar/3316014cff31ccb73779aa1214f3ca39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Glenn%20Andrews&#39;s gravatar image" /><p>Glenn Andrews<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Glenn Andrews has no accepted answers">0%</span></p></div></div><div id="comments-container-124" class="comments-container"></div><div id="comment-tools-124" class="comment-tools"></div><div class="clear"></div><div id="comment-124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="143"></span>

<div id="answer-container-143" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-143-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ahhhhhh, I see. I've just tried the same on my system (same Wireshark version, but on XP). Same problem. May you've to open a bug for this.</p><p>regards Oliver</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '10, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/ea89a7136cee2bff4cc1ddbaf5e1b676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oliver&#39;s gravatar image" /><p>Oliver<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oliver has no accepted answers">0%</span></p></div></div><div id="comments-container-143" class="comments-container"><span id="553"></span><div id="comment-553" class="comment"><div id="post-553-score" class="comment-score"></div><div class="comment-text"><p>I see that a bug was raised - https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5171 - but marked was WONTFIX. This seems odd to me - the file is shipped with Wireshark isn't it?</p></div><div id="comment-553-info" class="comment-info"><span class="comment-age">(20 Oct '10, 03:32)</span> Matthew Wilson</div></div></div><div id="comment-tools-143" class="comment-tools"></div><div class="clear"></div><div id="comment-143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

