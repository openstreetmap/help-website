+++
type = "question"
title = "How to find area of the IO graph"
description = '''Dear friends, I plotted a IO graph on a dump of packets collected over few seconds of time. I am able to see spikes/peaks in the graph with coordinates X-axis 1sec tick and Y-axis - bits/tick, scale - auto. I would like to find out the area of the peak above a certain point of y-axis. Say, my thresh...'''
date = "2011-03-06T13:40:00Z"
lastmod = "2011-03-06T14:46:00Z"
weight = 2682
keywords = [ "graph", "area", "burst", "io", "plot" ]
aliases = [ "/questions/2682" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find area of the IO graph](/questions/2682/how-to-find-area-of-the-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2682-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear friends, I plotted a IO graph on a dump of packets collected over few seconds of time. I am able to see spikes/peaks in the graph with coordinates X-axis 1sec tick and Y-axis - bits/tick, scale - auto. I would like to find out the area of the peak above a certain point of y-axis. Say, my threshold limit is 4Mbps, I would like to find the amount of over-subscribed traffic above 4Mbps for the duration it over-subscribed. If i am correct, we need to use integration but i am not able to nail down the function to do so. Please help me in this regard and throw some light on. Your help is highly appreciated. To summarize - Function through which the graph is plotted. - Finding out the area of a spike above a certain threshold.</p><p>Thanks, Rukesh</p></div><div id="question-tags" class="tags-container tags">graph area burst io plot</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '11, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/3ce92b08114e2c6940d1a780fb8616cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rukesh&#39;s gravatar image" /><p>Rukesh<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rukesh has no accepted answers">0%</span></p></div></div><div id="comments-container-2682" class="comments-container"></div><div id="comment-tools-2682" class="comment-tools"></div><div class="clear"></div><div id="comment-2682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2683"></span>

<div id="answer-container-2683" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2683-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't really just see what went above a threshhold, but you can look at the view of all traffic between two points in time. To do this, simply bring up your IO graph. Click on the are where it goes above the threshhold you have in mind. This will select a packet in the packet list. Set this as your starting point with a display filter based on the frame number. For example "frame.number &gt;=299". Go back to your IO Graph and choose the end of the period of time that goes above the threshhold. This will select another packet. Note the frame number and expand your display filter. For example frame.number &gt;=299 &amp;&amp; frame.number &lt;=375". This would display everything between frame 299 and 375. At this point, you can work with the data or save it out as an independent CAP file.<br />
</p><p>This is not as elegant as a drop and drag on the IO Graph, but it does allow you to focus. Beyond that, you might be interested in Cace Pilot. Watch some of the video's on that. Be aware that Cace is not a GPL product like Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '11, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span> </br></p></div></div><div id="comments-container-2683" class="comments-container"><span id="2684"></span><div id="comment-2684" class="comment"><div id="post-2684-score" class="comment-score"></div><div class="comment-text"><p>Dear Mr.Stewart,</p><p>Brilliant. Really, it brought some light into me. Thanks a lot. Immediately, i did use your suggestion - frame.numbe &gt;=,&lt;= and i got a nice extract. With this, can i go ahead using area of triangle or rectangle, which ever the way, the peak burst(&gt; committed rate over a period) looks like? Or is it just the difference between the frames with number &gt;= &amp;&amp; &lt;= ? Please extend your support. As CACE tool might take another 48 hrs to download, i need to analyse the data immediately. My req- is to find out the amount of burst occured &gt; CIR in the period of sec.</p><p>Many thanks, Rukesh</p></div><div id="comment-2684-info" class="comment-info"><span class="comment-age">(06 Mar '11, 16:45)</span> Rukesh</div></div><span id="2685"></span><div id="comment-2685" class="comment"><div id="post-2685-score" class="comment-score"></div><div class="comment-text"><p>The display filter "frame.number &gt;=# &amp;&amp; frame.number &lt;=##" would be every frame number between # and ##. Since they are captured in order, this will be a period of time. If you are wanting to see what the &gt; Cir is in a period of second, you can bring an IO Graph back up and set your Tick interval to 1 Second and set the Unit to Bits/s. If you want to keep the scale consistent, set it to something like 2x your CIR. Now the problem is you are looking at traffic in both directions. Read on.</p></div><div id="comment-2685-info" class="comment-info"><span class="comment-age">(06 Mar '11, 16:59)</span> Paul Stewart</div></div><span id="2686"></span><div id="comment-2686" class="comment"><div id="post-2686-score" class="comment-score"></div><div class="comment-text"><p>To look at the traffic one direction at a time in the IO Graph, click on the Graph1 button to disable it. Then in the Graph 2 text box next to the filter button filter based on your IP source range. For example, mine is "ip.src==192.168.1.0/24". Then in the same box near Graph 3, filter to your destination. For example mine is "ip.dst==192.168.1.0/24". Then click the "Graph 2" and "Graph 3" buttons. At this point, the red line will be your outbound bits/s and the green line is the inbound bits/s. HTH.</p></div><div id="comment-2686-info" class="comment-info"><span class="comment-age">(06 Mar '11, 17:03)</span> Paul Stewart</div></div></div><div id="comment-tools-2683" class="comment-tools"></div><div class="clear"></div><div id="comment-2683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

