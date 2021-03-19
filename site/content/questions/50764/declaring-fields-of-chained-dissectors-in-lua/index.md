+++
type = "question"
title = "Declaring fields of chained dissectors in lua"
description = '''Hi,  I started to make a lua port of the PTP/IP dissector split into the PTP/IP part and an dependent an PTP part. The idea is the PTP/IP dissector parses the IP specific structure parts (length, packet type) and then passes these to an PTP packet dissector. However, in the PTP dissector I can not d...'''
date = "2016-03-08T04:43:00Z"
lastmod = "2016-04-27T14:56:00Z"
weight = 50764
keywords = [ "lua", "sub-dissector" ]
aliases = [ "/questions/50764" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Declaring fields of chained dissectors in lua](/questions/50764/declaring-fields-of-chained-dissectors-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50764-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I started to make a lua port of the PTP/IP dissector split into the PTP/IP part and an dependent an PTP part. The idea is the PTP/IP dissector parses the IP specific structure parts (length, packet type) and then passes these to an PTP packet dissector.</p><p>However, in the PTP dissector I can not declare the 'imported' fields of the PTP/IP dissector:</p><p>top level</p><pre><code>local length_field = Field.new(&quot;ptp.length&quot;)
local packet_type_field = Field.new(&quot;ptp.pktType&quot;)   
local header_offset_field = Field.new(&quot;ptp.headerOffset&quot;) -- protocol specific offset from the PTP/IP or PTP dissector</code></pre><p>results in an error message <strong>bad argument #1 to 'new' (Field new: a field with this name must exist)</strong>.</p><p>When I move it to <code>function ptp_proto.dissector(tvb,pinfo,tree)</code> the error message is <strong>(Field new: A Field extractor must be defined before Taps or Dissectors are called)</strong></p></div><div id="question-tags" class="tags-container tags">lua sub-dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '16, 04:43</strong></p><img src="https://secure.gravatar.com/avatar/4875dbde2eebdc54b43edef7b9c29473?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20E&#39;s gravatar image" /><p>Thomas E<br />
<span class="score" title="36 reputation points">36</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas E has no accepted answers">0%</span></p></div></div><div id="comments-container-50764" class="comments-container"></div><div id="comment-tools-50764" class="comment-tools"></div><div class="clear"></div><div id="comment-50764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52024"></span>

<div id="answer-container-52024" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52024-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe this is due to the order which Wireshark finds &amp; executes your .lua files. Try creating a new script that initializes your dissectors in correct order.</p><p>Renaming your files in alphabetical order could also work .. if sorting order of read .lua files is the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '16, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/ce127a4716cc9b4c3401c9c47820f336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kim&#39;s gravatar image" /><p>kim<br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kim has one accepted answer">50%</span></p></div></div><div id="comments-container-52024" class="comments-container"><span id="53051"></span><div id="comment-53051" class="comment"><div id="post-53051-score" class="comment-score"></div><div class="comment-text"><p>It worked. The 'parent' dissector needs to load before the child dissectors. An implementation is at <a href="https://github.com/tengelmeier/mtp-tools/">https://github.com/tengelmeier/mtp-tools/</a></p></div><div id="comment-53051-info" class="comment-info"><span class="comment-age">(30 May '16, 07:49)</span> Thomas E</div></div></div><div id="comment-tools-52024" class="comment-tools"></div><div class="clear"></div><div id="comment-52024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

