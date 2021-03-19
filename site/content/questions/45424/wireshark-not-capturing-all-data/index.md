+++
type = "question"
title = "Wireshark not capturing all data?"
description = '''I am trying to isolate a network issue by using Wireshark. I am capturing packets from a PC using the dumpcap commands. I want to find out when a RDP session starts and stops. Using the dumpcap at a cmd prompt, I see Wireshark filling up the directory with .pcap files. After stopping the capture and...'''
date = "2015-08-27T14:16:00Z"
lastmod = "2015-08-31T08:29:00Z"
weight = 45424
keywords = [ "dumpcap" ]
aliases = [ "/questions/45424" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not capturing all data?](/questions/45424/wireshark-not-capturing-all-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45424-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45424-score" class="post-score" title="current number of votes">0</div><span id="post-45424-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to isolate a network issue by using Wireshark. I am capturing packets from a PC using the dumpcap commands. I want to find out when a RDP session starts and stops. Using the dumpcap at a cmd prompt, I see Wireshark filling up the directory with .pcap files. After stopping the capture and using the filter tcp.port eq 3389, I can see the start of the RDP session. Let’s say the SYN is in file 1.pcap. Throughout file 1.pcap, I see ACKs, COTPs and TPKTs. However, when I review file 2.pcap, file 3.pcap, etc and use the same filter, no data displays. But I check file 20.pcap and apply the same filter, data appears!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '15, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/e360edc5db6cd48658941723e6e02d1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjcreek55&#39;s gravatar image" /><p><span>tjcreek55</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjcreek55 has no accepted answers">0%</span></p></div></div><div id="comments-container-45424" class="comments-container"><span id="45426"></span><div id="comment-45426" class="comment"><div id="post-45426-score" class="comment-score"></div><div class="comment-text"><p>How large are your trace file (GB) and how long (time) are they?</p></div><div id="comment-45426-info" class="comment-info"><span class="comment-age">(27 Aug '15, 16:17)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="45428"></span><div id="comment-45428" class="comment"><div id="post-45428-score" class="comment-score"></div><div class="comment-text"><p>The trace files are 10Mb.</p></div><div id="comment-45428-info" class="comment-info"><span class="comment-age">(27 Aug '15, 18:08)</span> <span class="comment-user userinfo">tjcreek55</span></div></div><span id="45429"></span><div id="comment-45429" class="comment"><div id="post-45429-score" class="comment-score"></div><div class="comment-text"><p>Also, there were at least two trace files in a minute.</p></div><div id="comment-45429-info" class="comment-info"><span class="comment-age">(27 Aug '15, 19:04)</span> <span class="comment-user userinfo">tjcreek55</span></div></div><span id="45431"></span><div id="comment-45431" class="comment"><div id="post-45431-score" class="comment-score"></div><div class="comment-text"><p>Maybe there is just no data, because no packet has been send. Could that be?</p></div><div id="comment-45431-info" class="comment-info"><span class="comment-age">(27 Aug '15, 21:33)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="45437"></span><div id="comment-45437" class="comment"><div id="post-45437-score" class="comment-score"></div><div class="comment-text"><p>As Christian said, maybe there was no data.</p><p>When you're working with multiple files (filesets) I recommend Jasper's great TraceWrangler tool (<a href="https://www.tracewrangler.com/).">https://www.tracewrangler.com/).</a> With it you can extract packets for a specific conversation spanning multiple files.</p></div><div id="comment-45437-info" class="comment-info"><span class="comment-age">(27 Aug '15, 23:54)</span> <span class="comment-user userinfo">Uli</span></div></div></div><div id="comment-tools-45424" class="comment-tools"></div><div class="clear"></div><div id="comment-45424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45547"></span>

<div id="answer-container-45547" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45547-score" class="post-score" title="current number of votes">0</div><span id="post-45547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Christin and Uli, Thanks for the comments. And yes, it is a possibility there was no data. But, I don't know.</p><p>To further isolate this issue, I added two capture filters. Theses filters only captured frames from the host I am troubleshooting and where RDP. Example: dump cap "host 1.1.1.1" "port 3389" -i 1 -b files:10000 -b filesize:30000 c:\tjcreek55.pcap</p><p>The capture filters eliminated the multiple .pcap files in the same minute. Additionally, did not have a lot of files filling up the hard drive. The files I had only contained the frames I really wanted to see. I could clearly see, follow, and track what was going on with the TCP session. Please note, you must use quotes around the capture filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '15, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/e360edc5db6cd48658941723e6e02d1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjcreek55&#39;s gravatar image" /><p><span>tjcreek55</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjcreek55 has no accepted answers">0%</span></p></div></div><div id="comments-container-45547" class="comments-container"></div><div id="comment-tools-45547" class="comment-tools"></div><div class="clear"></div><div id="comment-45547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

