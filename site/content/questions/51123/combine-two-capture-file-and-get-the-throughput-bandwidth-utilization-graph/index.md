+++
type = "question"
title = "Combine Two Capture File And Get The Throughput Bandwidth Utilization Graph"
description = '''Hi Wireshark I have more than two capture files the capture time is different but there is NTP running and the time on the capture devices are sync with NTP. Now i want to merge these files and want to get maximum bandwidth utilization. Thanks Zeeshan Khan'''
date = "2016-03-23T06:12:00Z"
lastmod = "2016-03-23T06:12:00Z"
weight = 51123
keywords = [ "merge", "iograph" ]
aliases = [ "/questions/51123" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Combine Two Capture File And Get The Throughput Bandwidth Utilization Graph](/questions/51123/combine-two-capture-file-and-get-the-throughput-bandwidth-utilization-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51123-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Wireshark</p><p>I have more than two capture files the capture time is different but there is NTP running and the time on the capture devices are sync with NTP. Now i want to merge these files and want to get maximum bandwidth utilization.</p><p>Thanks Zeeshan Khan</p></div><div id="question-tags" class="tags-container tags">merge iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '16, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/52df8f586c3326b2bb940e1177dd7d58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZeeshanKhan&#39;s gravatar image" /><p>ZeeshanKhan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZeeshanKhan has no accepted answers">0%</span></p></div></div><div id="comments-container-51123" class="comments-container"><span id="51218"></span><div id="comment-51218" class="comment"><div id="post-51218-score" class="comment-score"></div><div class="comment-text"><p>Not sure what the question is or what you are struggling with...</p><p>you use mergecap * -w merged.pcapng and open it with wireshark and go to Statistics - IO Graph and switch Y-axis to bits/s ...</p><p>Am I missing something here ?</p></div><div id="comment-51218-info" class="comment-info"><span class="comment-age">(26 Mar '16, 09:29)</span> mrEEde</div></div><span id="51219"></span><div id="comment-51219" class="comment"><div id="post-51219-score" class="comment-score"></div><div class="comment-text"><p>I have two capture file from two different servers. Now i want to combine and want to get max bandwidth utilization.</p><p>For Exp both server are having 1 GB LAN cards. I want the max bandwidth utilization for both server as one 2 GB card.</p><p>Thanks Zeeshan Khan<br />
</p></div><div id="comment-51219-info" class="comment-info"><span class="comment-age">(26 Mar '16, 13:14)</span> ZeeshanKhan</div></div></div><div id="comment-tools-51123" class="comment-tools"></div><div class="clear"></div><div id="comment-51123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

