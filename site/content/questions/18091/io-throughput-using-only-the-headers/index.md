+++
type = "question"
title = "IO Throughput using only the Headers"
description = '''I have a device that it receiving a large amount of traffic on its gigabit link. I&#x27;m slightly worried about running a standard capture on it as it may create performance issues for the device. My question is what methods can I use to limit the amount of traffic I have to capture, that would still al...'''
date = "2013-01-30T03:43:00Z"
lastmod = "2013-01-30T11:43:00Z"
weight = 18091
keywords = [ "headers" ]
aliases = [ "/questions/18091" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [IO Throughput using only the Headers](/questions/18091/io-throughput-using-only-the-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18091-score" class="post-score" title="current number of votes">0</div><span id="post-18091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a device that it receiving a large amount of traffic on its gigabit link. I'm slightly worried about running a standard capture on it as it may create performance issues for the device. My question is what methods can I use to limit the amount of traffic I have to capture, that would still allow me to report the statistics within wireshark or tshark.</p><p>Can anyone confirm if tshark and wireshark uses the complete data payload when calculating the packet totals etc (i.e within the Protocol Hierarchy Stats), i.e and not just the TCP SEQ numbers in the case of TCP. As I was wondering if there is any way to only capture the headers and still be able to report the various protocol throughputs.</p><p>Many Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-headers" rel="tag" title="see questions tagged &#39;headers&#39;">headers</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '13, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p><span>bart80</span><br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div></div><div id="comments-container-18091" class="comments-container"></div><div id="comment-tools-18091" class="comment-tools"></div><div class="clear"></div><div id="comment-18091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18092"></span>

<div id="answer-container-18092" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18092-score" class="post-score" title="current number of votes">0</div><span id="post-18092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The stats will only be calculated for those parts of the packets that Wireshark can see. You'll need to ensure you capture enough to allow at least protocol detection for those protocols you want.</p><p>Do you need this info in real-time? If not, you'd also be better off using dumpcap to capture as Wireshark (and TShark to a lesser extent) will run out of memory due to maintaining conversations data etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18092" class="comments-container"><span id="18097"></span><div id="comment-18097" class="comment"><div id="post-18097-score" class="comment-score"></div><div class="comment-text"><p>It doesnt need to be in real time. So from what your saying as long as I capture the TCP headers or up to the first 100 bytes say, then I should be ok. I just wont be able to get too much in terms of UDP stats.</p></div><div id="comment-18097-info" class="comment-info"><span class="comment-age">(30 Jan '13, 05:53)</span> <span class="comment-user userinfo">bart80</span></div></div><span id="18100"></span><div id="comment-18100" class="comment"><div id="post-18100-score" class="comment-score"></div><div class="comment-text"><p>You could also miss out on stats where there are multiple pdu's, e.g. udp messages in a frame as the ones after the cutoff point won't be counted.</p><p>As you don't need this info in real-time I really recommend you use dumpcap for the captures.</p></div><div id="comment-18100-info" class="comment-info"><span class="comment-age">(30 Jan '13, 05:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="18110"></span><div id="comment-18110" class="comment"><div id="post-18110-score" class="comment-score"></div><div class="comment-text"><p>Trouble with dumpcap is that it isn't always available on the device that I am capturing on. The good thing with TCPdump is that is it normally always preinstalled.</p></div><div id="comment-18110-info" class="comment-info"><span class="comment-age">(30 Jan '13, 09:24)</span> <span class="comment-user userinfo">bart80</span></div></div><span id="18113"></span><div id="comment-18113" class="comment"><div id="post-18113-score" class="comment-score"></div><div class="comment-text"><p>tcpdump is also OK. The main thing is not to use Wireshark or TShark due to the memory consumption when there is a lot of traffic.</p></div><div id="comment-18113-info" class="comment-info"><span class="comment-age">(30 Jan '13, 09:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="18115"></span><div id="comment-18115" class="comment"><div id="post-18115-score" class="comment-score"></div><div class="comment-text"><p>Ah ok, so is there anything else I should consider when capturing traffic on a interface that is RX/TX around a gig per sec ?</p><p>Thanks for all your help...</p></div><div id="comment-18115-info" class="comment-info"><span class="comment-age">(30 Jan '13, 10:47)</span> <span class="comment-user userinfo">bart80</span></div></div><span id="18117"></span><div id="comment-18117" class="comment not_top_scorer"><div id="post-18117-score" class="comment-score"></div><div class="comment-text"><p>Disk i/o speed. <span>@jasper</span> knows more, but in another question he thought you needed 240MB/s write speed.</p></div><div id="comment-18117-info" class="comment-info"><span class="comment-age">(30 Jan '13, 11:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-18092" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-18092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

