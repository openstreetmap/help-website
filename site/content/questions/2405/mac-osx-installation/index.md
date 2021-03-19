+++
type = "question"
title = "MAC OSX Installation"
description = '''Ok, I&#x27;ve used the MAC OSX 64 bit installer for the latest version of Wireshark, copied the command line folder and dragged the ChmodBFP to StartupItems alias. My installation doesn&#x27;t seem to have a /dev folder, and I&#x27;m struggling to find where the &#x27;BPF&#x27; devices live !'''
date = "2011-02-17T09:47:00Z"
lastmod = "2011-03-01T04:59:00Z"
weight = 2405
keywords = [ "osx", "mac", "install", "bpf" ]
aliases = [ "/questions/2405" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAC OSX Installation](/questions/2405/mac-osx-installation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2405-score" class="post-score" title="current number of votes">0</div><span id="post-2405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok, I've used the MAC OSX 64 bit installer for the latest version of Wireshark, copied the command line folder and dragged the ChmodBFP to StartupItems alias. My installation doesn't seem to have a /dev folder, and I'm struggling to find where the 'BPF' devices live !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-bpf" rel="tag" title="see questions tagged &#39;bpf&#39;">bpf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '11, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/123d611fb8a1ade2ce573279aa1ae1cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim%20Arnold&#39;s gravatar image" /><p><span>Tim Arnold</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim Arnold has no accepted answers">0%</span></p></div></div><div id="comments-container-2405" class="comments-container"></div><div id="comment-tools-2405" class="comment-tools"></div><div class="clear"></div><div id="comment-2405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2407"></span>

<div id="answer-container-2407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2407-score" class="post-score" title="current number of votes">1</div><span id="post-2407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What's the question you're asking? "Why isn't it letting me start a capture even though I've installed the ChmodBPF startup item?", or "where are the BPF devices?"</p><p>The answer to the first question is "because, unfortunately, dragging ChmodBPF to StartupItems isn't good enough." You also need to open up a Terminal window (in an admin account) and do</p><pre><code>sudo chown -R root:wheel /Library/StartupItems/ChmodBPF</code></pre><p>and, once you've done that, you also have to do</p><pre><code>sudo SystemStarter start ChmodBPF</code></pre><p>to force that startup item to be run now, rather than only after a reboot. Once that's done, you shouldn't need to do those again.</p><p>The answer to the second question is "they live in the /dev directory". Mac OS X is UN*X - and, starting with Leopard, it's UNIX(R) - so it has "directories", not "folders", at the lowest level; a "folder" is what a directory looks like from higher levels in the OS, such as the Finder. The Finder won't show you /dev, but the UNIX command line will - in Terminal, do, for example, "ls /bpf".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '11, 21:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2407" class="comments-container"><span id="2419"></span><div id="comment-2419" class="comment"><div id="post-2419-score" class="comment-score"></div><div class="comment-text"><p>Guy, many thanks, done all that, but devices still not showing in the GUI. Do I need to edit the ChmodBPF file to recongine my 'admin group'? The file has this in (as the defaukt'</p><p>chgrp admin /dev/bpf <em>chmod g+rw /dev/bpf</em></p></div><div id="comment-2419-info" class="comment-info"><span class="comment-age">(18 Feb '11, 13:09)</span> <span class="comment-user userinfo">Tim Arnold</span></div></div><span id="2423"></span><div id="comment-2423" class="comment"><div id="post-2423-score" class="comment-score"></div><div class="comment-text"><p>Devices won't ever show in the GUI - as I said, "The Finder won't show you /dev". Or by "the GUI" do you mean the drop-down list in the Capture Options window in the Wireshark GUI?</p><p>What do you mean by "my 'admin group'"? Users who have "Allow user to administer this computer" are in the system's "admin" group, and the ChmodBPF script will, by default, make the BPF devices usable by anybody in that group, so they can capture network traffic with tcpdump or *shark or dumpcap or....</p></div><div id="comment-2423-info" class="comment-info"><span class="comment-age">(19 Feb '11, 01:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="2595"></span><div id="comment-2595" class="comment"><div id="post-2595-score" class="comment-score"></div><div class="comment-text"><p>You can open any directory in the GUI if you choose go to location from the menu and type it in. You just can't browse to there.</p></div><div id="comment-2595-info" class="comment-info"><span class="comment-age">(01 Mar '11, 01:33)</span> <span class="comment-user userinfo">Mark Baker</span></div></div><span id="2601"></span><div id="comment-2601" class="comment"><div id="post-2601-score" class="comment-score"></div><div class="comment-text"><p>You can open <em>almost</em> every directory in the GUI; /dev is not one of the ones you can open (try it with Go To Folder - the Finder informs you that "The folder can't be found").</p></div><div id="comment-2601-info" class="comment-info"><span class="comment-age">(01 Mar '11, 04:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-2407" class="comment-tools"></div><div class="clear"></div><div id="comment-2407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

