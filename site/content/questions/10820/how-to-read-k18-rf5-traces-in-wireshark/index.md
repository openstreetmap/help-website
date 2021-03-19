+++
type = "question"
title = "how to read K18 rf5 traces in Wireshark?"
description = '''Hi I am unable to open rf5 files(K18) using Wireshark. An error reading &quot;rf5 file may be corrupt or damaged&quot; appears. I am using Wireshark 1.6.7. kindly help. Abhinav '''
date = "2012-05-09T03:53:00Z"
lastmod = "2013-11-20T13:26:00Z"
weight = 10820
keywords = [ "k18" ]
aliases = [ "/questions/10820" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to read K18 rf5 traces in Wireshark?](/questions/10820/how-to-read-k18-rf5-traces-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10820-score" class="post-score" title="current number of votes">0</div><span id="post-10820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am unable to open rf5 files(K18) using Wireshark. An error reading "rf5 file may be corrupt or damaged" appears. I am using Wireshark 1.6.7. kindly help.</p><p>Abhinav</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-k18" rel="tag" title="see questions tagged &#39;k18&#39;">k18</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '12, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/4deaa42e352a0d933b70002ae22c3e2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhinav&#39;s gravatar image" /><p><span>Abhinav</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhinav has no accepted answers">0%</span></p></div></div><div id="comments-container-10820" class="comments-container"></div><div id="comment-tools-10820" class="comment-tools"></div><div class="clear"></div><div id="comment-10820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10842"></span>

<div id="answer-container-10842" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10842-score" class="post-score" title="current number of votes">1</div><span id="post-10842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>According to the <a href="http://wiki.wireshark.org/K12">Wiki page</a>, Wireshark supports reading rf5 files from K12 and K15 analyzers, but K18 is not mentioned. I'm guessing that the file format has changed; by how much is anyone's guess.</p><p>If you'd like Wireshark to support the K18 format, you should open an enhancement <a href="https://bugs.wireshark.org">bug</a> and attach a K18 rf5 file and, if possible, a sample decoding of that file (Tektronix' output). That way if someone has time and the inclination, they could (hopefully) add support for K18 rf5 files. (Of course if you're so inclined a patch against Wireshark's source code would be a sure way to speed up that process.)</p><p><a href="http://ask.wireshark.org/questions/5117/rf5-file-opening-error">This question</a> lists some output which I guess is the K18 file--not sure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '12, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-10842" class="comments-container"></div><div id="comment-tools-10842" class="comment-tools"></div><div class="clear"></div><div id="comment-10842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27181"></span>

<div id="answer-container-27181" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27181-score" class="post-score" title="current number of votes">0</div><span id="post-27181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try one of the <a href="http://www.wireshark.org/download/automated/">automated builds</a> with a version number of "SVN-53452" or later; somebody finally filed <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9455">a bug</a> for a failure to read a k18 capture, and attached a capture file that showed the problem, so it was finally possible for some reverse-engineering to be done to handle that file, at least.</p><p>If that still doesn't handle it, file another bug, and attach the capture file, so that more reverse-engineering can be done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27181" class="comments-container"></div><div id="comment-tools-27181" class="comment-tools"></div><div class="clear"></div><div id="comment-27181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

