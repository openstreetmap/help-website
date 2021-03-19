+++
type = "question"
title = "rf5 file (k18)"
description = '''Hi everybody , I need to open a rf5 file (k18) of tektronix by Wireshark, but an error &quot;rf5 file may be corrupt or damaged&quot; appears. Please could you suggest a way to dissect this capture (with a programming language , wireshark tool, ......). Thank you Yours Sincerely'''
date = "2013-11-19T02:19:00Z"
lastmod = "2013-11-20T13:25:00Z"
weight = 27092
keywords = [ "k18", "rf5", "tektronix" ]
aliases = [ "/questions/27092" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [rf5 file (k18)](/questions/27092/rf5-file-k18)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27092-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody ,</p><p>I need to open a rf5 file (k18) of tektronix by Wireshark, but an error "rf5 file may be corrupt or damaged" appears.</p><p>Please could you suggest a way to dissect this capture (with a programming language , wireshark tool, ......).</p><p>Thank you Yours Sincerely</p></div><div id="question-tags" class="tags-container tags">k18 rf5 tektronix</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '13, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/a8d6dbe511e45673d95529a8a6e6e7eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niamat&#39;s gravatar image" /><p>niamat<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niamat has no accepted answers">0%</span></p></div></div><div id="comments-container-27092" class="comments-container"></div><div id="comment-tools-27092" class="comment-tools"></div><div class="clear"></div><div id="comment-27092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27099"></span>

<div id="answer-container-27099" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27099-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Someone asked this same question on the wireshark-dev mailing list recently. The <a href="http://www.wireshark.org/lists/wireshark-dev/201311/msg00132.html">suggestion there</a> was to open a <a href="https://bugs.wireshark.org">bug report</a> so we can take a look at the file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '13, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-27099" class="comments-container"><span id="27105"></span><div id="comment-27105" class="comment"><div id="post-27105-score" class="comment-score"></div><div class="comment-text"><p>Thank you for reply. I have opened a bug as suggested .</p></div><div id="comment-27105-info" class="comment-info"><span class="comment-age">(19 Nov '13, 09:00)</span> niamat</div></div><span id="27107"></span><div id="comment-27107" class="comment"><div id="post-27107-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-27107-info" class="comment-info"><span class="comment-age">(19 Nov '13, 10:05)</span> grahamb ♦</div></div></div><div id="comment-tools-27099" class="comment-tools"></div><div class="clear"></div><div id="comment-27099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27180"></span>

<div id="answer-container-27180" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27180-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The bug, <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9455">bug 9455</a>, has been fixed, at least for the attached capture file.</p><p>Try one of the <a href="http://www.wireshark.org/download/automated/">automated builds</a> with a version number of "SVN-53452" or later.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-27180" class="comments-container"></div><div id="comment-tools-27180" class="comment-tools"></div><div class="clear"></div><div id="comment-27180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

