+++
type = "question"
title = "Register All Handoff fun crash for user defined dissector in Wireshark 2.0.3"
description = '''Hi I have encouterd the crah for Register All Handoff for user define dissector call (generic_*.dll) in wireshark 2.0.3 Attaching Image for the refrence  These issue is found in wireshark 2.0.3. Same code works fine in wireshark 1.12.7 Request your help. Thanks Dinesh Sadu'''
date = "2016-06-12T05:58:00Z"
lastmod = "2016-06-12T12:17:00Z"
weight = 53370
keywords = [ "registerallhandoff", "development", "protocol_regis", "wireshark" ]
aliases = [ "/questions/53370" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Register All Handoff fun crash for user defined dissector in Wireshark 2.0.3](/questions/53370/register-all-handoff-fun-crash-for-user-defined-dissector-in-wireshark-203)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53370-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53370-score" class="post-score" title="current number of votes">0</div><span id="post-53370-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have encouterd the crah for Register All Handoff for user define dissector call (generic_*.dll) in wireshark 2.0.3</p><p>Attaching Image for the refrence <img src="https://osqa-ask.wireshark.org/upfiles/Handoff_Capture.jpg" alt="alt text" /></p><p>These issue is found in wireshark 2.0.3. Same code works fine in wireshark 1.12.7</p><p>Request your help.</p><p>Thanks Dinesh Sadu</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-registerallhandoff" rel="tag" title="see questions tagged &#39;registerallhandoff&#39;">registerallhandoff</span> <span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-protocol_regis" rel="tag" title="see questions tagged &#39;protocol_regis&#39;">protocol_regis</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '16, 05:58</strong></p><img src="https://secure.gravatar.com/avatar/04334c27cb629065a13d61a61b611038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinesh%20Babu%20Sadu&#39;s gravatar image" /><p><span>Dinesh Babu ...</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinesh Babu Sadu has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53370" class="comments-container"></div><div id="comment-tools-53370" class="comment-tools"></div><div class="clear"></div><div id="comment-53370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53374"></span>

<div id="answer-container-53374" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53374-score" class="post-score" title="current number of votes">0</div><span id="post-53374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Plugins need to be compiled with the Wireshark source code of the major version you intend to use. You cannot take a plugin compiled for Wireshark 1.12.X and expect it to work with Wireshark 2.0.X. So if this not already the case, ensure to recompile your generic_dissector.dll plugin.</p><p>Also ensure that you do not have the same plugin installed in your user profile folder and in your build folder. This would also lead to a crash if you try to load twice the same plugin.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '16, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-53374" class="comments-container"><span id="53377"></span><div id="comment-53377" class="comment"><div id="post-53377-score" class="comment-score"></div><div class="comment-text"><p>Thanks Pascal...</p><p>I had compiled it with latest Wireshark version 2.0.X and did it as gtk-package , installed in User(C:) Program Files (x86). These would not pick the plugin from build Folder.. Build Folder: E:/Softwares/Wireshark-2.0.3/<strong>*</strong> But my installation path is from C: Drive and short-cut (Wireshark_Legacy) created on Desktop which launches from C: Drive... Crash is observed only in sometimes. Majority times Wireshark comes-up successfully. Want to understand is these because of not freeing my static memory/register handles in generic_dissector.dll</p></div><div id="comment-53377-info" class="comment-info"><span class="comment-age">(12 Jun '16, 11:24)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="53378"></span><div id="comment-53378" class="comment"><div id="post-53378-score" class="comment-score"></div><div class="comment-text"><p>Well, only you can tell as you are the only one having access to the plug-in code. As the crash appears at startup (from what I understood) then it should not be related to previous run memory allocation.</p></div><div id="comment-53378-info" class="comment-info"><span class="comment-age">(12 Jun '16, 12:17)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-53374" class="comment-tools"></div><div class="clear"></div><div id="comment-53374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

