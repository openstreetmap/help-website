+++
type = "question"
title = "Mac OS can&#x27;t detect any interface"
description = '''I have just installed wireshark 1.4.1 in my Mac 10.6.4 but i get the following error (-) &quot;There are no interfaces on which a capture can be done.&quot; What can i do?'''
date = "2010-10-21T13:26:00Z"
lastmod = "2011-05-07T02:36:00Z"
weight = 578
keywords = [ "macinterfacenotfound" ]
aliases = [ "/questions/578" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OS can't detect any interface](/questions/578/mac-os-cant-detect-any-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-578-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have just installed wireshark 1.4.1 in my Mac 10.6.4 but i get the following error (-) "There are no interfaces on which a capture can be done."</p><p>What can i do?</p></div><div id="question-tags" class="tags-container tags">macinterfacenotfound</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '10, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/2e066b781807f2723d487e6a344015c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="the_sniffer&#39;s gravatar image" /><p>the_sniffer<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="the_sniffer has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 May '11, 07:18</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-578" class="comments-container"><span id="7152"></span><div id="comment-7152" class="comment"><div id="post-7152-score" class="comment-score"></div><div class="comment-text"><p>When upgrading from 1.4.3 to 1.6.2 in 10.5.8 I had the same problem with dev permissions.</p><p>I noticed that ChmodBPF is different.</p><p>In 1.4.3 it issues the following commands</p><pre><code>chgrp admin /dev/bpf*
chmod g+rw /dev/bpf*</code></pre><p>In 1.6.2 it issues the following commands</p><pre><code>chgrp access_bpf /dev/bpf*
chmod g+rw /dev/bpf*</code></pre><p>The group access_bpf is not added by the Wireshark installer.</p></div><div id="comment-7152-info" class="comment-info"><span class="comment-age">(30 Oct '11, 05:09)</span> wsk</div></div><span id="7163"></span><div id="comment-7163" class="comment"><div id="post-7163-score" class="comment-score"></div><div class="comment-text"><p>It <em>is</em> added on 10.6, by using the "dseditgroup" command. What does the command "man dseditgroup" print on your 10.5.8 machine? Perhaps that command is missing, or perhaps it behaves differently in 10.5.x, so that the script's use of it works in 10.6.x but not 10.5.x.</p><p>Please file a bug on this at <a href="https://bugs.wireshark.org/">the Wireshark bugzilla</a>, and put the output of "man dseditgroup" in that bug. ask.wireshark.org is not the best place for discussion of bugs.</p></div><div id="comment-7163-info" class="comment-info"><span class="comment-age">(30 Oct '11, 13:51)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-578" class="comment-tools"></div><div class="clear"></div><div id="comment-578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

6 Answers:

</div>

</div>

<span id="2245"></span>

<div id="answer-container-2245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2245-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>This solution worked for me on OS X Leopard 10.6.6 running wireshark 1.4.3</p><ul><li>Open terminal</li><li>type 'whoami' to see your exact user name (for me that was keving)</li><li>execute the following commands (substituting your username for mine--also enter your login password when prompted, of course):</li></ul><blockquote><pre><code>cd /dev
sudo chown keving:admin bp*
ls -la | grep bp</code></pre></blockquote><p>The last command will display a list of files such as:</p><pre><code>crw-------   1 keving  admin      23,   0 Feb  9 00:52 bpf0
crw-------   1 keving  admin      23,   1 Feb  9 00:52 bpf1
crw-------   1 keving  admin      23,   2 Feb  7 10:59 bpf2
crw-------   1 keving  admin      23,   3 Feb  7 10:59 bpf3
crw-------   1 root    wheel      23,   4 Feb  9 01:03 bpf4</code></pre><p>Make sure all of them have your user name and admin as the user/group. For some reason, the last one didn't get assigned properly so I had to run the command:</p><pre><code>sudo chown keving:admin bpf4</code></pre><p>that fixed it</p><p>from there, you can type:</p><pre><code>cd /Applications
open WireShark.app</code></pre><p>And it will work.</p><p>Hope that helps someone,</p><p>-gmale</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 22:08</strong></p><img src="https://secure.gravatar.com/avatar/f0a7931509fe208105cdeec791c7ed04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmale&#39;s gravatar image" /><p>gmale<br />
<span class="score" title="90 reputation points">90</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmale has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '11, 22:12</p></div></div><div id="comments-container-2245" class="comments-container"><span id="3991"></span><div id="comment-3991" class="comment"><div id="post-3991-score" class="comment-score"></div><div class="comment-text"><p>BPF devices are created "on the fly" as needed, in groups of 4, in Mac OS X; the "chown" command (which should probably have "bpf<em>" rather than "bp</em>" as its argument) will affect only the BPF devices that currently exist; if all the BPF devices are currently open, the next program that tries to open one will provoke 4 more to be created, and they'll have permissions rw------- and be owned by root:wheel.</p><p>Perhaps someday OS X will switch to using a cloning BPF device.</p></div><div id="comment-3991-info" class="comment-info"><span class="comment-age">(07 May '11, 10:28)</span> Guy Harris ♦♦</div></div><span id="21090"></span><div id="comment-21090" class="comment"><div id="post-21090-score" class="comment-score"></div><div class="comment-text"><p>gmale, Perfect! Helped me: thank you :)</p><p>By the way, I did this with Wireshark running, and the fix worked in place.</p></div><div id="comment-21090-info" class="comment-info"><span class="comment-age">(10 May '13, 17:50)</span> Raymond Naseef</div></div></div><div id="comment-tools-2245" class="comment-tools"></div><div class="clear"></div><div id="comment-2245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3986"></span>

<div id="answer-container-3986" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3986-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>From <a href="http://ask.wireshark.org/questions/2829/capturing-with-wireshark-on-mac-os-1066">http://ask.wireshark.org/questions/2829/capturing-with-wireshark-on-mac-os-1066</a>:</p><ol><li><p>Download Wireshark 64 bit version launch WireShark .dmg file. a new Finder window opens. Leave it.</p></li><li><p>Open a terminal window. Issuing this command to verify that the dmg is loaded in the usual spot: "ls /Volumes/Wireshark/Utilities/" If u see the list of files then it's loaded properly.<br />
</p></li><li><p>Copy the ChmodBPF file : "sudo cp -R /Volumes/Wireshark/Utilities/ChmodBPF/ /Library/StartupItems"</p></li><li><p>sudo chown -R root:wheel /Library/StartupItems/ChmodBPF</p></li><li><p>sudo SystemStarter start ChmodBPF</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '11, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span> </br></p></div></div><div id="comments-container-3986" class="comments-container"></div><div id="comment-tools-3986" class="comment-tools"></div><div class="clear"></div><div id="comment-3986-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="583"></span>

<div id="answer-container-583" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-583-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you experience the common problem that your Wireshark does not have the necessary rights to access the network card for data capture. Maybe this Wiki page will help:</p><p>http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '10, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-583" class="comments-container"><span id="587"></span><div id="comment-587" class="comment"><div id="post-587-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper...</p><p>But i tried to understand the Mac OS part but it didnt pin to a solution that really helped. I did more diging and i tried some steps from youtube: http://www.youtube.com/watch?v=Tgm4n6zVDAY but all the mentioned steps didnt help :(</p></div><div id="comment-587-info" class="comment-info"><span class="comment-age">(22 Oct '10, 08:37)</span> the_sniffer</div></div><span id="588"></span><div id="comment-588" class="comment"><div id="post-588-score" class="comment-score"></div><div class="comment-text"><p>Hi, sorry, but I have no Mac skills whatsoever and I have no Mac around to try things out, otherwise I would try to get you a step by step solution. Maybe some other Mac hero can help you here?</p></div><div id="comment-588-info" class="comment-info"><span class="comment-age">(22 Oct '10, 09:01)</span> Jasper ♦♦</div></div><span id="589"></span><div id="comment-589" class="comment"><div id="post-589-score" class="comment-score"></div><div class="comment-text"><p>No mac user here, but may be you can find useful information in <a href="http://www.wireshark.org/lists/wireshark-users/201008/msg00024.html">this thread</a> or <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4909">bug 4909</a></p></div><div id="comment-589-info" class="comment-info"><span class="comment-age">(22 Oct '10, 11:40)</span> joke</div></div></div><div id="comment-tools-583" class="comment-tools"></div><div class="clear"></div><div id="comment-583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3975"></span>

<div id="answer-container-3975" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3975-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Another option is to run WireShark as su:</p><pre><code>sudo /opt/local/bin/wireshark</code></pre><p>This is not recommended - for security reasons - but at least you can quickly test if the installation works. In this example, WireShark was installed using MacPorts, hence the unusual path.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '11, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/a529c59f8c5ca62974e56c85865f8464?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="perqa&#39;s gravatar image" /><p>perqa<br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="perqa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 May '11, 01:30</p></div></div><div id="comments-container-3975" class="comments-container"></div><div id="comment-tools-3975" class="comment-tools"></div><div class="clear"></div><div id="comment-3975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="590"></span>

<div id="answer-container-590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-590-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Modify the shortcut / menu item to run "gksudo wireshark" or "kdesudo". This should then prompt you for the root password and enable you to access the interfaces with sufficient rights.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '10, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/1d8eda08758411bec29092a0b8220126?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter&#39;s gravatar image" /><p>Peter<br />
<span class="score" title="65 reputation points">65</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter has no accepted answers">0%</span></p></div></div><div id="comments-container-590" class="comments-container"><span id="899"></span><div id="comment-899" class="comment"><div id="post-899-score" class="comment-score"></div><div class="comment-text"><p>That's not the way to proceed, because: 1. It's a Mac, no a GNOME or KDE based desktop environment. 2. You should not run Wireshark with root privileges, see https://blog.wireshark.org/2010/02/running-wireshark-as-you/</p></div><div id="comment-899-info" class="comment-info"><span class="comment-age">(10 Nov '10, 10:28)</span> Jaap ♦</div></div></div><div id="comment-tools-590" class="comment-tools"></div><div class="clear"></div><div id="comment-590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="895"></span>

<div id="answer-container-895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-895-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had the same problem last night. The answer is to run from the terminal. Assuming the Wireshark application is in your Applications folder, it goes something like this: sudo /Applications/Wireshark.app/Contents/MacOS//Wireshark</p><p>As was eluded to in other messages, the issue seems to be about permissions. There my be a more responsible method rather than running as root, but I don't know it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '10, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/21bf7d5ef5e333cdfd85ef2f22486145?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbarnick&#39;s gravatar image" /><p>mbarnick<br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbarnick has no accepted answers">0%</span></p></div></div><div id="comments-container-895" class="comments-container"><span id="3990"></span><div id="comment-3990" class="comment"><div id="post-3990-score" class="comment-score"></div><div class="comment-text"><p>See Jaap Keuter's reply to the person who suggested using "gksudo" or "kdesudo" - you do <em>NOT</em> want to run million-lines-of-code applications such as Wireshark or TShark as root.</p></div><div id="comment-3990-info" class="comment-info"><span class="comment-age">(07 May '11, 10:25)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-895" class="comment-tools"></div><div class="clear"></div><div id="comment-895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

