+++
type = "question"
title = "follow tcp stream in wireshark"
description = '''I have a trace file with 2000 streams. I open this trace with wireshark in windows. for my work I need to create separate txt files that each file contains a tcp stream. but in wireshark I can see one stream each time by tcp follow and I should save the stream files one by one! how can I have these ...'''
date = "2013-08-25T04:26:00Z"
lastmod = "2013-08-25T06:27:00Z"
weight = 24018
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/24018" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [follow tcp stream in wireshark](/questions/24018/follow-tcp-stream-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24018-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace file with 2000 streams. I open this trace with wireshark in windows. for my work I need to create separate txt files that each file contains a tcp stream. but in wireshark I can see one stream each time by tcp follow and I should save the stream files one by one! how can I have these streams in separate files in easy way?! many thanks.</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '13, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/372d4c266bc96a0ef9b71b291c582d2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soroor&#39;s gravatar image" /><p>Soroor<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soroor has no accepted answers">0%</span></p></div></div><div id="comments-container-24018" class="comments-container"></div><div id="comment-tools-24018" class="comment-tools"></div><div class="clear"></div><div id="comment-24018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24019"></span>

<div id="answer-container-24019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24019-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to try tools other than Wireshark, e.g. <a href="http://www.circlemud.org/jelson/software/tcpflow/">TCPFlow</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '13, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-24019" class="comments-container"></div><div id="comment-tools-24019" class="comment-tools"></div><div class="clear"></div><div id="comment-24019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24020"></span>

<div id="answer-container-24020" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24020-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use some scripting around <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> to do that:</p><pre><code>for stream in $(tshark -nlr &lt;file&gt; -R tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq)
do
  echo &quot;Processing stream $stream&quot;
  tshark -nlr &lt;file&gt; -qz &quot;follow,tcp,ascii,$stream &gt; stream-$stream.log
done</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '13, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-24020" class="comments-container"><span id="24051"></span><div id="comment-24051" class="comment"><div id="post-24051-score" class="comment-score"></div><div class="comment-text"><p>first many thanks for your answer. actually I am new in this field. I know this code is useful but I have not any idea how can I use it in tshark! I whould be many thankful if you could help me more about running tshark and use of this code.</p></div><div id="comment-24051-info" class="comment-info"><span class="comment-age">(26 Aug '13, 02:43)</span> Soroor</div></div></div><div id="comment-tools-24020" class="comment-tools"></div><div class="clear"></div><div id="comment-24020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

