+++
type = "question"
title = "Ring Buffer stops capture after 1135 iterations"
description = '''Hi All, I am trying to capture packets for a really long duration of time. In order to save my hard disk from getting filled up I chose to use ring buffer. The option I gave were &quot;-b file:30&quot; Strangely the capture stops at 1135th iteration. What is the max file size for these 30 files. If it was hit...'''
date = "2015-01-14T22:18:00Z"
lastmod = "2015-01-15T00:53:00Z"
weight = 39139
keywords = [ "tshark", "ringbuffer" ]
aliases = [ "/questions/39139" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Ring Buffer stops capture after 1135 iterations](/questions/39139/ring-buffer-stops-capture-after-1135-iterations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39139-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am trying to capture packets for a really long duration of time. In order to save my hard disk from getting filled up I chose to use ring buffer.</p><p>The option I gave were "-b file:30" Strangely the capture stops at 1135th iteration. What is the max file size for these 30 files. If it was hitting the memory limit then why did it not complain after 1st iteration?</p><p>Thanks and Regards,</p><p>Aparna N</p></div><div id="question-tags" class="tags-container tags">tshark ringbuffer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '15, 22:18</strong></p><img src="https://secure.gravatar.com/avatar/b605d47d2e423a49d4a281eb597b9fba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aparna&#39;s gravatar image" /><p>Aparna<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aparna has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jan '15, 22:19</p></div></div><div id="comments-container-39139" class="comments-container"></div><div id="comment-tools-39139" class="comment-tools"></div><div class="clear"></div><div id="comment-39139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39145"></span>

<div id="answer-container-39145" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39145-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you are capturing with <strong>tshark</strong>, you will eventually run into the memory limit problem, see the following questions.</p><blockquote><p><a href="https://ask.wireshark.org/questions/34035/tshark-memory-usage-explanation-needed">https://ask.wireshark.org/questions/34035/tshark-memory-usage-explanation-needed</a><br />
<a href="https://ask.wireshark.org/questions/31648/tshark-uses-all-memory-on-mavericks-triggering-out-of-application-memory-errors">https://ask.wireshark.org/questions/31648/tshark-uses-all-memory-on-mavericks-triggering-out-of-application-memory-errors</a><br />
<a href="https://ask.wireshark.org/questions/25091/wireshark-tshark-out-of-memory-problem">https://ask.wireshark.org/questions/25091/wireshark-tshark-out-of-memory-problem</a><br />
</p></blockquote><p>Instead, you should do the pure capturing with <strong>dumpcap</strong> and later the analysis with Wireshark or tshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '15, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jan '15, 03:23</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></br></p></div></div><div id="comments-container-39145" class="comments-container"><span id="39149"></span><div id="comment-39149" class="comment"><div id="post-39149-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, Thank you for the apt answer. I am using tshark currently. I shall try dumpcap. Will know if it does the trick for me in 24-28 hours.</p></div><div id="comment-39149-info" class="comment-info"><span class="comment-age">(15 Jan '15, 01:58)</span> Aparna</div></div><span id="39150"></span><div id="comment-39150" class="comment"><div id="post-39150-score" class="comment-score"></div><div class="comment-text"><p>It will ;-))</p></div><div id="comment-39150-info" class="comment-info"><span class="comment-age">(15 Jan '15, 01:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-39145" class="comment-tools"></div><div class="clear"></div><div id="comment-39145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

