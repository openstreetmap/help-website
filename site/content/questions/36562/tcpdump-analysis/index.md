+++
type = "question"
title = "tcpdump analysis"
description = '''I&#x27;m trying to dig into an issue I&#x27;m seeing on a number of systems in my environment. It&#x27;s repeatable in a number of different areas, which makes me think there is something going on in the network equipment or NICs, but I&#x27;m trying to build up some evidence to help narrow the search. I get expected t...'''
date = "2014-09-24T07:01:00Z"
lastmod = "2014-09-24T09:09:00Z"
weight = 36562
keywords = [ "tcpdump" ]
aliases = [ "/questions/36562" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcpdump analysis](/questions/36562/tcpdump-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36562-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to dig into an issue I'm seeing on a number of systems in my environment. It's repeatable in a number of different areas, which makes me think there is something going on in the network equipment or NICs, but I'm trying to build up some evidence to help narrow the search.</p><p>I get expected throughput when running throughput tests with netperf or iperf when running from a 1 GbE or 10 GbE connected client system to a test host that is connected via 10 GbE. If I choose a host that is connected to 1 GbE or switch to a NIC that is 1 GbE on the same host, I get terrible performance. i.e.. 900 ish Mb/s on the good test..... down to 10-50 Mb/s on the bad.<br />
</p><p>I used tcpdump to capture traffic data and used Wireshark to examine. I'm a newbie with Wireshark and a relative newbie to network traffic analysis. I've attached an image of the wireshark 'expert info' summary from the poor performing test case (10 second test). Compared to the good performing 10 second test case, this trace has what appears to be alot of duplicate acks and retransmissions. In the good test case, I think I see perhaps at most one dup ack for packets transmitted. I'm asking here for confirmation of that assumption. And is there anything I can pull out of this trace to find a clue to what might be causing the problem? I can make this happen on several different systems, so it seems unlikely to be any one port/sfp/nic issue... but perhaps a bank of ports, or some other configuration issue could be causing it.<br />
</p><p>In an effort to learn more instead of nag my Network peers, I thought I'd ask here first.<br />
</p><p>Any advice for this Newb is much appreciated ;-)</p><p>-lp</p><p><img src="https://osqa-ask.wireshark.org/upfiles/1gb_expert_info_cS3wuYC.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '14, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/e9ac350ed16f7ccd93b81db42a7d384f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="luverofpeanuts&#39;s gravatar image" /><p>luverofpeanuts<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="luverofpeanuts has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '14, 06:03</p></div></div><div id="comments-container-36562" class="comments-container"><span id="36591"></span><div id="comment-36591" class="comment"><div id="post-36591-score" class="comment-score"></div><div class="comment-text"><p>Not sure if you're aware of this or not, but I can't download your trace because it's been downloaded too many times which has reached a bandwidth limit threshold. Perhaps you want to upload it to cloudshark for others to see. If you're concerned about anonymity, I just stumbled across a www.tracewrangler.com mention in another thread.</p></div><div id="comment-36591-info" class="comment-info"><span class="comment-age">(25 Sep '14, 05:36)</span> smp</div></div><span id="36593"></span><div id="comment-36593" class="comment"><div id="post-36593-score" class="comment-score"></div><div class="comment-text"><p>That's strange. I'll delete from google drive and put on cloud shark. Thanks for pointing that out.</p></div><div id="comment-36593-info" class="comment-info"><span class="comment-age">(25 Sep '14, 05:56)</span> luverofpeanuts</div></div></div><div id="comment-tools-36562" class="comment-tools"></div><div class="clear"></div><div id="comment-36562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36567"></span>

<div id="answer-container-36567" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36567-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>Any advice for this Newb is much appreciated ;-)</code></pre><p>Ok, well then: It's very difficult to troubleshoot from screen shots, so we would be better able to help you if you uploaded an actual trace file somewhere and then provided a link so we could look at the real packets. <a href="http://www.cloudshark.org">Cloudshark</a> is a good choice, but Dropbox or Google Drive would do as well.</p><p>Having said that, duplicate ACKs and retransmissions are a sign of packet loss, so some device along the path is dropping packets. You'll need to move Wireshark along the path and capture in different places to see what device is dropping packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '14, 09:09</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span> </br></p></div></div><div id="comments-container-36567" class="comments-container"><span id="36568"></span><div id="comment-36568" class="comment"><div id="post-36568-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply. When I realized I couldn't attach a file, I decided to post the screen shot first. I did just update the post with a link to my raw tcpdump file. ;-)</p></div><div id="comment-36568-info" class="comment-info"><span class="comment-age">(24 Sep '14, 09:52)</span> luverofpeanuts</div></div></div><div id="comment-tools-36567" class="comment-tools"></div><div class="clear"></div><div id="comment-36567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

