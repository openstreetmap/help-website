+++
type = "question"
title = "Plugin not loading"
description = '''I&#x27;m getting WAY more fun than just locating X11 on ML... Couldn&#x27;t load module /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so: dlopen(/Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so, 10): Symbol not found: dissector_get_port_handle ...'''
date = "2012-07-26T17:41:00Z"
lastmod = "2012-07-26T19:19:00Z"
weight = 13043
keywords = [ "plugin" ]
aliases = [ "/questions/13043" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Plugin not loading](/questions/13043/plugin-not-loading)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13043-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting WAY more fun than just locating X11 on ML...</p><pre><code>Couldn&#39;t load module /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so: dlopen(/Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so, 10): Symbol not found: dissector_get_port_handle
  Referenced from: /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so
  Expected in: flat namespace
 in /Applications/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so&lt;/p&gt;</code></pre></div><div id="question-tags" class="tags-container tags">plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '12, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/ef3a5b3953f513a678c48e8f9431ab44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IanJ&#39;s gravatar image" /><p>IanJ<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IanJ has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '12, 19:20</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-13043" class="comments-container"></div><div id="comment-tools-13043" class="comment-tools"></div><div class="clear"></div><div id="comment-13043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13045"></span>

<div id="answer-container-13045" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13045-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>That</em> problem is due to a plugin having been built against an older version of Wireshark that called that routine <code>dissector_get_port_handle</code> being run against a newer version of Wireshark that calls it <code>dissector_get_uint_handle</code>. Wireshark does not guarantee that plugins built against a given major release (such as 1.4.x, for various values of x) will continue to work with later major releases (such as 1.6.x or 1.8.x, for various values of x).</p><p>Note also that, as of Wireshark 1.8.0, the INTERLINK dissector is a built-in dissector rather than a plugin, and that the installer might not get rid of existing plugins, so if you installed 1.8.0 or 1.8.1 on top of a 1.4.x or 1.6.x installation, you may have an old INTERLINK plugin left around. I would suggest dragging Wireshark to the trash and re-installing it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 19:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '12, 19:28</p></div></div><div id="comments-container-13045" class="comments-container"></div><div id="comment-tools-13045" class="comment-tools"></div><div class="clear"></div><div id="comment-13045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

