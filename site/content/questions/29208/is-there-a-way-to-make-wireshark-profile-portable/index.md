+++
type = "question"
title = "Is there a way to make wireshark profile portable?"
description = '''Hi, I have several computers running wireshark, currently I have to configure each of them with the same profile, especially for the column configuration, which is really laborious.  Is there a way to make the profile portable so that I can just do copy paste from one computer to another. thanks!'''
date = "2014-01-27T17:23:00Z"
lastmod = "2014-01-27T19:22:00Z"
weight = 29208
keywords = [ "profile" ]
aliases = [ "/questions/29208" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to make wireshark profile portable?](/questions/29208/is-there-a-way-to-make-wireshark-profile-portable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29208-score" class="post-score" title="current number of votes">0</div><span id="post-29208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have several computers running wireshark, currently I have to configure each of them with the same profile, especially for the column configuration, which is really laborious.</p><p>Is there a way to make the profile portable so that I can just do copy paste from one computer to another.</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-profile" rel="tag" title="see questions tagged &#39;profile&#39;">profile</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '14, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-29208" class="comments-container"></div><div id="comment-tools-29208" class="comment-tools"></div><div class="clear"></div><div id="comment-29208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29210"></span>

<div id="answer-container-29210" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29210-score" class="post-score" title="current number of votes">3</div><span id="post-29210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Profiles are already portable. A Wireshark profile is simply a set of files that contain the various settings and preferences that you have configured.</p><p>In Wireshark, click on Help &gt; About Wireshark, click the Folders tab, then double-click the link for "Personal Configuration." This will take you to the folder that contains your profile(s). The files you see are for the default profile. If you have created any custom profiles, then there will be a folder named "Profiles," and each custom profile will have its own folder within the Profiles folder, with its own set of files.</p><p>To copy a profile, or all profiles, to another computer, just copy the appropriate files and folders.</p><p>Almost everything will work when you do that. There are a few things that are path-dependent, so you should try to put things in the same place on each computer. For example, if you configure GeoIP name resolution on the source computer, and expect it to work on the destination computer, you need to make sure that you've downloaded the GeoIP files to both computers, and you should put them in the same place on both computers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '14, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Jan '14, 14:37</strong> </span></p></div></div><div id="comments-container-29210" class="comments-container"></div><div id="comment-tools-29210" class="comment-tools"></div><div class="clear"></div><div id="comment-29210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

