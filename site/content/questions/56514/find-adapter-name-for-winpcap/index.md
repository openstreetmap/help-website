+++
type = "question"
title = "Find Adapter Name for WinPCAP"
description = '''I have WinPCAP running on a number of machines. I have a couple other devices running Wireshark. I have remote capture working. This is being done so I don&#x27;t increase too much load on the remote servers being monitored.  The problem is there is no way to save remote ports in Wireshark so I have to c...'''
date = "2016-10-19T14:14:00Z"
lastmod = "2016-10-19T16:34:00Z"
weight = 56514
keywords = [ "remote-capture", "rpcap", "winpcap" ]
aliases = [ "/questions/56514" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find Adapter Name for WinPCAP](/questions/56514/find-adapter-name-for-winpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56514-score" class="post-score" title="current number of votes">0</div><span id="post-56514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have WinPCAP running on a number of machines. I have a couple other devices running Wireshark. I have remote capture working. This is being done so I don't increase too much load on the remote servers being monitored.</p><p>The problem is there is no way to save remote ports in Wireshark so I have to create them each time.</p><p>There is a way to use a command line to start Wireshark and map a remote port:</p><p>wireshark -i <span>rpcap://hostname:2002/adaptername</span></p><p>From <a href="https://www.winpcap.org/docs/docs_40_2/html/group__remote.html">https://www.winpcap.org/docs/docs_40_2/html/group__remote.html</a></p><p>What do I use for <strong>adaptername</strong>? In Linux it is something like eth0 but I must be missing something as I don't know of the Windows equivalent. Anyone know what that is? It is my hope to write a batch file and call the three to five remote adapters even if it means opening multiple Wireshark windows.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-remote-capture" rel="tag" title="see questions tagged &#39;remote-capture&#39;">remote-capture</span> <span class="post-tag tag-link-rpcap" rel="tag" title="see questions tagged &#39;rpcap&#39;">rpcap</span> <span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '16, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/31da63849ac266b00a80719462331c72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jollyrgr&#39;s gravatar image" /><p><span>Jollyrgr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jollyrgr has no accepted answers">0%</span></p></div></div><div id="comments-container-56514" class="comments-container"></div><div id="comment-tools-56514" class="comment-tools"></div><div class="clear"></div><div id="comment-56514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56520"></span>

<div id="answer-container-56520" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56520-score" class="post-score" title="current number of votes">0</div><span id="post-56520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Windows equivalent is, in Windows 2000 and later, an ugly string including a GUID. There's no name that, like eth0, is likely to be the default interface.</p><p>And, unfortunately, there's no command-line way in Wireshark to say "give me a list of all the interfaces on a remote machine", so there really isn't a good way to find the name of the interface without running a command on the remote machine or starting up the Wireshark GUI and getting a list of the remote interfaces from the GUI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '16, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-56520" class="comments-container"></div><div id="comment-tools-56520" class="comment-tools"></div><div class="clear"></div><div id="comment-56520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

