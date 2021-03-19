+++
type = "question"
title = "Tshark -Windows, disable internal ports number resolution"
description = '''tshark -Nt -f &quot;host abc.com&quot;  this command in Windows will be make internal and external ports number resolution:  1 0.000000 10.0.2.15 -&amp;gt; 92.223.112.104 TCP 62 ardus-cntl https [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1  2 0.020856 92.223.112.104 -&amp;gt; 10.0.2.15 TCP 60 https ardus-cntl [SY...'''
date = "2014-12-18T06:53:00Z"
lastmod = "2014-12-18T07:47:00Z"
weight = 38623
keywords = [ "tshark" ]
aliases = [ "/questions/38623" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark -Windows, disable internal ports number resolution](/questions/38623/tshark-windows-disable-internal-ports-number-resolution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38623-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>tshark -Nt -f &quot;host abc.com&quot;</code></pre><p>this command in Windows will be make internal and external ports number resolution:</p><pre><code>  1   0.000000    10.0.2.15 -&gt; 92.223.112.104 TCP 62 ardus-cntl https [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1
  2   0.020856 92.223.112.104 -&gt; 10.0.2.15    TCP 60 https ardus-cntl [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460
  3   0.020914    10.0.2.15 -&gt; 92.223.112.104 TCP 54 ardus-cntl https [ACK] Seq=1 Ack=1 Win=64240 Len=0
  4   0.022235    10.0.2.15 -&gt; 92.223.112.104 SSL 376 Continuation Data</code></pre><p>but in Ubuntu happen only external ports number resolution</p><pre><code>0.000000    10.0.2.15 -&gt; 92.223.112.104 TCP 62 1116 https [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1
0.020856 92.223.112.104 -&gt; 10.0.2.15    TCP 60 https 1116 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1460
0.020914    10.0.2.15 -&gt; 92.223.112.104 TCP 54 1116 https [ACK] Seq=1 Ack=1 Win=64240 Len=0
0.022235    10.0.2.15 -&gt; 92.223.112.104 SSL 376 Continuation Data</code></pre><p>How to make only external ports number resolution in Windows?</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '14, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/356961d480eb308238931511a398a65f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="regexmix&#39;s gravatar image" /><p>regexmix<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="regexmix has no accepted answers">0%</span></p></div></div><div id="comments-container-38623" class="comments-container"><span id="38626"></span><div id="comment-38626" class="comment"><div id="post-38626-score" class="comment-score"></div><div class="comment-text"><p>What versions are you using on the two OS's? What do you mean by "internal" and "external" ports"?</p></div><div id="comment-38626-info" class="comment-info"><span class="comment-age">(18 Dec '14, 07:52)</span> grahamb ♦</div></div><span id="38628"></span><div id="comment-38628" class="comment"><div id="post-38628-score" class="comment-score"></div><div class="comment-text"><pre><code>1   0.000000    10.0.2.15 -&gt; 92.223.112.104 TCP 62 ardus-cntl https [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1</code></pre><p>here is:</p><p>ardus-cntl -&gt;internal port</p><p>https -&gt;external port</p><hr /><p>Windows XP</p><p>TShark 1.6.7</p><p>wireshark 1.6.7</p></div><div id="comment-38628-info" class="comment-info"><span class="comment-age">(18 Dec '14, 08:09)</span> regexmix</div></div></div><div id="comment-tools-38623" class="comment-tools"></div><div class="clear"></div><div id="comment-38623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38625"></span>

<div id="answer-container-38625" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38625-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can just turn the resolution on or off not select if it should be for only SRC or DST.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '14, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Dec '14, 07:47</p></div></div><div id="comments-container-38625" class="comments-container"></div><div id="comment-tools-38625" class="comment-tools"></div><div class="clear"></div><div id="comment-38625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

