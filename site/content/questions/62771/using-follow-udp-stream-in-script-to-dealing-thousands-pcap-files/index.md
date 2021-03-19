+++
type = "question"
title = "using follow udp stream&#x27; in script to dealing thousands pcap files"
description = '''Thanks. Maybe this is another question: I wrote a script to deal with multiple files as follows: #!/bin/bash for file in &#x27;datadir/*&#x27; do  tshark -r $file -R &#x27;(ip.addr eq 10.0.072 and ip.addr eq 10.0.1.102) and (udp.port eq 65505 and udp.port eq 4005)&#x27; -T fields -e data | tr -d &#x27;&#92;n&#x27; &amp;gt; $file.raw  if...'''
date = "2017-07-13T19:24:00Z"
lastmod = "2017-07-14T04:14:00Z"
weight = 62771
keywords = [ "tshark" ]
aliases = [ "/questions/62771" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [using follow udp stream' in script to dealing thousands pcap files](/questions/62771/using-follow-udp-stream-in-script-to-dealing-thousands-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62771-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thanks. Maybe this is another question:</p><p>I wrote a script to deal with multiple files as follows: <code></code></p><pre><code>#!/bin/bash
for file in &#39;datadir/*&#39;
do
    tshark -r $file -R &#39;(ip.addr eq 10.0.072 and ip.addr eq 10.0.1.102) and (udp.port eq 65505 and udp.port eq 4005)&#39; -T fields -e data | tr -d &#39;\n&#39; &gt; $file.raw</code></pre><p>if only 1 file in the datadir, i got one output file, but it fails if the files in datadir more than one.</p><p>Here is the message from system: tshark: Read filters were specified both with "-R" and with additional command-line arguments</p><p>Have i done something wrong?</p><p>Thanks for any hint.</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '17, 19:24</strong></p><img src="https://secure.gravatar.com/avatar/5c7f90f23654a6f637a2c1955a6fbd66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tree0520&#39;s gravatar image" /><p>tree0520<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tree0520 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 13 Jul '17, 22:42</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-62771" class="comments-container"><span id="62772"></span><div id="comment-62772" class="comment"><div id="post-62772-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a question as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-62772-info" class="comment-info"><span class="comment-age">(13 Jul '17, 22:43)</span> Jaap ♦</div></div></div><div id="comment-tools-62771" class="comment-tools"></div><div class="clear"></div><div id="comment-62771-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62775"></span>

<div id="answer-container-62775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62775-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess your for loop is wrong: the file variable contains a list of all files.</p><p>Better run:</p><pre><code>for file in `ls -1 datadir/*`</code></pre><p>Furthermore, when calling tshark with '-R' you also have to use '-2' or use single-pass filtering with '-Y'</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '17, 04:14</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-62775" class="comments-container"><span id="62782"></span><div id="comment-62782" class="comment"><div id="post-62782-score" class="comment-score"></div><div class="comment-text"><p>Well, as for me, the correct syntax would be</p><pre><code>for file in datadir/*</code></pre><p>or</p><pre><code>for file in $(ls datadir/*)</code></pre></div><div id="comment-62782-info" class="comment-info"><span class="comment-age">(14 Jul '17, 08:46)</span> sindy</div></div></div><div id="comment-tools-62775" class="comment-tools"></div><div class="clear"></div><div id="comment-62775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

