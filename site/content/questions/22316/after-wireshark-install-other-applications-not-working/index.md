+++
type = "question"
title = "After Wireshark install other applications not working"
description = '''I have two servers one Master and one USA, both are sparc. I have installed the wireshark and my application on Master server and accessing them from UAS server. When wireshark is not installed, my application is running and GUI launches fine but after installing the wireshark my application is not ...'''
date = "2013-06-25T04:44:00Z"
lastmod = "2013-06-26T04:29:00Z"
weight = 22316
keywords = [ "installation", "wireshark" ]
aliases = [ "/questions/22316" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [After Wireshark install other applications not working](/questions/22316/after-wireshark-install-other-applications-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22316-score" class="post-score" title="current number of votes">0</div><span id="post-22316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two servers one Master and one USA, both are sparc. I have installed the wireshark and my application on Master server and accessing them from UAS server.</p><p>When wireshark is not installed, my application is running and GUI launches fine but after installing the wireshark my application is not running, there are several other applications also in that server and all of them are not working after wireshark installation.</p><p>Can anyone have any idea why is this behavior?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '13, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/c83ca22a760e356093e591f491b6744f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KumarM&#39;s gravatar image" /><p><span>KumarM</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KumarM has no accepted answers">0%</span></p></div></div><div id="comments-container-22316" class="comments-container"></div><div id="comment-tools-22316" class="comment-tools"></div><div class="clear"></div><div id="comment-22316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22321"></span>

<div id="answer-container-22321" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22321-score" class="post-score" title="current number of votes">0</div><span id="post-22321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What do you mean the application doesn't run? Does it fail to load or does it run but not work?</p><p>The only thought I have is that installing Wireshark changed a library dependency that your application(s) use and that the application is failing to load (e.g., you get an ld.so error about a library not found or some such).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '13, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-22321" class="comments-container"><span id="22322"></span><div id="comment-22322" class="comment"><div id="post-22322-score" class="comment-score"></div><div class="comment-text"><p>additionally, does the problem occur <strong>after the installation</strong> of Wireshark or <strong>when Wireshark is started</strong>?</p></div><div id="comment-22322-info" class="comment-info"><span class="comment-age">(25 Jun '13, 06:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22324"></span><div id="comment-22324" class="comment"><div id="post-22324-score" class="comment-score"></div><div class="comment-text"><p>Thanks.</p><p>I mean that application fails to load. This problem occur only after installing the wireshark. If wireshark is not installed, in that case application loads and works properly.</p></div><div id="comment-22324-info" class="comment-info"><span class="comment-age">(25 Jun '13, 07:42)</span> <span class="comment-user userinfo">KumarM</span></div></div><span id="22325"></span><div id="comment-22325" class="comment"><div id="post-22325-score" class="comment-score"></div><div class="comment-text"><p>So what error is given when it fails to load?</p></div><div id="comment-22325-info" class="comment-info"><span class="comment-age">(25 Jun '13, 07:57)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="22339"></span><div id="comment-22339" class="comment"><div id="post-22339-score" class="comment-score"></div><div class="comment-text"><p>There is no specific error. In my application there is some Spring OSGI jar dependency and org.eclipse.equinox.launcher.gtk.solaris.sparc-1.1.2.jar. I am not sure that if this is causing any issue.</p></div><div id="comment-22339-info" class="comment-info"><span class="comment-age">(25 Jun '13, 21:32)</span> <span class="comment-user userinfo">KumarM</span></div></div><span id="22344"></span><div id="comment-22344" class="comment"><div id="post-22344-score" class="comment-score"></div><div class="comment-text"><p>O.K. then can you please add more information what you mean by "<strong>application fails to load</strong>", if there is no error message !??!</p></div><div id="comment-22344-info" class="comment-info"><span class="comment-age">(26 Jun '13, 00:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22348"></span><div id="comment-22348" class="comment not_top_scorer"><div id="post-22348-score" class="comment-score"></div><div class="comment-text"><p>I have GUI based application, and after wireshark installation that application does launch (GUI can't open). This time I found an error: org.springframework.osgi.extender.internal.activator.ContextLoaderListener - No application context created for bundle</p><p>But strange thing is that problem occurs only when I have Master and UAS two different server configuration and wireshark is installed on master server. When I have only one server (UAS) environment, then all application works fine.</p></div><div id="comment-22348-info" class="comment-info"><span class="comment-age">(26 Jun '13, 01:55)</span> <span class="comment-user userinfo">KumarM</span></div></div><span id="22353"></span><div id="comment-22353" class="comment not_top_scorer"><div id="post-22353-score" class="comment-score"></div><div class="comment-text"><p>is there a stack trace for your application?</p></div><div id="comment-22353-info" class="comment-info"><span class="comment-age">(26 Jun '13, 04:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22321" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-22321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

