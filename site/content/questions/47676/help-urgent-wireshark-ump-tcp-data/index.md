+++
type = "question"
title = "help urgent WireShark ump tcp DATA"
description = '''on wireshark in protocol hierarchy statistics under tcp it says DATA and only data and also under udp its says its nearly up to 10 % in packages and bytes what is this and why is it there please help, any help will be much appreciated.'''
date = "2015-11-17T11:25:00Z"
lastmod = "2015-11-17T12:07:00Z"
weight = 47676
keywords = [ "udp", "data", "urgent-help", "tcp", "wireshark" ]
aliases = [ "/questions/47676" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [help urgent WireShark ump tcp DATA](/questions/47676/help-urgent-wireshark-ump-tcp-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47676-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>on wireshark in protocol hierarchy statistics under tcp it says DATA and only data and also under udp its says its nearly up to 10 % in packages and bytes what is this and why is it there please help, any help will be much appreciated.</p></div><div id="question-tags" class="tags-container tags">udp data urgent-help tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '15, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/5ec0ec3600cc181ca2ba0df090a8749b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jakejd&#39;s gravatar image" /><p>jakejd<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jakejd has no accepted answers">0%</span></p></div></div><div id="comments-container-47676" class="comments-container"></div><div id="comment-tools-47676" class="comment-tools"></div><div class="clear"></div><div id="comment-47676-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47678"></span>

<div id="answer-container-47678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47678-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>what is this and why is it there<br />
</p></blockquote><p>it is there because the payload of the corresponding tcp or udp packets could not be identified more exactly. Normally, below tcp, you find lines like "hypertext transfer protocol", "Secure Sockets Layer" and alike.<br />
</p><p>The reasons may be<br />
- disabled dissection of higher protocol hierarchy<br />
- non-standard ports used (if the payload is identified based on port number)<br />
- missing beginning of the communication (if the payload is identified heuristically)<br />
- limitation of frame size during capture</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '15, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Nov '15, 13:14</p></div></div><div id="comments-container-47678" class="comments-container"><span id="47679"></span><div id="comment-47679" class="comment"><div id="post-47679-score" class="comment-score"></div><div class="comment-text"><p>sindy so this doesn't mean that anyone is trying to get my mac's idk passwords or something because i searched them all and there all private ip's and thanks for answering.</p></div><div id="comment-47679-info" class="comment-info"><span class="comment-age">(17 Nov '15, 12:11)</span> jakejd</div></div><span id="47683"></span><div id="comment-47683" class="comment"><div id="post-47683-score" class="comment-score"></div><div class="comment-text"><p>Not enough information from your side and not enough knowledge on my side to answer this even if you would provide the capture, but maybe someone else would be able to answer if you publish the capture somewhere and post here a link to it. Please use comments instead of answers, calm down and read the site FAQ.</p></div><div id="comment-47683-info" class="comment-info"><span class="comment-age">(17 Nov '15, 12:19)</span> sindy</div></div><span id="47684"></span><div id="comment-47684" class="comment"><div id="post-47684-score" class="comment-score"></div><div class="comment-text"><p>oh and i tracked an ip under data and it was from Amsterdam why the hell would i get this ip and another is from the organisation cloud fare witch is a dns security thing witch i am not with and like amazon ip's is the source but the destination isn't my ip its private one witch is weird and this private one pops up a lot 192.168.0.6 this is the private ip.</p></div><div id="comment-47684-info" class="comment-info"><span class="comment-age">(17 Nov '15, 12:21)</span> jakejd</div></div><span id="47685"></span><div id="comment-47685" class="comment"><div id="post-47685-score" class="comment-score"></div><div class="comment-text"><p>and it also looks like someone is trying to ddos attack me because there is a lot and i mean a lot of packages coming in like i leave wire shark on for 1 minute and i get like a 1000 packages or is this normal i don't know</p></div><div id="comment-47685-info" class="comment-info"><span class="comment-age">(17 Nov '15, 12:28)</span> jakejd</div></div><span id="47686"></span><div id="comment-47686" class="comment"><div id="post-47686-score" class="comment-score"></div><div class="comment-text"><ol><li>How is your machine connected to the network (ethernet/WiFi/something else)?<br />
</li><li>Is there something else connected to the same network<br />
</li><li>do you use "promiscuous mode" for capture?<br />
</li></ol><p>If 2 and 3 are true, you may be capturing someone else's traffic under circumstances. As for the unknown IP addresses, a lot of web pages are using Amazon's cloud, a lot of web pages are using other web pages as source of advertisement banners and videos...</p></div><div id="comment-47686-info" class="comment-info"><span class="comment-age">(17 Nov '15, 12:29)</span> sindy</div></div><span id="47687"></span><div id="comment-47687" class="comment not_top_scorer"><div id="post-47687-score" class="comment-score"></div><div class="comment-text"><p>DDOS at 1000 packets per minute? LOL, guy, that's next to silence. DDOS are hundreds of thousands of packets per second. What other applications are running on your machine?</p></div><div id="comment-47687-info" class="comment-info"><span class="comment-age">(17 Nov '15, 12:42)</span> sindy</div></div><span id="47688"></span><div id="comment-47688" class="comment not_top_scorer"><div id="post-47688-score" class="comment-score"></div><div class="comment-text"><p>yh but it might just be a noob trying to do it from his 1 computer which I know won't do anything, but when it's coming in and I don't have a webpage open or anything else open that used the internet that's the only thing I could think of.</p></div><div id="comment-47688-info" class="comment-info"><span class="comment-age">(17 Nov '15, 12:51)</span> jakejd</div></div><span id="47689"></span><div id="comment-47689" class="comment not_top_scorer"><div id="post-47689-score" class="comment-score"></div><div class="comment-text"><p>As said - save the capture file, place it to some publicly accessible web (like cloudshark, google drive...), and put here a link. If I can't see anything in it, someone else may.</p><p>But if your machine has a public IP address and there is no firewall device between it and the network, then yes, you are most likely under several attacks simultaneously, this is a default state. E.g., for a linux machine with default passwords and no firewall configured, the time to be hacked is not more than 20 minutes from getting connected to the 'net.</p></div><div id="comment-47689-info" class="comment-info"><span class="comment-age">(17 Nov '15, 13:00)</span> sindy</div></div></div><div id="comment-tools-47678" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-47678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

