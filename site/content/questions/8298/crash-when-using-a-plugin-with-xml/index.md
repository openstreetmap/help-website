+++
type = "question"
title = "Crash when using a Plugin with xml"
description = '''Hi, I have written a Plugin for Wireshark wich includes the library mxml. The compile of the plugin is successfull. But when I start wireshark with my plugin wireshark crashes. Do you have any experiences with using an external dll (mxml) in your own plugin? The problem seems to be in &#x27;mxmlloadfile&#x27;...'''
date = "2012-01-10T05:46:00Z"
lastmod = "2012-01-11T03:59:00Z"
weight = 8298
keywords = [ "xml", "crash", "plugin" ]
aliases = [ "/questions/8298" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Crash when using a Plugin with xml](/questions/8298/crash-when-using-a-plugin-with-xml)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8298-score" class="post-score" title="current number of votes">0</div><span id="post-8298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have written a Plugin for Wireshark wich includes the library mxml. The compile of the plugin is successfull. But when I start wireshark with my plugin wireshark crashes. Do you have any experiences with using an external dll (mxml) in your own plugin? The problem seems to be in 'mxmlloadfile'...</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '12, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/ce79034142dc613a1a30949664b84723?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic&#39;s gravatar image" /><p><span>Nic</span><br />
<span class="score" title="14 reputation points">14</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic has no accepted answers">0%</span></p></div></div><div id="comments-container-8298" class="comments-container"></div><div id="comment-tools-8298" class="comment-tools"></div><div class="clear"></div><div id="comment-8298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8299"></span>

<div id="answer-container-8299" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8299-score" class="post-score" title="current number of votes">0</div><span id="post-8299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nic has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming, as you mention dll, your platform is Windows. If so, are you sure your external dll is linked to the same c runtime library as Wireshark and your plugin?</p><p>Try starting Wireshark under a debugger and report the error you see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '12, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-8299" class="comments-container"><span id="8300"></span><div id="comment-8300" class="comment"><div id="post-8300-score" class="comment-score"></div><div class="comment-text"><p>Sorry, forgot to mention it, yes the platform is windows. I build only the plugin and not wireshark. The plugin is running while I don't call the mxmlloadfile. When I call other functions from the dll everthing works.... I try to get the debug messages</p></div><div id="comment-8300-info" class="comment-info"><span class="comment-age">(10 Jan '12, 06:00)</span> <span class="comment-user userinfo">Nic</span></div></div><span id="8302"></span><div id="comment-8302" class="comment"><div id="post-8302-score" class="comment-score"></div><div class="comment-text"><p>Do you build the external dll. What is it (mxml)?</p></div><div id="comment-8302-info" class="comment-info"><span class="comment-age">(10 Jan '12, 08:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="8317"></span><div id="comment-8317" class="comment"><div id="post-8317-score" class="comment-score"></div><div class="comment-text"><p>mxml is a free library for xml-parsing</p></div><div id="comment-8317-info" class="comment-info"><span class="comment-age">(11 Jan '12, 02:06)</span> <span class="comment-user userinfo">Nic</span></div></div><span id="8318"></span><div id="comment-8318" class="comment"><div id="post-8318-score" class="comment-score"></div><div class="comment-text"><p>Now I found the problem. It wasn't in the plugin but in the xml-library....</p></div><div id="comment-8318-info" class="comment-info"><span class="comment-age">(11 Jan '12, 02:07)</span> <span class="comment-user userinfo">Nic</span></div></div><span id="8319"></span><div id="comment-8319" class="comment"><div id="post-8319-score" class="comment-score"></div><div class="comment-text"><p>That's not much of an answer, would you like to elaborate?</p></div><div id="comment-8319-info" class="comment-info"><span class="comment-age">(11 Jan '12, 02:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="8321"></span><div id="comment-8321" class="comment not_top_scorer"><div id="post-8321-score" class="comment-score"></div><div class="comment-text"><p>Both dlls (mxml and the wireshark dll) included mscvr90.dll (from VisualStudio 2008). The mxml-lib was build with an other version of this dll than the wireshark plugin. So the internal dependencies were wrong. This caused the crash when calling some functions from the mxml lib.</p></div><div id="comment-8321-info" class="comment-info"><span class="comment-age">(11 Jan '12, 03:49)</span> <span class="comment-user userinfo">Nic</span></div></div><span id="8322"></span><div id="comment-8322" class="comment not_top_scorer"><div id="post-8322-score" class="comment-score"></div><div class="comment-text"><p>Ok, so my original answer was in the right area, I'll move your "answer" to a comment on that answer.</p><p>Can you mark the answer as "accepted".</p></div><div id="comment-8322-info" class="comment-info"><span class="comment-age">(11 Jan '12, 03:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-8299" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-8299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

