+++
type = "question"
title = "Why doesn&#x27;t the Wireshark Team fix the MacOsx version of wireshark install"
description = '''I ran the Wireshark installation and it fails to start. When run from the command line I get the following error: Incompatible library version: wireshark-bin requires version 14.0.0 or later, but libfreetype.6.dylib provides version 13.0.0 I googled around and saw suggestions such as update freetype...'''
date = "2012-04-19T09:54:00Z"
lastmod = "2015-04-16T17:30:00Z"
weight = 10289
keywords = [ "osx", "install" ]
aliases = [ "/questions/10289" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why doesn't the Wireshark Team fix the MacOsx version of wireshark install](/questions/10289/why-doesnt-the-wireshark-team-fix-the-macosx-version-of-wireshark-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10289-score" class="post-score" title="current number of votes">1</div><span id="post-10289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran the Wireshark installation and it fails to start. When run from the command line I get the following error: Incompatible library version: wireshark-bin requires version 14.0.0 or later, but libfreetype.6.dylib provides version 13.0.0</p><p>I googled around and saw suggestions such as update freetype and macports. I did this and am currently running latest macports and $ sudo port installed | grep freetype shows freetype <span>@2</span>.4.9_1 (active) It doesn't get anymore current than this. Another link on the web suggested that your installation package is broken.</p><p>When if ever do you plan to fix this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/36c739aedf31baf750724dfcb263fe8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WantaKnow&#39;s gravatar image" /><p><span>WantaKnow</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WantaKnow has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>19 Apr '12, 10:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p><span>bstn</span><br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span></p></div></div><div id="comments-container-10289" class="comments-container"><span id="10298"></span><div id="comment-10298" class="comment"><div id="post-10298-score" class="comment-score"></div><div class="comment-text"><p>The more I dig in to this the more things seem to be related to Wireshark dependencies on the very latest and greatest X11 and GTK code. This is problematic. First of all X11 is no longer supported by the Mac. Getting newer versions of GTK to build on the Mac (1.6.8) have been unsuccessful due to one or other dependencies. Why is it that the team has to use the latest graphics code which is not widely distributed on the Mac? Are you doing heavy duty 3D animations with advanced frame rates or something? You shouldn't need a gaming subsystem to run the UI.</p></div><div id="comment-10298-info" class="comment-info"><span class="comment-age">(19 Apr '12, 12:01)</span> <span class="comment-user userinfo">WantaKnow</span></div></div></div><div id="comment-tools-10289" class="comment-tools"></div><div class="clear"></div><div id="comment-10289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10312"></span>

<div id="answer-container-10312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10312-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10312-score" class="post-score" title="current number of votes">1</div><span id="post-10312-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not built with anything from MacPorts, so a MacPorts update will probably not update anything that Wireshark uses.</p><p>My MacBook Pro is running 10.6.8 with all security updates, and has libfreetype with a compatibility version of 14.0.0:</p><pre><code>$ otool -L /usr/X11/lib/libfreetype.6.dylib
/usr/X11/lib/libfreetype.6.dylib:
/usr/X11/lib/libfreetype.6.dylib (compatibility version 14.0.0, current version 14.2.0)</code></pre><p>The problem is that:</p><ol><li>We build the version of GTK+ distributed with Wireshark against the libraries installed on the buildbot, rather than the ones in the Snow Leopard SDK, which means that if you don't have as up-to-date a version of the OS as the one on the buildbot, there is a risk that the resulting binary won't work on your machine.</li><li>libfreetype uses GNU libtool, and the way libtool does versioning can cause library <em>major</em> version numbers to change with new versions even if the new version of the library is backwards-compatible with the old one.</li><li>Apple sometimes updates libfreetype.</li></ol><p>The first of those is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5937">bug 5937</a> in the Wireshark bug database. It requires some work on the Wireshark <code>macosx-setup.sh</code> script used to build the support libraries, as well as on the configure scripts etc., to allow Wireshark and its support libraries to be built against the SDK; it also then requires that the buildbots rebuild the support libraries against the SDK.</p><p>The second of those is a bug in the Apple bug database, but it's a bit tricky, and arguably the right thing to do in the shorter term is to fix the first of those, which would obviate the need for a change to the library versioning scheme.</p><p>The third of those, well, sometimes there are bugs in libfreetype, and some of them might even cause security issues, so Apple <em>should</em> update it.</p><p>The requirement for newer versions of X11 libraries has nothing to do with a requirement for high-end 3D graphic performance - it's just a consequence of the way the builds are currently being done and of the way library version numbers are assigned. Apple's not likely to spend a lot of time and energy worrying about frame rates for X11 <em>client</em> software, and, in any case, libfreetype isn't a fancy 3D graphics library, <a href="http://www.freetype.org/">it's just a font rendering engine</a>, so it's not as if the latest version is going to make much difference to frame rates in X11 applications.</p><p>And, yes, in the longer term we should stop using GTK+-on-X11 on the Mac, and probably stop using "native" GTK+ on Windows. There is a "native" GTK+ for OS X, which would avoid the requirement for the X11 server, and <em>possibly</em> avoid using the version of libfreetype that comes with Apple's X11, but I think that has some issues of its own. Currently, there's work in progress to support using <a href="http://qt.nokia.com/products">Qt</a> for the GUI; Qt's OS X and Windows support is, I think, better than GTK+'s, and its X11 support is probably at least as good as GTK+'s (and would probably make people using Wireshark on KDE happier :-)).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '12, 15:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10312" class="comments-container"><span id="41513"></span><div id="comment-41513" class="comment"><div id="post-41513-score" class="comment-score"></div><div class="comment-text"><p>As of late 2013, we're now building the support libraries against the SDK, so the GTK+ flavor of the problem should be fixed.</p><p>The current plan is to use Qt for the next major Wireshark release, and it will <em>not</em> be an X11-based flavor of Qt on OS X, so there won't be any X11 dependency for that release on OS X.</p></div><div id="comment-41513-info" class="comment-info"><span class="comment-age">(16 Apr '15, 17:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-10312" class="comment-tools"></div><div class="clear"></div><div id="comment-10312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

