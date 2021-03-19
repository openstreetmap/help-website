+++
type = "question"
title = "Eliminate duplicate source addresses"
description = '''How can I eliminate duplicate source addresses so that I only see how many computers are communicating on a certain port? The display is filtered to only show port 137 and the addresses are sorted, but there are hundreds of packets for each source address because the capture ran for quite a while. I...'''
date = "2011-01-13T14:22:00Z"
lastmod = "2011-01-16T00:52:00Z"
weight = 1744
keywords = [ "filter" ]
aliases = [ "/questions/1744" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Eliminate duplicate source addresses](/questions/1744/eliminate-duplicate-source-addresses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1744-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I eliminate duplicate source addresses so that I only see how many computers are communicating on a certain port? The display is filtered to only show port 137 and the addresses are sorted, but there are hundreds of packets for each source address because the capture ran for quite a while. I want to eliminate the duplicates to only show which computers are using 137.</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '11, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/1878767c7df09015d831a6b9a09e6697?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JTC&#39;s gravatar image" /><p>JTC<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JTC has no accepted answers">0%</span></p></div></div><div id="comments-container-1744" class="comments-container"></div><div id="comment-tools-1744" class="comment-tools"></div><div class="clear"></div><div id="comment-1744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1745"></span>

<div id="answer-container-1745" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1745-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Would something like the following work?</p><ul><li>Apply the display filter <code>udp.port eq 137</code> (or <code>udp.dstport eq 137</code>)</li><li>Go to <em>Statistics→Endpoints</em></li><li>Select the <em>UDP</em> tab</li><li>Select <em>Limit to display filter</em></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '11, 15:07</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-1745" class="comments-container"><span id="1746"></span><div id="comment-1746" class="comment"><div id="post-1746-score" class="comment-score"></div><div class="comment-text"><ul><li>and if there are many many many rows, take a look at the number in the tab header instead of counting the lines by hand.</li></ul><p>(yes, I had students in my class actually starting to count lines by hand once) :-)</p></div><div id="comment-1746-info" class="comment-info"><span class="comment-age">(13 Jan '11, 16:56)</span> Jasper ♦♦</div></div></div><div id="comment-tools-1745" class="comment-tools"></div><div class="clear"></div><div id="comment-1745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1764"></span>

<div id="answer-container-1764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1764-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or you can use tshark :-)</p><pre><code>tshark -r &lt;file&gt; -R &quot;udp.dstport==137&quot; -T fields -e ip.src | sort -n | uniq</code></pre><p>This will give you a list of all IP addresses that have sent packets to udp port 137 or ...</p><pre><code>tshark -r &lt;file&gt; -R &quot;udp.dstport==137&quot; -T fields -e ip.src | \
    sort | uniq -c | sort -rn | head</code></pre><p>...will give you a top 10 of all IP addresses that have sent packets to udp port 137.</p><p>(If you are on Windows, you can make this work by installing <a href="http://www.cygwin.com">cygwin</a>)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '11, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1764" class="comments-container"></div><div id="comment-tools-1764" class="comment-tools"></div><div class="clear"></div><div id="comment-1764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

