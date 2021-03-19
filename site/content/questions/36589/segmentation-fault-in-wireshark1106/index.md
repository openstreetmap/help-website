+++
type = "question"
title = "Segmentation Fault in Wireshark1.10.6"
description = '''Hi Expert,  I am having installed the wireshark version 1.10.6 in my solaris system and trying to open a .pcap file in that, but I am getting an error Segmentation Fault. Here is my command: root@atrcx1220:tail -f /import/MSC/MSC03/RT/20140924083321.pcap | /usr/local/bin/wireshark -k -i - Same comma...'''
date = "2014-09-25T04:06:00Z"
lastmod = "2014-10-20T05:47:00Z"
weight = 36589
keywords = [ "fault", "segmentation", "wireshark1.10.6", "in" ]
aliases = [ "/questions/36589" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Segmentation Fault in Wireshark1.10.6](/questions/36589/segmentation-fault-in-wireshark1106)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36589-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Expert, I am having installed the wireshark version 1.10.6 in my solaris system and trying to open a .pcap file in that, but I am getting an error Segmentation Fault. Here is my command: <strong>[email protected]:tail -f /import/MSC/MSC03/RT/20140924083321.pcap | /usr/local/bin/wireshark -k -i -</strong></p><p>Same command is working fine with Wireshark version 1.8.6.</p><p>And, when I am opening the wireshark1.10.6 using command <strong>[email protected]:./wireshark &amp;</strong>, it opens properly.</p><p>Any help on this is much appriciated. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">fault segmentation wireshark1.10.6 in</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '14, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/97e620804d00012d2cec1885d6422a13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="manojdeoli&#39;s gravatar image" /><p>manojdeoli<br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="manojdeoli has no accepted answers">0%</span></p></div></div><div id="comments-container-36589" class="comments-container"></div><div id="comment-tools-36589" class="comment-tools"></div><div class="clear"></div><div id="comment-36589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37195"></span>

<div id="answer-container-37195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37195-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you able to load the capture file in question into Wireshark? I suspect the problem is that there's something in the capture file that triggers a bug in Wireshark.</p><p>Assuming that's the case then you've got 2 basic options:</p><ol><li>Try upgrading to the latest version of Wireshark (1.12.1) or a development build to see if it fixes the problem.</li><li>(or, especially if (1) does not solve the problem), open a <a href="https://bugs.wireshark.org">bug report</a> together with the sample capture file that causes the crash, and someone will try to fix it.</li></ol><p>If you can't find a capture file that causes the problem then it may be your (unusual) method of starting Wireshark that is causing the problem. Normally "tail -f" is for use with ASCII files. You might want to find a different method.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37195" class="comments-container"><span id="37207"></span><div id="comment-37207" class="comment"><div id="post-37207-score" class="comment-score"></div><div class="comment-text"><p>Well, Wireshark shouldn't crash even if you're piping the output of "tail -f" to it as a capture, so a bug should be filed in any case.</p></div><div id="comment-37207-info" class="comment-info"><span class="comment-age">(20 Oct '14, 12:32)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-37195" class="comment-tools"></div><div class="clear"></div><div id="comment-37195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

