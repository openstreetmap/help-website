+++
type = "question"
title = "How to set config to cut off  captured packet length is larger than frame.cap_len"
description = '''while we captured the packet, we want wireshark cut off the packet when the packet len is larger than frame.cap_len, is there any config in wireshark ui or commands parameter?'''
date = "2016-11-22T01:25:00Z"
lastmod = "2016-11-22T04:43:00Z"
weight = 57540
keywords = [ "frame.cap_len", "cut", "off" ]
aliases = [ "/questions/57540" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to set config to cut off captured packet length is larger than frame.cap\_len](/questions/57540/how-to-set-config-to-cut-off-captured-packet-length-is-larger-than-framecap_len)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57540-score" class="post-score" title="current number of votes">0</div><span id="post-57540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>while we captured the packet, we want wireshark cut off the packet when the packet len is larger than frame.cap_len, is there any config in wireshark ui or commands parameter?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-frame.cap_len" rel="tag" title="see questions tagged &#39;frame.cap_len&#39;">frame.cap_len</span> <span class="post-tag tag-link-cut" rel="tag" title="see questions tagged &#39;cut&#39;">cut</span> <span class="post-tag tag-link-off" rel="tag" title="see questions tagged &#39;off&#39;">off</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '16, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/853d7093103a60a3b0083b42b705b99e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neil_hao&#39;s gravatar image" /><p><span>neil_hao</span><br />
<span class="score" title="26 reputation points">26</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neil_hao has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '16, 01:26</strong> </span></p></div></div><div id="comments-container-57540" class="comments-container"></div><div id="comment-tools-57540" class="comment-tools"></div><div class="clear"></div><div id="comment-57540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57547"></span>

<div id="answer-container-57547" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57547-score" class="post-score" title="current number of votes">1</div><span id="post-57547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="neil_hao has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go <code>Capture -&gt; Options</code> (or click the target symbol directly) to open the list of capture interfaces. At the row representing the interface on which you are going to capture, double-click the word <code>default</code> in column <code>Snaplen (B)</code>, change the 65535 value to 128, and press Enter. From now on, capture on this interface will be limited to 128 bytes per captured frame.</p><p>This instruction applies to Qt version of Wireshark. For GTK+ (legacy) Wireshark, the exact layout may differ, but the functionality is available too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '16, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '16, 04:29</strong> </span></p></div></div><div id="comments-container-57547" class="comments-container"><span id="57549"></span><div id="comment-57549" class="comment"><div id="post-57549-score" class="comment-score"></div><div class="comment-text"><p>And if <span>@Jaap</span> has understood you better than me - Wireshark does not allow to truncate already captured packets when saving the capture to a file. The truncation must be done already while capturing. To reduce packet length in an existing capture file, a command-line command <code>editcap -C 128:65535 infile outfile</code> <strong>may</strong> be the way to do that.</p></div><div id="comment-57549-info" class="comment-info"><span class="comment-age">(22 Nov '16, 04:43)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-57547" class="comment-tools"></div><div class="clear"></div><div id="comment-57547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57541"></span>

<div id="answer-container-57541" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57541-score" class="post-score" title="current number of votes">1</div><span id="post-57541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By definition the packet is 'cut short' to the capture length, as this is the amount of octets captured for that frame.</p><p>If you seek to have the 'reported length', ie. length incurred from a packet header field, changed then that is not possible. Wireshark shows you the frame data as it is, without modification, and is capable of handling 'cut short' packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '16, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57541" class="comments-container"><span id="57543"></span><div id="comment-57543" class="comment"><div id="post-57543-score" class="comment-score"></div><div class="comment-text"><p>we do not want modify ie in packet header field, but we want cut short the captured data packet len while we capture some pcap file . such as when the frame.cap_len is 128, we only want wireshark save the packets as 128 bytes. but in some sense. wireshark may save packets larger than 128 bytes by default configration.</p></div><div id="comment-57543-info" class="comment-info"><span class="comment-age">(22 Nov '16, 03:51)</span> <span class="comment-user userinfo">neil_hao</span></div></div><span id="57548"></span><div id="comment-57548" class="comment"><div id="post-57548-score" class="comment-score">1</div><div class="comment-text"><p>You've got things the wrong way around. frame.cap_len is the <em>result</em> of a capture action, not the cause of it.</p><p>If you want to limit the amount of octets captured by Wireshark then go to menu Capture | Options..., and in the dialog set the value in the column 'snaplen' of your capture interface to the value you desire. 'Default' represents the value of 65535.</p></div><div id="comment-57548-info" class="comment-info"><span class="comment-age">(22 Nov '16, 04:31)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-57541" class="comment-tools"></div><div class="clear"></div><div id="comment-57541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

