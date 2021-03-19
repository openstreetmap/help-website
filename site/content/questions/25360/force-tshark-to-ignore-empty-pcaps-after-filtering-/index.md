+++
type = "question"
title = "Force Tshark to ignore Empty pcaps after filtering ?--"
description = '''Hello how to make Tshark ignore writing an empty file if the filter in -R doesn&#x27;t return any result ?'''
date = "2013-09-30T00:35:00Z"
lastmod = "2013-09-30T02:07:00Z"
weight = 25360
keywords = [ "tshark" ]
aliases = [ "/questions/25360" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Force Tshark to ignore Empty pcaps after filtering ?--](/questions/25360/force-tshark-to-ignore-empty-pcaps-after-filtering-)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25360-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello how to make Tshark ignore writing an empty file if the filter in -R doesn't return any result ?</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '13, 00:35</strong></p><img src="https://secure.gravatar.com/avatar/27e19b1f6c0b00e4469bfa2fba760e79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ziad%20Kiwan&#39;s gravatar image" /><p>Ziad Kiwan<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ziad Kiwan has no accepted answers">0%</span></p></div></div><div id="comments-container-25360" class="comments-container"></div><div id="comment-tools-25360" class="comment-tools"></div><div class="clear"></div><div id="comment-25360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25361"></span>

<div id="answer-container-25361" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25361-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Hello how to make Tshark ignore writing an empty file</p></blockquote><p>by changing the code.</p><p>What are you trying to do? Maybe there is another solution?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '13, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25361" class="comments-container"><span id="25362"></span><div id="comment-25362" class="comment"><div id="post-25362-score" class="comment-score"></div><div class="comment-text"><p>i made a bash script that reads like 10000 pcap and cut the data from each 100MB file pcap and put in another file in the same pcap name some pcaps may contain the data some doesn't so i want only pcaps that contains the data to be written and if not it doesn't write anything not an empty pcap with the file name</p></div><div id="comment-25362-info" class="comment-info"><span class="comment-age">(30 Sep '13, 02:11)</span> Ziad Kiwan</div></div><span id="25366"></span><div id="comment-25366" class="comment"><div id="post-25366-score" class="comment-score">1</div><div class="comment-text"><p>As I said, that behavior can be changed by changing the tshark source code.</p><p>In your case, it's easy to remove the empty files in the bash script.</p><p>Run these commands after you ran tshark. Replace file.pcap with the name tshark wrote.</p><pre><code>capinfos file.pcap 2&gt;&amp;1 | egrep -i &#39;Number of packets:\s+0&#39; &gt; /dev/null
if [ $? -eq 0 ] 
then
   echo removing file.pcap
   rm -f file.pcap
fi</code></pre><p>capinfos looks for the number of packets in the file. If there are 0 packets, egrep will retun 0 as exit code. In that case you can delete the file.</p></div><div id="comment-25366-info" class="comment-info"><span class="comment-age">(30 Sep '13, 02:33)</span> Kurt Knochner ♦</div></div><span id="25368"></span><div id="comment-25368" class="comment"><div id="post-25368-score" class="comment-score"></div><div class="comment-text"><p>Wow that's something new to learn thank you man! real appreciated!</p></div><div id="comment-25368-info" class="comment-info"><span class="comment-age">(30 Sep '13, 02:56)</span> Ziad Kiwan</div></div><span id="25369"></span><div id="comment-25369" class="comment"><div id="post-25369-score" class="comment-score"></div><div class="comment-text"><p>Good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-25369-info" class="comment-info"><span class="comment-age">(30 Sep '13, 03:11)</span> Kurt Knochner ♦</div></div><span id="25370"></span><div id="comment-25370" class="comment"><div id="post-25370-score" class="comment-score"></div><div class="comment-text"><p>i couldn't find it before now i did thank you</p></div><div id="comment-25370-info" class="comment-info"><span class="comment-age">(30 Sep '13, 04:26)</span> Ziad Kiwan</div></div></div><div id="comment-tools-25361" class="comment-tools"></div><div class="clear"></div><div id="comment-25361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

