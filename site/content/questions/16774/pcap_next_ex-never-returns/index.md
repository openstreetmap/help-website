+++
type = "question"
title = "pcap_next_ex never returns"
description = '''This is probably more of a WinPcap question, but I call pcap_next_ex as follows: int iRes = pcap_next_ex(pPcapDev, &amp;amp;pHdr, (const u_char**)&amp;amp;pubFrmBuf); and it never returns.  But sending works: pcap_sendpacket(pPcapDev, pubBuf, (int)ulLen); Has anyone else seen this or know why pcap_next_ex f...'''
date = "2012-12-11T10:43:00Z"
lastmod = "2012-12-11T11:09:00Z"
weight = 16774
keywords = [ "returns", "never", "pcap_next_ex" ]
aliases = [ "/questions/16774" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pcap\_next\_ex never returns](/questions/16774/pcap_next_ex-never-returns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16774-score" class="post-score" title="current number of votes">0</div><span id="post-16774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is probably more of a WinPcap question, but I call pcap_next_ex as follows:</p><p>int iRes = pcap_next_ex(pPcapDev, &amp;pHdr, (const u_char**)&amp;pubFrmBuf);</p><p>and it never returns.</p><p>But sending works:</p><p>pcap_sendpacket(pPcapDev, pubBuf, (int)ulLen);</p><p>Has anyone else seen this or know why pcap_next_ex fails to return an error at least.</p><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-returns" rel="tag" title="see questions tagged &#39;returns&#39;">returns</span> <span class="post-tag tag-link-never" rel="tag" title="see questions tagged &#39;never&#39;">never</span> <span class="post-tag tag-link-pcap_next_ex" rel="tag" title="see questions tagged &#39;pcap_next_ex&#39;">pcap_next_ex</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '12, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p><span>brwiese</span><br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-16774" class="comments-container"></div><div id="comment-tools-16774" class="comment-tools"></div><div class="clear"></div><div id="comment-16774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16775"></span>

<div id="answer-container-16775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16775-score" class="post-score" title="current number of votes">0</div><span id="post-16775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>This is probably more of a WinPcap question</p></blockquote><p>Yes, it is. The best places to ask WinPcap questions would be:</p><ul><li><a href="https://www.winpcap.org/mailman/listinfo/winpcap-users">the winpcap-users mailing list</a>;</li><li><a href="http://www.tcpdump.org/#mailing-lists">the tcpdump-users mailing list</a>, given that WinPcap is based on libpcap and the issue you're having may be a generic issue with *pcap;</li><li><a href="http://stackoverflow.com"></a><a href="http://stackoverflow.com">stackoverflow.com</a>, if you want a Q&amp;A site (tag your question with "winpcap").</li></ul><blockquote><p>I call pcap_next_ex as follows:</p><p>int iRes = pcap_next_ex(pPcapDev, &amp;pHdr, (const u_char**)&amp;pubFrmBuf);</p><p>and it never returns.</p></blockquote><p>What <code>pcap_open()</code> or <code>pcap_open_live()</code> call are you making to get the <code>pPcapDev</code> handle? What arguments are you passing in that call? If you don't specify a timeout (i.e., you pass 0 as the timeout value), then, on many platforms - including, as far as I know, Windows - <code>pcap_next()</code> and <code>pcap_next_ex()</code> will return, and <code>pcap_loop()</code> and <code>pcap_dispatch()</code> will call the callback routine, only when the underlying capture mechanism's packet buffer fills up with packets, and, if the incoming packet rate (or the rate of incoming packets that pass the filter, if you've specified a filter with <code>pcap_setfilter()</code>) is low enough that the buffer takes a long time to fill up, that means that it could take an <em>indefinitely</em> long time for those routines to return or call the callback routine.</p><p>This is why there's a timeout argument - to allow packets to be buffered, so that there isn't a potentially-costly process wakeup for each packet received, but so that the packets will be delivered to your program after a relatively short period of time if the packets aren't arriving fast enough. Tcpdump sets the timeout to 1 second (1000 milliseconds), and dumpcap sets it to 1/4 second (250 milliseconds).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '12, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16775" class="comments-container"></div><div id="comment-tools-16775" class="comment-tools"></div><div class="clear"></div><div id="comment-16775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

