+++
type = "question"
title = "How to save the capture options?"
description = '''Hi, I use Wireshark version 1.8.4. Each time I would take a capture I enter Capture &amp;gt;&amp;gt; Options and change the default parameters of &#x27;Capture files&#x27; like enable &#x27;use multiple files&#x27; option, setting &#x27;next file every 200M&#x27;, browsing to a folder on Desktop where I want all the capture files to be ...'''
date = "2012-12-05T01:40:00Z"
lastmod = "2012-12-05T07:46:00Z"
weight = 16576
keywords = [ "capture", "save", "options" ]
aliases = [ "/questions/16576" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to save the capture options?](/questions/16576/how-to-save-the-capture-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16576-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I use Wireshark version 1.8.4.</p><p>Each time I would take a capture I enter Capture &gt;&gt; Options and change the default parameters of 'Capture files' like enable 'use multiple files' option, setting 'next file every 200M', browsing to a folder on Desktop where I want all the capture files to be saved at.</p><p>Is there any way to save those parameters so each time I open the Wireshark and take a capture, it will be based on those settings?</p><p>Thanks, Tal</p></div><div id="question-tags" class="tags-container tags">capture save options</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/a3edb2d483f228f4fcc54f5cfdb7be14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tal&#39;s gravatar image" /><p>tal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '12, 21:00</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-16576" class="comments-container"></div><div id="comment-tools-16576" class="comment-tools"></div><div class="clear"></div><div id="comment-16576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16596"></span>

<div id="answer-container-16596" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16596-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I recently was doing something somewhat similar. As Landi says you can save the capture filter, but you cannot save all the other parameters. So what I did was create a small shell script (batch file if you're on Windows). This is what I used (this was on Linux which supports the 'any' device):</p><pre><code>wireshark -B 10 -i any -f &quot;not ip host A.B.C.D and not localhost&quot; -k \
   -b filesize:10240 -w /path/to/my/captures/wireshark_`date +%m%d`</code></pre><p>The "date +%m+%d" stuff substitutes (on Unix) the current date. I'm not sure how one could do that in DOS/Windows.</p><p>The "-k" tells Wireshark to start capturing immediately upon startup. See the man page for any of the other options you don't know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-16596" class="comments-container"></div><div id="comment-tools-16596" class="comment-tools"></div><div class="clear"></div><div id="comment-16596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16580"></span>

<div id="answer-container-16580" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16580-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>One very easy way to save certain filters is to click on the "Capture Filter" button right in front of the field where you enter your capture filter. In the upcoming dialogue you can "bookmark" or save often needed filters with a label of your own and by double-clicking on one of the list entries apply that filter.</p><p>If you also want to avoid that step I suggest that you take a look at the dumpcap -h options, since over those you get the ability to completely configure the capture process via a command-line 1-liner, specifying everything you like e.g. by using a .bat or .cmd Batch Script</p><pre><code>Capture interface:</code></pre><p><code>-i &lt;interface&gt;           name or idx of interface (def: first non-loopback) -f &lt;capture filter&gt;      packet filter in libpcap filter syntax</code></p><p><code>Output (files):   -w &lt;filename&gt;            name of file to save (def: tempfile)   -b &lt;ringbuffer opt.&gt; ... duration:NUM - switch to next file after NUM secs                            filesize:NUM - switch to next file after NUM KB                               files:NUM - ringbuffer: replace after NUM files</code><br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '12, 03:04</p></div></div><div id="comments-container-16580" class="comments-container"></div><div id="comment-tools-16580" class="comment-tools"></div><div class="clear"></div><div id="comment-16580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

