+++
type = "question"
title = "Calculating Enterprise NetFlow Volume"
description = '''how can I use wireshark (or Pilot/Cascade) analysis to determine my enterprise netflows per sec?'''
date = "2012-05-25T13:04:00Z"
lastmod = "2012-05-26T04:39:00Z"
weight = 11349
keywords = [ "volume", "netflow", "enterprise" ]
aliases = [ "/questions/11349" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Calculating Enterprise NetFlow Volume](/questions/11349/calculating-enterprise-netflow-volume)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11349-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how can I use wireshark (or Pilot/Cascade) analysis to determine my enterprise netflows per sec?</p></div><div id="question-tags" class="tags-container tags">volume netflow enterprise</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '12, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/a6832dd5f2cb06ac82c0608be4f8950d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Philster&#39;s gravatar image" /><p>Philster<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Philster has no accepted answers">0%</span></p></div></div><div id="comments-container-11349" class="comments-container"><span id="11351"></span><div id="comment-11351" class="comment"><div id="post-11351-score" class="comment-score"></div><div class="comment-text"><blockquote><p>determine my enterprise netflows per sec?</p></blockquote><p>what does that mean?</p></div><div id="comment-11351-info" class="comment-info"><span class="comment-age">(25 May '12, 13:07)</span> Kurt Knochner ♦</div></div><span id="11352"></span><div id="comment-11352" class="comment"><div id="post-11352-score" class="comment-score"></div><div class="comment-text"><p>a) netflow records per second received, which would mean some sort of investigation of the volume of netflow records coming in b) statistical drilldown of flows reported, which would mean "can Wireshark do what a Netflow Collector does?"</p></div><div id="comment-11352-info" class="comment-info"><span class="comment-age">(25 May '12, 13:28)</span> Jasper ♦♦</div></div><span id="11367"></span><div id="comment-11367" class="comment"><div id="post-11367-score" class="comment-score"></div><div class="comment-text"><p>So in this case I'm not asking if Wireshark does what a netflow collector does. I'm asking if there's a filter or analysis you can perform on a capture of your netflow collector's input interface that can determine the actual count of netflows being received, in terms of flows per second?</p></div><div id="comment-11367-info" class="comment-info"><span class="comment-age">(25 May '12, 17:52)</span> Philster</div></div><span id="11368"></span><div id="comment-11368" class="comment"><div id="post-11368-score" class="comment-score"></div><div class="comment-text"><p>So I'm thinking, if you filter on the netflow traffic port on the flow collector interface - you can get a connection count between there and all of the remote devices sending flow. However, I don't think that a count of netflow connections is the same thing as the number of netflows being sent.</p></div><div id="comment-11368-info" class="comment-info"><span class="comment-age">(25 May '12, 17:56)</span> Philster</div></div></div><div id="comment-tools-11349" class="comment-tools"></div><div class="clear"></div><div id="comment-11349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11371"></span>

<div id="answer-container-11371" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11371-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>that can determine the actual count of netflows being received</p></blockquote><p>Can you please try this:</p><blockquote><p><code>tshark -r netflow.cap -T fields -e frame.number -e frame.time_relative -e cflow.flows -E header=y -E separator=;</code></p></blockquote><p>Then use an external tool (a script or Excel) to calculate the number of flows per second.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '12, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11371" class="comments-container"><span id="11382"></span><div id="comment-11382" class="comment"><div id="post-11382-score" class="comment-score"></div><div class="comment-text"><p>I will try this, THX! However, not being able to visualize it without data, what kind of calculation do you make in the spreadsheet?</p></div><div id="comment-11382-info" class="comment-info"><span class="comment-age">(26 May '12, 12:22)</span> Philster</div></div><span id="11385"></span><div id="comment-11385" class="comment"><div id="post-11385-score" class="comment-score"></div><div class="comment-text"><p>that depends on what you need. If you just need a total value, then summarize all flows and divide it by the duration (seconds) of the capture. If you need the flows for every second/minute, you'll have to summarize all flows during one second/minute. I'm not an excel expert and I would rather use a perl script, so I cannot help you with that calculation in excel. You could try to create a line chart from the data (y-axis: flows, x-axis: time).</p><p>Another option would be the IO Graphs of Wireshark:</p><blockquote><p>Statistics -&gt; IO Graph</p></blockquote><p>Select <strong>Advanced</strong> for the <strong>Y Axis</strong></p><p>then</p><p>Graph 1: Calc: AVG(*) <strong>cflow.flows</strong> Style: Line</p><p>If AVG(*) does not deliver what you need, try other calc methods (COUNT).</p></div><div id="comment-11385-info" class="comment-info"><span class="comment-age">(26 May '12, 14:49)</span> Kurt Knochner ♦</div></div><span id="11398"></span><div id="comment-11398" class="comment"><div id="post-11398-score" class="comment-score"></div><div class="comment-text"><p>The latter method using the Wireshark IO graphs - that doesn't require any intermediate processing in a spreadsheet, does it? Can't you use that directly on the capture? This sounds easier.</p></div><div id="comment-11398-info" class="comment-info"><span class="comment-age">(27 May '12, 06:25)</span> Philster</div></div><span id="11403"></span><div id="comment-11403" class="comment"><div id="post-11403-score" class="comment-score"></div><div class="comment-text"><p>Wireshark IO Graphs do not require Excel and it works directly on the capture data. Just follow my explanation.</p></div><div id="comment-11403-info" class="comment-info"><span class="comment-age">(27 May '12, 11:58)</span> Kurt Knochner ♦</div></div><span id="11454"></span><div id="comment-11454" class="comment"><div id="post-11454-score" class="comment-score"></div><div class="comment-text"><p>My version 1.4.6 Wireshark doesn't have any advanced options. What am I missing? <img src="https://osqa-ask.wireshark.org/upfiles/WIRESHARK.jpg" alt="alt text" /></p></div><div id="comment-11454-info" class="comment-info"><span class="comment-age">(29 May '12, 12:01)</span> Philster</div></div><span id="11460"></span><div id="comment-11460" class="comment not_top_scorer"><div id="post-11460-score" class="comment-score"></div><div class="comment-text"><p>Please check what you see in the drop down menu for <strong>Y Axis - Unit:</strong>. The default value is <strong>Packets/Tick</strong>. If there is no <strong>Advanced</strong> option in the drop down menu, you need a newer version of wireshark (1.6.8 or 1.7.x).</p></div><div id="comment-11460-info" class="comment-info"><span class="comment-age">(29 May '12, 20:45)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11371" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-11371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

