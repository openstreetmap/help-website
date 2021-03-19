+++
type = "question"
title = "SMB	Write AndX Request, FID: Process question"
description = '''Hello All, I need to understand the SMB Write AndX Request order Please correct me if i am wrong with process as follows: Thanks 1.Client &amp;gt; Storage SMB Write AndX Request,FID: 0x0009 next 2.TCP [TCP segment of a reassembled PDU] . . . . TCP [TCP segment of a reassembled PDU] . . 3.Storage &amp;gt; Cl...'''
date = "2012-02-14T06:07:00Z"
lastmod = "2012-02-14T14:54:00Z"
weight = 8994
keywords = [ "smb" ]
aliases = [ "/questions/8994" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SMB Write AndX Request, FID: Process question](/questions/8994/smb-write-andx-request-fid-process-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8994-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>I need to understand the SMB Write AndX Request order Please correct me if i am wrong with process as follows: Thanks</p><pre><code>1.Client &gt; Storage SMB Write AndX Request,FID: 0x0009
next
2.TCP [TCP segment of a reassembled PDU]
.
.
.
.
TCP [TCP segment of a reassembled PDU]
.
.
3.Storage &gt; Client SMB Write AndX Response, FID: 0x0009</code></pre></div><div id="question-tags" class="tags-container tags">smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '12, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p>tbaror<br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '12, 06:51</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-8994" class="comments-container"></div><div id="comment-tools-8994" class="comment-tools"></div><div class="clear"></div><div id="comment-8994-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8995"></span>

<div id="answer-container-8995" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8995-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you wonder why you see lots of packets (named "reassembled PDU") before the "Write AndX Response"? That is a result of your Wireshark having the setting "Allow subdisectors to reassemble TCP streams" enabled, which is the default. It basically means that Wireshark will first gather ALL packets that are part of the response before announcing it (in the last packet).</p><p>Try turning it of (Preferences -&gt; Protocols -&gt; TCP), and you'll see the "true" order of packets, but it will not reassemble their payload anymore (which is usually only bad if you need to reconstruct the contents that were transfered, see the Export -&gt; Objects -&gt; SMB menu option - it will not work as well if reassembly is turned off)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '12, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8995" class="comments-container"></div><div id="comment-tools-8995" class="comment-tools"></div><div class="clear"></div><div id="comment-8995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9008"></span>

<div id="answer-container-9008" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9008-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd actually expect to see several "[TCP segment of a reassembled PDU]" packets <em>before</em> a Write AndX request. A Write AndX request would contain the data to be written to the file, and it might not all fit in a single TCP segment, so I'd expect to see the earlier segments and then see the last segment marked as the request.</p><p>A Write AndX response should just contain information such as a success-or-failure indication and should fit in one TCP segment, although it could conceivably be split between TCP segments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '12, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9008" class="comments-container"></div><div id="comment-tools-9008" class="comment-tools"></div><div class="clear"></div><div id="comment-9008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

