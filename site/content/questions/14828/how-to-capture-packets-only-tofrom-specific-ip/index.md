+++
type = "question"
title = "How to capture packets only to/from specific ip."
description = '''Hello, I&#x27;m a naive user of Wireshark tool. Normally when we start capturing packets over specific interface, Wireshark will captures all packets over the interface and then we have to apply ip filters to view the data to/from specific ip.  Is there any way where we can capture packets to/from only s...'''
date = "2012-10-09T12:11:00Z"
lastmod = "2012-10-09T15:32:00Z"
weight = 14828
keywords = [ "wireshark" ]
aliases = [ "/questions/14828" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture packets only to/from specific ip.](/questions/14828/how-to-capture-packets-only-tofrom-specific-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14828-score" class="post-score" title="current number of votes">0</div><span id="post-14828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm a naive user of Wireshark tool. Normally when we start capturing packets over specific interface, Wireshark will captures all packets over the interface and then we have to apply ip filters to view the data to/from specific ip.</p><p>Is there any way where we can <strong>capture packets to/from only specific ip</strong> and save it to file rather than capturing all the packets and applying filters.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/301e8556a334719019209711cdbfd439?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dvsrk&#39;s gravatar image" /><p><span>dvsrk</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dvsrk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Oct '12, 12:26</strong> </span></p></div></div><div id="comments-container-14828" class="comments-container"></div><div id="comment-tools-14828" class="comment-tools"></div><div class="clear"></div><div id="comment-14828-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14829"></span>

<div id="answer-container-14829" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14829-score" class="post-score" title="current number of votes">2</div><span id="post-14829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, just use capture filters, for example "host 192.168.1.1" to capture everything to and from IP 192.168.1.1. You can set them in the capture dialog (pre 1.8) or for each interface starting with 1.8 (by double clicking the interface line in the capture dialog).</p><p>For more filters see <a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14829" class="comments-container"><span id="14830"></span><div id="comment-14830" class="comment"><div id="post-14830-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper for the quick response.</p><p>I added the filter and now it is capturing only data for specific ips. do we have any options to auto save that data to specific location.</p></div><div id="comment-14830-info" class="comment-info"><span class="comment-age">(09 Oct '12, 12:48)</span> <span class="comment-user userinfo">dvsrk</span></div></div><span id="14833"></span><div id="comment-14833" class="comment"><div id="post-14833-score" class="comment-score"></div><div class="comment-text"><p>not a problem, open the capture options and enter a file name in the "Capture File(s)" panel. You should probably capture to multiple files (for example to a new one each 64MB) because otherwise Wireshark might crash after a while if you capture a lot of frames.</p><p>You might also want to check out dumpcap, which is installed together with Wireshark and which actually does the capture for Wireshark whenever you start a capture. dumpcap -h tells you all parameters you might need to know.</p></div><div id="comment-14833-info" class="comment-info"><span class="comment-age">(09 Oct '12, 13:34)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="14837"></span><div id="comment-14837" class="comment"><div id="post-14837-score" class="comment-score"></div><div class="comment-text"><p>These are probably derived from environment variables. These are educated guesses on things as remote display sessions, etc. If you're running everything local you can erase them.</p></div><div id="comment-14837-info" class="comment-info"><span class="comment-age">(09 Oct '12, 13:57)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="14838"></span><div id="comment-14838" class="comment"><div id="post-14838-score" class="comment-score"></div><div class="comment-text"><p>I'm able to save the data to a file. Thank you so much.</p><p>I have one more ask for you. Do we have any specific display filter where i can find the response time from the host we are capturing the packets. Is there any way we can capture the response time from specific ip address.</p><p>From the data I'm capturing i can see TCP &amp; TLSV1 protocols.</p></div><div id="comment-14838-info" class="comment-info"><span class="comment-age">(09 Oct '12, 13:58)</span> <span class="comment-user userinfo">dvsrk</span></div></div><span id="14844"></span><div id="comment-14844" class="comment"><div id="post-14844-score" class="comment-score"></div><div class="comment-text"><p>I think that's not really a filter issue, it is more of a timing column issue, even though you can filter on things like "frame.time_delta &gt; 1.0", but that rarely helps. Best is usually to isolate a tcp flow by conversation filter (popup menu on a packet of the conversation) and then set the time column to display delta time from previous frame.</p></div><div id="comment-14844-info" class="comment-info"><span class="comment-age">(09 Oct '12, 15:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-14829" class="comment-tools"></div><div class="clear"></div><div id="comment-14829-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

