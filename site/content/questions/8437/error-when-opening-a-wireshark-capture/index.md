+++
type = "question"
title = "Error when opening a WireShark capture"
description = '''I was sent a wireshark capture from a customer but received the following error when I tried to open it: The file &quot;{network shared drive}CAD.cap&quot; is a capture for a network type that Wireshark doesn&#x27;t support. (Observer: unsupported file version ObserverPktBufferVersion=15.00) I&#x27;m trying to get info...'''
date = "2012-01-17T08:25:00Z"
lastmod = "2012-01-17T11:42:00Z"
weight = 8437
keywords = [ "captureerror" ]
aliases = [ "/questions/8437" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error when opening a WireShark capture](/questions/8437/error-when-opening-a-wireshark-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8437-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was sent a wireshark capture from a customer but received the following error when I tried to open it:</p><p>The file "{network shared drive}CAD.cap" is a capture for a network type that Wireshark doesn't support. (Observer: unsupported file version ObserverPktBufferVersion=15.00)</p><p>I'm trying to get information on this but not able to find anything yet. If there might be some suggestions, it would be helpful.</p></div><div id="question-tags" class="tags-container tags">captureerror</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '12, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/1e7e7237833aed1b6b36ec2e83f316b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vinnypie&#39;s gravatar image" /><p>Vinnypie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vinnypie has no accepted answers">0%</span></p></div></div><div id="comments-container-8437" class="comments-container"><span id="8439"></span><div id="comment-8439" class="comment"><div id="post-8439-score" class="comment-score"></div><div class="comment-text"><p>If it's really a Wireshark capture, I would not expect the error message shown. Could the file have gotten mangled when it was copied/transferred ? For instance, treating the file as ASCII when using FTP will mess up the file...</p></div><div id="comment-8439-info" class="comment-info"><span class="comment-age">(17 Jan '12, 08:55)</span> Bill Meier ♦♦</div></div><span id="8440"></span><div id="comment-8440" class="comment"><div id="post-8440-score" class="comment-score"></div><div class="comment-text"><p>I appreciate the response and have thought of that but get errors now matter how I try to open it. I will keep trying to get this figured out as I have asked the customer to provide more information. Thank you.</p></div><div id="comment-8440-info" class="comment-info"><span class="comment-age">(17 Jan '12, 08:58)</span> Vinnypie</div></div></div><div id="comment-tools-8437" class="comment-tools"></div><div class="clear"></div><div id="comment-8437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8443"></span>

<div id="answer-container-8443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8443-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I suspect that's <em>not</em> a Wireshark capture, but a capture from one of Network Instruments' <a href="http://www.netinst.com/products/observer/">Observer</a> products.</p><p>If so, this is probably <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5869">bug 5869</a>; older versions of Wireshark couldn't handle captures from newer versions of Observer. The fix is in 1.6.0 (and thus all 1.6.x releases); it's not in any 1.4.x release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '12, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8443" class="comments-container"></div><div id="comment-tools-8443" class="comment-tools"></div><div class="clear"></div><div id="comment-8443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

