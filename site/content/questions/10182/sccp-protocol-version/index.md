+++
type = "question"
title = "SCCP Protocol version?"
description = '''i use wireshark-win32-1.6.5. what sccp protocol version is supported for wireshark-win32-1.6.5 ?? i can&#x27;t have some information in sccp packet.'''
date = "2012-04-16T03:13:00Z"
lastmod = "2012-04-27T06:53:00Z"
weight = 10182
keywords = [ "sccp" ]
aliases = [ "/questions/10182" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SCCP Protocol version?](/questions/10182/sccp-protocol-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10182-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i use wireshark-win32-1.6.5. what sccp protocol version is supported for wireshark-win32-1.6.5 ?? i can't have some information in sccp packet.</p></div><div id="question-tags" class="tags-container tags">sccp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '12, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/b11767cf7593972106cc8170b735b29b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kernel7k&#39;s gravatar image" /><p>kernel7k<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kernel7k has no accepted answers">0%</span></p></div></div><div id="comments-container-10182" class="comments-container"><span id="42196"></span><div id="comment-42196" class="comment"><div id="post-42196-score" class="comment-score"></div><div class="comment-text"><p>What fields are missing? Keep in mind that if your MTP3 variant (ANSI or ITU or ???) is wrong, then the decoding of SCCP will be a train wreck because Wireshark will then not know where SCCP starts. As you're probably aware, the ITU MTP3 routing label is 32 bits. It has in it two 14-bit point codes and a 4-bit SLS. The ANSI MTP3 routing label is 7 octets. Two 24-bit point codes and a 5 or 8-bit SLS. A whole octet is donated to the ANSI MTP3 SLS no matter if it's 5 or 8 bits.</p><p>Check to make sure you're decoding MTP3 (or M3UA?) properly.</p></div><div id="comment-42196-info" class="comment-info"><span class="comment-age">(07 May '15, 14:19)</span> tiger762</div></div></div><div id="comment-tools-10182" class="comment-tools"></div><div class="clear"></div><div id="comment-10182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10482"></span>

<div id="answer-container-10482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10482-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The SCCP dissector's source code says that it is (hopefully) compliant with these specifications:</p><ul><li>ANSI T1.112.3-2001</li><li>ITU-T Q.713 7/1996</li><li>YDN 038-1997 (Chinese ITU variant)</li><li>JT-Q713 and NTT-Q713 (Japan)</li></ul><p>Though there hasn't been large changes in the SCCP specs in years so the actual versions shouldn't matter much.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '12, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-10482" class="comments-container"></div><div id="comment-tools-10482" class="comment-tools"></div><div class="clear"></div><div id="comment-10482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

