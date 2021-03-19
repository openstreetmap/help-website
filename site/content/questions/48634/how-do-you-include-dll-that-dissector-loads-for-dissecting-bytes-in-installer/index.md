+++
type = "question"
title = "How do you include dll that dissector loads for dissecting bytes in installer?"
description = '''Greetings, I created a dissector that loads a dll to assist in parsing bytes for display in Wireshark 2.0 using CMake and Visual Studio 2013. The testing piece of the instructions is successful for running the built Wireshark.exe when opening a PCAP files with the necessary packets to test the disse...'''
date = "2015-12-18T14:12:00Z"
lastmod = "2015-12-22T07:31:00Z"
weight = 48634
keywords = [ "installer", "dissector", "wireshark-2.0", "plugin" ]
aliases = [ "/questions/48634" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do you include dll that dissector loads for dissecting bytes in installer?](/questions/48634/how-do-you-include-dll-that-dissector-loads-for-dissecting-bytes-in-installer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48634-score" class="post-score" title="current number of votes">0</div><span id="post-48634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>I created a dissector that loads a dll to assist in parsing bytes for display in Wireshark 2.0 using CMake and Visual Studio 2013. The testing piece of the instructions is successful for running the built Wireshark.exe when opening a PCAP files with the necessary packets to test the dissector that imports the dll. I am very clear on how to include the dissector as a plugin on the built installer. But, I am having a problem making sure the imported dll is available for the dissector at deployment.</p><p>I notice that, at test time, the dll, which sits alongside Wireshark.exe in the build directory, is one level from the plugins directory in order to prevent Wireshark to think it's another dissector with no symbol. Once installed, the plugins directory is two levels from where Wireshark.exe is located since all plugins are placed in a "2.0.0-EXTRA] sub-directory. I would like to know what is best practice for deploying such plugin.</p><p>Thanks in advanced.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installer" rel="tag" title="see questions tagged &#39;installer&#39;">installer</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark-2.0" rel="tag" title="see questions tagged &#39;wireshark-2.0&#39;">wireshark-2.0</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '15, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/bfa53b64ea6967e45a614981c461a638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coloncm&#39;s gravatar image" /><p><span>coloncm</span><br />
<span class="score" title="76 reputation points">76</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coloncm has 2 accepted answers">66%</span></p></div></div><div id="comments-container-48634" class="comments-container"></div><div id="comment-tools-48634" class="comment-tools"></div><div class="clear"></div><div id="comment-48634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48673"></span>

<div id="answer-container-48673" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48673-score" class="post-score" title="current number of votes">0</div><span id="post-48673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="coloncm has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I managed to deploy the helper dll unto the Wireshark installation directory via an entry in the "Installation execution commands" section of the wireshark.nsi file in the ../wireshark/packaging/nsis directory as below:</p><pre><code>File &quot;${STAGING_DIR}\helper.dll&quot;</code></pre><p>In my dissector plugin code, I first check if the dll is located one level from the plugin in order to support debugging of the build and, if not, check its location two levels down from the plugin directory in case Wireshark was executed from an installation directory. If neither loads it (null pointer), I simply post text stating it's not available. Not pretty, but works.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '15, 07:31</strong></p><img src="https://secure.gravatar.com/avatar/bfa53b64ea6967e45a614981c461a638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coloncm&#39;s gravatar image" /><p><span>coloncm</span><br />
<span class="score" title="76 reputation points">76</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coloncm has 2 accepted answers">66%</span></p></div></div><div id="comments-container-48673" class="comments-container"></div><div id="comment-tools-48673" class="comment-tools"></div><div class="clear"></div><div id="comment-48673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48635"></span>

<div id="answer-container-48635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48635-score" class="post-score" title="current number of votes">1</div><span id="post-48635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The plugins for a build are in a single directory "plugins" underneath the Wireshark executable location, when installed there is an additional directory layer for the version number of the build.</p><p>There's nothing set up in the CMake build to copy helper DLLs into the build plugins directory from wherever the helper plugins reside so you'll have to do that yourself. Probably best to put your helper DLL in the wireshark-xxx-libs directory where all the other third party DLLs live, and copy it in your plugin CMakeLists.txt in a similar manner to the other third party DLLs in the main CMakeLists.txt.</p><p>The installer copies the standard DLLs from the build plugins directory into the installed plugins\${VERSION}. This is in packaging\nsis\wireshark.nsi.</p><p>To add additional plugin DLLs to the install, edit packaging\nsis\custom_plugins.txt to list the additional plugin and any helper DLLs to install. Ideally we should have a way to do this with an additional "custom" file rather than editing one that's under version control.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '15, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48635" class="comments-container"><span id="48641"></span><div id="comment-48641" class="comment"><div id="post-48641-score" class="comment-score"></div><div class="comment-text"><p>I'm glad that your recommendations match my choice of approach. I guess I would have to set the path to the helper dll differently at deployment vs build, i.e., "..\dll" vs "..\..\dll". Is there a way to make that distinction in code, perhaps, via a variable or something?</p></div><div id="comment-48641-info" class="comment-info"><span class="comment-age">(19 Dec '15, 10:38)</span> <span class="comment-user userinfo">coloncm</span></div></div><span id="48655"></span><div id="comment-48655" class="comment"><div id="post-48655-score" class="comment-score"></div><div class="comment-text"><p>It's unclear to me why you need to be aware of the path to the helper DLL. AFAICT, it will always be in the same directory as your plugin.</p></div><div id="comment-48655-info" class="comment-info"><span class="comment-age">(21 Dec '15, 01:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48658"></span><div id="comment-48658" class="comment"><div id="post-48658-score" class="comment-score"></div><div class="comment-text"><p>If I keep it in the same directory, Wireshark appears to think it's also a dissector and gives off an error message at startup that "the plugin helper.dll has no version symbol" though works as expected by ignoring the helper dll that's sitting alongside other dissector plugins. I'd rather avoid this. My only recourse is to include the helper dll in the root directory as Wireshark.exe at deployment and let the plugin know to go two directories down (instead of one in the build directory of the solution for debugging) to locate and load it.</p></div><div id="comment-48658-info" class="comment-info"><span class="comment-age">(21 Dec '15, 07:02)</span> <span class="comment-user userinfo">coloncm</span></div></div><span id="48664"></span><div id="comment-48664" class="comment"><div id="post-48664-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info, I understand the issue.</p><p>The CMake system (nor NSIS) isn't set-up to handle that at the moment. Please raise an enhancement request on the Wireshark <a href="https://bugs.wireshark.org">Bugzilla</a>, or even better submit a change when you have it worked out.</p></div><div id="comment-48664-info" class="comment-info"><span class="comment-age">(21 Dec '15, 09:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48635" class="comment-tools"></div><div class="clear"></div><div id="comment-48635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

