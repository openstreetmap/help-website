+++
type = "question"
title = "Whether Wireshark will be more than protocol analyser?"
description = '''Whether Wireshark will be more than protocol analyser? Currently it is, but is it official way? Wireshark can open files like MP3, JPG, GIF, PNG and XMLs. Could we treat Wireshark as &quot;file format analyser&quot;? Than can be added support to open text-file and binary files? Is it possible to send file for...'''
date = "2013-04-17T04:50:00Z"
lastmod = "2013-04-17T07:58:00Z"
weight = 20512
keywords = [ "binary", "file-format", "mime", "text" ]
aliases = [ "/questions/20512" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Whether Wireshark will be more than protocol analyser?](/questions/20512/whether-wireshark-will-be-more-than-protocol-analyser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20512-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Whether Wireshark will be more than protocol analyser? Currently it is, but is it official way? Wireshark can open files like MP3, JPG, GIF, PNG and XMLs. Could we treat Wireshark as "file format analyser"? Than can be added support to open text-file and binary files? Is it possible to send file format dissector? (for example ".tar", ".dll").</p><p>It will be nice to see that features.</p></div><div id="question-tags" class="tags-container tags">binary file-format mime text</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '13, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/45a69e9e5c0af55bfef57c8c6b637a95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michal%20Labedzki&#39;s gravatar image" /><p>Michal Labedzki<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michal Labedzki has no accepted answers">0%</span></p></div></div><div id="comments-container-20512" class="comments-container"></div><div id="comment-tools-20512" class="comment-tools"></div><div class="clear"></div><div id="comment-20512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20523"></span>

<div id="answer-container-20523" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20523-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is first and foremost a protocol analyzer. But its dissection engine architecture however is so flexible that one can envision it having a higher abstraction as 'record analyzer'. These records come in from a source, being a pipe from dumpcap, a (capture) file contents from wiretap or otherwise. That is where your experiments come into view. You open, through wiretap, files containing records, which the dissection engine happen to know how to handle.</p><p>It's very important to understand the distinction between file and record format. JPEG is the record format, while JFIF is the file format (even the Joint Picture Experts Group missed this and forgot to specify JFIF). Same goes for MP3.</p><p>TLDR; At best the dissection engine in Wireshark / Tshark is a record analyzer, where Wireshark / Tshark are tailored to network protocols. File formats are just containers for records, these won't be analyzed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '13, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-20523" class="comments-container"></div><div id="comment-tools-20523" class="comment-tools"></div><div class="clear"></div><div id="comment-20523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20513"></span>

<div id="answer-container-20513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20513-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark cannot open files like MP3, JPG etc, it can extract those file types from network packets contained in capture/trace files. The file formats Wireshark reads are listed here: <a href="http://wiki.wireshark.org/FileFormatReference">http://wiki.wireshark.org/FileFormatReference</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '13, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Apr '13, 04:57</p></div></div><div id="comments-container-20513" class="comments-container"><span id="20515"></span><div id="comment-20515" class="comment"><div id="post-20515-score" class="comment-score"></div><div class="comment-text"><p>Actually:</p><pre><code>tshark -r 01\ Don\&#39;t\ Know\ Why.mp3 
  1 0.000000000              -&gt;              ID3v2 4352 
  2 0.000000000     320 kb/s -&gt; 44,1 kHz     MPEG-1 1044 Audio Layer 3
  3 0.026121600     320 kb/s -&gt; 44,1 kHz     MPEG-1 1044 Audio Layer 3
  4 0.052243200     320 kb/s -&gt; 44,1 kHz     MPEG-1 1044 Audio Layer 3
  5 0.078364800     320 kb/s -&gt; 44,1 kHz     MPEG-1 1044 Audio Layer 3

[email protected]:~$ tshark -r /Applications/1Password.app/Contents/Import/images/ImportFirefoxPasswords.jpg 
  1                         -&gt;              MIME_FILE 34863 
  2                         -&gt;              MIME_FILE 0 
[email protected]:~$</code></pre><p>:-)</p></div><div id="comment-20515-info" class="comment-info"><span class="comment-age">(17 Apr '13, 05:08)</span> SYN-bit ♦♦</div></div><span id="20517"></span><div id="comment-20517" class="comment"><div id="post-20517-score" class="comment-score"></div><div class="comment-text"><p>Okay, learning something new every day... but what is this good for? I guess it's some sort of dissector test?</p><p>Anyway, lesson learned and documented at <a href="http://blog.packet-foo.com/2013/04/learning-something-new-every-day/">http://blog.packet-foo.com/2013/04/learning-something-new-every-day/</a> :-)</p></div><div id="comment-20517-info" class="comment-info"><span class="comment-age">(17 Apr '13, 05:23)</span> Jasper ♦♦</div></div></div><div id="comment-tools-20513" class="comment-tools"></div><div class="clear"></div><div id="comment-20513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

