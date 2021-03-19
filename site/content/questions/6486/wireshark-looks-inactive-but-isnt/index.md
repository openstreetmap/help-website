+++
type = "question"
title = "Wireshark looks inactive but isn&#x27;t..."
description = '''Hello. We had used Wireshark 1.2.6 with a ring buffer to get traces for 72 hours. Yesterday, I installed a newer version of Wireshark on a WinXP machine. A shortcut to Wireshark was put in the autorun folder for XP. The shortcut command looks like this: C:&#92;Program Files&#92;Wireshark&#92;wireshark.exe -C &quot;E...'''
date = "2011-09-22T00:27:00Z"
lastmod = "2011-09-28T04:59:00Z"
weight = 6486
keywords = [ "windows", "gui", "troubleshooting" ]
aliases = [ "/questions/6486" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark looks inactive but isn't...](/questions/6486/wireshark-looks-inactive-but-isnt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6486-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>We had used Wireshark 1.2.6 with a ring buffer to get traces for 72 hours. Yesterday, I installed a newer version of Wireshark on a WinXP machine. A shortcut to Wireshark was put in the autorun folder for XP. The shortcut command looks like this:</p><pre><code>C:\Program Files\Wireshark\wireshark.exe -C &quot;EM02&quot; -b duration:1800 -b files:144 -B 20 -f &quot;ether host 08:00:06:01:60:02&quot; -i 1 -k -n -w \\Server61\Traces\EM02 -y EN10MB</code></pre><p>The profile "EM02" is the standard profile. Only the Capture Info dialog is hidden.</p><p>Everything works great, but I'm a little bit confused about the behavior of Wireshark after the first file is written, after 30 minutes, and when the next file starts.</p><ul><li>In the old version (1.2.6), the Wireshark icon stayed green. Now, it turns back to blue.</li><li>The buttons for start capture and options couldn't be used and stayed gray. Now, they can be used and look normal.</li><li>The buttons for stop and restart capture were useable. Now, they become unusable and turn to gray.</li></ul><p>It looks like Wireshark has stopped the capture, but in the deepest rows, there is still the message <strong>&lt; live capture in progress &gt; to file...</strong>, and the packet counter still increases.</p><p>Wireshark still works correctly despite these false GUI indications... ;-) Any ideas how to workaround this?</p><p>Thanks, Armin</p></div><div id="question-tags" class="tags-container tags">windows gui troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '11, 00:27</strong></p><img src="https://secure.gravatar.com/avatar/b9ade8046b7d3d3c95a33c49f273b179?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="P3F&#39;s gravatar image" /><p>P3F<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="P3F has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Sep '11, 15:48</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6486" class="comments-container"><span id="6487"></span><div id="comment-6487" class="comment"><div id="post-6487-score" class="comment-score"></div><div class="comment-text"><p>Doesn't sound right. What version of Wireshark are you using now?</p></div><div id="comment-6487-info" class="comment-info"><span class="comment-age">(22 Sep '11, 02:46)</span> Jaap ♦</div></div><span id="6491"></span><div id="comment-6491" class="comment"><div id="post-6491-score" class="comment-score"></div><div class="comment-text"><p>As a side note, you might want to consider using dumpcap instead of Wireshark for lengthy capture sessions.</p></div><div id="comment-6491-info" class="comment-info"><span class="comment-age">(22 Sep '11, 07:00)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-6486" class="comment-tools"></div><div class="clear"></div><div id="comment-6486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6616"></span>

<div id="answer-container-6616" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6616-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark works fine, just try to use the updated version .....(1.6.2)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p>flashkicker<br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6616" class="comments-container"><span id="6860"></span><div id="comment-6860" class="comment"><div id="post-6860-score" class="comment-score"></div><div class="comment-text"><p>Hi Flashkicker.</p><p>I forgot to wrote that I installed the actual 1.6.2 Version, sorry.</p></div><div id="comment-6860-info" class="comment-info"><span class="comment-age">(11 Oct '11, 23:58)</span> P3F</div></div></div><div id="comment-tools-6616" class="comment-tools"></div><div class="clear"></div><div id="comment-6616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

