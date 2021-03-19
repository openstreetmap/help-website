+++
type = "question"
title = "Scripting Follow TCP Stream -&gt; Save As [Raw]"
description = '''I captured HTTP traffic using tcpdump. For each TCP stream I want to extract the RAW TCP contents, ideally all streams to the same file.  Manually, I am currently doing the following: for each $i:  select tcp.stream eq $i  Save As [Raw] to file$i concatenate files  Is there any way to script this us...'''
date = "2016-06-30T04:38:00Z"
lastmod = "2016-06-30T05:53:00Z"
weight = 53747
keywords = [ "raw", "http", "file", "tcp" ]
aliases = [ "/questions/53747" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Scripting Follow TCP Stream -&gt; Save As \[Raw\]](/questions/53747/scripting-follow-tcp-stream-save-as-raw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53747-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured HTTP traffic using tcpdump. For each TCP stream I want to extract the RAW TCP contents, ideally all streams to the same file.</p><p>Manually, I am currently doing the following:</p><pre><code>for each $i:
  select tcp.stream eq $i
  Save As [Raw] to file$i
concatenate files</code></pre><p>Is there any way to script this using thark? I was trying for quite some time, but did not succeed.</p></div><div id="question-tags" class="tags-container tags">raw http file tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '16, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/742d007f0eb5671048fbdf7b13ec781b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fk18&#39;s gravatar image" /><p>fk18<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fk18 has no accepted answers">0%</span></p></div></div><div id="comments-container-53747" class="comments-container"></div><div id="comment-tools-53747" class="comment-tools"></div><div class="clear"></div><div id="comment-53747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53750"></span>

<div id="answer-container-53750" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53750-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <code>-z follow,tcp,raw</code> option of tshark. Still needs some post processing, but should get you started.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '16, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53750" class="comments-container"><span id="53753"></span><div id="comment-53753" class="comment"><div id="post-53753-score" class="comment-score"></div><div class="comment-text"><p>I'h tried that before (<code>tshark -r in.pcap -z follow,tcp,raw,0 -w f</code>). As it seems, Ethernet/IP/TCP headers are still saved to the file. This is exactly what I wanted to avoid.</p></div><div id="comment-53753-info" class="comment-info"><span class="comment-age">(30 Jun '16, 06:30)</span> fk18</div></div><span id="53755"></span><div id="comment-53755" class="comment"><div id="post-53755-score" class="comment-score"></div><div class="comment-text"><p>It is not a filter, it's a statistical tap, which generates statistical output on the console. In this case it also produces records of the data you seek. That is where the post processing comes in; having to pick up this console output and rework it into a form you can use further down in your toolchain.</p></div><div id="comment-53755-info" class="comment-info"><span class="comment-age">(30 Jun '16, 07:58)</span> Jaap ♦</div></div><span id="53767"></span><div id="comment-53767" class="comment"><div id="post-53767-score" class="comment-score">1</div><div class="comment-text"><p>What do you mean the Ethernet/IP/TCP headers are saved? If I use <code>-z follow,tcp,ascii,0</code> on a capture file with HTTP traffic the actual followed data contains only the HTTP (switching to <code>raw</code> is similar but is harder for me to read :-)).</p><p>There are some brief headers telling you what the tool is doing (which can easily be grep'd out) as well as the frame list (which can be suppressed by adding the <code>-q</code> option) but there aren't any lower-level headers in there.</p><p>OHHHH, I see... The <code>-z follow</code> option sends its output to the standard output. If you're putting <code>-w f</code> and looking at the resulting file <code>f</code> then, yes, you're going to see the full headers because <code>f</code> is going to be a PCAPNG file. That's not the output of the <code>-z follow</code> option...</p></div><div id="comment-53767-info" class="comment-info"><span class="comment-age">(01 Jul '16, 07:13)</span> JeffMorriss ♦</div></div><span id="54177"></span><div id="comment-54177" class="comment"><div id="post-54177-score" class="comment-score"></div><div class="comment-text"><p>Thanks to your answers and <a href="https://ask.wireshark.org/questions/24207/invalid-addressport-pair">this post</a>, the following script does exactly what I wanted:</p><pre><code>infile=in.pcap
outfile=out
ext=txt
for stream in $(tshark -nlr $infile -Y tcp.flags.syn==1 -T fields -e tcp.stream | sort -n | uniq | sed &#39;s/\r//&#39;)
do
    echo &quot;Processing stream $stream: ${outfile}_${stream}.${ext}&quot;
    tshark -nlr $infile -qz &quot;follow,tcp,raw,$stream&quot; | tail -n +7 | sed &#39;s/^\s\+//g&#39; | xxd -r -p &gt; ${outfile}_${stream}.${ext}
done</code></pre></div><div id="comment-54177-info" class="comment-info"><span class="comment-age">(19 Jul '16, 23:11)</span> fk18</div></div></div><div id="comment-tools-53750" class="comment-tools"></div><div class="clear"></div><div id="comment-53750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

