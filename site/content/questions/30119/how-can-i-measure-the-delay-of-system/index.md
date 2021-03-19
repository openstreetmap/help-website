+++
type = "question"
title = "How can I measure the delay of system?"
description = '''Hi all  I&#x27;m posting to know how can I measure the system delay.  for the details, please refer to attached picture.  '''
date = "2014-02-24T00:47:00Z"
lastmod = "2014-02-24T10:01:00Z"
weight = 30119
keywords = [ "delay" ]
aliases = [ "/questions/30119" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How can I measure the delay of system?](/questions/30119/how-can-i-measure-the-delay-of-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30119-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all I'm posting to know how can I measure the system delay. for the details, please refer to attached picture. <img src="https://osqa-ask.wireshark.org/upfiles/ScreenHunter_03_Feb._24_17.46.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">delay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '14, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/27e4d1e97303115b07caf9ba39267f2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ray_Han&#39;s gravatar image" /><p>Ray_Han<br />
<span class="score" title="56 reputation points">56</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ray_Han has no accepted answers">0%</span></p></img></div></div><div id="comments-container-30119" class="comments-container"></div><div id="comment-tools-30119" class="comment-tools"></div><div class="clear"></div><div id="comment-30119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30136"></span>

<div id="answer-container-30136" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30136-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want 'real results', you should not rely on the mirror functionality of the switch for this, as you will never know how exactly (in which order) the switch copies the frames from 3+2 to the mirror port. The best option would be to capture the traffic of port 3 and 2 with a TAP for each port and with two systems with 'highly synchronized' clocks.</p><p><strong>However:</strong> That's pretty much overhead (TAPs, two systems, etc.). If the expected delay is small (a few microseconds), you'll have to do it like described above, if you want to get 'real results'. If the expected delay is much larger (a few milliseconds) the approach with a switch mirror port and one capture system <strong>might</strong> be good enough.</p><p>Either way you need to calculate the delay between two identical frames in the capture file. That can be done with tshark and a script (perl, python, whatever).</p><blockquote><p>tshark -nr input.pcap -T fields -e frame.number -e ip.id -e frame.time_relative</p></blockquote><p>The output looks similar to this:</p><pre><code>1       0xf038  0.000000000
2       0xf039  0.019413000
3       0xf038  0.02136700
4       0xf039  0.03316100</code></pre><p>With the script you can find duplicate IP IDs and calculate the delta between the two time stamps. The delta values can be loaded into a spreadsheet software to create a chart.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '14, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30136" class="comments-container"><span id="30914"></span><div id="comment-30914" class="comment"><div id="post-30914-score" class="comment-score"></div><div class="comment-text"><p>appology late update. it's good help to get the delay but don't use tshark what you said. but I think your comments is very good. I'm studying tshrark. Thank you.</p></div><div id="comment-30914-info" class="comment-info"><span class="comment-age">(18 Mar '14, 00:29)</span> Ray_Han</div></div></div><div id="comment-tools-30136" class="comment-tools"></div><div class="clear"></div><div id="comment-30136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

