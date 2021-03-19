+++
type = "question"
title = "Wireshark keeps crashing"
description = '''Hello, I&#x27;m building a new server and installed Wireshark and it keeps crashing. I have spanned a port off our Cisco switch which is basically our WAN link to our remote offices, so lots of data. The server is a Dell R710 CPU: 2 x Xeons 2.27Ghz Mem: 20GB HD: SAS 500GB (RAID6) OS: Windows 2012 R2 64bi...'''
date = "2015-02-12T01:57:00Z"
lastmod = "2015-02-12T02:03:00Z"
weight = 39827
keywords = [ "windows2012r2" ]
aliases = [ "/questions/39827" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark keeps crashing](/questions/39827/wireshark-keeps-crashing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39827-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm building a new server and installed Wireshark and it keeps crashing. I have spanned a port off our Cisco switch which is basically our WAN link to our remote offices, so lots of data.</p><p>The server is a Dell R710 CPU: 2 x Xeons 2.27Ghz Mem: 20GB HD: SAS 500GB (RAID6) OS: Windows 2012 R2 64bit</p><p>I've set Wireshark to create multiple after 5 mins (2gb a file), but after 20 mins it crashes and I have multiple Wireshark windows open.</p><p>Any ideas on what I can do?</p></div><div id="question-tags" class="tags-container tags">windows2012r2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '15, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/09e8dc62bc7c0b2a6d62edf9aebb8707?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gonzo&#39;s gravatar image" /><p>gonzo<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gonzo has no accepted answers">0%</span></p></div></div><div id="comments-container-39827" class="comments-container"></div><div id="comment-tools-39827" class="comment-tools"></div><div class="clear"></div><div id="comment-39827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39828"></span>

<div id="answer-container-39828" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39828-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yep, read this: <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '15, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39828" class="comments-container"><span id="39829"></span><div id="comment-39829" class="comment"><div id="post-39829-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it could be a different issue as it crashed after 2 mins and only used 1.7GB of 20GB.</p><p>And spits this out:</p><p>Problem signature: Problem Event Name: APPCRASH Application Name: Wireshark.exe Application Version: 1.12.3.0 Application Timestamp: 54ad9bac Fault Module Name: libwireshark.dll Fault Module Version: 1.12.3.0 Fault Module Timestamp: 54ad9a8c Exception Code: c0000005 Exception Offset: 00000000000122d7 OS Version: 6.3.9600.2.0.0.272.7 Locale ID: 2057 Additional Information 1: b911 Additional Information 2: b911134c916a531e14249c0801bebd15 Additional Information 3: b0bf Additional Information 4: b0bf9c0f8d87a9670fe011511bbca199</p></div><div id="comment-39829-info" class="comment-info"><span class="comment-age">(12 Feb '15, 03:45)</span> gonzo</div></div><span id="39830"></span><div id="comment-39830" class="comment"><div id="post-39830-score" class="comment-score"></div><div class="comment-text"><p>I'd say try dumpcap and see if it works ;-)</p></div><div id="comment-39830-info" class="comment-info"><span class="comment-age">(12 Feb '15, 03:50)</span> Jasper ♦♦</div></div><span id="39831"></span><div id="comment-39831" class="comment"><div id="post-39831-score" class="comment-score"></div><div class="comment-text"><p>let me look into this, thanks.</p></div><div id="comment-39831-info" class="comment-info"><span class="comment-age">(12 Feb '15, 03:51)</span> gonzo</div></div><span id="39853"></span><div id="comment-39853" class="comment"><div id="post-39853-score" class="comment-score"></div><div class="comment-text"><p>Seems to be working much better, can I merge more that 2 files together in Wireshark? I'm outputting files every 5 mins and need about 30 mins worth merged.</p></div><div id="comment-39853-info" class="comment-info"><span class="comment-age">(13 Feb '15, 08:23)</span> gonzo</div></div><span id="39854"></span><div id="comment-39854" class="comment"><div id="post-39854-score" class="comment-score"></div><div class="comment-text"><p>yes, either via the file menu, or using mergecap (another command line tool) with the -a parameter</p></div><div id="comment-39854-info" class="comment-info"><span class="comment-age">(13 Feb '15, 08:59)</span> Jasper ♦♦</div></div><span id="39952"></span><div id="comment-39952" class="comment not_top_scorer"><div id="post-39952-score" class="comment-score"></div><div class="comment-text"><p>Via the menu it seems to only let me select 2 files to merge, the one I have currently open and only one more, does mergecap allow me to do muiltiple in one go?</p></div><div id="comment-39952-info" class="comment-info"><span class="comment-age">(19 Feb '15, 09:03)</span> gonzo</div></div><span id="39953"></span><div id="comment-39953" class="comment not_top_scorer"><div id="post-39953-score" class="comment-score"></div><div class="comment-text"><p>ah I worked it out, I have to save the capture after adding the first merge file to my current one.</p></div><div id="comment-39953-info" class="comment-info"><span class="comment-age">(19 Feb '15, 09:06)</span> gonzo</div></div></div><div id="comment-tools-39828" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-39828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

