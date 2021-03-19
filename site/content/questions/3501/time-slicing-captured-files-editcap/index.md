+++
type = "question"
title = "Time slicing captured files - editcap"
description = '''I&#x27;m trying to time slice of a captured file.  using editcap &amp;lt;file_in&amp;gt; &amp;lt;file_out&amp;gt; I get the whole input file. Using editcp -r &amp;lt;file_in&amp;gt; &amp;lt;file_out&amp;gt; I get the output file with only a couple lines of data. Using editcp -r -A -B yyyy-mm-dd hh:mm:ss yyyy-mm-dd hh:mm:ss &amp;lt;file_in&amp;...'''
date = "2011-04-14T10:11:00Z"
lastmod = "2011-04-14T11:09:00Z"
weight = 3501
keywords = [ "editcap" ]
aliases = [ "/questions/3501" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Time slicing captured files - editcap](/questions/3501/time-slicing-captured-files-editcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3501-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to time slice of a captured file.<br />
</p><p>using editcap &lt;file_in&gt; &lt;file_out&gt; I get the whole input file.</p><p>Using editcp -r &lt;file_in&gt; &lt;file_out&gt; I get the output file with only a couple lines of data.</p><p>Using editcp -r -A -B yyyy-mm-dd hh:mm:ss yyyy-mm-dd hh:mm:ss &lt;file_in&gt; &lt;file_out&gt; I get error feedback of incorrect DTG.</p><p>Using editcp -r -A -B yyyy-mm-ddhh:mm:ss yyyy-mm-ddhh:mm:ss &lt;file_in&gt; &lt;file_out&gt; I get only one line in the file.</p></div><div id="question-tags" class="tags-container tags">editcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '11, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/a3693c84af5886bc0cd71e0944f6b6ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fredhoef&#39;s gravatar image" /><p>fredhoef<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fredhoef has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 22:31</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3501" class="comments-container"></div><div id="comment-tools-3501" class="comment-tools"></div><div class="clear"></div><div id="comment-3501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3502"></span>

<div id="answer-container-3502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3502-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Let me give you an example on how to use editcap to create a timeslice of a tracefile. When you want to keep only packets with timestamps between 11:00 to 13:00 on April 14th 2011, you would use the command:</p><pre><code>editcap -A &quot;2011-04-14 11:00:00&quot; -B &quot;2011-04-14 13:00:00&quot; infile.cap outfile.cap</code></pre><p>Hope this helps :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '11, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3502" class="comments-container"></div><div id="comment-tools-3502" class="comment-tools"></div><div class="clear"></div><div id="comment-3502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

