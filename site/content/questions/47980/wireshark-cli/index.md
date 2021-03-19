+++
type = "question"
title = "Wireshark CLI"
description = '''I see documentation for using the CLI commands for Wireshark, yet when I installed Wireshark on my Windows system, I get an error message when trying to call the &quot;wireshark&quot; command. &quot;wireshark is not a recognized command&quot;. What do I need to get this working? My end goal is to automatically start a ...'''
date = "2015-11-25T08:56:00Z"
lastmod = "2015-11-25T11:20:00Z"
weight = 47980
keywords = [ "cli", "command-line" ]
aliases = [ "/questions/47980" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark CLI](/questions/47980/wireshark-cli)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47980-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I see documentation for using the CLI commands for Wireshark, yet when I installed Wireshark on my Windows system, I get an error message when trying to call the "wireshark" command. "wireshark is not a recognized command". What do I need to get this working?</p><p>My end goal is to automatically start a capture and have it run only for a set time. In order for me to start a capture automatically, I believe I must use the CLI. Unfortunately, upon completion of the Wireshark 2.0 installation, the command "wireshark" in CMD is not recognized. I am unable to find documentation about this particular error anywhere. Is this something I can only do on a Linux based system?</p><p>What is the best approach for my end goal?</p></div><div id="question-tags" class="tags-container tags">cli command-line</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/1d21a47e935f5c18bd559d53bcdb1236?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikej&#39;s gravatar image" /><p>mikej<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikej has no accepted answers">0%</span></p></div></div><div id="comments-container-47980" class="comments-container"></div><div id="comment-tools-47980" class="comment-tools"></div><div class="clear"></div><div id="comment-47980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47981"></span>

<div id="answer-container-47981" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47981-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You would need to navigate in the CLI to the path where wireshark.exe is located. For instance on my machine at a command prompt, I typed the following "cd c:\Program files\Wireshark" and then launched wireshark.exe from there. Alternatively you can add "c:\Program files\Wireshark" to the Windows System Path environment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/cdf00a4782de9ff30ec2a5f7ab369ea0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jimbo&#39;s gravatar image" /><p>Jimbo<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jimbo has one accepted answer">100%</span></p></div></div><div id="comments-container-47981" class="comments-container"><span id="47983"></span><div id="comment-47983" class="comment"><div id="post-47983-score" class="comment-score"></div><div class="comment-text"><p>I appreciate your input, though it doesn't solve my problem. Wireshark does not have a means to automatically begin a packet capture once opened. The CLI version of Wireshark can be used in conjunction with Windows task scheduler for exactly what I need. I can have a task that is designed to run the Wireshark CLI and also stop the capture. The GUI Wireshark will not work for this according to what I have seen in the options menus.</p></div><div id="comment-47983-info" class="comment-info"><span class="comment-age">(25 Nov '15, 10:02)</span> mikej</div></div><span id="47984"></span><div id="comment-47984" class="comment"><div id="post-47984-score" class="comment-score">2</div><div class="comment-text"><p>Wireshark.exe is the GUI application, generally controlled by clicking on the GUI.</p><p>Parameters can be passed on the command line to initiate a capture i.e. <code>-i xxx</code> where xxx is the interface number determined by using <code>Wireshark.exe -D</code> and further parameters cna set filters and stop conditions, i.e. <code>-c &lt;packet count&gt;</code> and <code>-a &lt;autostop cond.&gt;</code> where the condition is a duration or a file size.</p><p>However, tshark <strong>is</strong> the command line version of Wireshark. It uses exactly the same capture and dissection engine, but it's output is built for using from the command line.</p><p>Please read the help pages for the applications in the Wireshark suite that can be found <a href="https://www.wireshark.org/docs/man-pages/">here</a>, and in your local install directory. The help file (userguide.chm) in the same directory has Appendix D. with much the same info.</p></div><div id="comment-47984-info" class="comment-info"><span class="comment-age">(25 Nov '15, 10:25)</span> grahamb ♦</div></div><span id="47988"></span><div id="comment-47988" class="comment"><div id="post-47988-score" class="comment-score"></div><div class="comment-text"><p>That did it. That is what I was looking for. Everywhere I looked said to use "wireshark", not "wireshark.exe" while in the Wireshark directory.</p></div><div id="comment-47988-info" class="comment-info"><span class="comment-age">(25 Nov '15, 11:13)</span> mikej</div></div><span id="47990"></span><div id="comment-47990" class="comment"><div id="post-47990-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Everywhere I looked said to use "wireshark", not "wireshark.exe" while in the Wireshark directory.</p></blockquote><p>That's a little surprising, as I think the Windows shell <em>should</em> treat a command of "{XXX}.exe" and just "{XXX}" the same, as executables on Windows should all have names ending with ".exe", but perhaps sometimes you have to give the full name.</p></div><div id="comment-47990-info" class="comment-info"><span class="comment-age">(25 Nov '15, 11:21)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-47981" class="comment-tools"></div><div class="clear"></div><div id="comment-47981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47989"></span>

<div id="answer-container-47989" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47989-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Unfortunately, upon completion of the Wireshark 2.0 installation, the command "wireshark" in CMD is not recognized. I am unable to find documentation about this particular error anywhere.</p></blockquote><p>I presume Microsoft felt it didn't need documentation, but what it means is that it didn't find a .exe file anywhere in your path setting (the PATH environment variable) whose name was "{XXX}.exe", where "{XXX}" is the command name you typed.</p><p>This is similar to the "command not found" error from the bash shell, or the "not found" error from the Korn shell, or the "Command not found." error from [t]csh, on UN*X (or on Windows with Cygwin).</p><blockquote><p>My end goal is to automatically start a capture and have it run only for a set time.</p></blockquote><p>Do you want to have the Wireshark <em>GUI</em> start automatically and run only for a set time? If so, then, as Graham said, you need to make sure that <code>c:\Program files\Wireshark</code> is in your Windows System Path, and then need to run the "wireshark" command, with the appropriate command line arguments. However, you'd need to have that command run automatically, somehow.</p><p>Or do you want to have some capture running in the background? If so, then, if you just want to save the capture to a file that you'd later read with Wireshark (or some other tool capable of reading pcap or pcapng files), you probably just want to use the "dumpcap" command (which is the command that Wireshark and TShark run in order to do traffic capture). If you want to run the capture in the background but write out <em>dissected packets</em> as text to a file, you'd use TShark (the command for which is <code>tshark</code>), with the <code>-V</code> option if you want output like what appears in Wireshark's packet detail pane rather than what appears in its packet summary pane.</p><p>The command line options to control capturing are similar in dumpcap, Wireshark, and TShark.</p><blockquote><p>Is this something I can only do on a Linux based system?</p></blockquote><p>No. As indicated, it works on Windows if you have the installation directory for Wireshark in your path. It also works on UNIX-like systems other than Linux (OS X, Solaris, *BSD, HP-UX, AIX, etc.), as long as the commands are in a directory that's in your path.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '15, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-47989" class="comments-container"><span id="47991"></span><div id="comment-47991" class="comment"><div id="post-47991-score" class="comment-score"></div><div class="comment-text"><p>Having the command on the system path isn't the only way, you can also pass the full path wherever Wireshark.exe is referenced.</p></div><div id="comment-47991-info" class="comment-info"><span class="comment-age">(25 Nov '15, 11:44)</span> grahamb ♦</div></div></div><div id="comment-tools-47989" class="comment-tools"></div><div class="clear"></div><div id="comment-47989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

