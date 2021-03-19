+++
type = "question"
title = "Dumpcap capture filter question"
description = '''Hi, I am struggling to create a filter to capture VoIP traffic using Dumpcap. I can capture everything but I cannot apply a capture filter successfully. I need to basically capture the following. Port 13060 TCP/UDP Port 13061 TCP Port 13090 TCP/UDP Ports 54000-65000 UDP This is the command I have so...'''
date = "2016-04-07T02:02:00Z"
lastmod = "2016-04-07T04:12:00Z"
weight = 51456
keywords = [ "libpcap", "sip", "dumpcap", "voip", "rtp" ]
aliases = [ "/questions/51456" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap capture filter question](/questions/51456/dumpcap-capture-filter-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51456-score" class="post-score" title="current number of votes">0</div><span id="post-51456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am struggling to create a filter to capture VoIP traffic using Dumpcap. I can capture everything but I cannot apply a capture filter successfully. I need to basically capture the following.</p><p>Port 13060 TCP/UDP</p><p>Port 13061 TCP</p><p>Port 13090 TCP/UDP</p><p>Ports 54000-65000 UDP</p><p>This is the command I have so far.</p><p>dumpcap.exe -i 1 -f "<strong>SomeTextGoesHere</strong>" -a filesize:100000 -w "C:\Users\Administrator\Desktop\Dumpcap\Dumpcap.pcapng" -b files:100</p><p>Its the "<strong>SomeTextGoesHere</strong>" bit I'm struggling with! Is anybody able to help please?</p><p>Regards,</p><p>Jonathan.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '16, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/8ac8aaabcf360cef154c972fb2a2292a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonathanbaird&#39;s gravatar image" /><p><span>jonathanbaird</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonathanbaird has one accepted answer">50%</span></p></div></div><div id="comments-container-51456" class="comments-container"></div><div id="comment-tools-51456" class="comment-tools"></div><div class="clear"></div><div id="comment-51456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51458"></span>

<div id="answer-container-51458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51458-score" class="post-score" title="current number of votes">0</div><span id="post-51458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're looking for a capture (or tcpdump) filter. The reference page is <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">here</a>.</p><p>As that's a bit intense, to get you started you create a filter with expressions and combine them with <em>and</em>, <em>or</em> or <em>not</em>. To include both tcp and udp on port 13060 use <code>"port 13060"</code>. To include tcp on port 13061 use <code>"tcp port 13061"</code>. To combine these so that packets match the first <strong>or</strong> the second expression use <code>"port 13060 or tcp port 13061"</code> To specify a range of ports use <em>portrange</em>, e.g. <code>"udp portrange 54000-65000"</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '16, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51458" class="comments-container"><span id="51461"></span><div id="comment-51461" class="comment"><div id="post-51461-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham I'll give it a go! :)</p></div><div id="comment-51461-info" class="comment-info"><span class="comment-age">(07 Apr '16, 04:12)</span> <span class="comment-user userinfo">jonathanbaird</span></div></div></div><div id="comment-tools-51458" class="comment-tools"></div><div class="clear"></div><div id="comment-51458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

