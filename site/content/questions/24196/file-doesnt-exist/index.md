+++
type = "question"
title = "file doesn&#x27;t exist!"
description = '''Hi, I wrote this code in cygwin in windows:  file=c:&#92;man.pcap for stream in $(tshark -nlr $file -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq) do  echo &quot;Processing stream $stream&quot;  tshark -nlr $file -qz &quot;follow,tcp,ascii,$stream&quot; &amp;gt; stream-$stream.log done  but I got this error mess...'''
date = "2013-08-30T07:05:00Z"
lastmod = "2013-08-30T07:34:00Z"
weight = 24196
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/24196" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [file doesn't exist!](/questions/24196/file-doesnt-exist)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24196-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I wrote this code in cygwin in windows:</p><pre><code>file=c:\man.pcap
for stream in $(tshark -nlr $file -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq)
do
  echo &quot;Processing stream $stream&quot;
  tshark -nlr $file -qz &quot;follow,tcp,ascii,$stream&quot; &gt; stream-$stream.log
done</code></pre><p>but I got this error message: tshark: The file "c:man.pcap" doesn't exist.</p><p>the file "man.pcap" is located in C drive. I haven't any idea for fix this problem.What should I do? tnx for ur attention.</p></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Aug '13, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/372d4c266bc96a0ef9b71b291c582d2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soroor&#39;s gravatar image" /><p>Soroor<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soroor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Aug '13, 07:49</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-24196" class="comments-container"></div><div id="comment-tools-24196" class="comment-tools"></div><div class="clear"></div><div id="comment-24196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24198"></span>

<div id="answer-container-24198" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24198-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use a forward "/" slash in the path spec, e.g. <code>C:/man.pcap</code>. Cygwin thinks a backlash is escaping the next character.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '13, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24198" class="comments-container"><span id="24213"></span><div id="comment-24213" class="comment"><div id="post-24213-score" class="comment-score">1</div><div class="comment-text"><p>Or try</p><pre><code>file=c:\\man.pcap</code></pre><p>so that Cygwin thinks that's a literal backslash, rather than a backslash escaping the next character.</p></div><div id="comment-24213-info" class="comment-info"><span class="comment-age">(30 Aug '13, 13:17)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-24198" class="comment-tools"></div><div class="clear"></div><div id="comment-24198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

