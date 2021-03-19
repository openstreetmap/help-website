+++
type = "question"
title = "Can we build MAC OS X: .dmg packages on mavericks?"
description = '''Downloaded the source code and try to build a *.dmg package on MAC os mavericks.  The error I am getting is : Building Wireshark Building Wireshark Copying extra files Copying Scripts Copying root to temporary location Preserving resource forks Warning: package.build.findSplitForks Creating permissi...'''
date = "2014-05-12T18:57:00Z"
lastmod = "2014-05-12T18:57:00Z"
weight = 32742
keywords = [ "macosx" ]
aliases = [ "/questions/32742" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can we build MAC OS X: .dmg packages on mavericks?](/questions/32742/can-we-build-mac-os-x-dmg-packages-on-mavericks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32742-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Downloaded the source code and try to build a *.dmg package on MAC os mavericks. The error I am getting is :</p><p>Building Wireshark</p><p>Building Wireshark</p><p>Copying extra files</p><p>Copying Scripts</p><p>Copying root to temporary location</p><p>Preserving resource forks</p><p>Warning: package.build.findSplitForks</p><p>Creating permission hierarchy</p><p>2014-05-12 18:45:57.542 packagemaker[12999:4103] *** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: 'must provide a launch path'</p><p>*** Call stack at first throw:</p><p>(</p><p>0 CoreFoundation 0x993d06b1 __raiseError + 193</p><p>1 libobjc.A.dylib 0x9276f091 objc_exception_throw + 162</p><p>2 CoreFoundation 0x993d05cb +[NSException raise:format:] + 139</p><p>3 Foundation 0x9127d3df COPY_SETTER_IMPL + 208</p><p>4 Foundation 0x9127d55e -[NSConcreteTask setLaunchPath:] + 42</p><p>5 packagemaker 0x00130eb6 packagemaker + 229046</p><p>6 Foundation 0x91132f2e -[NSThread main] + 45</p><p>7 Foundation 0x91132e86 <strong>NSThread</strong>main__ + 1426</p><p>8 libsystem_pthread.dylib 0x97cc95fb _pthread_body + 144</p><p>9 libsystem_pthread.dylib 0x97cc9485 _pthread_struct_init + 0</p><p>10 libsystem_pthread.dylib 0x97ccecf2 thread_start + 34</p><p>)</p><p>./osx-dmg.sh: line 150: 12999 Trace/BPT trap: 5 packagemaker --doc "Wireshark_package.pmdoc" --title "$pkg_title" --id "org.wireshark.pkg.Wireshark" --version "$version" --target 10.5 --verbose</p><p>make: *** [osx-package] Error 1</p></div><div id="question-tags" class="tags-container tags">macosx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '14, 18:57</strong></p><img src="https://secure.gravatar.com/avatar/a0493f47a59fa99e13242a0f65449dd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="happy123&#39;s gravatar image" /><p>happy123<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="happy123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 May '14, 18:59</p></div></div><div id="comments-container-32742" class="comments-container"><span id="32750"></span><div id="comment-32750" class="comment"><div id="post-32750-score" class="comment-score"></div><div class="comment-text"><p>find the same problem here: <a href="http://www.wireshark.org/lists/wireshark-bugs/201401/msg00266.html">http://www.wireshark.org/lists/wireshark-bugs/201401/msg00266.html</a> is it a bug need to be fix?</p></div><div id="comment-32750-info" class="comment-info"><span class="comment-age">(13 May '14, 00:50)</span> happy123</div></div></div><div id="comment-tools-32742" class="comment-tools"></div><div class="clear"></div><div id="comment-32742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

