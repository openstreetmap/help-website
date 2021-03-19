+++
type = "question"
title = "traffic drop after migration"
description = '''Hi Experts, we have done migration from one platform to another platform. after migration , the traffic volume dropped more than 50%. we capture traffic with tcpdump and we see in wireshark that there are many ip fragmentation and re-transmissions in the trace. how can i share this trace to see how ...'''
date = "2014-07-03T02:02:00Z"
lastmod = "2014-07-05T00:16:00Z"
weight = 34375
keywords = [ "fragmentation", "retransmissions", "others" ]
aliases = [ "/questions/34375" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [traffic drop after migration](/questions/34375/traffic-drop-after-migration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34375-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts, we have done migration from one platform to another platform. after migration , the traffic volume dropped more than 50%. we capture traffic with tcpdump and we see in wireshark that there are many ip fragmentation and re-transmissions in the trace. how can i share this trace to see how much healthy is the traffic being generated ? could the drop be due to fragmentation or re-transmission or some thing in the trace we could not understand. please your kind support is needed to check the trace.</p></div><div id="question-tags" class="tags-container tags">fragmentation retransmissions others</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '14, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/f789cb523e8b046abc6500d2bd148f45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hanikhatib&#39;s gravatar image" /><p>hanikhatib<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hanikhatib has no accepted answers">0%</span></p></div></div><div id="comments-container-34375" class="comments-container"></div><div id="comment-tools-34375" class="comment-tools"></div><div class="clear"></div><div id="comment-34375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34433"></span>

<div id="answer-container-34433" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34433-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, hanikhatib</p><p>You migrated What from which platform to which platfom ?</p><p>Here some answers to your questions</p><p><strong>"How can I share this trace ?"</strong></p><ul><li><a href="http://cloudshark.org"></a><a href="http://cloudshark.org">http://cloudshark.org</a></li></ul><p><strong>"How much healthy traffic is being generated" ?</strong></p><ul><li>Look at the relative sequence numbers if you are interested in healthy TCP traffic.</li></ul><p><strong>Could the drop be due to fragmentation or re-transmission or something in the trace we could not understand" ?</strong></p><ul><li>The drop (= packet loss) probably is due to fragmentation as most firewalls wont allow fragmented ip traffic</li><li>the re-transmission is a result of packet loss, not a cause.</li><li>it could be something that we don't understand yet so back to answer number 1 if you want help from us ;-)</li></ul><p>Regards Matthias</p><hr /><p>If I read your comment correctly you changed your network provider...</p><p><strong>"we need to analyse the traffic ongoing"</strong><br />
</p><p>As this is a best-effort Q&amp;A site I think it's not the appropriate place to have an urgent prolem analyzed. I'd suggest you engage a professional network trouble shooting service.</p><p>As for wireshark handling: You can use <strong><code>editcap -i 60</code></strong> to split large traces in smaller pieces and using <strong><code>editcap -s 150</code></strong> you can even shrink it some more so it would fit on cloudshark and would enable us to take a brief look at it from any device like a smart phone from anywhere. I don't usually carry a PC with wireshark to look at traces in my leisure time ;-)</p><p>Anyhow as this is urgent, here's my 10.000 feet suggestion to what might be your problem.</p><p>Usually ip fragmentation should not occur as most modern IP stacks use PMTUD these days. This requires packet loss due to fragmentation required but would signal to the sender what the next hop's MTU size would be. This always comes with a delay and poor performance. I've seen this sceario happening when the traffic goes through a VPN infrastructure. To avoid this it is good practice for the VPN routers to reduce the MSS option in the SYN packets. This obviously does not happen in your (new core) environment.</p><p>So my suggestion would be to point your network provider to this URL:</p><p><a href="http://lmgtfy.com/?q=adjust-mss">http://lmgtfy.com/?q=adjust-mss</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '14, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jul '14, 08:48</p></div></div><div id="comments-container-34433" class="comments-container"><span id="34434"></span><div id="comment-34434" class="comment"><div id="post-34434-score" class="comment-score"></div><div class="comment-text"><p>Hi Matthias</p><p>we migrated GPRS traffic from one telecom core GGN to a new core GGN. the performance on the new core is low compared to previous core, even new core is much powerful. we investigated all elements in the network without any major issue. now we need to analyse the traffic ongoing. please note that i captured few mins of traffic and it is generating big traffic and i could not upload it to the cloushark.org site , it is 15MB.</p><p>so i uploaded it to another web site. <a href="https://www.wetransfer.com/downloads/6a4b6206d2dab6439f6eec0aa1f6b17e20140705090105/1ff278f46f75daac7eecfc5e6877da9c20140705090105/dfd5c3">https://www.wetransfer.com/downloads/6a4b6206d2dab6439f6eec0aa1f6b17e20140705090105/1ff278f46f75daac7eecfc5e6877da9c20140705090105/dfd5c3</a></p><p>i hope you can have look at the trace and give us any hint regarding the traffic in this capture. none of the team is able to analyse or understand what to do with this traffic capture or if it can tell us what is wrong.</p><p>it is very urgent to have any hand or support in this matter. i hope you can help us here. many thanks in advance. BR hani</p></div><div id="comment-34434-info" class="comment-info"><span class="comment-age">(05 Jul '14, 02:36)</span> hanikhatib</div></div></div><div id="comment-tools-34433" class="comment-tools"></div><div class="clear"></div><div id="comment-34433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

