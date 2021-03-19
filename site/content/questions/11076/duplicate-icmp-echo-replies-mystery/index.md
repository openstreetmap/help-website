+++
type = "question"
title = "Duplicate ICMP echo replies mystery"
description = '''When running a ping -t to one of our Cisco routers, we noticed on occasion a (DUP!) after a few of the replies. When looking at the pcap, I can see the sequence number of the request with 2 replies from the same target. The only difference I could see was that in the first reply, WS showed that it w...'''
date = "2012-05-16T20:01:00Z"
lastmod = "2012-05-17T00:36:00Z"
weight = 11076
keywords = [ "icmp" ]
aliases = [ "/questions/11076" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate ICMP echo replies mystery](/questions/11076/duplicate-icmp-echo-replies-mystery)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11076-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When running a ping -t to one of our Cisco routers, we noticed on occasion a (DUP!) after a few of the replies. When looking at the pcap, I can see the sequence number of the request with 2 replies from the same target. The only difference I could see was that in the first reply, WS showed that it was a response to the requesting packet and in the second reply, there was no such reference. 99% of the pings are fine but now we have concerns that the unit might be defective. How should I interprete these duplicate replies?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '12, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p>EricKnaus<br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-11076" class="comments-container"></div><div id="comment-tools-11076" class="comment-tools"></div><div class="clear"></div><div id="comment-11076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11085"></span>

<div id="answer-container-11085" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11085-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Is the router connected to the same switch as your client? If so, are the two replies from the same MAC address?</li><li>Is the router part of a HSRP configuration?</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '12, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '12, 00:57</p></div></div><div id="comments-container-11085" class="comments-container"><span id="11103"></span><div id="comment-11103" class="comment"><div id="post-11103-score" class="comment-score"></div><div class="comment-text"><p>Kurt - No HSRP. Pinging across the Internet (to a WAN), same MAC - nothing else was plugged into the router when we were testing this.</p><p>Thanks</p><p>Eric</p></div><div id="comment-11103-info" class="comment-info"><span class="comment-age">(17 May '12, 08:08)</span> EricKnaus</div></div><span id="11108"></span><div id="comment-11108" class="comment"><div id="post-11108-score" class="comment-score"></div><div class="comment-text"><p>Is the router publicly pingable so we might be able to reproduce the issue? Do you see duplicates from multiple sources to this router? Do you see duplicates ping other systems from the same source?</p></div><div id="comment-11108-info" class="comment-info"><span class="comment-age">(17 May '12, 09:33)</span> SYN-bit ♦♦</div></div><span id="11116"></span><div id="comment-11116" class="comment"><div id="post-11116-score" class="comment-score"></div><div class="comment-text"><p>can you post a cpature file with the DUP replys to <a href="http://cloudshark.org">cloudshark.org</a>? Did both replies have the same TTL?</p></div><div id="comment-11116-info" class="comment-info"><span class="comment-age">(17 May '12, 14:16)</span> Kurt Knochner ♦</div></div><span id="11174"></span><div id="comment-11174" class="comment"><div id="post-11174-score" class="comment-score"></div><div class="comment-text"><p>I was going to but the owner asked me not to because he did not want the world pinging it all day! Looking for a plan B</p></div><div id="comment-11174-info" class="comment-info"><span class="comment-age">(21 May '12, 06:35)</span> EricKnaus</div></div><span id="11195"></span><div id="comment-11195" class="comment"><div id="post-11195-score" class="comment-score"></div><div class="comment-text"><p>You may send me a small capture file with the dup ping responses in it at [email protected]<a href="http://SYN-bit.nl">SYN-bit.nl</a> and I will have a quick look at it to see whether I can see anything funny in the trace.</p></div><div id="comment-11195-info" class="comment-info"><span class="comment-age">(21 May '12, 21:36)</span> SYN-bit ♦♦</div></div><span id="11198"></span><div id="comment-11198" class="comment not_top_scorer"><div id="post-11198-score" class="comment-score"></div><div class="comment-text"><p>you could randomize the ip addresses with tcprewrite <a href="http://tcpreplay.synfin.net/wiki/tcprewrite">http://tcpreplay.synfin.net/wiki/tcprewrite</a> and then post the capture file on <a href="http://cloudshark.org">cloudshark.org</a></p></div><div id="comment-11198-info" class="comment-info"><span class="comment-age">(21 May '12, 23:45)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11085" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-11085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

