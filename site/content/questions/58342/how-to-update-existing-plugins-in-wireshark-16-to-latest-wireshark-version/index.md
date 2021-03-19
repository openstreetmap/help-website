+++
type = "question"
title = "How to update existing plugins in Wireshark 1.6 to latest Wireshark version?"
description = '''I am here looking for the things we need to change to make the Wireshark plugins written for the 1.6 version compatible with the latest version. Any help will be appreciated. Thanks in advance.'''
date = "2016-12-26T20:42:00Z"
lastmod = "2016-12-27T00:56:00Z"
weight = 58342
keywords = [ "version2.2.0", "upgrade", "plugin", "version", "wireshark" ]
aliases = [ "/questions/58342" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to update existing plugins in Wireshark 1.6 to latest Wireshark version?](/questions/58342/how-to-update-existing-plugins-in-wireshark-16-to-latest-wireshark-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58342-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am here looking for the things we need to change to make the Wireshark plugins written for the 1.6 version compatible with the latest version. Any help will be appreciated. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">version2.2.0 upgrade plugin version wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '16, 20:42</strong></p><img src="https://secure.gravatar.com/avatar/54b13e716c5802540b3b28701372e876?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chirag&#39;s gravatar image" /><p>chirag<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chirag has no accepted answers">0%</span></p></div></div><div id="comments-container-58342" class="comments-container"></div><div id="comment-tools-58342" class="comment-tools"></div><div class="clear"></div><div id="comment-58342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58345"></span>

<div id="answer-container-58345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58345-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think we have a list of all the API changes made. I'd check some other plugin for changes made to make and cmake files, nmake is now gone. Then build a unchanged version of wireshark to make sure your build system is up to scratch. config.h is now unconditionally included, there is changes in the registration routines proto_tree_add_text() is gone etc. It's probably best to try to compile and fix the compilation errors as you go when adding your plugin to the new build. You can always compare with the code in other plugins or in the history how changes was implemented.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '16, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-58345" class="comments-container"><span id="58460"></span><div id="comment-58460" class="comment"><div id="post-58460-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer Anders. I was able to make out some of the changes which are done to the interface. I have one more doubt, from where can we find libwireshark.lib, for my project to build i need this file for the latest version.</p></div><div id="comment-58460-info" class="comment-info"><span class="comment-age">(02 Jan '17, 03:19)</span> chirag</div></div></div><div id="comment-tools-58345" class="comment-tools"></div><div class="clear"></div><div id="comment-58345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

