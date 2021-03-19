+++
type = "question"
title = "How to get the iostats near realtime from tshark ?"
description = '''Hi All,  I am trying to plot the stats output from tshark. I want to know if there is a way i can print the stats every few seconds rather than printing at the end. It will be of great help for me.  Thanks is advance'''
date = "2013-11-20T02:25:00Z"
lastmod = "2013-11-20T19:20:00Z"
weight = 27145
keywords = [ "tshark" ]
aliases = [ "/questions/27145" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to get the iostats near realtime from tshark ?](/questions/27145/how-to-get-the-iostats-near-realtime-from-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27145-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><pre><code> I am trying to plot the stats output from tshark. I want to know if there is a way i can print the stats every few seconds rather than printing at the end. It will be of great help for me.</code></pre><p>Thanks is advance</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/b98f9333b02c07c31bb91986b6f720d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran&#39;s gravatar image" /><p>Kiran<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran has no accepted answers">0%</span></p></div></div><div id="comments-container-27145" class="comments-container"></div><div id="comment-tools-27145" class="comment-tools"></div><div class="clear"></div><div id="comment-27145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27189"></span>

<div id="answer-container-27189" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27189-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've done what you're trying to do, sort of. My approach was:</p><ul><li>Use dumpcap to perform automated captures over a short time period (short as in 5 minutes or 15 minutes.)</li><li>Use tshark -z io,stats option to pull packet counts matching various display filters to use as graph metrics</li><li>Take those metrics and add them to the end of an incrementing .csv file with a timestamp column.</li><li>Use a web dashboard utility (in my case, I used open flash chart, <a href="http://teethgrinder.co.uk/open-flash-chart-2/)">http://teethgrinder.co.uk/open-flash-chart-2/)</a> to take the .csv file data and generate dynamic chart content.</li></ul><p>Now there are a couple things to caution on here:</p><ul><li>Ensure your -z io,stats is done once against a capture file, and you get all the stats you need from it in one query. This makes it immeasurably more scalable.</li><li>Be careful about starting the tshark -z query immediately after dumpcap finishes. You may need to delay it for a few time intervals to ensure the file is there to be read.</li><li>If you want, add an unlink statement against the old capture files based on mtime if you don't want to keep them.</li><li>Consider how much traffic you need to parse. Dumpcap can probably take it, but tshark is a slower process. Once the time it takes to read a time interval exceeds the time it takes to analyze it and save it, your near-real-time graph concept is over.</li><li>I can't give you my source code for the above project. I am sorry and wish I could, but for a perl person it's relatively straightforward. :)</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Nov '13, 19:26</p></div></div><div id="comments-container-27189" class="comments-container"><span id="27196"></span><div id="comment-27196" class="comment"><div id="post-27196-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Its good to know somebody already tried and got success in similar thing that I want to do. :)</p><p>I also observed the same thing with "-z query immediately after dumpcap finishes".</p><p>Its ok i will manage writing my own code :).</p><p>I also used perl for getting my offline analysis which updates and plots in browser.</p><p>I think I will to try pcap directly and see what I can do with that.</p><p>Thank you for your feedback. I will getback when if I stuck again in something.</p><p>BRs, Kiran</p></div><div id="comment-27196-info" class="comment-info"><span class="comment-age">(20 Nov '13, 22:25)</span> Kiran</div></div></div><div id="comment-tools-27189" class="comment-tools"></div><div class="clear"></div><div id="comment-27189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27151"></span>

<div id="answer-container-27151" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27151-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's only possible with a code change. If you think you need that feature please file an enhancement 'bug' at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a>.</p><p><strong>HOWEVER</strong>: You request sounds like you are trying to use tshark as a (real time, long term) network monitoring solution. That won't work, as neither Wireshark nor tshark have been developed with that goal in mind. There are well known problems (ever increasing memory usage and others), that will create problems if you run tshark/wireshark for a longer period of time (see other questions).</p><p>What kind of statistics do you need? Maybe there are other solutions.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 03:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27151" class="comments-container"><span id="27154"></span><div id="comment-27154" class="comment"><div id="post-27154-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for quick answer. I am actually trying to simulate the behavior of IO Graph in wireshark. (It has 5 filters from which it can generate graphs updating after every few seconds. I don't know whether it is possible to add more filters to it. And I want to know whether Lua can be of any help regarding adding more filters in IOGraph of wireshark.)</p><p>I want to actually do the same thing by sending data to a CSV file and plot in a browser. Regarding the size of the buffer, if i want to plot some kind of data say every 1 sec, it is sufficient it just stores upto 'n' sec(if it calculates the required data that required for the graph in that time) and do this in circular manner. Cos I don't require any more analysis than the graphs that I want to plot.</p><p>I hope I made myself clear here.</p><p>BRs, Kiran</p></div><div id="comment-27154-info" class="comment-info"><span class="comment-age">(20 Nov '13, 03:47)</span> Kiran</div></div><span id="27166"></span><div id="comment-27166" class="comment"><div id="post-27166-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I hope I made myself clear here.</p></blockquote><p>clear enough to understand what you are trying to do ;-)</p><p>However, as I mentioned you are (apparently) trying to use tshark as a real time, long term network monitoring solution. That's not going to work due to the way tshark/Wireshark was designed.</p><p>Unless you need the 'power' of the Wireshark dissectors to extract some fields from an esoteric protocol, there might be better network (performance) monitoring tools available. Mr. google will help.</p><p>If however, you need the 'magic power' of wireshark/tshark dissectors, I have bad news for you: You won't be able to implement what you are looking for with tshark/Wireshark.</p><p>See the discussions with @hoangsonk49 about a similar problem:</p><blockquote><p><a href="http://ask.wireshark.org/questions/25794/tshark-generate-core-dump">http://ask.wireshark.org/questions/25794/tshark-generate-core-dump</a><br />
<a href="http://ask.wireshark.org/questions/26563/smaller-tshark-for-specific-protocol">http://ask.wireshark.org/questions/26563/smaller-tshark-for-specific-protocol</a><br />
<a href="http://ask.wireshark.org/questions/25984/what-does-processing-speed-of-dissectors-depend-on">http://ask.wireshark.org/questions/25984/what-does-processing-speed-of-dissectors-depend-on</a><br />
<a href="http://ask.wireshark.org/questions/25091/wireshark-tshark-out-of-memory-problem">http://ask.wireshark.org/questions/25091/wireshark-tshark-out-of-memory-problem</a></p></blockquote><p>Just for the records: What kind of filters do you use in IO graphs?</p></div><div id="comment-27166-info" class="comment-info"><span class="comment-age">(20 Nov '13, 08:06)</span> Kurt Knochner ♦</div></div><span id="27195"></span><div id="comment-27195" class="comment"><div id="post-27195-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks again for your reply. My Filters are very simple. I am trying to see how much bandwidth my application is taking on some port and some ip -- which depends on my estimation algorithm. In turn i am validating my algorithm. I can actually do that offline also but i wan t to do that by plotting the data on a browser. The reason I am trying Wireshark is that some times i need to analyze data also. I don't want to use two tools for that purpose.</p><p>And thanks for taking time in searching and giving those links which were helpful.</p><p>BRs, Kiran</p></div><div id="comment-27195-info" class="comment-info"><span class="comment-age">(20 Nov '13, 22:15)</span> Kiran</div></div></div><div id="comment-tools-27151" class="comment-tools"></div><div class="clear"></div><div id="comment-27151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

