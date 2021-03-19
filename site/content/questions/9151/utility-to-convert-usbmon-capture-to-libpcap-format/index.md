+++
type = "question"
title = "utility to convert usbmon capture to libpcap format"
description = '''I am working on an embedded system. no GUI. Would like to analyze usbmon file offline to see output like wireshark produces. I gather there is no way to do this at the moment since wireshark uses libpcap format.  a) Has someone written a utility to convert usbmon file to correct format. b) if not --...'''
date = "2012-02-20T14:30:00Z"
lastmod = "2012-02-23T21:18:00Z"
weight = 9151
keywords = [ "usbmon" ]
aliases = [ "/questions/9151" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [utility to convert usbmon capture to libpcap format](/questions/9151/utility-to-convert-usbmon-capture-to-libpcap-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9151-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on an embedded system. no GUI. Would like to analyze usbmon file offline to see output like wireshark produces. I gather there is no way to do this at the moment since wireshark uses libpcap format.<br />
</p><p>a) Has someone written a utility to convert usbmon file to correct format. b) if not --&gt; can you point me in the right direction to see if I can do this.</p></div><div id="question-tags" class="tags-container tags">usbmon</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '12, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/c23c9a5c55668ba8fc6724895a527943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pmr&#39;s gravatar image" /><p>pmr<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pmr has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-9151" class="comments-container"></div><div id="comment-tools-9151" class="comment-tools"></div><div class="clear"></div><div id="comment-9151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9188"></span>

<div id="answer-container-9188" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9188-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If your embedded system runs Linux (i.e., if "usbmon" is the Linux USB monitoring mechanism, and the "usbmon file" comes from somehow using usbmon to generate a file, e.g. just dumping the text usbmon output to a text file), then the lack of a GUI wouldn't prevent you from running tcpdump or dumpcap or TShark on the embedded system, and, if the Linux on your embedded system has a sufficiently recent version of libpcap, or if the tcpdump or dumpcap is statically linked with a sufficiently recent version of libpcap (TShark runs dumpcap to do the capture), you should just be able to use tcpdump or dumpcap or TShark to capture using USB, and the output will be in pcap format.</p><p>See <a href="http://wiki.wireshark.org/CaptureSetup/USB">the Wireshark Wiki page on USB capture</a> for more information. If you're already using usbmon on the embedded system, the setup stuff there won't apply, as you've already done what's necessary to get usbmon to work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '12, 21:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9188" class="comments-container"><span id="61014"></span><div id="comment-61014" class="comment"><div id="post-61014-score" class="comment-score"></div><div class="comment-text"><p>I am facing the same issue.. tcpdump or dumpcap or TShark is not installed in Embedded system. I dump/save the raw output of usbmon to a file.</p><p>And for offline debugging, how to decode the usbmon-trace in HOST system (e.g. Ubuntu desktop) to view in Wireshark?</p></div><div id="comment-61014-info" class="comment-info"><span class="comment-age">(24 Apr '17, 09:50)</span> sghorai</div></div></div><div id="comment-tools-9188" class="comment-tools"></div><div class="clear"></div><div id="comment-9188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

