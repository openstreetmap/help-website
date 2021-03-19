+++
type = "question"
title = "Creating Profile in Wireshark 2.0.1"
description = '''The current Wireshark 101 book uses a downloaded zip file to create the &quot;HTTP-DNS_Errors&quot; profile. The process has apparently changed in Wireshark 2.0. Looks like you have to use the &quot;Profile Copy&quot; icon next to the &quot;+&quot; and &quot;-&quot; symbols at the bottom of the Wireshark Configuration Profiles window to c...'''
date = "2016-01-06T22:41:00Z"
lastmod = "2016-01-07T02:12:00Z"
weight = 48937
keywords = [ "profile" ]
aliases = [ "/questions/48937" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating Profile in Wireshark 2.0.1](/questions/48937/creating-profile-in-wireshark-201)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48937-score" class="post-score" title="current number of votes">0</div><span id="post-48937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The current Wireshark 101 book uses a downloaded zip file to create the "HTTP-DNS_Errors" profile. The process has apparently changed in Wireshark 2.0. Looks like you have to use the "Profile Copy" icon next to the "+" and "-" symbols at the bottom of the Wireshark Configuration Profiles window to create a profile from the Default profile. (Right click on "Profile" on the right side of the Task Bar and then left-click on "Manage Profiles".) This will provide a "recent" file in the user profile folder. You can then manually copy the 3 unzipped book configuration files into the new user profile. Without a valid "recent" file in the new folder, Wireshark goes in to a "Not-responding" mode and hangs forever. The same is true if you try to create a "Troubleshooting" or "wireshark101" profile in the user profile directory. I'm guessing you have to do the same thing for any other new profile that you want to create from the Default profile.</p><p>Am I missing something here?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-profile" rel="tag" title="see questions tagged &#39;profile&#39;">profile</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '16, 22:41</strong></p><img src="https://secure.gravatar.com/avatar/8be7639e51caa074a018c93335e399f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fastwilly&#39;s gravatar image" /><p><span>Fastwilly</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fastwilly has no accepted answers">0%</span></p></div></div><div id="comments-container-48937" class="comments-container"></div><div id="comment-tools-48937" class="comment-tools"></div><div class="clear"></div><div id="comment-48937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48939"></span>

<div id="answer-container-48939" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48939-score" class="post-score" title="current number of votes">0</div><span id="post-48939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like a bug. File this as a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, with a title such as "Wireshark hangs with a profile directory with no recent file", and with the httpdnsprofile.zip file as an attachment. Give the full sequence of steps used to reproduce the problem, including both operations performed in the Wireshark GUI and performed at the command line or in your OS's file manager (Windows Explorer, Finder, etc.), in the order in which they're done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '16, 02:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jan '16, 02:20</strong> </span></p></div></div><div id="comments-container-48939" class="comments-container"></div><div id="comment-tools-48939" class="comment-tools"></div><div class="clear"></div><div id="comment-48939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

