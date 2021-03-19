+++
type = "question"
title = "Is there a way to stop capture upon http error 404?"
description = '''I would like to be able to do a free-running capture of all packets until it encounters any HTTP error code 400 and above then for wireshark to stop and save the last 10 minutes of packets? Many thanks in advance for your help!!'''
date = "2015-01-28T09:08:00Z"
lastmod = "2015-02-04T07:43:00Z"
weight = 39456
keywords = [ "capture", "autostop" ]
aliases = [ "/questions/39456" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to stop capture upon http error 404?](/questions/39456/is-there-a-way-to-stop-capture-upon-http-error-404)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39456-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to be able to do a free-running capture of all packets until it encounters any HTTP error code 400 and above then for wireshark to stop and save the last 10 minutes of packets? Many thanks in advance for your help!!</p></div><div id="question-tags" class="tags-container tags">capture autostop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '15, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/db2dc5fe78bd4633790190dccfdac479?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TennisFan&#39;s gravatar image" /><p>TennisFan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TennisFan has no accepted answers">0%</span></p></div></div><div id="comments-container-39456" class="comments-container"></div><div id="comment-tools-39456" class="comment-tools"></div><div class="clear"></div><div id="comment-39456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39462"></span>

<div id="answer-container-39462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39462-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has no complex filter driven start/stop mechanism, so this is not supported natively.</p><p>What you could do is script something using the command line tools dumpcap and tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '15, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39462" class="comments-container"></div><div id="comment-tools-39462" class="comment-tools"></div><div class="clear"></div><div id="comment-39462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39642"></span>

<div id="answer-container-39642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39642-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Recently I published a batch file, <code>dumpcap.bat</code> on <a href="http://wiki.wireshark.org/Tools">http://wiki.wireshark.org/Tools</a>, which <em>might</em> help you if you're running on the Windows platform. Since the batch file currently only supports <code>dumpcap</code> and thus only capture filters and not Wireshark display filters, it would only be practical to use if the HTTP response codes always appear at the same offset in the TCP payload. That might be true for all 404's, but it's probably not going to be true for every error code greater than or equal to 400.</p><p>In case you want to look at it, the following might help you get started - modify settings as needed:</p><hr /><p><code>  1. Dumpcap runtime priority: NORMAL  2. Dumpcap Mode:             Dumpcap+Event ------------------------------[ DUMPCAP OPTIONS ]------------------------------  3. Interface:                TBD  4. Capture file:             http404.pcapng  5. Capture filter:           tcp port 80  6. Snaplen                   Use default value  7. Promiscuous mode?         Y  8. Buffer size               Use default value  9. Use pcapng format?        Y      Autostop conditions:  10. Stop after               &lt;</code>infinite<code>&gt;</code> packets 11. Stop after <code>&lt;</code>infinite<code>&gt;</code> seconds 12. Stop after <code>&lt;</code>infinite<code>&gt;</code> kB 13. Stop after <code>&lt;</code>infinite<code>&gt;</code> files Ringbuffer settings: 14. Switch files after: 600 seconds 15. Switch files after <code>&lt;</code>infinite<code>&gt;</code> kB 16. Ringbuffer max files 2 files ---------------------------[ CAPTURE EVENT OPTIONS ]--------------------------- 17. Event Interface <strong><em>TBD</em></strong> 18. Event capture filter tcp port 80 and tcp[29] = 0x34 and tcp[30] = 0x30 and tcp[31] = 0x34 19. Event count 1 20. Event kills dumpcap? Y 21. Delay before kill/action 0 seconds </code></p><p>You can also enable the <code>mailsend</code> feature if you'd like an e-mail notification of when the event occurs.</p><p>I know this isn't as easy as being able to specify a <code>tshark</code> display filter of <code>"http.response.code &gt;= 400"</code>, but it <em>might</em> be better than nothing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '15, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-39642" class="comments-container"></div><div id="comment-tools-39642" class="comment-tools"></div><div class="clear"></div><div id="comment-39642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

