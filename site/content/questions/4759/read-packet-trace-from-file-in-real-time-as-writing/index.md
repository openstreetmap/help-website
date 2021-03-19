+++
type = "question"
title = "Read packet trace from file in real time as writing"
description = '''For example I write a packet trace in file with tcpdump: tcpdump -w file.pcap By now i need reopen whole file for every new entry. Maybe wireshark can read the file as write without reopen? Like as doing in UNIX: tail -F file.pcap'''
date = "2011-06-26T08:30:00Z"
lastmod = "2011-06-26T09:00:00Z"
weight = 4759
keywords = [ "tail", "file" ]
aliases = [ "/questions/4759" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Read packet trace from file in real time as writing](/questions/4759/read-packet-trace-from-file-in-real-time-as-writing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4759-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For example I write a packet trace in file with tcpdump:</p><p><strong>tcpdump -w file.pcap</strong></p><p>By now i need reopen whole file for every new entry. Maybe wireshark can read the file as write without reopen? Like as doing in UNIX: <strong>tail -F file.pcap</strong></p></div><div id="question-tags" class="tags-container tags">tail file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '11, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/67a3a51ea6e8fe061569f79e9495702b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhovner&#39;s gravatar image" /><p>zhovner<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhovner has no accepted answers">0%</span></p></div></div><div id="comments-container-4759" class="comments-container"></div><div id="comment-tools-4759" class="comment-tools"></div><div class="clear"></div><div id="comment-4759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4761"></span>

<div id="answer-container-4761" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4761-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found solution in using pipes http://wiki.wireshark.org/CaptureSetup/Pipes</p><p>Unfortunately I can't use pipes by following this instruction in Mac OS X 10.5.</p><p>This works for me:</p><p><strong>sudo /Applications/Wireshark.app/Contents/Resources/bin/wireshark -k -i &lt;(tail -n 100000000000 -F dump.pcap)</strong></p><p><strong>tail -n 100000000000</strong> - is for jump to begining of file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '11, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/67a3a51ea6e8fe061569f79e9495702b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zhovner&#39;s gravatar image" /><p>zhovner<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zhovner has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '11, 13:43</p></div></div><div id="comments-container-4761" class="comments-container"><span id="23794"></span><div id="comment-23794" class="comment"><div id="post-23794-score" class="comment-score"></div><div class="comment-text"><p>A better approach would be to use <code>tail -c +0</code> or <code>tail -n +0</code> if you want to list all data from the beginning of the file.</p><p>Your final command will look like this: <code>sudo /Applications/Wireshark.app/Contents/Resources/bin/wireshark -k -i &lt;(tail -c +0 -F dump.pcap)</code></p></div><div id="comment-23794-info" class="comment-info"><span class="comment-age">(15 Aug '13, 03:03)</span> Sergei</div></div></div><div id="comment-tools-4761" class="comment-tools"></div><div class="clear"></div><div id="comment-4761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

