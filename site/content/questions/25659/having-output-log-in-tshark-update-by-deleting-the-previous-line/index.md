+++
type = "question"
title = "Having output Log in tshark update by deleting the previous line."
description = '''I&#x27;m using tshark to capture RSSI values in an attempt at wifi triangulation. I have it set up so that the log only outputs the RSSI value. The command I&#x27;m using is:  &#x27;tshark -I -i wlan2 -R &quot;wlan.addr == 58:1f:aa:2a:80:1e &amp;amp;&amp;amp; wlan.addr == Broadcast&quot; -o column.format:&#x27;&quot;RSSI&quot;, %e&#x27; &amp;gt; /tmp/log....'''
date = "2013-10-04T18:53:00Z"
lastmod = "2013-10-07T13:40:00Z"
weight = 25659
keywords = [ "tshark", "log" ]
aliases = [ "/questions/25659" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Having output Log in tshark update by deleting the previous line.](/questions/25659/having-output-log-in-tshark-update-by-deleting-the-previous-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25659-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using tshark to capture RSSI values in an attempt at wifi triangulation.</p><p>I have it set up so that the log only outputs the RSSI value. The command I'm using is:</p><p>'tshark -I -i wlan2 -R "wlan.addr == 58:1f:aa:2a:80:1e &amp;&amp; wlan.addr == Broadcast" -o column.format:'"RSSI", %e' &gt; /tmp/log.txt'</p><p>I'm using python function readline() to grab the first line of the log file and assign the RSSI to a variable to be sent into a triangulation algorithm.</p><p>I'm wondering if there's a way to have the log update constantly re-writing the first line of the log file.</p></div><div id="question-tags" class="tags-container tags">tshark log</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '13, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/dd4464c7c7fa8f0d53c25f217b310cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Evan%20Watler&#39;s gravatar image" /><p>Evan Watler<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Evan Watler has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Oct '13, 18:54</p></div></div><div id="comments-container-25659" class="comments-container"></div><div id="comment-tools-25659" class="comment-tools"></div><div class="clear"></div><div id="comment-25659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25669"></span>

<div id="answer-container-25669" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25669-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I see a couple of options:</p><ul><li>Use "tail -f /tmp/log.txt" within python to read from</li><li>Use "tshark -I -i wlan2 -R "wlan.addr == 58:1f:aa:2a:80:1e &amp;&amp; wlan.addr == Broadcast" -o column.format:'"RSSI", %e'" within python to read from</li></ul><p>If you really need to read from a file, then you can use some command line piping to overwrite the first line, something like:</p><pre><code>tshark -r pcap/http.cap | awk &#39;{print &gt;&quot;/tmp/log.txt&quot;;close &quot;/tmp/log.txt&quot;}&#39;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Oct '13, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25669" class="comments-container"></div><div id="comment-tools-25669" class="comment-tools"></div><div class="clear"></div><div id="comment-25669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25728"></span>

<div id="answer-container-25728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm wondering if there's a way to have the log update constantly re-writing the first line of the log file.</p></blockquote><p>That's where named pipes can help. They work like a FIFO and thus you will always get the lines in the order they were written, one by one, just by calling readline() on them.</p><p>Here is how you can do it:</p><pre><code>&gt;mkfifo /tmp/tshark_pipe   
&gt;tshark -I -i wlan2 -l -R &quot;wlan.addr == 58:1f:aa:2a:80:1e &amp;&amp; wlan.addr == Broadcast&quot; -o column.format:&#39;&quot;RSSI&quot;, %e&#39; &gt;/tmp/tshark_pipe 2&gt;/dev/null&#39; &amp;  
&gt;python -u analyze.py</code></pre><p>I added some options (-l and 2&gt;/dev/null) to your tshark command. <code>-l</code> is necessary to disable buffered output, which tells tshark to flush the output buffer after every packet. The rest should be clear.</p><p>Here is the (very basic!) python code. Please extend it to your needs. Obviously you need to extract the RSSI values from the line in the python code and then feed that into your algorithm.</p><pre><code>import os

tshark_pipe = &quot;/tmp/tshark_pipe&quot;

pipe = open(tshark_pipe, &#39;r&#39;)

while True:
    data=pipe.readline()
    if data:
       print &quot;Data: &quot; + data

pipe.close()</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Oct '13, 13:41</p></div></div><div id="comments-container-25728" class="comments-container"></div><div id="comment-tools-25728" class="comment-tools"></div><div class="clear"></div><div id="comment-25728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

