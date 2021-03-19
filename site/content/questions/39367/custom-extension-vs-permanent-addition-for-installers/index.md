+++
type = "question"
title = "Custom Extension vs. Permanent Addition for Installers"
description = '''I recently just got a custom plugin working on my Windows build of Wireshark by adding it as a custom extension. However, I now want to be able to give the installer to other people so they can use this version of Wireshark. Is this possible with a custom extension, or does it have to be a permanent...'''
date = "2015-01-23T10:30:00Z"
lastmod = "2015-01-23T10:58:00Z"
weight = 39367
keywords = [ "windows", "installer", "custom", "extension", "plugin" ]
aliases = [ "/questions/39367" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Extension vs. Permanent Addition for Installers](/questions/39367/custom-extension-vs-permanent-addition-for-installers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39367-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently just got a custom plugin working on my Windows build of Wireshark by adding it as a custom extension. However, I now want to be able to give the installer to other people so they can use this version of Wireshark. Is this possible with a custom extension, or does it have to be a permanent addition?</p><p>In the README.plugins file, it says "The custom extension is easy to configure, but won't be used for inclusion in the distribution." This makes me think I can't use it for giving it to others. But, in the 3.1 section it talks about how to "add the plugin to your own Windows installer". What does it mean, "your own" installer? Can I not send this installer to other people?</p><p>Is there any way for me to give this version of Wireshark to other people without going in and making it a permanent addition?</p></div><div id="question-tags" class="tags-container tags">windows installer custom extension plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '15, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/8151306827aa578935b52f99a49cbde2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mehubb985&#39;s gravatar image" /><p>mehubb985<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mehubb985 has no accepted answers">0%</span></p></div></div><div id="comments-container-39367" class="comments-container"></div><div id="comment-tools-39367" class="comment-tools"></div><div class="clear"></div><div id="comment-39367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39368"></span>

<div id="answer-container-39368" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39368-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's quite easy to add your plugin dissector to the Windows installer, actually. Simply edit the <code>wireshark/packaging/nsis/Custom_plugins.txt</code> (or add your plugin to <code>wireshark/packaging/nsis/wireshark.nsi</code> anywhere it mentions <code>gryphon</code>).</p><p>Then, when you run <code>nmake -f Makefile.nmake packaging</code>, your plugin will be included in the installer that gets created.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '15, 10:58</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-39368" class="comments-container"><span id="39370"></span><div id="comment-39370" class="comment"><div id="post-39370-score" class="comment-score"></div><div class="comment-text"><p>I already did add 'File "....\plugins\foo\foo.dll"' to my custom-plugins.txt, like it said in the instructions (with foo replaced with my plugin name, obviously). It still doesn't seem to be added into the installer when I create it. I also added the same .dll file's path to the CUSTOM_PLUGINS part of my packaging/nsis/Custom.nmake, like it says in the instructions. Should that not work?</p></div><div id="comment-39370-info" class="comment-info"><span class="comment-age">(23 Jan '15, 11:29)</span> mehubb985</div></div><span id="39371"></span><div id="comment-39371" class="comment"><div id="post-39371-score" class="comment-score"></div><div class="comment-text"><p>I believe that should work. However, as I noted in my answer, you can also edit the <code>wireshark.nsi</code> file and add in your plugin there without having to worry about the <code>custom*</code> files. I know for certain that doing this will include your plugin in the installer.</p></div><div id="comment-39371-info" class="comment-info"><span class="comment-age">(23 Jan '15, 11:34)</span> multipleinte...</div></div></div><div id="comment-tools-39368" class="comment-tools"></div><div class="clear"></div><div id="comment-39368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

