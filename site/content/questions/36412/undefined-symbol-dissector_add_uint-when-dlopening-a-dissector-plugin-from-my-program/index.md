+++
type = "question"
title = "undefined symbol: dissector_add_uint when dlopening a dissector plugin from my program"
description = '''Hello everyone, I&#x27;m a newbie regarding wireshark so accept my apologies in advanced if this is too obvious I&#x27;m on linux/C++ trying to perform a blunt/raw dlopen of a wireshark dissector (asterxi.so). It compiles perfectly but when it&#x27;s executed this exception arises: Exception: /usr/lib/wireshark/pl...'''
date = "2014-09-17T11:29:00Z"
lastmod = "2014-09-17T12:47:00Z"
weight = 36412
keywords = [ "dissector_add_uint", "dissector" ]
aliases = [ "/questions/36412" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [undefined symbol: dissector\_add\_uint when dlopening a dissector plugin from my program](/questions/36412/undefined-symbol-dissector_add_uint-when-dlopening-a-dissector-plugin-from-my-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36412-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I'm a newbie regarding wireshark so accept my apologies in advanced if this is too obvious</p><p>I'm on linux/C++ trying to perform a blunt/raw dlopen of a wireshark dissector (asterxi.so). It compiles perfectly but when it's executed this exception arises:</p><p><strong>Exception: /usr/lib/wireshark/plugins/asterix.so: undefined symbol: dissector_add_uint</strong></p><p>Well, I'd really appreciate any hints 'cause I'm really lost</p><p>Regards,</p></div><div id="question-tags" class="tags-container tags">dissector_add_uint dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '14, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/b8c80a58a48e369b72cf3a2a5bdf51c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jlseminara&#39;s gravatar image" /><p>jlseminara<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jlseminara has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Sep '14, 12:48</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-36412" class="comments-container"><span id="36415"></span><div id="comment-36415" class="comment"><div id="post-36415-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark is this?</p></div><div id="comment-36415-info" class="comment-info"><span class="comment-age">(17 Sep '14, 12:17)</span> Guy Harris ♦♦</div></div><span id="36416"></span><div id="comment-36416" class="comment"><div id="post-36416-score" class="comment-score"></div><div class="comment-text"><p>And by "blunt/raw dlopen", do you mean that you're trying to dlopen the .so in <em>your own program</em>?</p></div><div id="comment-36416-info" class="comment-info"><span class="comment-age">(17 Sep '14, 12:18)</span> Guy Harris ♦♦</div></div><span id="36418"></span><div id="comment-36418" class="comment"><div id="post-36418-score" class="comment-score"></div><div class="comment-text"><p>It's wireshark 1.8.2-1, and yes I'm doing a dlopen in my program</p></div><div id="comment-36418-info" class="comment-info"><span class="comment-age">(17 Sep '14, 12:36)</span> jlseminara</div></div></div><div id="comment-tools-36412" class="comment-tools"></div><div class="clear"></div><div id="comment-36412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36419"></span>

<div id="answer-container-36419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36419-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark plugin dissectors use APIs from libwireshark, so if you're going to use a plugin dissector, you're going to have to link your program with libwireshark - they're not usable (and are not intended to be usable) from a random program.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '14, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36419" class="comments-container"><span id="36421"></span><div id="comment-36421" class="comment"><div id="post-36421-score" class="comment-score"></div><div class="comment-text"><p>Thank you Guy, I'm already linking against libwireshark, but now I believe the problem is that the dissector (asterix.so) is linked against wireshark-1.8.2-1 and my libwireshark is version 1.10</p><p>I believe that could be a problem :O<br />
</p></div><div id="comment-36421-info" class="comment-info"><span class="comment-age">(17 Sep '14, 12:58)</span> jlseminara</div></div><span id="36422"></span><div id="comment-36422" class="comment"><div id="post-36422-score" class="comment-score">1</div><div class="comment-text"><p>Yes, the APIs change from major release to major release, so a plugin built against Wireshark 1.M.x won't necessarily work with Wireshark 1.N.x or a program linked with its libraries. In particular, <code>dissector_add()</code> was renamed in 1.10 to <code>dissector_add_uint()</code> to parallel <code>dissector_add_string()</code> and to indicate that it's specifically for dissectors that register in a table of unsigned integer values.</p></div><div id="comment-36422-info" class="comment-info"><span class="comment-age">(17 Sep '14, 13:07)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-36419" class="comment-tools"></div><div class="clear"></div><div id="comment-36419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

