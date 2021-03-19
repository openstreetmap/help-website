+++
type = "question"
title = "How to start wireshark in command line to directly capture packets on a given interface?"
description = '''Launching  wireshark -i wlan0  in Linux lead to the main wireshark menu and not to the capture directly. How to directly capture on wlan0 without having to choose the device from the menu.'''
date = "2016-10-31T08:55:00Z"
lastmod = "2016-10-31T10:26:00Z"
weight = 56870
keywords = [ "terminal", "capture", "linux", "command-line", "wireshark" ]
aliases = [ "/questions/56870" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to start wireshark in command line to directly capture packets on a given interface?](/questions/56870/how-to-start-wireshark-in-command-line-to-directly-capture-packets-on-a-given-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56870-score" class="post-score" title="current number of votes">0</div><span id="post-56870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Launching</p><pre><code>wireshark -i wlan0</code></pre><p>in Linux lead to the main wireshark menu and not to the capture directly.</p><p><strong>How to directly capture on wlan0 without having to choose the device from the menu.</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-terminal" rel="tag" title="see questions tagged &#39;terminal&#39;">terminal</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '16, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/1d0a5c898c23c1ae1a7b009804920031?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user31415&#39;s gravatar image" /><p><span>user31415</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user31415 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Oct '16, 09:25</strong> </span></p></div></div><div id="comments-container-56870" class="comments-container"></div><div id="comment-tools-56870" class="comment-tools"></div><div class="clear"></div><div id="comment-56870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56872"></span>

<div id="answer-container-56872" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56872-score" class="post-score" title="current number of votes">2</div><span id="post-56872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="user31415 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As the <a href="https://www.wireshark.org/docs/man-pages/wireshark.html">manual page</a> says, add the <code>-k</code> option to your command line to start capture immediately.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '16, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Oct '16, 10:27</strong> </span></p></div></div><div id="comments-container-56872" class="comments-container"></div><div id="comment-tools-56872" class="comment-tools"></div><div class="clear"></div><div id="comment-56872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

