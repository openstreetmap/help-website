+++
type = "question"
title = "Are wireshark custom dissector .so files loaded at run time or initialization time"
description = '''I wanted to know if the custom dissector which users have written under /plugin/ directory and created a .so for the same are loaded during run time or initialization time ? I mean the .so files loaded under /usr/lib64/wireshark/plugins/1.12.7/ directory.'''
date = "2016-05-25T08:02:00Z"
lastmod = "2016-05-25T15:30:00Z"
weight = 52915
keywords = [ "shared-object" ]
aliases = [ "/questions/52915" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Are wireshark custom dissector .so files loaded at run time or initialization time](/questions/52915/are-wireshark-custom-dissector-so-files-loaded-at-run-time-or-initialization-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52915-score" class="post-score" title="current number of votes">0</div><span id="post-52915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to know if the custom dissector which users have written under /plugin/ directory and created a .so for the same are loaded during run time or initialization time ?</p><p>I mean the .so files loaded under /usr/lib64/wireshark/plugins/1.12.7/ directory.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-shared-object" rel="tag" title="see questions tagged &#39;shared-object&#39;">shared-object</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '16, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p><span>Kiran Kumar G</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div></div><div id="comments-container-52915" class="comments-container"></div><div id="comment-tools-52915" class="comment-tools"></div><div class="clear"></div><div id="comment-52915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52927"></span>

<div id="answer-container-52927" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52927-score" class="post-score" title="current number of votes">0</div><span id="post-52927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's little difference between the two, but at a stretch one could say initialization time. The plugins are loaded as glib modules, and this is happening in <code>wsutil/plugins.c:plugins_scan_dir()</code>, called from <code>scan_plugins()</code>, which is called from <code>wireshark-qt.cpp:main()</code> during initialization of <code>epan</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '16, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52927" class="comments-container"><span id="52934"></span><div id="comment-52934" class="comment"><div id="post-52934-score" class="comment-score"></div><div class="comment-text"><p>glib modules means -- libglib-2.0.so.0 ?</p></div><div id="comment-52934-info" class="comment-info"><span class="comment-age">(25 May '16, 12:36)</span> <span class="comment-user userinfo">Kiran Kumar G</span></div></div><span id="52936"></span><div id="comment-52936" class="comment"><div id="post-52936-score" class="comment-score"></div><div class="comment-text"><p>No, "the plugins are loaded as glib modules" means "the plugins are loaded using <a href="https://developer.gnome.org/glib/stable/glib-Dynamic-Loading-of-Modules.html">the g_module APIs</a>". Those APIs are wrappers around the OS's dynamic loading APIs, such as <code>dlopen()</code>/<code>dlsym()</code> on most UN*Xes, <code>LoadLibrary()</code>/<code>GetProcAddress()</code> on Windows, or whatever the laggard UN*Xes such as 32-bit HP-UX use.</p></div><div id="comment-52936-info" class="comment-info"><span class="comment-age">(25 May '16, 15:17)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-52927" class="comment-tools"></div><div class="clear"></div><div id="comment-52927-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52937"></span>

<div id="answer-container-52937" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52937-score" class="post-score" title="current number of votes">0</div><span id="post-52937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>They're not linked in, they're loaded by calls Wireshark makes, so in that sense they're loaded at run time. The part of run time when they're loaded is during the startup process of Wireshark, not while Wireshark is actually dissecting packets, so, for example, they're not loaded "on-demand".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '16, 15:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-52937" class="comments-container"></div><div id="comment-tools-52937" class="comment-tools"></div><div class="clear"></div><div id="comment-52937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

