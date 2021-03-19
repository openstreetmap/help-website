+++
type = "question"
title = "init.lua gets overwritten during an upgrade. How can I prevent that?"
description = '''Currently, a Wireshark upgrade overwrites the system init.lua without checking for user modifications. If would be nice if there was a way to keep the custom entries there.'''
date = "2014-01-13T05:40:00Z"
lastmod = "2014-01-13T07:03:00Z"
weight = 28838
keywords = [ "lua" ]
aliases = [ "/questions/28838" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [init.lua gets overwritten during an upgrade. How can I prevent that?](/questions/28838/initlua-gets-overwritten-during-an-upgrade-how-can-i-prevent-that)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28838-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Currently, a Wireshark upgrade overwrites the system <code>init.lua</code> without checking for user modifications. If would be nice if there was a way to keep the custom entries there.</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '14, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/06ac1b2e4c4c0c36fcb14ed5424f65d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MattKnepp&#39;s gravatar image" /><p>MattKnepp<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MattKnepp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Feb '14, 13:56</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-28838" class="comments-container"></div><div id="comment-tools-28838" class="comment-tools"></div><div class="clear"></div><div id="comment-28838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28840"></span>

<div id="answer-container-28840" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28840-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just place your version of <strong><code>init.lua</code></strong> in your personal config directory (on Windows: <strong><code>%APPDATA%\wireshark</code></strong>) and your modifications will survive an update.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '14, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '14, 07:13</p></div></div><div id="comments-container-28840" class="comments-container"><span id="29360"></span><div id="comment-29360" class="comment"><div id="post-29360-score" class="comment-score"></div><div class="comment-text"><p>Note though that your init.lua won't pick up any changes Wireshark's init.lua has had in the new version. init.lua doesn't change very often, but if it does your Lua scripts might need those changes. (some of the things in init.lua are constants used inside wireshark, which could theoretically change) So just keep that in mind if something's not working in your scripts when you upgrade.</p></div><div id="comment-29360-info" class="comment-info"><span class="comment-age">(31 Jan '14, 14:46)</span> Hadriel</div></div><span id="29375"></span><div id="comment-29375" class="comment"><div id="post-29375-score" class="comment-score"></div><div class="comment-text"><p>Unless you need to <em>change</em> things in the system <code>init.lua</code> (in which case you run the risk of having your changes no longer apply to an updated system <code>init.lua</code>), putting just your new stuff in your personal <code>init.lua</code> should work.</p><p>If you want those additions to be global for all users on your system, there's currently no good way to do that; perhaps there should be a system Lua init file containing stuff such as Wireshark's definitions, an optional system Lua init file containing site customizations and additionsl, and an optional personal Lua init file containing user customizations and additions.</p></div><div id="comment-29375-info" class="comment-info"><span class="comment-age">(01 Feb '14, 19:48)</span> Guy Harris ♦♦</div></div><span id="29382"></span><div id="comment-29382" class="comment"><div id="post-29382-score" class="comment-score"></div><div class="comment-text"><p>Actually, the system <code>init.lua</code> is always loaded first, and then, the personal <code>init.lua</code>. You would only lose the system changes if your personal <code>init.lua</code> overwrites the system values, which you'd want to avoid for the very reason @Hadriel points out.</p><p>If you find a need to add to system tables (e.g., adding to the Wiretap file types), make sure to <em>append</em> your own values rather than <em>copy</em> so that you'll pick up any updates from the system initialization. System flags/enumerations in <code>init.lua</code> (e.g., <code>MENU_ANALYZE_UNSORTED</code>, <code>ENC_UTF_8</code>) normally should not be overwritten unless you're "feeling experimental".</p><p>@GuyHarris, You're probably right in that there's no "good way" to support global additions to <code>init.lua</code>, but it's still feasible with a one-line modification to the system <code>init.lua</code> to load a "global <code>init.lua</code>", stored in a location that is accessible to all users and not overwriteable by the Wireshark installation.</p></div><div id="comment-29382-info" class="comment-info"><span class="comment-age">(02 Feb '14, 13:41)</span> helloworld</div></div></div><div id="comment-tools-28840" class="comment-tools"></div><div class="clear"></div><div id="comment-28840-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

