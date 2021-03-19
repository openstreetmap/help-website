+++
type = "question"
title = "Transforming a .pcap file to a text file on windows 7 using tshark"
description = '''I want to transform a captured sample .pcap file stored in the windows 7 desktop into a text file on windows 7 command line cmd using tshark. I tried : C:&amp;gt;Program Files&amp;gt;Wireshark&amp;gt; tshark -V -r C:&#92;Users&#92;myName&#92;Desktop&#92;WiresharkLog&#92;SynFlood Sample.pcap &amp;gt; C:&#92;Users&#92;myName&#92;Desktop&#92;logcapture....'''
date = "2012-04-16T18:16:00Z"
lastmod = "2012-04-16T23:11:00Z"
weight = 10205
keywords = [ "text", "windows7", "pcap" ]
aliases = [ "/questions/10205" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Transforming a .pcap file to a text file on windows 7 using tshark](/questions/10205/transforming-a-pcap-file-to-a-text-file-on-windows-7-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10205-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to transform a captured sample .pcap file stored in the windows 7 desktop into a text file on windows 7 command line cmd using tshark. I tried : C:&gt;Program Files&gt;Wireshark&gt; tshark -V -r C:\Users\myName\Desktop\WiresharkLog\SynFlood Sample.pcap &gt; C:\Users\myName\Desktop\<a href="http://logcapture.txt">logcapture.txt</a> When i hit enter after entering this command, the message on the command line says "access is denied." How do i make sure that i can convert a pcap file source into a text file using tshark commands on windows 7 cmd?</p></div><div id="question-tags" class="tags-container tags">text windows7 pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '12, 18:16</strong></p><img src="https://secure.gravatar.com/avatar/94990dfa38fcf1b33157bef842da0291?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misteryuku&#39;s gravatar image" /><p>misteryuku<br />
<span class="score" title="20 reputation points">20</span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misteryuku has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jun '12, 23:28</p></div></div><div id="comments-container-10205" class="comments-container"></div><div id="comment-tools-10205" class="comment-tools"></div><div class="clear"></div><div id="comment-10205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10209"></span>

<div id="answer-container-10209" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10209-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your login name contains spaces, so you might have to quote it on the command line:</p><pre><code>tshark -V -r &quot;C:\Users\Tok Jun Xin\Desktop\WiresharkLog\SynFlood Sample.pcap&quot; &gt; &quot;C:\Users\Tok Jun Xin\Desktop\logcapture.txt&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 23:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jun '12, 20:32</p></div></div><div id="comments-container-10209" class="comments-container"><span id="10210"></span><div id="comment-10210" class="comment"><div id="post-10210-score" class="comment-score"></div><div class="comment-text"><p>When i typed that, the windows 7 command line interface showed this message : tshark: "Sample.pcap" is neither a field or a protocol name. Is there a mistake in the command or there is another problem?</p></div><div id="comment-10210-info" class="comment-info"><span class="comment-age">(16 Apr '12, 23:22)</span> misteryuku</div></div><span id="10211"></span><div id="comment-10211" class="comment"><div id="post-10211-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is there a mistake in the command</p></blockquote><p>Yes. What is the pathname of the capture file? Is <code>C:\Users\Tok Jun Xin\Desktop\WiresharkLog\SynFlood</code> a directory with a <code>Sample.pcap</code> file in it? If so, the command you want is</p><pre><code>tshark -V -r &quot;C:\Users\Tok Jun Xin\Desktop\WiresharkLog\SynFlood\Sample.pcap&quot; &gt; &quot;C:\Users\Tok Jun Xin\Desktop\logcapture.txt&quot;</code></pre></div><div id="comment-10211-info" class="comment-info"><span class="comment-age">(16 Apr '12, 23:32)</span> Guy Harris ♦♦</div></div><span id="10212"></span><div id="comment-10212" class="comment"><div id="post-10212-score" class="comment-score"></div><div class="comment-text"><p>Yeah. That is what i meant</p></div><div id="comment-10212-info" class="comment-info"><span class="comment-age">(16 Apr '12, 23:33)</span> misteryuku</div></div><span id="12156"></span><div id="comment-12156" class="comment"><div id="post-12156-score" class="comment-score"></div><div class="comment-text"><p>OK, I fixed the command line in the answer to reflect the pathname of the capture file being</p><pre><code>C:\Users\Tok Jun Xin\Desktop\WiresharkLog\SynFlood Sample.pcap</code></pre><p>as, when looking at the original question, it looks as if the capture file name is <code>SynFlood Sample.pcap</code> (with a space in the name) and it's in the directory <code>C:\Users\Tok Jun Xin\Desktop\WiresharkLog</code> (with a space in the user name).</p></div><div id="comment-12156-info" class="comment-info"><span class="comment-age">(25 Jun '12, 20:33)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-10209" class="comment-tools"></div><div class="clear"></div><div id="comment-10209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

