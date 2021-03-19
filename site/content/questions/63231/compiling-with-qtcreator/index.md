+++
type = "question"
title = "Compiling with QtCreator"
description = '''Topic :) The downloaded source tarball doesn&#x27;t appear to contain a .pro file. Thank you.'''
date = "2017-07-29T02:38:00Z"
lastmod = "2017-10-21T11:08:00Z"
weight = 63231
keywords = [ "compile" ]
aliases = [ "/questions/63231" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Compiling with QtCreator](/questions/63231/compiling-with-qtcreator)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63231-score" class="post-score" title="current number of votes">0</div><span id="post-63231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Topic :) The downloaded source tarball doesn't appear to contain a .pro file. Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '17, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/feeceb13b3a434a147fa2c173ad18db8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DigiAngelXX&#39;s gravatar image" /><p><span>DigiAngelXX</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DigiAngelXX has no accepted answers">0%</span></p></div></div><div id="comments-container-63231" class="comments-container"></div><div id="comment-tools-63231" class="comment-tools"></div><div class="clear"></div><div id="comment-63231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63236"></span>

<div id="answer-container-63236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63236-score" class="post-score" title="current number of votes">1</div><span id="post-63236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try opening CMakeLists.txt. Qt Creator has supported CMake for some time, and I often use that combination to build on macOS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '17, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-63236" class="comments-container"><span id="63237"></span><div id="comment-63237" class="comment"><div id="post-63237-score" class="comment-score"></div><div class="comment-text"><p>Thank you...yes I did get that working...the CMakeLists.txt at least...but the above error is what QtCreator gives me. Ideally I'd like to just use the dev environment that is present in /opt/Qt5.6.1 instead of installing a bunch of system libraries, but I've not had any luck with getting wireshark to see /opt/Qt5.6.1 as the location for libs and headers and what not.</p></div><div id="comment-63237-info" class="comment-info"><span class="comment-age">(29 Jul '17, 08:31)</span> <span class="comment-user userinfo">DigiAngelXX</span></div></div><span id="63238"></span><div id="comment-63238" class="comment"><div id="post-63238-score" class="comment-score"></div><div class="comment-text"><p>You should be able to fix this within Qt Creator by opening the preferences dialog, selecting "Build &amp; Run", then "Qt Versions" and manually adding the 5.6.1 qmake location.</p></div><div id="comment-63238-info" class="comment-info"><span class="comment-age">(29 Jul '17, 09:00)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-63236" class="comment-tools"></div><div class="clear"></div><div id="comment-63236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63233"></span>

<div id="answer-container-63233" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63233-score" class="post-score" title="current number of votes">0</div><span id="post-63233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is because you are not supposed to use QtCreator to compile Wireshark. Follow the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBuildFirstTime.html">development guide</a> instead. Note hat CMake is also supported on Linux (you have a dedicated README in the source tree).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '17, 05:21</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-63233" class="comments-container"><span id="63234"></span><div id="comment-63234" class="comment"><div id="post-63234-score" class="comment-score"></div><div class="comment-text"><p>Thanks...I <em>sort of</em> figured it out here:</p><p><a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChUIQt.html">https://www.wireshark.org/docs/wsdg_html_chunked/ChUIQt.html</a></p><p>However the build failed with: :-1: error: No rule to make target '/home/build/wireshark-2.4.0/doc/udpdump.pod', needed by 'doc/udpdump.1'. Stop.</p><p>I also tried to tell ./configure that Qt is in /opt/Qt5.6.1, but that failed as well :(</p></div><div id="comment-63234-info" class="comment-info"><span class="comment-age">(29 Jul '17, 05:27)</span> <span class="comment-user userinfo">DigiAngelXX</span></div></div><span id="63239"></span><div id="comment-63239" class="comment"><div id="post-63239-score" class="comment-score"></div><div class="comment-text"><p>This is a bug we fixed after 2.4 release. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13903">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13903</a></p></div><div id="comment-63239-info" class="comment-info"><span class="comment-age">(29 Jul '17, 10:19)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="64067"></span><div id="comment-64067" class="comment"><div id="post-64067-score" class="comment-score"></div><div class="comment-text"><p>Thanks..this worked well with 2.4.2.</p></div><div id="comment-64067-info" class="comment-info"><span class="comment-age">(21 Oct '17, 11:08)</span> <span class="comment-user userinfo">DigiAngelXX</span></div></div></div><div id="comment-tools-63233" class="comment-tools"></div><div class="clear"></div><div id="comment-63233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

