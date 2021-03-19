+++
type = "question"
title = "Is there a reason the install overwrites Visual Studio redistritable 12.0.21005 x86"
description = '''When I installed Wireshark onto my PC, the install deleted the 12.0.21005 redistributable file. Some of my other programs required the file to run, and I had to manually go and get it again. Is that supposed to happen?'''
date = "2016-04-22T07:17:00Z"
lastmod = "2016-08-05T11:06:00Z"
weight = 51870
keywords = [ "installer" ]
aliases = [ "/questions/51870" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a reason the install overwrites Visual Studio redistritable 12.0.21005 x86](/questions/51870/is-there-a-reason-the-install-overwrites-visual-studio-redistritable-12021005-x86)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51870-score" class="post-score" title="current number of votes">0</div><span id="post-51870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I installed Wireshark onto my PC, the install deleted the 12.0.21005 redistributable file. Some of my other programs required the file to run, and I had to manually go and get it again.</p><p>Is that supposed to happen?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installer" rel="tag" title="see questions tagged &#39;installer&#39;">installer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '16, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/e061c773a1da6ea2c8efe307b688ad7f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cantthinkofaname1029&#39;s gravatar image" /><p><span>cantthinkofa...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cantthinkofaname1029 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Aug '16, 23:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-51870" class="comments-container"><span id="51871"></span><div id="comment-51871" class="comment"><div id="post-51871-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark, and what do you mean by "deleted the 12.0.21005 redistributable file"? Do you mean uninstalled the VC 12.0.xx redist completely, or replaced it with a newer version, or actually delete a file.</p></div><div id="comment-51871-info" class="comment-info"><span class="comment-age">(22 Apr '16, 07:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="51941"></span><div id="comment-51941" class="comment"><div id="post-51941-score" class="comment-score">1</div><div class="comment-text"><p>A few people have reported this problem, but so far no one has provided enough information to track the problem down and fix it. Can you <em>please oh please</em> provide more information on the following?</p><ul><li>Were files overwritten or removed?</li><li>Which files, exactly?</li><li>Which programs are refusing to run?</li></ul><p>Wireshark 2.0.x ships with the <a href="https://www.microsoft.com/en-us/download/confirmation.aspx?id=40784">Visual C++ Redistributable Packages for Visual Studio 2013</a> version 12.0.30501.0. This is the latest version recommended by Microsoft. I seriously doubt we're the only ones installing this version. If some other software is linking with version 12.0.21005.1 such that it won't run with any other version, then that's arguably a bug in that software. If we're installing vcredist_x86.exe with incorrectly then that's a bug in Wireshark. It's not clear at this point which of these (or something else entirely) is happening.</p></div><div id="comment-51941-info" class="comment-info"><span class="comment-age">(25 Apr '16, 16:27)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div><span id="54194"></span><div id="comment-54194" class="comment"><div id="post-54194-score" class="comment-score"></div><div class="comment-text"><p>We just experienced the same thing where the older version of the redist package was uninstalled. My application software requires a specific version. The older version needed to be reinstalled. I doubt I will be able to use Wireshark on any server that requires the older version.</p></div><div id="comment-54194-info" class="comment-info"><span class="comment-age">(20 Jul '16, 10:51)</span> <span class="comment-user userinfo">shanejnelson</span></div></div><span id="54196"></span><div id="comment-54196" class="comment"><div id="post-54196-score" class="comment-score"></div><div class="comment-text"><p>Any application that depends on a specific version of the redist is faulty, although that's not much help to you.</p><p>Any installer is free to update the VC redist files, including Windows update.</p><p>So, for clarity, when you installed Wireshark did it install the expected VC redist as <span>@Gerald Combs</span> noted above, or did it uninstall the redist entirely?</p></div><div id="comment-54196-info" class="comment-info"><span class="comment-age">(20 Jul '16, 11:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="54197"></span><div id="comment-54197" class="comment"><div id="post-54197-score" class="comment-score"></div><div class="comment-text"><p>Again, "If some other software is linking with version 12.0.21005.1 such that it won't run with any other version, then that's arguably a bug in that software."</p><p>Have you tried reporting this as a bug in <em>that</em> software? If so, what was the response?</p></div><div id="comment-54197-info" class="comment-info"><span class="comment-age">(20 Jul '16, 11:42)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-51870" class="comment-tools"></div><div class="clear"></div><div id="comment-51870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54618"></span>

<div id="answer-container-54618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54618-score" class="post-score" title="current number of votes">1</div><span id="post-54618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The deleted files are apparently due to a bug in version 12.0.30501.0 of the redistributable installer. Microsoft released an updated installer (12.0.40649.5) via <a href="https://support.microsoft.com/en-us/kb/3138367">KB3138367</a> but for some reason haven't updated the installer on the main download page. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12712">bug 12712</a> for details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '16, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-54618" class="comments-container"></div><div id="comment-tools-54618" class="comment-tools"></div><div class="clear"></div><div id="comment-54618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

