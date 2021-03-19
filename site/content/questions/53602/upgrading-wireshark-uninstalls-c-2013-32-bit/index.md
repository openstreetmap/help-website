+++
type = "question"
title = "Upgrading Wireshark Uninstalls C++ 2013 32-Bit"
description = '''Hello, We have found a bug within the upgrade process of Wireshark to the latest version. If you open an old version of Wireshark and run the installer for the upgrade it will ask you if you wish to uninstall the previous version of Wireshark. It appears that if you select yes it will uninstall this...'''
date = "2016-06-22T02:00:00Z"
lastmod = "2016-06-22T04:13:00Z"
weight = 53602
keywords = [ "upgrade", "bug", "c++" ]
aliases = [ "/questions/53602" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Upgrading Wireshark Uninstalls C++ 2013 32-Bit](/questions/53602/upgrading-wireshark-uninstalls-c-2013-32-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53602-score" class="post-score" title="current number of votes">0</div><span id="post-53602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>We have found a bug within the upgrade process of Wireshark to the latest version.</p><p>If you open an old version of Wireshark and run the installer for the upgrade it will ask you if you wish to uninstall the previous version of Wireshark. It appears that if you select yes it will uninstall this and also uninstall C++ 2013 32-Bit Redistributables without warning.</p><p>This may not cause issues for most people but when you have software which relies on this its definately not a good thing!</p><p>Just to note the C++ 2013 32-Bit Redistributables were installed seperately prior to the original installation of Wireshark.</p><p>Thanks</p><p>John</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-upgrade" rel="tag" title="see questions tagged &#39;upgrade&#39;">upgrade</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '16, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/536df87338625126497d591dcc38d06e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Freebo&#39;s gravatar image" /><p><span>Freebo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Freebo has no accepted answers">0%</span></p></div></div><div id="comments-container-53602" class="comments-container"></div><div id="comment-tools-53602" class="comment-tools"></div><div class="clear"></div><div id="comment-53602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53604"></span>

<div id="answer-container-53604" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53604-score" class="post-score" title="current number of votes">0</div><span id="post-53604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark uninstaller is not removing MSVC 2013 redistributable. But when you install Wireshark (so after uninstallation of the previous version), it executes the MSVC 2013 redistributable installer with the following flags: "/quiet /norestart".</p><p>This appears to create issues for some users. So we changed to "/install /quiet /norestart" in our development builds (it is already part of our Wireshark 2.1.0 development build found on the main website. We need to add those flags to the Wireshark 2.0.x installers (I will do it right now).</p><p>[Edit] This is now merged and will be part of the next Wireshark 2.0.5 stable release. Hopefully the MSVC redistributable will behave more sanely now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '16, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jun '16, 06:25</strong> </span></p></div></div><div id="comments-container-53604" class="comments-container"></div><div id="comment-tools-53604" class="comment-tools"></div><div class="clear"></div><div id="comment-53604-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

