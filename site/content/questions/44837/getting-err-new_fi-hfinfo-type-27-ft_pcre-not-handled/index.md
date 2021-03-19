+++
type = "question"
title = "Getting Err new_fi-&gt;hfinfo-&gt;type 27 (FT_PCRE) not handled"
description = '''I cloned the latest version I believed without tagging with any version, in Repostitory to clone: https://code.wireshark.org/review/wireshark. I would expect this will be the latest version 1_12_6? The plugin I modified and generated using win64 with this source code and it works fine when I opened ...'''
date = "2015-08-04T14:20:00Z"
lastmod = "2015-08-04T15:04:00Z"
weight = 44837
keywords = [ "plugins" ]
aliases = [ "/questions/44837" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting Err new\_fi-&gt;hfinfo-&gt;type 27 (FT\_PCRE) not handled](/questions/44837/getting-err-new_fi-hfinfo-type-27-ft_pcre-not-handled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44837-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I cloned the latest version I believed without tagging with any version, in Repostitory to clone: <a href="https://code.wireshark.org/review/wireshark.">https://code.wireshark.org/review/wireshark.</a> I would expect this will be the latest version 1_12_6? The plugin I modified and generated using win64 with this source code and it works fine when I opened the wireshark-gtk2. Frames are dissectable, etc... I built this code on a virtual machine. But when I used this generated dll on the released version 1_12_6 (win64) downloaded in my PC, I could not open the frames that used this dll. It works with generated code. Wireshark will not open and on Debug Console it stated: Err new_fi-&gt;hfinfo-&gt;type 27 (FT_PCRE) not handled. I googled and looked through some other people responses but could not shed light other than the source code maybe not the same version as the one I think I downloaded?. How do you figure out what source version you obtained when you cloned? And what does the Err really telling me. thanks in advance, Muriel This plugins is working on version 1.10.7 (win32).</p></div><div id="question-tags" class="tags-container tags">plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '15, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/fe7b8b8f82626427d3ae7d5428f2102d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="christenmu&#39;s gravatar image" /><p>christenmu<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="christenmu has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Aug '15, 14:23</p></div></div><div id="comments-container-44837" class="comments-container"></div><div id="comment-tools-44837" class="comment-tools"></div><div class="clear"></div><div id="comment-44837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44840"></span>

<div id="answer-container-44840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44840-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think that path will clone the Wireshark development master, i.e. currently 1.99.x. You can check the version in your built copy of Wireshark from the Help &gt; About Wireshark dialog, or directly from git with <code>git branch --list</code>, your current branch is indicated with "*". If it's "master" then that's the development branch.</p><p>To clone the wireshark-1.12.6 tag to build a plugin for use with Wireshark 1.12.6 you'll need to explicitly checkout the 1.12 tag in your repo: <code>git checkout tags/wireshark-1.12.6</code>. Clean your build directory first before switching, and then rebuild.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '15, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44840" class="comments-container"><span id="44842"></span><div id="comment-44842" class="comment"><div id="post-44842-score" class="comment-score"></div><div class="comment-text"><p>oh ok, thank you for the quick response. I will clone the 1.12.6.</p></div><div id="comment-44842-info" class="comment-info"><span class="comment-age">(04 Aug '15, 15:55)</span> christenmu</div></div><span id="44858"></span><div id="comment-44858" class="comment"><div id="post-44858-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-44858-info" class="comment-info"><span class="comment-age">(05 Aug '15, 01:54)</span> Jaap ♦</div></div></div><div id="comment-tools-44840" class="comment-tools"></div><div class="clear"></div><div id="comment-44840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

