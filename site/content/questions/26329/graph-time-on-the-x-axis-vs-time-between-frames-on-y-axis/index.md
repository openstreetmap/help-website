+++
type = "question"
title = "graph time on the x axis vs, time between frames on y axis"
description = '''How can I graph time on the x axis vs, time between frames on y axis? I will filter my display on only 1 side of the conversation, A -&amp;gt; B Then I want to see when the time between frames spikes up. It will allow me to see when the Source has &#x27;paused&#x27; so to speak.'''
date = "2013-10-23T11:32:00Z"
lastmod = "2013-10-24T09:53:00Z"
weight = 26329
keywords = [ "graph", "graphs" ]
aliases = [ "/questions/26329" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [graph time on the x axis vs, time between frames on y axis](/questions/26329/graph-time-on-the-x-axis-vs-time-between-frames-on-y-axis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26329-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I graph time on the x axis vs, time between frames on y axis? I will filter my display on only 1 side of the conversation, A -&gt; B Then I want to see when the time between frames spikes up. It will allow me to see when the Source has 'paused' so to speak.</p></div><div id="question-tags" class="tags-container tags">graph graphs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/722e2a7c83c6f67e7d382bf314b6fa6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="condor27&#39;s gravatar image" /><p>condor27<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="condor27 has no accepted answers">0%</span></p></div></div><div id="comments-container-26329" class="comments-container"></div><div id="comment-tools-26329" class="comment-tools"></div><div class="clear"></div><div id="comment-26329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26368"></span>

<div id="answer-container-26368" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26368-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>How about something like:</p><pre><code>Statistics -&gt; IO Graph -&gt; Unit: Advanced... -&gt; Filter: *filter*, Calc: AVG(*), frame.time_delta -&gt; X Axis Tick interval: 0.1 sec</code></pre><p>... where *<em>filter</em>* is the display filter of only the packets you're interested in. If you want all packets, just leave the *<em>filter</em>* blank. Change the tick interval to suit your needs and feel free to experiment with the other "Calc's" such as <code>MAX(*)</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '13, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-26368" class="comments-container"><span id="26415"></span><div id="comment-26415" class="comment"><div id="post-26415-score" class="comment-score"></div><div class="comment-text"><p>In Statistics | IO Graph | When I graph... Filter = frame.time_delta_displayed I was hoping to get the Y Axis to show the values for the time_delta between each frame. But it says the Y Axis Unit is "Packets/Tick". Why doesn't it say something like "Time in ms" or just plane "Data Value"?</p><p>Oh, maybe if I do this: UNIT = Advanced , and SET Filter = blank, Calc = AVG(*) = frame.time_delta_displayed I don't understand why I'd need to use the AVG function. Is it doing an AVG for each tick on the X axis, so if each tick is 1s then I get the AVG delta over all frames that were sent in the whole 1 second?</p><p>I have about 500k packets in the capture, so I guess there is no way to graph all those data points, so we have to use AVG, correct?</p></div><div id="comment-26415-info" class="comment-info"><span class="comment-age">(25 Oct '13, 14:23)</span> condor27</div></div><span id="26416"></span><div id="comment-26416" class="comment"><div id="post-26416-score" class="comment-score"></div><div class="comment-text"><p>Thanks cmaynard! Now I just need to confirm my understanding of what the AVG function is doing exactly? or what the MAX function would do? Its all in relation to the tick size, right?</p></div><div id="comment-26416-info" class="comment-info"><span class="comment-age">(25 Oct '13, 14:29)</span> condor27</div></div><span id="26421"></span><div id="comment-26421" class="comment"><div id="post-26421-score" class="comment-score"></div><div class="comment-text"><p>You are correct. <code>AVG(*)</code> will plot the average delta time for all packets that passed the specified filter and fall within the tick interval. Similarly <code>MAX(*)</code> will plot the maximum delta time of all the packets that passed the specified filter and fall within the tick interval. The bigger the tick interval, the more packets are included in the <code>AVG(*)</code> calculation or taken into account to find the <code>MAX(*)</code>; the smaller the tick interval, the fewer packets will be included in the <code>AVG(*)</code> calculation or taken into account to find the <code>MAX(*)</code>.</p><p>If you want the actual plot <strong>values</strong> themselves, you can click the "Copy" button in the lower-left corner of the IO Graph and then paste those values into a spreadsheet for further graphing, processing, analysis, whatever.</p></div><div id="comment-26421-info" class="comment-info"><span class="comment-age">(26 Oct '13, 07:46)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-26368" class="comment-tools"></div><div class="clear"></div><div id="comment-26368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

