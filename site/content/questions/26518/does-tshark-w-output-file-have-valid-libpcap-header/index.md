+++
type = "question"
title = "Does tshark -w output file have valid libpcap header?"
description = '''Having written a file using tshark -w option, I find when I read the file the libpcap header has key values set to null:  magic 0 version_major 0 version_minor 0 thiszone 0 I was expecting values as given in this spec.'''
date = "2013-10-29T09:33:00Z"
lastmod = "2013-10-29T11:56:00Z"
weight = 26518
keywords = [ "tshark", "libpcap" ]
aliases = [ "/questions/26518" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Does tshark -w output file have valid libpcap header?](/questions/26518/does-tshark-w-output-file-have-valid-libpcap-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26518-score" class="post-score" title="current number of votes">0</div><span id="post-26518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Having written a file using tshark -w option, I find when I read the file the libpcap header has key values set to null: <code> magic          0 version_major   0 version_minor   0 thiszone      0</code></p><p>I was expecting values as given in <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat#Global_Header">this spec</a>.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '13, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/310c7b54264c9e10ad43acb3bb1d042a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiggers&#39;s gravatar image" /><p><span>wiggers</span><br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiggers has no accepted answers">0%</span></p></div></div><div id="comments-container-26518" class="comments-container"></div><div id="comment-tools-26518" class="comment-tools"></div><div class="clear"></div><div id="comment-26518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26519"></span>

<div id="answer-container-26519" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26519-score" class="post-score" title="current number of votes">1</div><span id="post-26519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wiggers has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>tshark</code> now writes pcapng files by default, so if you want a pcap file, you will need to specify <code>-F pcap</code>. If you want to understand the pcapng file format, then refer to the "<a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html">PCAP Next Generation Dump File Format</a>" page.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '13, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-26519" class="comments-container"><span id="26526"></span><div id="comment-26526" class="comment"><div id="post-26526-score" class="comment-score"></div><div class="comment-text"><p>If you're using your own code to read libpcap files, please consider using libpcap instead. Libpcap 1.1.0 and later supports reading pcap and pcap-ng files, as long, in the pcap-ng files, all network interfaces have the same link-layer header type and snapshot length (due to current libpcap API limitations).</p><p>Unfortunately, there isn't yet a version of WinPcap based on libpcap 1.1.0 or later, so that won't work on Windows.</p><p>If you can't use libpcap, see the page Chris Maynard cited, and use that to write your own code to read those files.</p></div><div id="comment-26526-info" class="comment-info"><span class="comment-age">(29 Oct '13, 11:56)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-26519" class="comment-tools"></div><div class="clear"></div><div id="comment-26519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

