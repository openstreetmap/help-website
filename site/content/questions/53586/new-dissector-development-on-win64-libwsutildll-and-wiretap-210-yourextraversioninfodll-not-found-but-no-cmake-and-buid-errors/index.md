+++
type = "question"
title = "New Dissector development on WIN64 :Libwsutil.dll and wiretap-2.1.0-YourExtraVersionInfo.dll not found BUT no cmake and buid errors"
description = '''Hi, i&#x27;m trying to develop a new heuristic dissector. Actually i have no cmake errors and no msbuild errors but when i try to debug my plugin wireshark starts to display some run-time errors.  After that it starts but obv i don&#x27;t want this errors and i don&#x27;t understand why. Suggestions? thanks in adv...'''
date = "2016-06-21T05:19:00Z"
lastmod = "2016-06-21T08:17:00Z"
weight = 53586
keywords = [ "win64", "dissector", "source-code" ]
aliases = [ "/questions/53586" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [New Dissector development on WIN64 :Libwsutil.dll and wiretap-2.1.0-YourExtraVersionInfo.dll not found BUT no cmake and buid errors](/questions/53586/new-dissector-development-on-win64-libwsutildll-and-wiretap-210-yourextraversioninfodll-not-found-but-no-cmake-and-buid-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53586-score" class="post-score" title="current number of votes">0</div><span id="post-53586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i'm trying to develop a new heuristic dissector. Actually i have no cmake errors and no msbuild errors but when i try to debug my plugin wireshark starts to display some run-time errors.</p><p><a href="http://it.tinypic.com?ref=9uxb2v"><img src="http://i67.tinypic.com/9uxb2v.png" alt="Image and video hosting by TinyPic" /></a></p><p>After that it starts but obv i don't want this errors and i don't understand why.</p><p>Suggestions?</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-win64" rel="tag" title="see questions tagged &#39;win64&#39;">win64</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-source-code" rel="tag" title="see questions tagged &#39;source-code&#39;">source-code</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '16, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/39c90bff22b6fa58db657d5af50c7899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kenhero&#39;s gravatar image" /><p><span>kenhero</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kenhero has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53586" class="comments-container"><span id="53591"></span><div id="comment-53591" class="comment"><div id="post-53591-score" class="comment-score"></div><div class="comment-text"><p>I deleted wsbuild64 and builded again the project with msbuild Actually i have this error:</p><p>C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V120\Microsoft.CppCommon.targets(170,5): error MSB6006: "cmd.exe" terminato con il codice 9009. [C:\Development\wsbuild64\copy_data_files.vcxproj]</p></div><div id="comment-53591-info" class="comment-info"><span class="comment-age">(21 Jun '16, 07:44)</span> <span class="comment-user userinfo">kenhero</span></div></div><span id="53592"></span><div id="comment-53592" class="comment"><div id="post-53592-score" class="comment-score">1</div><div class="comment-text"><p>Ensure that no program is running (like Wireshark.exe or dumpcap.exe for example) from your previous build attempt while executing the msbuild command. This error means that your system fails to copy a file (probably because the target is already in use).</p></div><div id="comment-53592-info" class="comment-info"><span class="comment-age">(21 Jun '16, 08:17)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-53586" class="comment-tools"></div><div class="clear"></div><div id="comment-53586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53590"></span>

<div id="answer-container-53590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53590-score" class="post-score" title="current number of votes">1</div><span id="post-53590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I presume you are launching Wireshark from the Wireshark.sln file.</p><p>This solution files is messing with the environment variables, leading to the popups you see. You have 2 solutions:</p><ul><li>Remove the extcap executables from the extcap folder as you do not care about them</li><li>or do not launch Wireshark from the solution file, but instead in open Visual Studio IDE, do File -&gt; Open -&gt; Project/Solution and selects Wireshark.exe in your run\relWithDebInfo or run\Debug folder. Then open whatever source file you watn and put your breakpoint.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '16, 07:43</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-53590" class="comments-container"></div><div id="comment-tools-53590" class="comment-tools"></div><div class="clear"></div><div id="comment-53590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

