+++
type = "question"
title = "Export packets saves more packets than displayed."
description = '''Hello community! I filtered the packets with following command: &quot;http.request or http.response&quot;. I can only see 2 packets. I click on &quot;Export Specified Packets...&quot; and click on &quot;Displayed&quot; instead of &quot;Captured&quot;.  Funny thing: over 1000 packets will be saved. On the bottom of wireshark stands &quot;Packet...'''
date = "2016-06-17T12:29:00Z"
lastmod = "2016-06-18T11:50:00Z"
weight = 53541
keywords = [ "export", "packets", "bug", "displayed" ]
aliases = [ "/questions/53541" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Export packets saves more packets than displayed.](/questions/53541/export-packets-saves-more-packets-than-displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53541-score" class="post-score" title="current number of votes">0</div><span id="post-53541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello community!</p><p>I filtered the packets with following command: "http.request or http.response". I can only see 2 packets. I click on "Export Specified Packets..." and click on "Displayed" instead of "Captured".</p><p>Funny thing: over 1000 packets will be saved. On the bottom of wireshark stands "Packets: 2000, Displayed: 2(0,1%)" but in the save dialog "Packets: 2000, Displayed: 1000". So how to solve this problem?</p><p>PS: Everything works fine without the "or" command, but I can't use the "and" keyword because there wont be any packets.</p><p>pls help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span> <span class="post-tag tag-link-displayed" rel="tag" title="see questions tagged &#39;displayed&#39;">displayed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '16, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/1aeb2c7d7cb46ffeb750c1a26d353e3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shuffle&#39;s gravatar image" /><p><span>shuffle</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shuffle has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '16, 19:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-53541" class="comments-container"></div><div id="comment-tools-53541" class="comment-tools"></div><div class="clear"></div><div id="comment-53541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="53548"></span>

<div id="answer-container-53548" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53548-score" class="post-score" title="current number of votes">0</div><span id="post-53548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shuffle has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Ok I realise it now. It is logical but I think Wireshark should change the GUI element a little bit. I have a SOLUTION to this "problem". Because I don't need the whole TCP packets I use the</p><ul><li>"http.request or http.response" filter and only 2 are shown (just an example).</li><li>Then go to "Edit&gt;" and choose "Mark all displayed packets"</li><li>now go to "Export Specified Packets..." and choose the option "market packets".</li></ul><p>This solved my problem. Because in my case the TCP packets contained a HUGE picture where I just needed the HTTP Request and Response for my work. Thx to you guys!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '16, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/1aeb2c7d7cb46ffeb750c1a26d353e3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shuffle&#39;s gravatar image" /><p><span>shuffle</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shuffle has one accepted answer">100%</span></p></div></div><div id="comments-container-53548" class="comments-container"><span id="53556"></span><div id="comment-53556" class="comment"><div id="post-53556-score" class="comment-score"></div><div class="comment-text"><p>I think you could also just disable TCP desegmentation to achieve the same effect.</p></div><div id="comment-53556-info" class="comment-info"><span class="comment-age">(18 Jun '16, 11:03)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="53557"></span><div id="comment-53557" class="comment"><div id="post-53557-score" class="comment-score"></div><div class="comment-text"><p><span>@shuffle</span>, next time please don't use answers and hints provided by others to create an answer yourself you then accept. This is unfair to those who try to help you. You should have added your solution to e.g. the one by <span>@JeffMorriss</span> of the other two instead of doing it this way. Thanks.</p></div><div id="comment-53557-info" class="comment-info"><span class="comment-age">(18 Jun '16, 11:50)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-53548" class="comment-tools"></div><div class="clear"></div><div id="comment-53548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53543"></span>

<div id="answer-container-53543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53543-score" class="post-score" title="current number of votes">1</div><span id="post-53543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What's happening is Wireshark is including all the frames that are necessary to dissect those HTTP requests and responses. Presumably you've got a bunch of frames reassembled into (probably) that HTTP response.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7667">Bug 7667</a> asks to make it possible to select whether those "dependent" frames are included or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '16, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-53543" class="comments-container"></div><div id="comment-tools-53543" class="comment-tools"></div><div class="clear"></div><div id="comment-53543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53545"></span>

<div id="answer-container-53545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53545-score" class="post-score" title="current number of votes">1</div><span id="post-53545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Without looking at your packets is seems that these single packets are the last ones of the set that makes the HTTP request and response complete? In order to be complete the previous packets are needed as well, so they're saved with them, as related packets to make sure the displayed packets stay indeed intact.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '16, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53545" class="comments-container"></div><div id="comment-tools-53545" class="comment-tools"></div><div class="clear"></div><div id="comment-53545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

