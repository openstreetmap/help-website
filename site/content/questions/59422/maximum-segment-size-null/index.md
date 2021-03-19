+++
type = "question"
title = "Maximum Segment Size - NULL"
description = '''I am doing a TCP evaluation and i am confused with the value of MSS (maximum segment size) i am getting on Wireshark. When i capture the traffic using Wireshark, it only shows the value of MSS as 1460 in few packets but shows NULL for many of the packets. Why do you think is that I am getting a NULL...'''
date = "2017-02-14T13:35:00Z"
lastmod = "2017-02-15T16:52:00Z"
weight = 59422
keywords = [ "mss", "ask.wireshark.org", "wireshark" ]
aliases = [ "/questions/59422" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Maximum Segment Size - NULL](/questions/59422/maximum-segment-size-null)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59422-score" class="post-score" title="current number of votes">0</div><span id="post-59422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am doing a TCP evaluation and i am confused with the value of MSS (maximum segment size) i am getting on Wireshark. When i capture the traffic using Wireshark, it only shows the value of MSS as 1460 in few packets but shows NULL for many of the packets. Why do you think is that I am getting a NULL value for MSS? How can fix this problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mss" rel="tag" title="see questions tagged &#39;mss&#39;">mss</span> <span class="post-tag tag-link-ask.wireshark.org" rel="tag" title="see questions tagged &#39;ask.wireshark.org&#39;">ask.wireshark.org</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '17, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p><span>armodes</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '17, 06:57</strong> </span></p></div></div><div id="comments-container-59422" class="comments-container"><span id="59423"></span><div id="comment-59423" class="comment"><div id="post-59423-score" class="comment-score">1</div><div class="comment-text"><p>The link takes one to a page with a prompt to "Upload and share your images" and buttons to login or to create an account, but there is nothing to download.</p><p>Also, if the link is to a screenshot, it would be much better to post an actual trace file, anonymized if necessary.</p></div><div id="comment-59423-info" class="comment-info"><span class="comment-age">(14 Feb '17, 13:39)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="59424"></span><div id="comment-59424" class="comment"><div id="post-59424-score" class="comment-score"></div><div class="comment-text"><p>I have fixed the URL now but how can i post the whole actual trace file?</p></div><div id="comment-59424-info" class="comment-info"><span class="comment-age">(14 Feb '17, 13:44)</span> <span class="comment-user userinfo">armodes</span></div></div><span id="59426"></span><div id="comment-59426" class="comment"><div id="post-59426-score" class="comment-score">1</div><div class="comment-text"><p>You can share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, Dropbox etc.</p></div><div id="comment-59426-info" class="comment-info"><span class="comment-age">(14 Feb '17, 15:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-59422" class="comment-tools"></div><div class="clear"></div><div id="comment-59422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59430"></span>

<div id="answer-container-59430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59430-score" class="post-score" title="current number of votes">3</div><span id="post-59430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maximum Segment Size is a TCP option where a TCP peer announces to the other TCP peer the maximum size TCP data segment that it can receive. The MSS option is found only in the SYN and SYN/ACK packets of the TCP connection establishment three-way handshake. In your trace, MSS is present only in packets 1, 2, 16, 17, 191,897, and 191,898, and in every one of those packets, the MSS is 1460.</p><p>Where do you think you are seeing an MSS NULL value? If you're talking about packets with "Len=0" in the Info column, that is not the <em>maximum</em> segment size, that's the size of the actual data segment in those packets. TCP packets with no data are mostly acknowledgements.</p><p>Your image link still does not work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '17, 18:44</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-59430" class="comments-container"></div><div id="comment-tools-59430" class="comment-tools"></div><div class="clear"></div><div id="comment-59430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59450"></span>

<div id="answer-container-59450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59450-score" class="post-score" title="current number of votes">0</div><span id="post-59450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know what software generated that table, but it's showing one row for every packet, and, for every packet that doesn't have a TCP Maximum Segment Size option - i.e., for most packets in a TCP connection - it's showing NULL rather than just an empty column.</p><p>There's nothing to fix - most of those packets don't <em>have</em> the MSS option, because the MSS is established when the connection is set up and not changed after that - so it's not <em>supposed</em> to show an MSS option because there isn't one to show.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '17, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-59450" class="comments-container"></div><div id="comment-tools-59450" class="comment-tools"></div><div class="clear"></div><div id="comment-59450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

