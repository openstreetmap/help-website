+++
type = "question"
title = "tshark time format"
description = '''Hi I add a column using Edit -&amp;gt; Preferences -&amp;gt; Columns. The column that I want to add is the &quot;Absolute date and time&quot; column. with a title &quot;AbsTime&quot;, but it doesn&#x27;t work for me, I get this error :  tshark -r khadidja.pcap -T fields -e frame.number -e col.AbsTime tshark: Some fields aren&#x27;t vali...'''
date = "2016-05-13T06:56:00Z"
lastmod = "2016-05-13T07:54:00Z"
weight = 52509
keywords = [ "absolute_time" ]
aliases = [ "/questions/52509" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark time format](/questions/52509/tshark-time-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52509-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I add a column using Edit -&gt; Preferences -&gt; Columns. The column that I want to add is the "Absolute date and time" column. with a title "AbsTime", but it doesn't work for me, I get this error :</p><blockquote><p>tshark -r khadidja.pcap -T fields -e frame.number -e col.AbsTime</p><p>tshark: Some fields aren't valid: col.AbsTime</p></blockquote><p>can you help me please :)</p></div><div id="question-tags" class="tags-container tags">absolute_time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '16, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/279908d3c8338ae7ec02baa9f51a3c1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Khadidja%20Khadidja&#39;s gravatar image" /><p>Khadidja Kha...<br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Khadidja Khadidja has no accepted answers">0%</span></p></div></div><div id="comments-container-52509" class="comments-container"></div><div id="comment-tools-52509" class="comment-tools"></div><div class="clear"></div><div id="comment-52509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52512"></span>

<div id="answer-container-52512" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As of <a href="https://www.wireshark.org/news/20140731.html">Wireshark 1.12.0</a>, released on July 31, 2014, all the column fields need to be prefixed with <code>_ws.</code>, so you would need to use the following instead:</p><pre><code>tshark -r khadidja.pcap -T fields -e frame.number -e _ws.col.AbsTime</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '16, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-52512" class="comments-container"><span id="52513"></span><div id="comment-52513" class="comment"><div id="post-52513-score" class="comment-score"></div><div class="comment-text"><p>Thanks, it's work perfectly :)</p></div><div id="comment-52513-info" class="comment-info"><span class="comment-age">(13 May '16, 08:00)</span> Khadidja Kha...</div></div><span id="52517"></span><div id="comment-52517" class="comment"><div id="post-52517-score" class="comment-score">1</div><div class="comment-text"><p>As also shown in the tshark help output, although you do have to infer it from the comment:</p><pre><code>-e &lt;field&gt;               field to print if -Tfields selected (e.g. tcp.port,  
                         _ws.col.Info)                                        
                         this option can be repeated to print multiple fields</code></pre></div><div id="comment-52517-info" class="comment-info"><span class="comment-age">(13 May '16, 08:32)</span> grahamb ♦</div></div></div><div id="comment-tools-52512" class="comment-tools"></div><div class="clear"></div><div id="comment-52512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

