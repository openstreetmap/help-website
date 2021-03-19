+++
type = "question"
title = "how to separate a trace file?"
description = '''I have a large trace file of several GBs, but not all of traffic is needed. I would like to save the interesting traffic into a separate file in two ways:  filter out the interesting packets and save as a new file multiselect the interesting packets and save as a new file  How to achieve that? thank...'''
date = "2013-12-26T23:19:00Z"
lastmod = "2013-12-27T05:41:00Z"
weight = 28419
keywords = [ "separate_trace" ]
aliases = [ "/questions/28419" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [how to separate a trace file?](/questions/28419/how-to-separate-a-trace-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28419-score" class="post-score" title="current number of votes">0</div><span id="post-28419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a large trace file of several GBs, but not all of traffic is needed. I would like to save the interesting traffic into a separate file in two ways:</p><ul><li>filter out the interesting packets and save as a new file</li><li>multiselect the interesting packets and save as a new file</li></ul><p>How to achieve that? thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-separate_trace" rel="tag" title="see questions tagged &#39;separate_trace&#39;">separate_trace</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '13, 23:19</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-28419" class="comments-container"></div><div id="comment-tools-28419" class="comment-tools"></div><div class="clear"></div><div id="comment-28419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="28435"></span>

<div id="answer-container-28435" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28435-score" class="post-score" title="current number of votes">2</div><span id="post-28435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have a large trace file of several GBs, but not all of traffic is needed.</p></blockquote><p>to load a file of <strong>several GByte</strong> into Wireshark, you would need a system with a 64Bit OS and 'enough' RAM if want to avoid the <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">known memory problem</a>.</p><p>So, if you <strong>can</strong> load the capture file in Wireshark , you <strong>can filter</strong> the frames however you like (multi select via CRTL-M (mark) or via display filters) and then <strong>export</strong> those frames (File -&gt; Export Specified Packets).</p><p><strong>However</strong> if you <strong>cannot load</strong> the large capture file into Wireshark (crash due to memory problem), you need to reduce the size of the capture file,</p><ul><li>either by splitting it into several smaller files (<a href="http://www.wireshark.org/docs/man-pages/editcap.html">editcap</a>)</li><li>or by extracting the 'interesting frames' from the large capture file.</li></ul><p>The second option is the harder part, as extracting the '<strong>interesting</strong> frames' can get tricky, as you can't use the power of Wiresharks display filters (as you can't load the file). You can <strong>try</strong> to filter the frames with tshark, <strong>however</strong> if Wireshark fails due to memory problems, tshark will almost certainly fail as well, as they both use the same dissection engine (hence they have nearly the same RAM usage).</p><p>Then the only option would be to use <strong>capture filters</strong> with a tool that is able to filter <strong>and</strong> write a new file based on those filters. On Windows I use SplitCap for that.</p><blockquote><p><a href="http://www.netresec.com/?page=SplitCap">http://www.netresec.com/?page=SplitCap</a></p></blockquote><p>On Linux you can use tcpdump</p><blockquote><p>tcpdump -nr input.pcap -w output.pcap "host x.x.x.x and port yyy"</p></blockquote><p>If that is good enough to filter 'interesting frames' depends on your definition of 'interesting frames'. If it is <strong>not</strong> good enough, you still have the option to split the large file into files (see editcap above), small enough to load it into Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '13, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Dec '13, 06:04</strong> </span></p></div></div><div id="comments-container-28435" class="comments-container"></div><div id="comment-tools-28435" class="comment-tools"></div><div class="clear"></div><div id="comment-28435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28420"></span>

<div id="answer-container-28420" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28420-score" class="post-score" title="current number of votes">1</div><span id="post-28420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can do that by using export specified packet. Open your file, apply your filter and then go to file-&gt;export specified packet. Save all displayed packet in a new file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '13, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p><span>Afrim</span><br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-28420" class="comments-container"></div><div id="comment-tools-28420" class="comment-tools"></div><div class="clear"></div><div id="comment-28420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28421"></span>

<div id="answer-container-28421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28421-score" class="post-score" title="current number of votes">1</div><span id="post-28421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the file is too big to load into wireshark you can use tshark to filter on the desired traffic and write the output into a new file. The -Y allows you to filter all interesting packets.</p><pre><code>tshark -Y &quot;expert&quot; -r t1_400k.pcap -w t1_400k.expert.pcapng</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '13, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28421" class="comments-container"></div><div id="comment-tools-28421" class="comment-tools"></div><div class="clear"></div><div id="comment-28421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

