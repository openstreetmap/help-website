+++
type = "question"
title = "prefix udp payload length after &quot;follow UDP Stream&quot;"
description = '''I have a .pcap file after capturing voice packets. I now want to filter RTP packets (with header). When I select stream I am interested in and do &quot;follow UDP stream&quot; I get the udp payload (RTP including the header). But for all the packets captured there is no packet size. My application would want ...'''
date = "2011-08-02T09:23:00Z"
lastmod = "2011-08-03T01:25:00Z"
weight = 5403
keywords = [ "length", "udp", "payload", "rtp" ]
aliases = [ "/questions/5403" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [prefix udp payload length after "follow UDP Stream"](/questions/5403/prefix-udp-payload-length-after-follow-udp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5403-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5403-score" class="post-score" title="current number of votes">0</div><span id="post-5403-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a .pcap file after capturing voice packets. I now want to filter RTP packets (with header). When I select stream I am interested in and do "follow UDP stream" I get the udp payload (RTP including the header). But for all the packets captured there is no packet size. My application would want a 4 byte "packet length" before each packet. How can I get this fro wireshark.</p><p>Thanks for the help in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '11, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/a93f17d087fcc6182314daa5e7218994?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shailesh&#39;s gravatar image" /><p><span>shailesh</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shailesh has no accepted answers">0%</span></p></div></div><div id="comments-container-5403" class="comments-container"></div><div id="comment-tools-5403" class="comment-tools"></div><div class="clear"></div><div id="comment-5403-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5418"></span>

<div id="answer-container-5418" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5418-score" class="post-score" title="current number of votes">1</div><span id="post-5418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no way to do that with "Follow UDP Stream" unless you change the source code and recompile Wireshark.</p><p>It might be easier to write a little script/program that uses the libpcap library to extract the UDP payload and save it with a length header in front of it. Then you can feed the individual RTP streams to it...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5418" class="comments-container"></div><div id="comment-tools-5418" class="comment-tools"></div><div class="clear"></div><div id="comment-5418-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

