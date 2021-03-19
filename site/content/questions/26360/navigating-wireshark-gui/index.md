+++
type = "question"
title = "Navigating Wireshark GUI"
description = '''I find really a pain when browsing the &quot;Packet List&quot; pane the indication of the current selected packet. It is not really contrasting and it completely disappears when I click on the &quot;Packet detail&quot; pane. This makes virtually impossible going back to the &quot;Packet List&quot; pane over the same packet I was...'''
date = "2013-10-24T05:38:00Z"
lastmod = "2013-10-28T14:41:00Z"
weight = 26360
keywords = [ "gui", "navigation" ]
aliases = [ "/questions/26360" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Navigating Wireshark GUI](/questions/26360/navigating-wireshark-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26360-score" class="post-score" title="current number of votes">0</div><span id="post-26360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I find really a pain when browsing the "Packet List" pane the indication of the current selected packet. It is not really contrasting and it completely disappears when I click on the "Packet detail" pane. This makes virtually impossible going back to the "Packet List" pane over the same packet I was just analyzing in detail.</p><p>Is there a way to solve this? what am I doing wrong? Having an "*" indicating the currently selected "Packet List" row would be awesome, I understand colors are required for packet analysis but not having a clear indication of the selected packet is very frustrating.... Please let me know</p><p>Thanks for an awesome product.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '13, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/780da1b12d54141a048ff61b098ff162?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patpat&#39;s gravatar image" /><p><span>patpat</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patpat has no accepted answers">0%</span></p></div></div><div id="comments-container-26360" class="comments-container"><span id="26410"></span><div id="comment-26410" class="comment"><div id="post-26410-score" class="comment-score"></div><div class="comment-text"><p>I cannot believe I'm the only one dealing with this... :-(</p></div><div id="comment-26410-info" class="comment-info"><span class="comment-age">(25 Oct '13, 11:18)</span> <span class="comment-user userinfo">patpat</span></div></div></div><div id="comment-tools-26360" class="comment-tools"></div><div class="clear"></div><div id="comment-26360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26485"></span>

<div id="answer-container-26485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26485-score" class="post-score" title="current number of votes">1</div><span id="post-26485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to solve this?</p></blockquote><p>If you are in the <code>Packet Details</code> pane, press <strong>CRTL-SHIFT-TAB</strong> and Wireshark will change the focus to the <code>Packet List</code> pane. By doing so, it will 'jump' into that pane and highlight the previously selected frame.</p><p>That's how I 'solve' this problem for me, until there is a better solution :-)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26485" class="comments-container"><span id="26491"></span><div id="comment-26491" class="comment"><div id="post-26491-score" class="comment-score"></div><div class="comment-text"><p>far from good but better than nothing; I'll take it; thanks a lot.</p></div><div id="comment-26491-info" class="comment-info"><span class="comment-age">(28 Oct '13, 14:41)</span> <span class="comment-user userinfo">patpat</span></div></div></div><div id="comment-tools-26485" class="comment-tools"></div><div class="clear"></div><div id="comment-26485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26411"></span>

<div id="answer-container-26411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26411-score" class="post-score" title="current number of votes">0</div><span id="post-26411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, you're not the only one dealing with this, but that's just the way Wireshark works right now. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9285">Bug 9285</a> at the Wireshark Bugzilla for one enhancement request suggesting an alternate way to indicate the selected packet. Feel free to add a comment to that request or to add a different enhancement request if you think it should be done differently.</p><p>In the meantime, as far as finding your way back to the selected packet in the Packet List pane, simply pay attention to the Frame number, which is shown on the first line in the Packet Details pane.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Oct '13, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-26411" class="comments-container"><span id="26412"></span><div id="comment-26412" class="comment"><div id="post-26412-score" class="comment-score"></div><div class="comment-text"><p>See also <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3944">bug 3944</a>?</p><p>Note that the only real question that matters today is, <em>"How does it look with Qt?"</em></p></div><div id="comment-26412-info" class="comment-info"><span class="comment-age">(25 Oct '13, 12:37)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="26419"></span><div id="comment-26419" class="comment"><div id="post-26419-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer; looking at the Frame number is not really practical when the number gets big. I think that making the selected line text bold (or just the Frame # field) on a QT ListView could be easily done and solves the problem. What do you guys think?</p></div><div id="comment-26419-info" class="comment-info"><span class="comment-age">(26 Oct '13, 03:26)</span> <span class="comment-user userinfo">patpat</span></div></div><span id="26420"></span><div id="comment-26420" class="comment"><div id="post-26420-score" class="comment-score"></div><div class="comment-text"><p>I just read the Bug 9285 provided link and says "Bold" as I've said before; sorry. I agree with that idea then.</p></div><div id="comment-26420-info" class="comment-info"><span class="comment-age">(26 Oct '13, 03:27)</span> <span class="comment-user userinfo">patpat</span></div></div></div><div id="comment-tools-26411" class="comment-tools"></div><div class="clear"></div><div id="comment-26411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

