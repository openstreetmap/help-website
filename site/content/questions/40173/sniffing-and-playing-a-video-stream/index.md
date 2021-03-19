+++
type = "question"
title = "Sniffing and playing a video stream"
description = '''New user here. Hopefully I&#x27;m in the right place. I&#x27;m trying to send a unicast udp video stream from a Raspberry pi to a Windows server. The server will do two things. It will forward the stream and it will optionally let a person logged into the server view the stream. I can accomplish both of those...'''
date = "2015-03-01T21:57:00Z"
lastmod = "2015-03-02T08:00:00Z"
weight = 40173
keywords = [ "windows", "windump", "tcpdump", "tshark" ]
aliases = [ "/questions/40173" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Sniffing and playing a video stream](/questions/40173/sniffing-and-playing-a-video-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40173-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40173-score" class="post-score" title="current number of votes">0</div><span id="post-40173-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>New user here. Hopefully I'm in the right place.</p><p>I'm trying to send a unicast udp video stream from a Raspberry pi to a Windows server. The server will do two things. It will forward the stream and it will optionally let a person logged into the server view the stream. I can accomplish both of those tasks fairly easily with Windows versions of netcat and mplayer. However, I'm having a major difficulty doing both at the same time.</p><p>So right now I have the following command working great:</p><p>ncat -u -l -p 5000 | mplayer -fps 60 -cache 1024 -vo direct3d -</p><p>Similarly I will also want to use netcat to forward the stream. But, I can't have two netcat processes listen on the same port. Then I figured out I could use socat to multicast and then use another socat to listen to the multicast and do two unicasts, but that's a bit kludgy and my video ended up garbled.</p><p>Doing more research led me to trying to find a command line tool to mirror ports on the server. While researching this, I read about tcpdump, windump, tshark, and wireshark. I thought why mirror a port when I really could just sniff packets.</p><p>My hope was to sniff packets coming into port 5000 and pipe those off to mplayer. And at the same time, run netcat to forward the packets to the final destination. I started testing just the mplayer functionality. Unfortunately the video is quite garbled. Since I'm pretty new to tshark, I was hoping I could get some pointers. Here's what I'm trying:</p><p>tshark -i 1 -p -q -s 0 -w - udp port 5000</p><p>And I'm piping that to my mplayer command listed earlier. When testing this kind of thing with windump, I also got garbled video. But I wonder if that's because the windump (and maybe tshark) output is more than just the raw bytes? Or maybe something else is going on here? Should I go back to researching a port mirroring tool?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-windump" rel="tag" title="see questions tagged &#39;windump&#39;">windump</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '15, 21:57</strong></p><img src="https://secure.gravatar.com/avatar/adab1baa086933c505c754249d426f60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanU&#39;s gravatar image" /><p><span>DanU</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanU has no accepted answers">0%</span></p></div></div><div id="comments-container-40173" class="comments-container"></div><div id="comment-tools-40173" class="comment-tools"></div><div class="clear"></div><div id="comment-40173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40178"></span>

<div id="answer-container-40178" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40178-score" class="post-score" title="current number of votes">1</div><span id="post-40178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DanU has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it is more than just the raw bytes. It contains all things <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">PCAP</a>, which is to say datalink meta data and per packet meta data. And then the full network frame used to transport your bytes. Indeed a 'port mirror tool' would be better than these analysis tools.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '15, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40178" class="comments-container"><span id="40185"></span><div id="comment-40185" class="comment"><div id="post-40185-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response. I'll head my research in that direction.</p></div><div id="comment-40185-info" class="comment-info"><span class="comment-age">(02 Mar '15, 08:00)</span> <span class="comment-user userinfo">DanU</span></div></div></div><div id="comment-tools-40178" class="comment-tools"></div><div class="clear"></div><div id="comment-40178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

