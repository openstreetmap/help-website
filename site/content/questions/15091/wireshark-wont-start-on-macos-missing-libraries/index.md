+++
type = "question"
title = "Wireshark won&#x27;t start on MacOS - missing libraries?"
description = '''Wireshark fails on 10.7.5 with the following errors: Couldn&#x27;t load module /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so: dlopen(/Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so, 10): Symbol not found: _dissector_get_port_handle  Re...'''
date = "2012-10-18T13:20:00Z"
lastmod = "2012-10-18T21:48:00Z"
weight = 15091
keywords = [ "osx", "macosx" ]
aliases = [ "/questions/15091" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark won't start on MacOS - missing libraries?](/questions/15091/wireshark-wont-start-on-macos-missing-libraries)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15091-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark fails on 10.7.5 with the following errors:</p><p>Couldn't load module /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so: dlopen(/Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so, 10): Symbol not found: _dissector_get_port_handle Referenced from: /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so Expected in: flat namespace in /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so</p><p>Couldn't load module /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so: dlopen(/Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so, 10): Symbol not found: _dissector_add Referenced from: /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so Expected in: flat namespace in /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so</p><p>Am I missing something that should be in there?</p></div><div id="question-tags" class="tags-container tags">osx macosx</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '12, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/5ddacaa1ea5ce2b84c365db950cbc0d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meatwad_650&#39;s gravatar image" /><p>meatwad_650<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meatwad_650 has no accepted answers">0%</span></p></div></div><div id="comments-container-15091" class="comments-container"></div><div id="comment-tools-15091" class="comment-tools"></div><div class="clear"></div><div id="comment-15091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15099"></span>

<div id="answer-container-15099" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15099-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You probably installed a newer version of Wireshark when you had an older one installed; the installer doesn't remove old plugins, so if a dissector is a plugin in the older version of Wireshark and a built-in dissector in the newer version, the old plugin is left behind. If the plugin interface changes - if, for example, a routine's name changes, such as <code>dissector_get_port_handle()</code> changing to <code>dissector_get_uint_handle()</code> or <code>dissector_add()</code> changing to <code>dissector_add_uint()</code> - then the old plugins won't load.</p><p>It looks as if OS X's run-time linker fails if the application tries to load a plugin with <code>dlopen()</code> and a symbol can't be found - and, it appears, doesn't just return a "can't load that plugin" error; instead, it causes the program to fail.</p><p>Try uninstalling Wireshark completely and then re-installing it.</p><p>The installer not removing old plugins is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7401">bug 7401</a>. I'll look into why the run-time linker is killing Wireshark rather than just returning a "that plugin won't load" error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '12, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15099" class="comments-container"></div><div id="comment-tools-15099" class="comment-tools"></div><div class="clear"></div><div id="comment-15099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

