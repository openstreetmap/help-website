+++
type = "question"
title = "Plotting graphs for network delay"
description = '''Hi, i&#x27;m a newbie in wireshark. i have a &quot;.pcap&quot; file that contains a VoIP call. I wana know the network delay of this call for each packet. I can see the delay (the time taken by packets to reach the destination) but i wana plot this data on graph. does wireshark have capability to give me the graph...'''
date = "2014-02-22T12:03:00Z"
lastmod = "2014-02-28T11:06:00Z"
weight = 30100
keywords = [ "latency", "graphs", "packetdelay", "packetloss" ]
aliases = [ "/questions/30100" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Plotting graphs for network delay](/questions/30100/plotting-graphs-for-network-delay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30100-score" class="post-score" title="current number of votes">0</div><span id="post-30100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i'm a newbie in wireshark. i have a ".pcap" file that contains a VoIP call. I wana know the network delay of this call for each packet. I can see the delay (the time taken by packets to reach the destination) but i wana plot this data on graph. does wireshark have capability to give me the graph? if NO, then what tool should i use? the graph may have time along x-axis and delay (in seconds or Milli seconds) along y-axis. i also wana see the packet losses in this call in graphical form. one thing u should keep in mind while answering is that i'm newbie, i don't have good command on wireshark filters or such.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-graphs" rel="tag" title="see questions tagged &#39;graphs&#39;">graphs</span> <span class="post-tag tag-link-packetdelay" rel="tag" title="see questions tagged &#39;packetdelay&#39;">packetdelay</span> <span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '14, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/f610e4a11992d3a39effbeb0cf10c906?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Javeeria%20Jalil&#39;s gravatar image" /><p><span>Javeeria Jalil</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Javeeria Jalil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Feb '14, 12:04</strong> </span></p></div></div><div id="comments-container-30100" class="comments-container"><span id="30240"></span><div id="comment-30240" class="comment"><div id="post-30240-score" class="comment-score"></div><div class="comment-text"><p>still no answer even after 5 days....... even if there is no answer to my question, someone may say its not possible with wireshark.......... or atleast guide me in the right direction........ some one plz help</p></div><div id="comment-30240-info" class="comment-info"><span class="comment-age">(27 Feb '14, 10:11)</span> <span class="comment-user userinfo">Javeeria Jalil</span></div></div></div><div id="comment-tools-30100" class="comment-tools"></div><div class="clear"></div><div id="comment-30100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30279"></span>

<div id="answer-container-30279" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30279-score" class="post-score" title="current number of votes">0</div><span id="post-30279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well I can take a shot, but I'm not sure I'm right. As far as I know, the exact graph you're looking for doesn't exist natively in Wireshark, at least in the sense that there's no such graph already created for you.</p><p>There <em>are</em> ways of seeing various stats for SIP-based calls. For example, clicking on the menu item 'Telephony-&gt;Voip Calls' brings up a dialog showing the various calls in the capture; if you select one of those calls and click the "Flow" button, it will show you another dialog with the timestamps on the left, and message flow in the mdidle (what is typically called a "ladder diagram" in the SIP world).</p><p>There is also the "Statistics-&gt;IO Graph", which is very customizable. You could try playing with that to see if you can get what you want. But I don't think it will do what you want. It's really meant more as a way to graph packet rates/counts over time.</p><p>With regard to other tools - there are a LOT of SIP based analysis tools; most of them cost money. Otherwise, you could submit an enhancement request on <a href="https://bugs.wireshark.org/bugzilla/">bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '14, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30279" class="comments-container"></div><div id="comment-tools-30279" class="comment-tools"></div><div class="clear"></div><div id="comment-30279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

