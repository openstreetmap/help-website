+++
type = "question"
title = "Export xml data - Any workaround for [truncated]?"
description = '''I&#x27;ve seen a few questions about the [truncated] problem, but no good answers. I&#x27;ve tried both WireShark and tshark. I&#x27;d like to export http/xml data from a .pcapng file. Any format would be fine (I can manipulate raw bytes or whatever), but my requirements are that packets are reassembled (i.e. enti...'''
date = "2016-02-23T11:49:00Z"
lastmod = "2016-02-25T11:40:00Z"
weight = 50447
keywords = [ "export" ]
aliases = [ "/questions/50447" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Export xml data - Any workaround for \[truncated\]?](/questions/50447/export-xml-data-any-workaround-for-truncated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50447-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've seen a few questions about the [truncated] problem, but no good answers. I've tried both WireShark and tshark. I'd like to export http/xml data from a .pcapng file. Any format would be fine (I can manipulate raw bytes or whatever), but my requirements are that packets are reassembled (i.e. entire conversation), and that the data is not truncated.<br />
</p></div><div id="question-tags" class="tags-container tags">export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '16, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/7d1bd4bcd2430996dcd2c87af31d4b40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DennisR&#39;s gravatar image" /><p>DennisR<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DennisR has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-50447" class="comments-container"></div><div id="comment-tools-50447" class="comment-tools"></div><div class="clear"></div><div id="comment-50447-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50513"></span>

<div id="answer-container-50513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50513-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It might help if you were a bit more specific about what you'd like to export. For now I'll assume you want to export the entire http stream which would mean that the "-z follow" option to tshark would be ideal.</p><p><a href="https://ask.wireshark.org/questions/10023/command-line-option-for-follow-tcp-stream">Another answer</a> also suggests using <a href="http://linux.die.net/man/1/tcpflow">tcpflow</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '16, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-50513" class="comments-container"><span id="50518"></span><div id="comment-50518" class="comment"><div id="post-50518-score" class="comment-score"></div><div class="comment-text"><p>Yes, I'd like to see the entire http stream. I tried tshark.exe" -r "myfile.pcapng" -z follow and it complained: tshark: Invalid -z argument "follow"; it must be one of: ... (I also tried "-z follow.tcp" and got the same error)</p><p>I looked into tcpflow. I had to editcap convert from pcapng to pcap, and and deal with the thousands of files tcpflow generates, but I think this will work. Thanks.</p></div><div id="comment-50518-info" class="comment-info"><span class="comment-age">(25 Feb '16, 15:11)</span> DennisR</div></div><span id="50522"></span><div id="comment-50522" class="comment"><div id="post-50522-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark/tshark are you using? Does "-z follow" show up in the man page/help (tshark -z help)? It may be the version you're using is too old (pre-1.8?!?).</p><p>Note that it's "follow,tcp", not "follow.tcp".</p></div><div id="comment-50522-info" class="comment-info"><span class="comment-age">(25 Feb '16, 16:09)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-50513" class="comment-tools"></div><div class="clear"></div><div id="comment-50513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

