+++
type = "question"
title = "Why is my SSH key rejected by SSH Remote Capture?"
description = '''When I try to set my SSH private key for SSH Remote Capture, the box stays red, and the Start button stays grayed out regardless of what file I give it. I also tried setting extcap.ssh.sshkey in .config/wireshark/preferences but when I open the GUI and start the capture, it sits on the main screen f...'''
date = "2016-10-07T13:38:00Z"
lastmod = "2017-03-02T12:01:00Z"
weight = 56228
keywords = [ "ssh", "linux" ]
aliases = [ "/questions/56228" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why is my SSH key rejected by SSH Remote Capture?](/questions/56228/why-is-my-ssh-key-rejected-by-ssh-remote-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56228-score" class="post-score" title="current number of votes">1</div><span id="post-56228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I try to set my SSH private key for SSH Remote Capture, the box stays red, and the Start button stays grayed out regardless of what file I give it. I also tried setting extcap.ssh.sshkey in .config/wireshark/preferences but when I open the GUI and start the capture, it sits on the main screen forever, and collects no packets.</p><p>How can I use my SSH private key with SSH Remote Capture?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '16, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/ffed6e56b0fb44ac76638b7bc7917a0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thurstylark&#39;s gravatar image" /><p><span>thurstylark</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thurstylark has no accepted answers">0%</span></p></div></div><div id="comments-container-56228" class="comments-container"><span id="59803"></span><div id="comment-59803" class="comment"><div id="post-59803-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure how to get this to work either. And unfortunately, clicking on the "Help" only brings you to this non-existent page: <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChExtcapOptions.html">https://www.wireshark.org/docs/wsug_html_chunked/ChExtcapOptions.html</a>. Hopefully someone more knowledgeable in this area than I am can chime in with some advice.</p></div><div id="comment-59803-info" class="comment-info"><span class="comment-age">(02 Mar '17, 06:56)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-56228" class="comment-tools"></div><div class="clear"></div><div id="comment-56228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59811"></span>

<div id="answer-container-59811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59811-score" class="post-score" title="current number of votes">0</div><span id="post-59811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps you need to update your version of Wireshark for this to work. If you're already using the latest stable release version, try updating to the most recent available <a href="https://www.wireshark.org/download/automated/">automated version</a>.</p><p>See also <a href="https://ask.wireshark.org/questions/58696/ssh-remote-capture-tcpdump">this related question</a> where grahamb suggests doing this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '17, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59811" class="comments-container"></div><div id="comment-tools-59811" class="comment-tools"></div><div class="clear"></div><div id="comment-59811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

