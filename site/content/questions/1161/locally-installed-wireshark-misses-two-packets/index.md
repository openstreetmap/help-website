+++
type = "question"
title = "Locally installed wireshark misses two packets"
description = '''Very strange behavior between Win7 and W2k3. From Win7 &#92;&amp;lt;servername&amp;gt; and the wireshark on that workstation does not capture the session setup request. A laptop running wireshark on a span port of the Win7 device does see the session setup request packets. This coincides with a significant dela...'''
date = "2010-11-29T13:11:00Z"
lastmod = "2010-11-29T13:11:00Z"
weight = 1161
keywords = [ "windows", "7.x", "smb" ]
aliases = [ "/questions/1161" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Locally installed wireshark misses two packets](/questions/1161/locally-installed-wireshark-misses-two-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1161-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Very strange behavior between Win7 and W2k3. From Win7 \&lt;servername&gt; and the wireshark on that workstation does not capture the session setup request. A laptop running wireshark on a span port of the Win7 device does see the session setup request packets. This coincides with a significant delay in actually seeing the shares on the server.</p><p>There are lots of theories and work arounds for the issue, but they don't seem to change that the setup request packet is missed by wireshark but is put on the wire.</p><p>Anyone have any thoughts?</p><p>Mike</p></div><div id="question-tags" class="tags-container tags">windows 7.x smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '10, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/5a43b9da657dcd22050e7564f3f4ac55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoeChieftain&#39;s gravatar image" /><p>JoeChieftain<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoeChieftain has no accepted answers">0%</span></p></div></div><div id="comments-container-1161" class="comments-container"><span id="1163"></span><div id="comment-1163" class="comment"><div id="post-1163-score" class="comment-score"></div><div class="comment-text"><p>Mike, some questions 1) Are you capturing the packets from boot up? Many CIFS sessions are long-lived.<br />
2) Are you filtering the capture? Remember, the conversation can be happening with the AD server, or any other server that's housing the virtual share.</p><p>If you are capturing from boot up <em>without</em> any filters, I would say it's a bug. But if not, I would say it's a filtering (most likely) problem.</p></div><div id="comment-1163-info" class="comment-info"><span class="comment-age">(29 Nov '10, 13:53)</span> hansangb</div></div><span id="1206"></span><div id="comment-1206" class="comment"><div id="post-1206-score" class="comment-score"></div><div class="comment-text"><p>I think if he can capture it on a spanned port, but not on the local system then he's just missed the packets. This is an example of why one would capture on a spanned port or even better a tap me thinks.</p></div><div id="comment-1206-info" class="comment-info"><span class="comment-age">(02 Dec '10, 00:26)</span> lchappell ♦</div></div></div><div id="comment-tools-1161" class="comment-tools"></div><div class="clear"></div><div id="comment-1161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

