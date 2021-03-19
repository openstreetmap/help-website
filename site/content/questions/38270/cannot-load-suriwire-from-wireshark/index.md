+++
type = "question"
title = "Cannot load suriwire from wireshark"
description = '''I installed wireshark 1.8.10 on CentOS 6.5. I followed the instructions here to install suriwire on wireshark, both by making the directory ~/wireshark/plugins and copying suriwire.lua and also by making a subdirectory called plugins under /root/.wireshark and copying suriwire.lua there. I also run ...'''
date = "2014-12-01T18:02:00Z"
lastmod = "2014-12-05T07:00:00Z"
weight = 38270
keywords = [ "lua" ]
aliases = [ "/questions/38270" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot load suriwire from wireshark](/questions/38270/cannot-load-suriwire-from-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38270-score" class="post-score" title="current number of votes">0</div><span id="post-38270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed wireshark 1.8.10 on CentOS 6.5. I followed the instructions <a href="https://github.com/regit/suriwire">here</a> to install suriwire on wireshark, both by making the directory ~/wireshark/plugins and copying suriwire.lua and also by making a subdirectory called plugins under /root/.wireshark and copying suriwire.lua there. I also run wireshark both as root and as unprivileged. However, when I pull down the tools menu, there is only</p><pre><code>  Firewall ACL Rules</code></pre><p>and it is disabled.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '14, 18:02</strong></p><img src="https://secure.gravatar.com/avatar/87ec0ce8ac23df0e004db289a8677a34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OtagoHarbour&#39;s gravatar image" /><p><span>OtagoHarbour</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OtagoHarbour has no accepted answers">0%</span></p></div></div><div id="comments-container-38270" class="comments-container"></div><div id="comment-tools-38270" class="comment-tools"></div><div class="clear"></div><div id="comment-38270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38276"></span>

<div id="answer-container-38276" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38276-score" class="post-score" title="current number of votes">1</div><span id="post-38276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="OtagoHarbour has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check the 'About Wireshark' dialog, accessible from the Help menu. It has to state that your Wireshark instance is build with Lua support ("...with Lua 5.1....")</p><p>If that's the case then check if your <code>init.lua</code> file (in the installation or your home directory) has <code>disable_lua</code> set to <code>true</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '14, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-38276" class="comments-container"><span id="38285"></span><div id="comment-38285" class="comment"><div id="post-38285-score" class="comment-score"></div><div class="comment-text"><p>That seems to be the problem. It says that it was built without lua support. I will try rebuilding it with lua support this evening. I will let you know how it works. Thanks very much,</p></div><div id="comment-38285-info" class="comment-info"><span class="comment-age">(02 Dec '14, 18:35)</span> <span class="comment-user userinfo">OtagoHarbour</span></div></div><span id="38287"></span><div id="comment-38287" class="comment"><div id="post-38287-score" class="comment-score"></div><div class="comment-text"><p>I unpacked the tarball for Wireshark 1.12.2 and entered "sudo ./configure --with-lua"/ It failed with the message "configure: error: Qt is not available". I have qt-4.6.2-28.el6_5.i686 installed. Thanks,</p></div><div id="comment-38287-info" class="comment-info"><span class="comment-age">(02 Dec '14, 18:57)</span> <span class="comment-user userinfo">OtagoHarbour</span></div></div><span id="38290"></span><div id="comment-38290" class="comment"><div id="post-38290-score" class="comment-score">1</div><div class="comment-text"><p>As Qt based GUI lacks many features in the 1.12 branch, I highly recommend you to execute ./configure with the --with-gtk2 or --with-gtk3 option. Of course you will need to have the GTK2 or GTK3 development package installed.</p></div><div id="comment-38290-info" class="comment-info"><span class="comment-age">(02 Dec '14, 22:11)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="38364"></span><div id="comment-38364" class="comment"><div id="post-38364-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-38364-info" class="comment-info"><span class="comment-age">(05 Dec '14, 07:00)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-38276" class="comment-tools"></div><div class="clear"></div><div id="comment-38276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

