+++
type = "question"
title = "Maximum supported bitrate(UDP/RTP)"
description = '''Hello, What is maximum supported bitrate(UDP/RTP) that wireshark can analyse?'''
date = "2015-07-01T06:27:00Z"
lastmod = "2015-07-02T07:08:00Z"
weight = 43783
keywords = [ "maximum_bitrate" ]
aliases = [ "/questions/43783" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maximum supported bitrate(UDP/RTP)](/questions/43783/maximum-supported-bitrateudprtp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43783-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43783-score" class="post-score" title="current number of votes">0</div><span id="post-43783-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, What is maximum supported bitrate(UDP/RTP) that wireshark can analyse?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-maximum_bitrate" rel="tag" title="see questions tagged &#39;maximum_bitrate&#39;">maximum_bitrate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '15, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/2bddb2f0490a0a3bda165670ae059d5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mor&#39;s gravatar image" /><p><span>Mor</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jul '15, 06:29</strong> </span></p></div></div><div id="comments-container-43783" class="comments-container"></div><div id="comment-tools-43783" class="comment-tools"></div><div class="clear"></div><div id="comment-43783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43810"></span>

<div id="answer-container-43810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43810-score" class="post-score" title="current number of votes">0</div><span id="post-43810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Infinite. It's software after all. But then you have to provide the platform to run it on, that's where the performance is to be made.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '15, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-43810" class="comments-container"><span id="43814"></span><div id="comment-43814" class="comment"><div id="post-43814-score" class="comment-score"></div><div class="comment-text"><p>My question was related to winpcap library used by wireshark. if 10Gig network card is used, how much bitrate winpcap lib can handle? I observed wireshark hangs and crashe at bitrate greater than 600Mbps</p></div><div id="comment-43814-info" class="comment-info"><span class="comment-age">(02 Jul '15, 06:37)</span> <span class="comment-user userinfo">Mor</span></div></div><span id="43816"></span><div id="comment-43816" class="comment"><div id="post-43816-score" class="comment-score">1</div><div class="comment-text"><p>Depends on many factors, have a look at this answer made by Syn-bit <a href="https://ask.wireshark.org/questions/41844/duplicated-sequence-number?page=1&amp;focusedAnswerId=41877#41877">https://ask.wireshark.org/questions/41844/duplicated-sequence-number?page=1&amp;focusedAnswerId=41877#41877</a></p><p>To capture 10G traffic you must be able to store the data. (&gt; 2GByte/s). There are reasons why the comercial capture solution have their price.</p></div><div id="comment-43816-info" class="comment-info"><span class="comment-age">(02 Jul '15, 07:02)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="43817"></span><div id="comment-43817" class="comment"><div id="post-43817-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>wireshark hangs and crashe at bitrate greater than 600Mbps</p></blockquote><p>At that bitrate using the GUI version is not realy useful, I hope you had "Update packets in real time" turned off at least. Dumpcap or tshark is much more apropriate to use in that case. That said on comodity HW at that rate my unsientific tests start to show severe packet drops, with filters it might be possible to reach higer rates e.g the rate of packets passing the filter is less than 600Mbps.( Tested on Ubuntu, not Windows).</p></div><div id="comment-43817-info" class="comment-info"><span class="comment-age">(02 Jul '15, 07:08)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-43810" class="comment-tools"></div><div class="clear"></div><div id="comment-43810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

