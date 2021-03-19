+++
type = "question"
title = "Wireshark crashes on startup on MacOS Yosemite"
description = '''Hi, I just installed Wireshark 1.12.4 on my MacBook Pro, went to start it and it immediately crashed. From the crash report, I see the following report about missing files: Dyld Error Message:  Library not loaded: /usr/X11/lib/libcairo.2.dylib  Referenced from: /Applications/Wireshark.app/Contents/R...'''
date = "2015-04-06T10:08:00Z"
lastmod = "2015-04-10T14:37:00Z"
weight = 41225
keywords = [ "macosx", "wireshark" ]
aliases = [ "/questions/41225" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes on startup on MacOS Yosemite](/questions/41225/wireshark-crashes-on-startup-on-macos-yosemite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41225-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I just installed Wireshark 1.12.4 on my MacBook Pro, went to start it and it immediately crashed. From the crash report, I see the following report about missing files:</p><p>Dyld Error Message: Library not loaded: /usr/X11/lib/libcairo.2.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Reason: image not found</p><p>I have XQuartz installed and there is no /usr/X11 directory even though all of the X11 parts and pieces work fine. So, is 1.12.4 the wrong version of Wireshark for my machine, or is there a different X11 package that I should install instead of XQuartz?</p><p>Thanks, Rob</p></div><div id="question-tags" class="tags-container tags">macosx wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '15, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/dc0c6f4c3adac90b43426fea1fdd3af4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="caspersgrin&#39;s gravatar image" /><p>caspersgrin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="caspersgrin has no accepted answers">0%</span></p></div></div><div id="comments-container-41225" class="comments-container"><span id="41325"></span><div id="comment-41325" class="comment"><div id="post-41325-score" class="comment-score"></div><div class="comment-text"><p>The September and October entries have the issue identified. I didn't pay attention at first because of the poster's spelling. The solution is also silly. Why uninstall two packages and reinstall them just to get a sym link?</p><p>I had the crash problem as well but my directory structure is different from what was posted: usr/X11R6 1 (A completely different name for the X11 directory.) opt/X11 Both exist on the machine.</p><p>Relevant parts of the report: OS Version: Mac OS X 10.10.2 (14C1514) Application Specific Information: dyld: launch, loading dependent libraries</p><p>Dyld Error Message: Library not loaded: /usr/X11/lib/libcairo.2.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin Reason: image not found</p><p>However, libcairo.2.dylib exists at usr/X11/lib/</p><p>I suppose my problem is I can't understand what my crashlog is kindly telling me. I think X Quartz is telling us that the X11 folder is really the X11R6 1 folder that doesn't have the necessary files in it. Creating the symbolic link cured the issue: sudo ln -s /opt/X11 /usr/X11</p></div><div id="comment-41325-info" class="comment-info"><span class="comment-age">(09 Apr '15, 07:58)</span> bob_calder</div></div></div><div id="comment-tools-41225" class="comment-tools"></div><div class="clear"></div><div id="comment-41225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41362"></span>

<div id="answer-container-41362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41362-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have XQuartz installed and there is no /usr/X11</p></blockquote><p>There shouldn't be.</p><p>What there should be is a <code>/opt/X11</code> directory, and a <code>/usr/X11</code> <em>symbolic link</em> to it.</p><pre><code>$ ls -ld /opt/X11
drwxr-xr-x  8 root  wheel  272 Aug 11  2014 /opt/X11
$ ls -ld /usr/X11
lrwxr-xr-x  1 root  wheel  8 Oct 17 12:50 /usr/X11 -&gt; /opt/X11</code></pre><p>So you need to, as bob_calder notes, do <code>sudo ln -s /opt/X11 /usr/X11</code>.</p><p>In response to his comments:</p><p>There should, in addition to the <code>/usr/X11</code> symbolic link, be a <code>/usr/X11R6</code> symbolic link.</p><pre><code>$ ls -ld /usr/X11R6
lrwxr-xr-x  1 root  wheel  8 Oct 17 12:50 /usr/X11R6 -&gt; /opt/X11</code></pre><p>(all three commands run, for what it's worth, on a Yosemite (virtual) machine). So <em>both</em> symbolic links should exist.</p><p>I'm not sure what "X11R6 1" is, here. Is it a folder whose name is "X11R6", followed by a space, followed by "1", or is it a folder whose name is "X11R6.1"? And is it truly a folder, or just a symbolic link? What does <code>ls -ld /usr/X11*</code> print?</p><p>The XQuartz installer will install XQuartz under <code>/opt/X11</code>, and should make the two symbolic links - <code>/usr/X11</code> and <code>/usr/X11R6</code> - point to <code>/opt/X11</code>.</p><p>The <em>Yosemite</em> installer, when used to upgrade from an earlier OS X release to Yosemite, will, unfortunately, <em>remove</em> the <code>/usr/X11</code> symbolic link and not put it back; I don't know whether it'll also remove the <code>/usr/X11R6</code> symbolic link.</p><p>What the crashing is telling you is that you need to do <code>sudo ln -s /opt/X11 /usr/X11</code>. XQuartz isn't telling you anything; the OS X run-time linker is telling you that it couldn't find anything in <code>/usr/X11/lib/libcairo.2.dylib</code>. If you did <code>sudo ln -s /opt/X11 /usr/X11</code>, then <code>/usr/X11</code> didn't exist before you did that, so <code>/usr/X11/lib/libcairo.2.dylib</code> didn't exist before you did that. Perhaps <code>/usr/X11R6/lib/libcairo.2.dylib</code> existed before you did that, but that's not the path being used, so it doesn't matter.</p><p>So the folder in question is neither <code>/usr/X11</code> nor <code>/usr/X11R6</code>, it's <code>/opt/X11</code>, and that folder <em>does</em> have the relevant files in it. There need to be symbolic links to <code>/opt/X11</code> to allow programs built with the old built-in X11 - which <em>did</em> exist in a <code>/usr/X11</code> folder, with <code>/usr/X11R6</code> being a symbolic link to <code>/usr/X11</code> - continue to work with XQuartz. (Building with XQuartz, in a fashion that directly looks in <code>/opt/X11</code>, would produce programs that won't work with the old built-in X11.)</p><p>I.e., the problem has nothing to do with "the X11 folder" or "the X11R6 folder" or "the X11R6 1" folder or "the X11R6.1 folder" not having the relevant files, it has something to do with <code>/usr/X11</code> not existing at all. Nothing with "X11R6" in the name enters into it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '15, 14:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41362" class="comments-container"><span id="41364"></span><div id="comment-41364" class="comment"><div id="post-41364-score" class="comment-score"></div><div class="comment-text"><p>Thanks! The "1" was separated by a space, so it's possible there was some sort of error after Yosemite update ran having to do with creating a new directory before the old one was deleted, then deleting the old one and not renaming the new one. No, it wasn't a sym link. Everything works since I created the new link, so at this point, it's just another example of Apple doing their own thing. :(</p></div><div id="comment-41364-info" class="comment-info"><span class="comment-age">(10 Apr '15, 15:32)</span> bob_calder</div></div><span id="41370"></span><div id="comment-41370" class="comment"><div id="post-41370-score" class="comment-score"></div><div class="comment-text"><p>Programs in the higher levels of OS X try to deal with duplicate file names by giving the new file (or folder) a name with a blank and a number appended to it; perhaps <code>/usr/X11R6 1</code> was created when there was already a <code>/usr/X11R6</code> (folder or symbolic link) and a program was somehow trying to set up <code>/usr/X11R6</code> and dealt with that by making <code>/usr/X11R6 1</code>.</p><p>In any case, Yosemite doesn't have its own built-in X11, so, on Yosemite with XQuartz, there should be a folder <code>/opt/X11</code> with both <code>/usr/X11</code> and <code>/usr/X11R6</code> being symbolic links to <code>/opt/X11</code>.</p></div><div id="comment-41370-info" class="comment-info"><span class="comment-age">(10 Apr '15, 20:03)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-41362" class="comment-tools"></div><div class="clear"></div><div id="comment-41362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

