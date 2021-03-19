+++
type = "question"
title = "Server resource usage"
description = '''How does Wireshark affects server resources? Is it safe to put on a production server? We are experiencing time-outs in accessing the server. We want to see what&#x27;s in the packets that&#x27;s why we are planning to install wireshark on the server. Is this advisable? What is the alternative way to look/cap...'''
date = "2013-01-08T08:56:00Z"
lastmod = "2013-01-08T14:13:00Z"
weight = 17573
keywords = [ "wireshark" ]
aliases = [ "/questions/17573" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Server resource usage](/questions/17573/server-resource-usage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17573-score" class="post-score" title="current number of votes">0</div><span id="post-17573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How does Wireshark affects server resources? Is it safe to put on a production server? We are experiencing time-outs in accessing the server. We want to see what's in the packets that's why we are planning to install wireshark on the server. Is this advisable? What is the alternative way to look/capture packets to the server? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '13, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/008cf314acdcafe71f123ddc637f5875?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bbmh123&#39;s gravatar image" /><p><span>bbmh123</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bbmh123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jan '13, 08:57</strong> </span></p></div></div><div id="comments-container-17573" class="comments-container"></div><div id="comment-tools-17573" class="comment-tools"></div><div class="clear"></div><div id="comment-17573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="17576"></span>

<div id="answer-container-17576" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17576-score" class="post-score" title="current number of votes">0</div><span id="post-17576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark for the most part is pretty benign. Unless you're talking about a 1Gig attached server going at 100% utilization, it should be safe. But to be absolutely sure, why not span/mirror the switch port connected to the server? This way, you can get access to the packet data w/o installing anything on the server. Also, just as an FYI, if your server is Unix/Linux/Solaris, you already have tcpdump/snoop on the server. So you can use that to capture the packets as necessary. If it's a Windows server, it may or may not have NetMon installed. You can also use that to capture the packets. In either case, you can analyze the data using Wireshark after the fact.</p><p>But some baseline troubleshooting should take place. For example, can you ping the server during the timeout events? You can write a ping script to ping the server once every few seconds and log it. This will help you nail down if this is an application issue or a physical issue.<br />
</p><p>Are there any logs on the switch port connecting the server? drops, link up/down messages? BPDU forwarding messages etc.? Not every message may get logged depending on the configuration, but it's the first thing you should rule out.</p><p>Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '13, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p><span>hansangb</span><br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div></div><div id="comments-container-17576" class="comments-container"></div><div id="comment-tools-17576" class="comment-tools"></div><div class="clear"></div><div id="comment-17576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17579"></span>

<div id="answer-container-17579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17579-score" class="post-score" title="current number of votes">0</div><span id="post-17579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not advisable, but there may be situations where there is no other option. Running a capture on one of the systems taking part in the conversation is problematic, since it will usually mess up at least some of the packets you're recording. This will make analysis a lot more difficult, and you need to know the side effects of capturing packets locally like that to be able to rule them out as a cause of any problems you're investigating.</p><p>It's a lot better to run a passive capture system that only records what the others are sending. That way you get a unbiased view at what is happening. Ways to do that are usually either capturing with a SPAN port, or (if you can afford it) by using a TAP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '13, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-17579" class="comments-container"></div><div id="comment-tools-17579" class="comment-tools"></div><div class="clear"></div><div id="comment-17579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17581"></span>

<div id="answer-container-17581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17581-score" class="post-score" title="current number of votes">0</div><span id="post-17581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If there's anything to put on a production server it would be dumpcap, Wireshark's capture client. I've run that for ages on a (lightly loaded) production server, writing out limited size capture files on a loop, so that I could pick up the capture once a problem was reported. Make sure to plan for enough storage though, on loaded networks this can add up quickly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '13, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-17581" class="comments-container"></div><div id="comment-tools-17581" class="comment-tools"></div><div class="clear"></div><div id="comment-17581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

