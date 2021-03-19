+++
type = "question"
title = "Conversion : Invalid data length 2110274 (runs past the end of the record)"
description = '''Hello everybody, 1st I speak French, so please excuse my mistakes. I&#x27;m trying to convert a txt capture in a pcap format, but I see this error: The capture file appears to be damaged or corrupt. (vwr: Invalid data length 2110274 (runs past the end of the record))  It has taken me 2 days to try to sol...'''
date = "2014-08-28T02:32:00Z"
lastmod = "2014-08-28T02:32:00Z"
weight = 35833
keywords = [ "capture", "convert", "packets", "conversationcapture", "wireshark" ]
aliases = [ "/questions/35833" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Conversion : Invalid data length 2110274 (runs past the end of the record)](/questions/35833/conversion-invalid-data-length-2110274-runs-past-the-end-of-the-record)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35833-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody,</p><p>1st I speak French, so please excuse my mistakes. I'm trying to convert a txt capture in a pcap format, but I see this error:</p><pre><code>The capture file appears to be damaged or corrupt.
(vwr: Invalid data length 2110274 (runs past the end of the record))</code></pre><p>It has taken me 2 days to try to solve that. Please, can someone help me? Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">capture convert packets conversationcapture wireshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '14, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/d18e4540b563eddaa4be168e11eedd71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Schadrac%20Akroman&#39;s gravatar image" /><p>Schadrac Akr...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Schadrac Akroman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Aug '14, 08:29</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-35833" class="comments-container"><span id="35841"></span><div id="comment-35841" class="comment"><div id="post-35841-score" class="comment-score"></div><div class="comment-text"><p>To be sure I (we?) understand the question, you're trying to convert a text file of a format similar to the following to a binary .pcap file format, is that correct?</p><pre><code>000000 00 e0 1e a7 05 6f 00 10 ........
000008 5a a0 b9 12 08 00 46 00 ........
000010 03 68 00 00 00 00 0a 2e ........
000018 ee 33 0f 19 08 7f 0f 19 ........
000020 03 80 94 04 00 00 10 01 ........
000028 16 a2 0a 00 03 50 00 0c ........
000030 01 01 0f 19 03 80 11 01 ........</code></pre><p>The above sample was taken from the <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap.html</a> man page.</p><p>Is that what you're trying to use, <code>text2pcap</code>, to do the conversion? If so, which version of text2pcap are you using; if not, which tool are you using?</p><p>Maybe you could provide a sample of the data you're trying to convert?</p></div><div id="comment-35841-info" class="comment-info"><span class="comment-age">(28 Aug '14, 08:27)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-35833" class="comment-tools"></div><div class="clear"></div><div id="comment-35833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

