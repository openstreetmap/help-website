+++
type = "question"
title = "Build a Plugin on Linux"
description = '''Hello community, I successfully developed two Dissectors for my companies own network protocols. They are compiling without problems on Windows. But now I have to build them for Linux, too. I have no idea how to do this. On Windows I just go into the plugin folder and run &quot;nmake Makefile.nmake&quot;, on ...'''
date = "2015-06-05T03:48:00Z"
lastmod = "2015-06-05T04:15:00Z"
weight = 42914
keywords = [ "development", "building", "make", "linux", "plugin" ]
aliases = [ "/questions/42914" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Build a Plugin on Linux](/questions/42914/build-a-plugin-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42914-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello community,</p><p>I successfully developed two Dissectors for my companies own network protocols. They are compiling without problems on Windows. But now I have to build them for Linux, too. I have no idea how to do this.</p><p>On Windows I just go into the plugin folder and run "nmake Makefile.nmake", on Linux I found a Makefile in the ethercat folder, but how do I generate a Makefile for my plugin. Do I have to write my own? Is there maybe a README for this.</p><p>Thankfully lal12</p></div><div id="question-tags" class="tags-container tags">development building make linux plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '15, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/cc56ba9bd225bd68cea09a404ecc0b6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lal12&#39;s gravatar image" /><p>lal12<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lal12 has 2 accepted answers">33%</span></p></div></div><div id="comments-container-42914" class="comments-container"></div><div id="comment-tools-42914" class="comment-tools"></div><div class="clear"></div><div id="comment-42914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42917"></span>

<div id="answer-container-42917" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42917-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes doc/README.plugins</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '15, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-42917" class="comments-container"><span id="42921"></span><div id="comment-42921" class="comment"><div id="post-42921-score" class="comment-score"></div><div class="comment-text"><p>Yes, I looked into README.plugins, but there was no information about how to create the Makefile, it is just mentioned there, that I have to add it to the AC_OUTPUT in configure.ac (Section 3.2.4)</p></div><div id="comment-42921-info" class="comment-info"><span class="comment-age">(05 Jun '15, 04:35)</span> lal12</div></div><span id="42928"></span><div id="comment-42928" class="comment"><div id="post-42928-score" class="comment-score">1</div><div class="comment-text"><p>The Makefile is just copied, see section 2. of README.plugins.</p><p>Section 3. of README.plugins for the changes to core Wireshark files to integrate your plugin.</p><p>You have two build options on Linux, using Autotools or using CMake. If using Autotools you'll need to do the autogen.sh and configure steps again after modifying the files.</p></div><div id="comment-42928-info" class="comment-info"><span class="comment-age">(05 Jun '15, 05:53)</span> grahamb ♦</div></div><span id="43370"></span><div id="comment-43370" class="comment"><div id="post-43370-score" class="comment-score"></div><div class="comment-text"><p>I did several changes, don't know which one helped, but now the build seems to work. But there is no foo.so file in my plugin/foo folder. Just a foo.la, I assume it has to be linked, but how can I archieve this.</p></div><div id="comment-43370-info" class="comment-info"><span class="comment-age">(19 Jun '15, 07:53)</span> lal12</div></div><span id="43373"></span><div id="comment-43373" class="comment"><div id="post-43373-score" class="comment-score">2</div><div class="comment-text"><p>the .so file is located in the hidden .libs subfolder of your plugin folder.</p></div><div id="comment-43373-info" class="comment-info"><span class="comment-age">(19 Jun '15, 08:33)</span> Pascal Quantin</div></div><span id="43434"></span><div id="comment-43434" class="comment"><div id="post-43434-score" class="comment-score"></div><div class="comment-text"><p>Thank You. Maybe it should be added do the README?</p></div><div id="comment-43434-info" class="comment-info"><span class="comment-age">(22 Jun '15, 00:39)</span> lal12</div></div><span id="43438"></span><div id="comment-43438" class="comment not_top_scorer"><div id="post-43438-score" class="comment-score"></div><div class="comment-text"><p>I still got a problem. I found the .so files, but they are only 10K sized. The dll files are much bigger and different sized (60K to 130K). I have the same issue with three different dissectors (all self developed and working on windows).</p><p>If I try to load themid wireshark, the following error occurs:</p><p><code>undefined symbol: proto_register_myprotocol</code></p><p>I assume this is kind of a linker error. So I tried to run <code>./configure</code> with the <code>--enable-static</code> parameter. Which didn't changed the size.</p></div><div id="comment-43438-info" class="comment-info"><span class="comment-age">(22 Jun '15, 05:53)</span> lal12</div></div><span id="43448"></span><div id="comment-43448" class="comment not_top_scorer"><div id="post-43448-score" class="comment-score"></div><div class="comment-text"><p>I now used CMake which worked. But still would be interesting where is the problem with autotools.</p></div><div id="comment-43448-info" class="comment-info"><span class="comment-age">(22 Jun '15, 09:52)</span> lal12</div></div></div><div id="comment-tools-42917" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-42917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

