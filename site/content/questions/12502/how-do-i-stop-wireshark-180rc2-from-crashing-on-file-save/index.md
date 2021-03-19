+++
type = "question"
title = "How do I stop Wireshark 1.8.0rc2 from crashing on file save?"
description = '''Whenever I try to save a packet to disk or even export a packet, Wireshark crashes immediately. Here&#x27;s the log: http://pastebin.com/Cxz0PBBL What&#x27;s the workaround for this problem?'''
date = "2012-07-07T18:54:00Z"
lastmod = "2012-07-08T13:31:00Z"
weight = 12502
keywords = [ "crash" ]
aliases = [ "/questions/12502" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I stop Wireshark 1.8.0rc2 from crashing on file save?](/questions/12502/how-do-i-stop-wireshark-180rc2-from-crashing-on-file-save)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12502-score" class="post-score" title="current number of votes">0</div><span id="post-12502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Whenever I try to save a packet to disk or even export a packet, Wireshark crashes immediately. Here's the log: <a href="http://pastebin.com/Cxz0PBBL">http://pastebin.com/Cxz0PBBL</a></p><p>What's the workaround for this problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '12, 18:54</strong></p><img src="https://secure.gravatar.com/avatar/a72d9631e59943be376df1db6867f744?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ostar2&#39;s gravatar image" /><p><span>ostar2</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ostar2 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '12, 13:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-12502" class="comments-container"></div><div id="comment-tools-12502" class="comment-tools"></div><div class="clear"></div><div id="comment-12502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12512"></span>

<div id="answer-container-12512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12512-score" class="post-score" title="current number of votes">0</div><span id="post-12512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is any <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> installed on that machine? In general any kind of security software, like AV, IDS, VPN, Endpoint Security and the like? If so, please disable that software and try again. If it works without that software, please read the manual of the interfering software how to add an exception for Wireshark.</p><p>BTW: Do you have enough permissions to write to that directory?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '12, 11:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12512" class="comments-container"></div><div id="comment-tools-12512" class="comment-tools"></div><div class="clear"></div><div id="comment-12512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12515"></span>

<div id="answer-container-12515" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12515-score" class="post-score" title="current number of votes">0</div><span id="post-12515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the log:</p><pre><code>PRODUCT_VERSION=&quot;1.8.0rc2&quot;</code></pre><p>Are you running 1.8.0:</p><p><a href="http://wiresharkdownloads.riverbed.com/wireshark/win32/Wireshark-win64-1.8.0.exe">http://wiresharkdownloads.riverbed.com/wireshark/win64/Wireshark-win64-1.8.0.exe</a> <a href="http://wiresharkdownloads.riverbed.com/wireshark/win32/Wireshark-win32-1.8.0.exe">http://wiresharkdownloads.riverbed.com/wireshark/win32/Wireshark-win32-1.8.0.exe</a></p><p>or are you running the earlier 1.8.0rc2? If you're running 1.8.0rc2 rather than the official 1.8.0 release, you might be running into <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7382">bug 7382</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '12, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12515" class="comments-container"></div><div id="comment-tools-12515" class="comment-tools"></div><div class="clear"></div><div id="comment-12515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

