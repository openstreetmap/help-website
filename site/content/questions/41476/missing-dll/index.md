+++
type = "question"
title = "missing dll"
description = '''I created a plugin it is working fine in my system as i had visual studio installed in my system.when i took the same .dll file and copied it in other system under win64 wireshark plugin directory it is giving missing msvcr120.dll while executing the wireshark.Is there any way to solve this problem....'''
date = "2015-04-16T00:10:00Z"
lastmod = "2015-04-16T03:02:00Z"
weight = 41476
keywords = [ "missing", "dll" ]
aliases = [ "/questions/41476" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [missing dll](/questions/41476/missing-dll)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41476-score" class="post-score" title="current number of votes">0</div><span id="post-41476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created a plugin it is working fine in my system as i had visual studio installed in my system.when i took the same .dll file and copied it in other system under win64 wireshark plugin directory it is giving missing msvcr120.dll while executing the wireshark.Is there any way to solve this problem.please help me with this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '15, 00:10</strong></p><img src="https://secure.gravatar.com/avatar/a2e29df6af5eb33f09d1ed5321ea6586?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakshmi&#39;s gravatar image" /><p><span>lakshmi</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakshmi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '15, 00:42</strong> </span></p></div></div><div id="comments-container-41476" class="comments-container"></div><div id="comment-tools-41476" class="comment-tools"></div><div class="clear"></div><div id="comment-41476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41477"></span>

<div id="answer-container-41477" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41477-score" class="post-score" title="current number of votes">0</div><span id="post-41477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lakshmi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you compile a plugin (or any other application) with current versions of Visual Studio, it often comes with a dependency on the C runtime library for that version of Visual Studio.</p><p>In your case, the dependency on msvcr120.dll indicates the plugin was compiled with Visual Studio 2013 (aka 12).</p><p>In addition to this, if the item is a dll, such as a plugin, then it must use the same C runtime as the application that's loading the dll.</p><p>If you're using the current release of Wireshark (1.12.x) then that was compiled with VS2010 and uses msvcr100.dll and any plugins should be compiled using the same compiler.</p><p>The current development release (1.99.x) uses the VS2013 compiler.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '15, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41477" class="comments-container"><span id="41478"></span><div id="comment-41478" class="comment"><div id="post-41478-score" class="comment-score"></div><div class="comment-text"><p>so, there is no option other than copying msvcr120.dll in the wiresahrk directory in order to execute. i compiled the wireshark using visual studio 2013. Is there any way to remove the dependency and compile my wireshark build?</p></div><div id="comment-41478-info" class="comment-info"><span class="comment-age">(16 Apr '15, 01:48)</span> <span class="comment-user userinfo">lakshmi</span></div></div><span id="41479"></span><div id="comment-41479" class="comment"><div id="post-41479-score" class="comment-score"></div><div class="comment-text"><p>You can try running the appropriate <a href="https://www.microsoft.com/en-gb/download/details.aspx?id=40784">vcredist_xxx</a> from MS which will install the VS2013 C runtime dll's, but I don't think the plugin will run due to mismatched runtime dll's.</p><p>As I explained above, currently the rules require that a dll and the application loading it must use the same C runtime version.</p><p>You can produce a complete installer with your current VS2013 build which will work, but your users must install the entire VS2013 built version, not just the plugin.</p></div><div id="comment-41479-info" class="comment-info"><span class="comment-age">(16 Apr '15, 02:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41480"></span><div id="comment-41480" class="comment"><div id="post-41480-score" class="comment-score"></div><div class="comment-text"><p>I have another doubt .I know my doubts are silly but please clarify. I have downloaded 1.12 source code and wrote a plugin and compiled it using visual studio 2013. I tried using my plugin dll in windows 1.12 installer 64 bit .it worked fine even though installer is compiled using visual studio 2010. but when i tried with the windows 1.10.3 64 bit installer and installer is also using visual studio 2010,while executing the wireshark,it is stopping in the middle when it comes to registering plugins. can i know reason for this? Is it like it will execute only in one version.</p></div><div id="comment-41480-info" class="comment-info"><span class="comment-age">(16 Apr '15, 02:25)</span> <span class="comment-user userinfo">lakshmi</span></div></div><span id="41481"></span><div id="comment-41481" class="comment"><div id="post-41481-score" class="comment-score"></div><div class="comment-text"><p>Thanks grahamb,for your quick reply.please clarify my other doubt.</p></div><div id="comment-41481-info" class="comment-info"><span class="comment-age">(16 Apr '15, 02:33)</span> <span class="comment-user userinfo">lakshmi</span></div></div><span id="41482"></span><div id="comment-41482" class="comment"><div id="post-41482-score" class="comment-score"></div><div class="comment-text"><p>Yes. Plugins can only be built for a specific major version of Wireshark.<br />
</p><p>You will need two separate builds of the plugin for 1.10.x and 1.12.x.</p><p>Having an application using one version of the C runtime and a dll using another might work, it's really not recommended. See <a href="http://stackoverflow.com/questions/19944589/how-bad-is-it-to-mix-and-match-vc-runtime-dlls-in-one-process">here</a> for a discussion on why it's a bad idea.</p><p>A final point to note, plugins must still follow the GPL requirements, in that if you distribute the plugin outside your company you must make the source code available.</p></div><div id="comment-41482-info" class="comment-info"><span class="comment-age">(16 Apr '15, 02:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41483"></span><div id="comment-41483" class="comment not_top_scorer"><div id="post-41483-score" class="comment-score"></div><div class="comment-text"><p>thank u for your reply.</p><p>Is it the same case if we write the dissector using lua? Do we have to build it for different versions?</p></div><div id="comment-41483-info" class="comment-info"><span class="comment-age">(16 Apr '15, 02:41)</span> <span class="comment-user userinfo">lakshmi</span></div></div><span id="41485"></span><div id="comment-41485" class="comment not_top_scorer"><div id="post-41485-score" class="comment-score"></div><div class="comment-text"><p>The Lua support has changed quite a bit over the versions, but if you only use the Lua API that was available in the lowest version, and implement workarounds where that API has changed in later versions, then possibly.</p><p>I think the code will have to be version aware though, and will still be subject to the GPL.</p></div><div id="comment-41485-info" class="comment-info"><span class="comment-age">(16 Apr '15, 03:02)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41477" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-41477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

