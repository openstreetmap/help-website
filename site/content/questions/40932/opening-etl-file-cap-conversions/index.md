+++
type = "question"
title = "Opening etl file cap conversions"
description = '''so. I have recently been capturing traces with the netsh command, because it is a lot easier for quickly doing something. The only drawback I have noticed is that the .etl file I capture and then convert to .cap wont dissect the wlan traffic. LAN Traffic no problem.  According to https://social.tech...'''
date = "2015-03-27T00:56:00Z"
lastmod = "2015-03-31T15:55:00Z"
weight = 40932
keywords = [ "analyer", "message", "cap", "ms", "etl" ]
aliases = [ "/questions/40932" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Opening etl file cap conversions](/questions/40932/opening-etl-file-cap-conversions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40932-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>so. I have recently been capturing traces with the netsh command, because it is a lot easier for quickly doing something. The only drawback I have noticed is that the .etl file I capture and then convert to .cap wont dissect the wlan traffic. LAN Traffic no problem.</p><p>According to <a href="https://social.technet.microsoft.com/Forums/en-US/25dcf65d-0d18-4d11-b25a-a5d3aa4a81e9/exporting-etl-cap-getting-nonreadable-cap-file?forum=messageanalyzer">https://social.technet.microsoft.com/Forums/en-US/25dcf65d-0d18-4d11-b25a-a5d3aa4a81e9/exporting-etl-cap-getting-nonreadable-cap-file?forum=messageanalyzer</a> the data is all there, but Wireshark can't read it due to missing dissectors for NDIS? Is this true? If yes, is this in the works or what must be done to create one?</p><p>To be honest, the scenario is oh so useful.. I have a machine that is showing problems right now, I open a cmd and start a trace. no reboot, no install, nothing extra installed to change things. The data is kinda useless to me in etl format as I have no interest in learning another program just to read wlan traces :/</p><p>Anyone one else see this and can I/we open a change request?</p></div><div id="question-tags" class="tags-container tags">analyer message cap ms etl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '15, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-40932" class="comments-container"><span id="40939"></span><div id="comment-40939" class="comment"><div id="post-40939-score" class="comment-score"></div><div class="comment-text"><p>I just ran some tests using both wired and wireless connections and the convertion is fine, I see the same data in both Wireshark 1.99.x and Message Analyzer 1.2.</p><p>What version of Wireshark are you using and what are you using (and version) to do the conversion?</p></div><div id="comment-40939-info" class="comment-info"><span class="comment-age">(27 Mar '15, 08:25)</span> grahamb ♦</div></div><span id="41053"></span><div id="comment-41053" class="comment"><div id="post-41053-score" class="comment-score"></div><div class="comment-text"><p>I am on WS 1.12.4 an MSMA 1.2. Both newest I can get.</p><p>MA / Save as / export</p><p>I have a cap file and an etl.</p></div><div id="comment-41053-info" class="comment-info"><span class="comment-age">(31 Mar '15, 04:22)</span> DarrenWright</div></div></div><div id="comment-tools-40932" class="comment-tools"></div><div class="clear"></div><div id="comment-40932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40936"></span>

<div id="answer-container-40936" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40936-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think there's already an enhancement request at <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6694">bugs.wireshark.org</a> around this issue. So far no one with the required programming skills has had the time or inclination to develop the code for this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '15, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40936" class="comments-container"><span id="40938"></span><div id="comment-40938" class="comment"><div id="post-40938-score" class="comment-score"></div><div class="comment-text"><p>That bug appears to conflate two things; the ability to read .etl files which still isn't possible, and the ability to read a .cap file converted from a .etl which does work for Ethernet connections, but apparently not for wireless ones.</p></div><div id="comment-40938-info" class="comment-info"><span class="comment-age">(27 Mar '15, 07:44)</span> grahamb ♦</div></div><span id="41045"></span><div id="comment-41045" class="comment"><div id="post-41045-score" class="comment-score"></div><div class="comment-text"><p>Hi Graham. Yeah, basically it has 2 problems in one.</p><p>Reading an etl file is however kind of unrequired programming, you can just convert the etl to cap and job done. I think the only real thing is reading the converted cap file. It is not really an end of the world thing, but just a nice to have. The question was basically if this is a MS or a WireShark problem: I've been burned too often by MS with the "it's somebody elses problem (field. sorry about that :D)"</p><p>So basically the problem is that the dissector for Wireshark cannot read the converted file correctly and really does require an update? Can someone point me in the right direction?</p></div><div id="comment-41045-info" class="comment-info"><span class="comment-age">(31 Mar '15, 03:10)</span> DarrenWright</div></div><span id="41047"></span><div id="comment-41047" class="comment"><div id="post-41047-score" class="comment-score"></div><div class="comment-text"><p>In my tests the .cap file was read correctly, both for wired and wireless traffic. Unless you have a .cap that isn't read correctly, I don't see a bug.</p></div><div id="comment-41047-info" class="comment-info"><span class="comment-age">(31 Mar '15, 03:18)</span> grahamb ♦</div></div><span id="41071"></span><div id="comment-41071" class="comment"><div id="post-41071-score" class="comment-score"></div><div class="comment-text"><p>According to Paul Long at Microsoft, there are multiple types of 802.11 metadata, so an 802.11 .cap file from Network Monitor might work but an 802.11 .cap file from Message Analyzer might not.</p></div><div id="comment-41071-info" class="comment-info"><span class="comment-age">(31 Mar '15, 15:56)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-40936" class="comment-tools"></div><div class="clear"></div><div id="comment-40936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41070"></span>

<div id="answer-container-41070" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41070-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"A change request" means "a bug report", which you'd file on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>. You'll need to attach one of the .cap files that Wireshark doesn't handle (attaching a .etl file would require converting it to .cap format).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Mar '15, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41070" class="comments-container"></div><div id="comment-tools-41070" class="comment-tools"></div><div class="clear"></div><div id="comment-41070-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

