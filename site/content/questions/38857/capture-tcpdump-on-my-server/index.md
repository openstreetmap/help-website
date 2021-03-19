+++
type = "question"
title = "capture tcpdump on my server"
description = '''I have installed Tcpdump on my RPI and placed the RPI between my router and server, i want to capture ip add. there is connecting and what files they are getting access to and ofc with a timestamp- But i can figure out what flags i have to use ? right know i am running tcpdump -I br0  and i really n...'''
date = "2015-01-02T16:31:00Z"
lastmod = "2015-01-05T08:40:00Z"
weight = 38857
keywords = [ "flags", "tcpdump" ]
aliases = [ "/questions/38857" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture tcpdump on my server](/questions/38857/capture-tcpdump-on-my-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38857-score" class="post-score" title="current number of votes">0</div><span id="post-38857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed Tcpdump on my RPI and placed the RPI between my router and server, i want to capture ip add. there is connecting and what files they are getting access to and ofc with a timestamp-</p><p>But i can figure out what flags i have to use ? right know i am running</p><p>tcpdump -I br0</p><p>and i really need it to be readable by a human :D</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flags" rel="tag" title="see questions tagged &#39;flags&#39;">flags</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jan '15, 16:31</strong></p><img src="https://secure.gravatar.com/avatar/eec29ee392df056f48c8b65be9a86716?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="notaduck&#39;s gravatar image" /><p><span>notaduck</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="notaduck has no accepted answers">0%</span></p></div></div><div id="comments-container-38857" class="comments-container"></div><div id="comment-tools-38857" class="comment-tools"></div><div class="clear"></div><div id="comment-38857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38874"></span>

<div id="answer-container-38874" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38874-score" class="post-score" title="current number of votes">2</div><span id="post-38874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I assume by 'RPI' you mean a Raspberry Pi (apparently) in bridged mode. If that's the case, you can can indeed use tcpdump to capture the traffic on the Pi. <strong>However I suggest to do the analysis with Wireshark</strong>, as it has more and better dissectors than tcpdump AND <strong>this is the Wireshark Q&amp;A site</strong> ;-)</p><blockquote><p>tcpdump -ni br0 -s0 -w /var/tmp/br0_frames.pcap</p></blockquote><p>After you have finished capturing, copy /var/tmp/br0_frames.pcap with scp or WinSCP to a system where you have Wireshark installed and open the file with Wireshark.</p><blockquote><p>and i really need it to be readable by a human :D</p></blockquote><p>If you understand what Wireshark will show you, depends on your knowledge of networking protocols. If you don't have that knowledge there is nothing Wireshark can do for you. Then you should look at the following resources.</p><p><strong>Books:</strong><br />
</p><ul><li><strong><a href="http://www.amazon.com/TCP-Illustrated-Vol-Addison-Wesley-Professional/dp/0201633469/ref=sr_1_1?ie=UTF8&amp;qid=1296828460&amp;sr=8-1">TCP/IP Illustrated (Volume 1)</a></strong> still the best resource to start with<br />
</li><li><strong><a href="http://www.wiresharkbook.com/">The Wireshark book</a></strong></li></ul><p>There obviously other books about networking. google will help: 'books networking'.</p><p><strong>Online resources:</strong><br />
</p><ul><li><strong><a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol">TCP on Wikipedia</a></strong><br />
</li><li><strong><a href="http://www.tcpipguide.com/index.htm">The TCP/IP guide</a></strong><br />
</li></ul><p>There are also some video tutorials about Wireshark on Youtube <strong><a href="http://www.youtube.com/results?search_query=wireshark">http://www.youtube.com/results?search_query=wireshark</a> tutorial</strong> - Hint: Please open the link in a separate browser window/tab manually, if clicking the link in your browser does not work).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '15, 02:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jan '15, 02:57</strong> </span></p></div></div><div id="comments-container-38874" class="comments-container"><span id="38893"></span><div id="comment-38893" class="comment"><div id="post-38893-score" class="comment-score"></div><div class="comment-text"><p>Somewhat off topic: As a Raspberry Pi user you may be aware of the fact that the SD card may not be the ideal storage for your capture file. You could mount a USB disk (on /media for instance) and write your capture file there.</p></div><div id="comment-38893-info" class="comment-info"><span class="comment-age">(05 Jan '15, 08:40)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-38874" class="comment-tools"></div><div class="clear"></div><div id="comment-38874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

