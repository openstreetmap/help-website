+++
type = "question"
title = "How would one generate an RPM for wireshark?"
description = '''I&#x27;m sorry if the question is really broad. As far as I know you need to create a spec file. But besides that what else do I have to keep in mind? Furthermore, are there are build scripts out there already that I can use to generate it? I know ethereal came in rpms...'''
date = "2011-03-30T16:37:00Z"
lastmod = "2011-03-30T19:25:00Z"
weight = 3237
keywords = [ "generating", "rpms" ]
aliases = [ "/questions/3237" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How would one generate an RPM for wireshark?](/questions/3237/how-would-one-generate-an-rpm-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3237-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm sorry if the question is really broad. As far as I know you need to create a spec file. But besides that what else do I have to keep in mind?</p><p>Furthermore, are there are build scripts out there already that I can use to generate it? I know ethereal came in rpms...</p></div><div id="question-tags" class="tags-container tags">generating rpms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '11, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/e38821ea7ed026bbdf8032a0fdc64d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tokolosh&#39;s gravatar image" /><p>Tokolosh<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tokolosh has no accepted answers">0%</span></p></div></div><div id="comments-container-3237" class="comments-container"></div><div id="comment-tools-3237" class="comment-tools"></div><div class="clear"></div><div id="comment-3237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3239"></span>

<div id="answer-container-3239" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3239-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>In the packaging/rpm directory tree in the source there's a SPECS subdirectory with a wireshark.spec.in file, which is turned into a wireshark.spec file by the configure script. In addition, there are "rpm-package" and "srpm-package" rules in the top-level Makefile.am; try running the configure script, if you haven't done it already, and then doing "make rpm-package" and see whether it generates an acceptable RPM. (If not, file bugs at <a href="http://bugs.wireshark.org">the Wireshark bug database</a>.)</p><p>(And, yes, <a href="http://www.rpmfind.net/linux/rpm2html/search.php?query=Wireshark&amp;submit=Search+...">people continued generating RPMs after the name changed from Ethereal to Wireshark</a>....)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '11, 19:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3239" class="comments-container"><span id="3249"></span><div id="comment-3249" class="comment"><div id="post-3249-score" class="comment-score"></div><div class="comment-text"><p>Awesome, exactly what I was looking for =D</p></div><div id="comment-3249-info" class="comment-info"><span class="comment-age">(31 Mar '11, 10:52)</span> Tokolosh</div></div></div><div id="comment-tools-3239" class="comment-tools"></div><div class="clear"></div><div id="comment-3239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

