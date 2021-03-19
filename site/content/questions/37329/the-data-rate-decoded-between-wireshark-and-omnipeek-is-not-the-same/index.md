+++
type = "question"
title = "The data rate decoded between wireshark and omnipeek is not the same"
description = '''Hi, I encounter a situation that the data rate decoded between wireshark and omniPeek is not the same. It&#x27;s a 802.11 packet. In omnipeek, it shows the data rate is 65.0Mbps, and it is correct. However in wireshark, it shows the data rate is 3.5Mbps. It is weird. I upload the capture file on google d...'''
date = "2014-10-24T02:17:00Z"
lastmod = "2014-10-27T20:04:00Z"
weight = 37329
keywords = [ "rate", "802.11" ]
aliases = [ "/questions/37329" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The data rate decoded between wireshark and omnipeek is not the same](/questions/37329/the-data-rate-decoded-between-wireshark-and-omnipeek-is-not-the-same)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37329-score" class="post-score" title="current number of votes">0</div><span id="post-37329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I encounter a situation that the data rate decoded between wireshark and omniPeek is not the same. It's a 802.11 packet. In omnipeek, it shows the data rate is 65.0Mbps, and it is correct. However in wireshark, it shows the data rate is 3.5Mbps. It is weird. I upload the capture file on google drive (It's better opened with crome): <a href="https://drive.google.com/file/d/0B4Zm6QEQbQ50eGRqNGJibzBIVGc/view?usp=sharing">https://drive.google.com/file/d/0B4Zm6QEQbQ50eGRqNGJibzBIVGc/view?usp=sharing</a></p><p>Could anyone answer this question, thanks! <img src="https://osqa-ask.wireshark.org/upfiles/Image_4.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Image_3_iwiczYW.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rate" rel="tag" title="see questions tagged &#39;rate&#39;">rate</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '14, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/ef060f8ee1d14f85debcd929c14ec608?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s0204995&#39;s gravatar image" /><p><span>s0204995</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s0204995 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-37329" class="comments-container"></div><div id="comment-tools-37329" class="comment-tools"></div><div class="clear"></div><div id="comment-37329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37339"></span>

<div id="answer-container-37339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37339-score" class="post-score" title="current number of votes">0</div><span id="post-37339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's code to read the "tagged" file format for {Ether,Airo,Omni}Peek is incomplete (it's not publicly documented anywhere for use by people who <em>don't</em> have OmniPeek, so it had to be reverse-engineered), so it may get some fields wrong.</p><p>Could you please file a bug on this at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach the capture <em>AND</em> an image of what <em>OmniPeek</em> shows for the packet - giving a <em>full</em> list of all the "meta-data" fields, including the data rate and any <em>other</em> fields, such as an MCS index, signal and noise values for multiple antennas, flags for packets, etc., as that might allow us not only to fix this issue but to get more such information from the packet?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '14, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Oct '14, 15:57</strong> </span></p></div></div><div id="comments-container-37339" class="comments-container"><span id="37381"></span><div id="comment-37381" class="comment"><div id="post-37381-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your suggestion. I have submit a bug on Bugzilla. It's link: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10637">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10637</a></p></div><div id="comment-37381-info" class="comment-info"><span class="comment-age">(27 Oct '14, 18:58)</span> <span class="comment-user userinfo">s0204995</span></div></div><span id="37382"></span><div id="comment-37382" class="comment"><div id="post-37382-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Could you please attach to that bug a screenshot of the dissection of all the metadata details (data rate, channel, signal strength(s), noise level(s), etc.) from OmniPeek, so we can see whether it's showing, for example, and MCS index from which we could calculate the data rate?</p></div><div id="comment-37382-info" class="comment-info"><span class="comment-age">(27 Oct '14, 20:04)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-37339" class="comment-tools"></div><div class="clear"></div><div id="comment-37339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

