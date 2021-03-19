+++
type = "question"
title = "reconstruct/create a stream file from pcap"
description = '''i have a pcap and filter it to a TCP stream index and source ip. i want to build a file from the packets (reconstruct) streamed data. is there away to do this with Wireshark? or do i need to create my own method for this?'''
date = "2012-03-19T15:38:00Z"
lastmod = "2012-03-19T17:30:00Z"
weight = 9618
keywords = [ "data", "stream" ]
aliases = [ "/questions/9618" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [reconstruct/create a stream file from pcap](/questions/9618/reconstructcreate-a-stream-file-from-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9618-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have a pcap and filter it to a TCP stream index and source ip. i want to build a file from the packets (reconstruct) streamed data.</p><p>is there away to do this with Wireshark? or do i need to create my own method for this?</p></div><div id="question-tags" class="tags-container tags">data stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '12, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/8845605616472c24c3b06854529cf404?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="auldh&#39;s gravatar image" /><p>auldh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="auldh has no accepted answers">0%</span></p></div></div><div id="comments-container-9618" class="comments-container"></div><div id="comment-tools-9618" class="comment-tools"></div><div class="clear"></div><div id="comment-9618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9619"></span>

<div id="answer-container-9619" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9619-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on what you're trying to do.</p><p>If you want all the data from one or both sides of a TCP connection, try using Analyze-&gt;Follow TCP Stream and saving from that.</p><p>If you want an object transferred with, for example, HTTP or the SMB file access protocol, try File-&gt;Export-&gt;Objects-&gt;{HTTP,SMB} (it will offer a list of objects in the capture and let you save one or all of them).</p><p>If neither of those are what you want, you might want to look at <a href="http://afflib.org/software/tcpflow">tcpflow</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '12, 17:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9619" class="comments-container"><span id="9865"></span><div id="comment-9865" class="comment"><div id="post-9865-score" class="comment-score"></div><div class="comment-text"><p>thank you i will do. i only want onside of the stream the receiving side.</p></div><div id="comment-9865-info" class="comment-info"><span class="comment-age">(30 Mar '12, 08:39)</span> auldh</div></div><span id="9876"></span><div id="comment-9876" class="comment"><div id="post-9876-score" class="comment-score"></div><div class="comment-text"><p>the protocol is TCP. i want to extract the <em>TCP segment data</em> of the specified bytes on the receive side/source.</p><p>i want to reconstruct that it is not a VOIP so i can't use the <em>telephony</em> feature.</p></div><div id="comment-9876-info" class="comment-info"><span class="comment-age">(31 Mar '12, 09:36)</span> auldh</div></div><span id="9882"></span><div id="comment-9882" class="comment"><div id="post-9882-score" class="comment-score"></div><div class="comment-text"><p>Then it sounds as if you want the first of my suggestins - Analyze-&gt;Follow TCP Stream, which, as I remember, will let you save only one side of the conversation if you want that.</p></div><div id="comment-9882-info" class="comment-info"><span class="comment-age">(31 Mar '12, 19:17)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9619" class="comment-tools"></div><div class="clear"></div><div id="comment-9619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

