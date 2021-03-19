+++
type = "question"
title = "Wireshark doesn&#x27;t work correctly with rvi0 on MacOS X 10.9.5"
description = '''On MacOS X 10.9.4, Wireshark 1.12.1 (v1.12.1-0-g01b65bf from master-1.12) worked with rvi0 interface without any problems. After update to 10.9.5, I see just  Source=00.00.00 Dest. = 00.00.00 Protocol = FC Info = Unknown frame (Bogus Fragment)  for any package on rvi0. Live capturing just stop worki...'''
date = "2014-09-24T11:29:00Z"
lastmod = "2014-09-24T17:05:00Z"
weight = 36570
keywords = [ "live", "macosx", "livecapturetcp", "rvi0" ]
aliases = [ "/questions/36570" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark doesn't work correctly with rvi0 on MacOS X 10.9.5](/questions/36570/wireshark-doesnt-work-correctly-with-rvi0-on-macos-x-1095)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36570-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On MacOS X 10.9.4, Wireshark 1.12.1 (v1.12.1-0-g01b65bf from master-1.12) worked with rvi0 interface without any problems. After update to 10.9.5, I see just</p><pre><code>Source=00.00.00
Dest. = 00.00.00
Protocol = FC
Info = Unknown frame (Bogus Fragment)</code></pre><p>for any package on rvi0. Live capturing just stop working for rvi0. At the same time, Wireshark works ok with any other interfaces, as well as it parses tcpdump's out for rvi0 well.</p><p>Could you please tell what happened to live capturing on rvi0?</p></div><div id="question-tags" class="tags-container tags">live macosx livecapturetcp rvi0</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '14, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/bd81007fb5768cea2e679ee9b60084eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dimakovalenko&#39;s gravatar image" /><p>dimakovalenko<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dimakovalenko has no accepted answers">0%</span></p></div></div><div id="comments-container-36570" class="comments-container"></div><div id="comment-tools-36570" class="comment-tools"></div><div class="clear"></div><div id="comment-36570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36575"></span>

<div id="answer-container-36575" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36575-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I suspect Apple "improved" the rvi mechanism in an incompatible fashion, breaking the DLT_PKTAP format.</p><p>Please file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and save one of the bad captures from 10.9.5 to a file and attach the file so we can see what the result of their "improvements" are.</p><p>UPDATE: no, based on the data in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10502">the bug you filed</a> (thanks), we weren't using the header length field in the pktap header to determine where the packet payload was, and Apple made the PKTAP header bigger in 10.9.5, so we weren't correctly dissecting packets in captures done on 10.9.5. A fix has been checked in on the trunk and the 1.12 branch, so the 1.12.2 release, when it comes out, should be able to dissect the packets (and should be able to handle future lengthening of the PKTAP header).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '14, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '14, 01:31</p></div></div><div id="comments-container-36575" class="comments-container"><span id="36588"></span><div id="comment-36588" class="comment"><div id="post-36588-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris: Thanks a lot for your support! Is there any workaround? E.g. to add something to Edit-&gt;Preferences-&gt;Protocols&gt;DLT_USER-&gt;Edit Encapsulations Table? I am thinking about (temporary) using other network capturing tool, and then back to Wireshark 1.12.2. May be I should not do it because it's possible to fix the problem with some workaround right now?</p></div><div id="comment-36588-info" class="comment-info"><span class="comment-age">(25 Sep '14, 03:58)</span> dimakovalenko</div></div><span id="36613"></span><div id="comment-36613" class="comment"><div id="post-36613-score" class="comment-score"></div><div class="comment-text"><p>You could try downloading the latest "Wireshark 1.12.2rc0 ... Intel 64.dmg" build from the automated build section of one of the Wireshark download sites. Go to <a href="https://www.wireshark.org/download/automated/osx/">https://www.wireshark.org/download/automated/osx/</a> and pick the most recent 1.12.2 Intel 64 build. Those builds have the fix.</p></div><div id="comment-36613-info" class="comment-info"><span class="comment-age">(25 Sep '14, 11:57)</span> Guy Harris ♦♦</div></div><span id="36622"></span><div id="comment-36622" class="comment"><div id="post-36622-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.wireshark.org/download/automated/osx/Wireshark%201.12.2rc0-32-gce0e169%20Intel%2064.dmg">https://www.wireshark.org/download/automated/osx/Wireshark%201.12.2rc0-32-gce0e169%20Intel%2064.dmg</a> works just perfect! Thanks a lot! No need to temporary switch to other tool.</p></div><div id="comment-36622-info" class="comment-info"><span class="comment-age">(26 Sep '14, 00:09)</span> dimakovalenko</div></div></div><div id="comment-tools-36575" class="comment-tools"></div><div class="clear"></div><div id="comment-36575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

