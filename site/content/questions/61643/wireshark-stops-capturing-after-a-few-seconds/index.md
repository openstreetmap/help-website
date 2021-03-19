+++
type = "question"
title = "Wireshark stops capturing after a few seconds"
description = '''Wireshark stops after capturing a few seconds using version Version 2.2.6 (v2.2.6-0-g32dac6a) - 64bits Parameters :  - OS = Windows 7 Pro, 8G RAM but had similar results on Windows 2012 with 128G of RAM ;  - Network Interfaces are 10Gigs ;  - Very high bandwidth environment ;  - I capture only the f...'''
date = "2017-05-26T11:53:00Z"
lastmod = "2017-05-26T12:55:00Z"
weight = 61643
keywords = [ "high", "capture", "bandwidth", "crash" ]
aliases = [ "/questions/61643" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark stops capturing after a few seconds](/questions/61643/wireshark-stops-capturing-after-a-few-seconds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61643-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark stops after capturing a few seconds using version Version 2.2.6 (v2.2.6-0-g32dac6a) - 64bits</p><p><strong>Parameters :</strong> - OS = Windows 7 Pro, 8G RAM but had similar results on Windows 2012 with 128G of RAM ; - Network Interfaces are 10Gigs ; - Very high bandwidth environment ; - I capture only the first 68 bytes of each packet ; - splitted into many 50Megs files (usually doesnt get past 2nd one) ; - update list of packet in realtime is disabled so is autoscroll</p><p>Any ideas on how I could prevent it from crashing ?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">high capture bandwidth crash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '17, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/ceaa156fe9957bed4abb791f6804382c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andguay&#39;s gravatar image" /><p>andguay<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andguay has no accepted answers">0%</span></p></div></div><div id="comments-container-61643" class="comments-container"></div><div id="comment-tools-61643" class="comment-tools"></div><div class="clear"></div><div id="comment-61643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61645"></span>

<div id="answer-container-61645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61645-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to consider other tools to capture in such high bandwidth environments. As a first attempt have a look at dumpcap, the capture engine which Wireshark uses. Running it in a shell could help keeping the capture going. If you still are met with packet drops or other problems maybe another environment and tool may be beneficial, I'm referring to <a href="http://www.ntop.org/products/traffic-recording-replay/n2disk/">n2disk from ntop</a> here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '17, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61645" class="comments-container"></div><div id="comment-tools-61645" class="comment-tools"></div><div class="clear"></div><div id="comment-61645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

