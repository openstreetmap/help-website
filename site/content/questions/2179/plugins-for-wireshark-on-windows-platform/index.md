+++
type = "question"
title = "Plugins for Wireshark on Windows platform"
description = '''I have created plugin in ubuntu. It works fine. But as per the requirements, I have been asked to create a windows installation of wireshark. In windows, under the plugins directory, there is a list of DLL&#x27;s. So is it possible that I can convert my plugin written for ubuntu platform into a DLL that ...'''
date = "2011-02-06T21:41:00Z"
lastmod = "2011-02-08T03:31:00Z"
weight = 2179
keywords = [ "plugins", "wireshark" ]
aliases = [ "/questions/2179" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Plugins for Wireshark on Windows platform](/questions/2179/plugins-for-wireshark-on-windows-platform)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2179-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have created plugin in ubuntu. It works fine. But as per the requirements, I have been asked to create a windows installation of wireshark. In windows, under the plugins directory, there is a list of DLL's. So is it possible that I can convert my plugin written for ubuntu platform into a DLL that I can use in windows directly without having to recompile wireshark on windows again and again.</p><p>If yes, how do create a DLL?</p><p>Thanks in advance,</p><p>Sid</p></div><div id="question-tags" class="tags-container tags">plugins wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Feb '11, 21:41</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2179" class="comments-container"></div><div id="comment-tools-2179" class="comment-tools"></div><div class="clear"></div><div id="comment-2179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2188"></span>

<div id="answer-container-2188" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2188-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is indeed possible.</p><p>First setup your Windows development environment as per <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Developers Guide</a> and compile Wireshark once.</p><p>As per <a href="http://anonsvn.wireshark.org/wireshark/trunk-1.4/doc/README.plugins">README.plugins</a> add a directory of your new dissector plugin and setup the build files. Then you can compile your plugin over and over again, if needed, without recompiling Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Feb '11, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2188" class="comments-container"><span id="2212"></span><div id="comment-2212" class="comment"><div id="post-2212-score" class="comment-score"></div><div class="comment-text"><p>jaap,</p><p>I dont exactly get the method. When I created the plugin in ubuntu, I followed all the steps in README.plugins. Now I want to create a DLL for my plugin, ie 'nnm' so that I can use it in Windows. And since DLL's are dynamically loaded, I would not have to recompile wireshark over and over again, is that right??</p><p>So exactly what do I have to do??</p><p>I am really stuck here. Please help..</p><p>Thanks in advance,</p><p>sid</p></div><div id="comment-2212-info" class="comment-info"><span class="comment-age">(07 Feb '11, 20:32)</span> sid</div></div><span id="2215"></span><div id="comment-2215" class="comment"><div id="post-2215-score" class="comment-score"></div><div class="comment-text"><p>Read my answer carefully: "...and compile Wireshark once." So no, there's no need to compile it over and over again. You'll need to do it once to setup your build environment for the plugin compilation.</p><p>Then "As per README.plugins add a directory of your new dissector plugin and setup the build files". This now amends your Wireshark build for your plugin build which you can do right there in that directory.</p></div><div id="comment-2215-info" class="comment-info"><span class="comment-age">(07 Feb '11, 22:50)</span> Jaap ♦</div></div></div><div id="comment-tools-2188" class="comment-tools"></div><div class="clear"></div><div id="comment-2188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2224"></span>

<div id="answer-container-2224" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2224-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>jaap,</p><p>while compiling wireshark, I am getting this error everytime. Can you please help me out with that??</p><p>**if not exist wireshark-gtk2diameter mkdir wireshark-gtk2diameter</p><p>xcopy ".diameter*.dtd" wireshark-gtk2diameter</p><p>File not found - *.dtd</p><p>0 File(s) copied</p><p>NMAKE : Fatal error U1077: 'C:WindowsSystem32xcopy.EXE' : return code '0x4' stop**</p><p>please help??</p><p>thanks a lot..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '11, 02:17</p></div></div><div id="comments-container-2224" class="comments-container"></div><div id="comment-tools-2224" class="comment-tools"></div><div class="clear"></div><div id="comment-2224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2226"></span>

<div id="answer-container-2226" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2226-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>jaap,</p><p>Please help me one last time. I will try and explain to you my situation precisely.</p><p>I had a wireshark SVN version which had a plugin for nnm protocol running on ubuntu. I took that source into windows. I build the environment in windows to compile wireshark. And thereafter I compiled wireshark on windows. Now with that wireshark built, I can run wireshark and be able to dissect nnm packets successfully.</p><p>However, in the wireshark/plugins folder I have directories for all protocols. Not DLL's.</p><p>Now I installed a wireshark 1.4.3 application on windows. In the wireshark/plugins folder, there are DLL's for all the plugins that are available.</p><p>So when I take my nnm directory from the previous SVN built and put it in the new 1.4.3 plugins directory (as a folder) and try to dissect nnm packets, it fails.</p><p>What should I do inorder to make sure that wireshark 1.4.3 is able to dissect nnm packets??</p><p>Please guide me through this. Your help has been immense. This is probably the last straw.</p><p>Thanks,</p><p>Sid</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '11, 03:31</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2226" class="comments-container"></div><div id="comment-tools-2226" class="comment-tools"></div><div class="clear"></div><div id="comment-2226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

