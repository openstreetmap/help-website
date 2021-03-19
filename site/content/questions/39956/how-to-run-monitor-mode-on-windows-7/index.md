+++
type = "question"
title = "How to run monitor mode on windows 7?"
description = '''taking a wifi class and was told to use wireshark and capture data in 4 modes such as avs, radio tap and 802.11 and compare them but when I go to &quot;edit interface settings and then link-layer header type only ethernet and DOCSIS comes up. does windows not support monitor mode or is it possibly my net...'''
date = "2015-02-19T10:33:00Z"
lastmod = "2015-02-21T00:56:00Z"
weight = 39956
keywords = [ "capture", "wireshark" ]
aliases = [ "/questions/39956" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to run monitor mode on windows 7?](/questions/39956/how-to-run-monitor-mode-on-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39956-score" class="post-score" title="current number of votes">0</div><span id="post-39956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>taking a wifi class and was told to use wireshark and capture data in 4 modes such as avs, radio tap and 802.11 and compare them but when I go to "edit interface settings and then link-layer header type only ethernet and DOCSIS comes up. does windows not support monitor mode or is it possibly my network card?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '15, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/7ef5bc2877530135dc43ef1ce2f39f3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nickb&#39;s gravatar image" /><p><span>Nickb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nickb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Feb '15, 10:38</strong> </span></p></div></div><div id="comments-container-39956" class="comments-container"></div><div id="comment-tools-39956" class="comment-tools"></div><div class="clear"></div><div id="comment-39956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39964"></span>

<div id="answer-container-39964" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39964-score" class="post-score" title="current number of votes">2</div><span id="post-39964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ask your teacher what operating system he or she expects students to be using on their computers, because it sure ain't Windows - on Windows, WinPcap (which is what Wireshark uses to capture traffic) only supports those types of capture with an AirPcap adapter (if he or she expects you to use an AirPcap card, ask them to buy it for you!).</p><p>They may be expecting you to use a Linux box or a Mac (if they expect AVS <em>and</em> radiotap <em>and</em> 802.11-without-radio-data, they're probably expecting you to use a Mac); if so, ask them to buy <em>that</em> for you.</p><p>(You might want to learn about Wi-Fi somewhere else, if your teacher is so clueless as to assume nobody's running Windows or that everybody who is has an AirPcap adapter!)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '15, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-39964" class="comments-container"><span id="39986"></span><div id="comment-39986" class="comment"><div id="post-39986-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help! He ended up emailing everyone today about how he forgot to mention we couldn't do this with windows. He said same reason you gave me. I really aperciate the help!</p></div><div id="comment-39986-info" class="comment-info"><span class="comment-age">(20 Feb '15, 10:58)</span> <span class="comment-user userinfo">Nickb</span></div></div><span id="39998"></span><div id="comment-39998" class="comment"><div id="post-39998-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-39998-info" class="comment-info"><span class="comment-age">(21 Feb '15, 00:56)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-39964" class="comment-tools"></div><div class="clear"></div><div id="comment-39964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

