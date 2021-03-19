+++
type = "question"
title = "trouble building stand-alone osx app for mountain lion"
description = '''I have tried for several days to build an OSX app that can run on other systems. I can run both cli and app wireshark on my build machine (mountain lion). But when i try to run the app on another mountain lion machine, there are libraries missing, etc. I&#x27;ve added some of those libs manually, but now...'''
date = "2013-04-23T22:33:00Z"
lastmod = "2013-04-25T07:52:00Z"
weight = 20756
keywords = [ "osx", "macosx", "build", "macports" ]
aliases = [ "/questions/20756" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [trouble building stand-alone osx app for mountain lion](/questions/20756/trouble-building-stand-alone-osx-app-for-mountain-lion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20756-score" class="post-score" title="current number of votes">0</div><span id="post-20756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried for several days to build an OSX app that can run on other systems. I can run both cli and app wireshark on my build machine (mountain lion). But when i try to run the app on another mountain lion machine, there are libraries missing, etc. I've added some of those libs manually, but now i seem to have dependencies on two different versions of libiconv. Are the scripts in SVN supposed to work to build a a stand-alone app on mountain lion? Have I missed some flags that should be set? I've used different combinations of macosx-setup, autogen, configure, osx-app, etc. but to no avail. Has anyone successfully built a ML app from the SVN sources?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-macports" rel="tag" title="see questions tagged &#39;macports&#39;">macports</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '13, 22:33</strong></p><img src="https://secure.gravatar.com/avatar/1de7dea2b27c6685881142d7cb26a5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmfinn9&#39;s gravatar image" /><p><span>jmfinn9</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmfinn9 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Apr '13, 09:45</strong> </span></p></div></div><div id="comments-container-20756" class="comments-container"></div><div id="comment-tools-20756" class="comment-tools"></div><div class="clear"></div><div id="comment-20756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20799"></span>

<div id="answer-container-20799" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20799-score" class="post-score" title="current number of votes">1</div><span id="post-20799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have solved my problem - it was because I had macports installed on my development machine. Once I removed macports, I was able to easily build the macos app with the supplied make target. Thanks everyone for their input.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '13, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/1de7dea2b27c6685881142d7cb26a5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmfinn9&#39;s gravatar image" /><p><span>jmfinn9</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmfinn9 has no accepted answers">0%</span></p></div></div><div id="comments-container-20799" class="comments-container"></div><div id="comment-tools-20799" class="comment-tools"></div><div class="clear"></div><div id="comment-20799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20757"></span>

<div id="answer-container-20757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20757-score" class="post-score" title="current number of votes">0</div><span id="post-20757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have tried for several days to build an OSX app that can run on other systems.</p></blockquote><p>After you ran <code>make</code>, you ran <code>make osx-package</code>, and used the dmg that produced to install Wireshark on the other systems, right?</p><p>If not, do so. If you just run <code>make</code>, what you have is a Wireshark binary that you can run from the command line and that will work <em>only</em> on a system that has the same libraries installed; that's useful for testing and debugging (and for those of us who view OS X as "a nice BSD Unix that can run Safari, iTunes, and Quicken" :-)), but it's not a self-contained app bundle, like the ones on the dmg you can download from wireshark.org, so you'll have to manually install all the libraries it requires.</p><p>(This has nothing to do with Mountain Lion, BTW; it's true for all OS X releases.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '13, 23:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20757" class="comments-container"><span id="20758"></span><div id="comment-20758" class="comment"><div id="post-20758-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick reply. I have tried building the package, but packagemaker (which is now deprecated by Apple) throws an exception and crashes. I'll revisit that, though. Has anyone run packagemaker in ML? Is it just crashing on my system?</p></div><div id="comment-20758-info" class="comment-info"><span class="comment-age">(24 Apr '13, 03:55)</span> <span class="comment-user userinfo">jmfinn9</span></div></div><span id="20769"></span><div id="comment-20769" class="comment"><div id="post-20769-score" class="comment-score"></div><div class="comment-text"><p>I manually built the package with the package manager, but still had the same error. After further investigation - it seems that some parts of wireshark require version 7.0.0 of libiconv and some parts require version 8.0.0 of libiconv. I have not been able to get around this yet.</p><p>Has anyone successfully built the stand-alone osx app from either the current svn or the latest source tarball?</p></div><div id="comment-20769-info" class="comment-info"><span class="comment-age">(24 Apr '13, 09:37)</span> <span class="comment-user userinfo">jmfinn9</span></div></div><span id="20781"></span><div id="comment-20781" class="comment"><div id="post-20781-score" class="comment-score">1</div><div class="comment-text"><p><span></span><span>@jmfinn9</span> Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-20781-info" class="comment-info"><span class="comment-age">(24 Apr '13, 13:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="20782"></span><div id="comment-20782" class="comment"><div id="post-20782-score" class="comment-score"></div><div class="comment-text"><p>I've run packagemaker on my 10.8.2 system with Xcode 4.6, build version 4H127, so it definitely works on 10.8.2 with that build of Xcode 4.6, at least. Apple may have broken something in a later Xcode release or in 10.8.3; if so, you might have to find a later version of Auxiliary Tools for Xcode - go to <a href="https://developer.apple.com/downloads/index.action">Downloads for Apple Developers</a> (you'll need an ADC account for that), and search for "Auxiliary Tools for Xcode" and see whether a later version helps.</p></div><div id="comment-20782-info" class="comment-info"><span class="comment-age">(24 Apr '13, 14:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="20800"></span><div id="comment-20800" class="comment"><div id="post-20800-score" class="comment-score"></div><div class="comment-text"><p>Thanks graham for fixing my mistake.</p></div><div id="comment-20800-info" class="comment-info"><span class="comment-age">(25 Apr '13, 07:52)</span> <span class="comment-user userinfo">jmfinn9</span></div></div></div><div id="comment-tools-20757" class="comment-tools"></div><div class="clear"></div><div id="comment-20757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

