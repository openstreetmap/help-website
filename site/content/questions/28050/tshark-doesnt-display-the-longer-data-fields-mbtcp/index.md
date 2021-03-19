+++
type = "question"
title = "Tshark doesn&#x27;t display the longer data fields (mbtcp)"
description = '''Hello, I&#x27;m using tshark to get some packets from a pcap file, and some of the data fields (the longer ones) are not displayed. For example: 10.0.100.211 10.0.2.234 68 126 05:03:01:00:00:30 10.0.2.234 10.0.100.211 70 126 07:03:01:00:00:30:08:83 10.0.100.211 10.0.2.234 68 126 05:03:10:00:00:30 10.0.2....'''
date = "2013-12-12T05:58:00Z"
lastmod = "2013-12-15T06:23:00Z"
weight = 28050
keywords = [ "mbtcp", "tshark" ]
aliases = [ "/questions/28050" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark doesn't display the longer data fields (mbtcp)](/questions/28050/tshark-doesnt-display-the-longer-data-fields-mbtcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28050-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm using tshark to get some packets from a pcap file, and some of the data fields (the longer ones) are not displayed. For example:</p><pre><code>10.0.100.211    10.0.2.234  68  126 05:03:01:00:00:30
10.0.2.234  10.0.100.211    70  126 07:03:01:00:00:30:08:83
10.0.100.211    10.0.2.234  68  126 05:03:10:00:00:30
10.0.2.234  10.0.100.211    100 126 
10.0.100.211    10.0.2.234  68  126 05:03:01:0f:ff:51
10.0.2.234  10.0.100.211    70  126 07:03:01:0f:ff:51:00:01
10.0.100.211    10.0.2.234  68  126 05:03:08:00:01:51</code></pre><p>As you can see - the 4th packets' data isn't displayed.</p><p>This is the command line I use:</p><pre><code>tshark.exe -nr 1.pcapng -Y &quot;mbtcp&quot; -T fields -E header=y -e ip.src -e ip.dst -e frame.len -e modbus.func_code -e modbus.data &gt; 1.txt</code></pre><p>And here is some input and output data: <a href="https://www.dropbox.com/sh/9jlq93td5kahhir/a3cZTTWEhd">https://www.dropbox.com/sh/9jlq93td5kahhir/a3cZTTWEhd</a></p><p>I've went over the tshark specs, but it doesn't say anything about fields lengths...</p><p>Is this a bug? Am I missing a flag?</p><p>Nitay</p></div><div id="question-tags" class="tags-container tags">mbtcp tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/cf80c41726cc4ecbf60678ed38645f0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nitay&#39;s gravatar image" /><p>nitay<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nitay has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 15 Dec '13, 01:31</p></div></div><div id="comments-container-28050" class="comments-container"></div><div id="comment-tools-28050" class="comment-tools"></div><div class="clear"></div><div id="comment-28050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28118"></span>

<div id="answer-container-28118" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28118-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think it's a bug.</p><p>As you're using a non-standard Modbus function code (126), the data isn't dissected by the the normal Modbus routines. Instead the data is handed off to any dissectors that are registered in the "Modbus Data" table. This table allows other dissectors to register so that they can dissect data that is outwith the bounds of standard Modbus.</p><p>With my built version of Wireshark (SVN Rev 53869 from /trunk with default preferences), the openSAFETY dissector registers with the Modbus Data table. If the data is greater than the minimum openSAFETY package size (11 bytes) then the openSAFETY dissector tries to dissect it and fails but erroneously tells the Modbus dissector that it <strong>did</strong> dissect the data, so the Modbus dissector doesn't take the fallback option of passing the data to the generic data dissector that produces the hex strings you see in other packets where the data is smaller than the minimum openSAFETY package size.</p><p>To prevent the openSAFETY dissector from attempting to parse the data you can turn the preference off using the command line flag <code>-o "opensafety.enable_mbtcp:0"</code>.</p><p>You should raise an entry on the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a>, attaching your capture to ensure this is fixed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '13, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-28118" class="comments-container"><span id="28212"></span><div id="comment-28212" class="comment"><div id="post-28212-score" class="comment-score"></div><div class="comment-text"><p>filed a bug. Thanks!</p><p>EDIT [@Kurt]: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9572">Bug 9572</a></p></div><div id="comment-28212-info" class="comment-info"><span class="comment-age">(17 Dec '13, 05:56)</span> nitay</div></div></div><div id="comment-tools-28118" class="comment-tools"></div><div class="clear"></div><div id="comment-28118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

