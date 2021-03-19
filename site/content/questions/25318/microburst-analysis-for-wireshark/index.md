+++
type = "question"
title = "Microburst analysis for wireshark"
description = '''Hello, I am suspecting microbursts happening at time intervals too short to show up in i/o statistics in some pcap files. Does wireshark have built-in automated search through large captures to find microbursts? Is there a way to get a better resolution than 0.001s in i/o Graph ? Thanks.'''
date = "2013-09-27T08:27:00Z"
lastmod = "2014-06-11T13:52:00Z"
weight = 25318
keywords = [ "graphs", "microburst" ]
aliases = [ "/questions/25318" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Microburst analysis for wireshark](/questions/25318/microburst-analysis-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25318-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am suspecting microbursts happening at time intervals too short to show up in i/o statistics in some pcap files.</p><p>Does wireshark have built-in automated search through large captures to find microbursts?</p><p>Is there a way to get a better resolution than 0.001s in i/o Graph ?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">graphs microburst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '13, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/6a4166b5fb1b51d5574b2ba1c085905f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Metakent&#39;s gravatar image" /><p>Metakent<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Metakent has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Sep '13, 08:44</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-25318" class="comments-container"></div><div id="comment-tools-25318" class="comment-tools"></div><div class="clear"></div><div id="comment-25318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="25341"></span>

<div id="answer-container-25341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25341-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to get a better resolution than 0.001s in i/o Graph ?</p></blockquote><p>well, if you don't see a microburst with a resolution of 1ms, then it is either not there or really, really short (which might be the case). Unfortunately there is no commonly accepted definition for a microburst, at least I don't know one. So it is hard to 'describe/define' what a microburst is and/or what is not, especially as it heavily depends on the environment.</p><p>As you cannot draw IO graphs with microsecond resolution, your options are:</p><ul><li>extend the wireshark code to allow that (may be some work)</li><li>use tshark to output the data in 'CSV' and then use a <a href="http://en.wikipedia.org/wiki/List_of_spreadsheet_software">Spreadsheet software</a> or a tool for statistical calculations (like the <a href="http://www.r-project.org/">R language/environment</a> or ) to generate graphs with a lower (or higher) resolution.</li></ul><p>Example:</p><blockquote><p>tshark -nr input.pcap -T fields -e frame.number -e frame.time_relative -e ip.src -e ip.dst -e frame.len -E header=y -E separator=; &gt; out.txt</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '13, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25341" class="comments-container"></div><div id="comment-tools-25341" class="comment-tools"></div><div class="clear"></div><div id="comment-25341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33669"></span>

<div id="answer-container-33669" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33669-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>one thing that could be deceiving is when you choose .0001 sec on x axis tick interval in I/O graph, it doesn't really tell you what the bits/sec rate is.</p><p>at first i had the impression that if you chose .0001sec (1 millisecond) you would see higher spikes than when you chose tick interval of 1 sec. But that's clearly not the case.</p><p>the reason for this is wireshark is simply telling you how many bits are matched every 1 millisecond, instead of telling you the "rate" on a per second basis.</p><p>the question is: during this 1 millisecond interval sample, based on the bits that were seen, if we were to have this many bits for 1000 consecutive milliseconds, what would be the bits per second rate. And unfortunately, wireshark doesn't seem to calculate this for us in IO graph.</p><p>However, you can get a very detailed throughput graph when you go to statistics&gt;tcp stream graph &gt; throughput graph. the only problem with this is it only gives you the stats for the tcp conversation you have highlighted.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/957157dab509f28c4a101054f2548c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="audyn&#39;s gravatar image" /><p>audyn<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="audyn has no accepted answers">0%</span></p></div></div><div id="comments-container-33669" class="comments-container"><span id="33670"></span><div id="comment-33670" class="comment"><div id="post-33670-score" class="comment-score"></div><div class="comment-text"><p>is this a comment, an answer or a question?</p></div><div id="comment-33670-info" class="comment-info"><span class="comment-age">(11 Jun '14, 13:15)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33669" class="comment-tools"></div><div class="clear"></div><div id="comment-33669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33675"></span>

<div id="answer-container-33675" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33675-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>this is more of an answer and a comment.</p><p>the question i added to the comment was basically one that answers what we're trying to actually gather from io graph.</p><p>So interestingly one way we could use the IO graph is for example: you get some spikes here and there and let's say one of the spikes went up to 5000 bits per tick (and you have the tick interval set to 1 millisecond). The way to figure out the bits per second rate is to simply multiply by 1000 (1000milliseconds) and you come up with 5000000 bits per sec (5Mbps).</p><p>hope that helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '14, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/957157dab509f28c4a101054f2548c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="audyn&#39;s gravatar image" /><p>audyn<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="audyn has no accepted answers">0%</span></p></div></div><div id="comments-container-33675" class="comments-container"></div><div id="comment-tools-33675" class="comment-tools"></div><div class="clear"></div><div id="comment-33675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

