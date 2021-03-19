+++
type = "question"
title = "Custom Dissector Portability"
description = '''Hi, I have a custom plug-in that I want to distribute across many different versions of Windows.  My question is, if I compile the plugin with VS2008, will I be able to simply distribute the resulting DLL file and have any recipients place it in their Personal Plugins folder? I&#x27;ve tried a couple of ...'''
date = "2012-07-13T08:37:00Z"
lastmod = "2012-07-16T14:03:00Z"
weight = 12706
keywords = [ "windows", "dissector", "plugin" ]
aliases = [ "/questions/12706" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Custom Dissector Portability](/questions/12706/custom-dissector-portability)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12706-score" class="post-score" title="current number of votes">0</div><span id="post-12706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a custom plug-in that I want to distribute across many different versions of Windows.</p><p>My question is, if I compile the plugin with VS2008, will I be able to simply distribute the resulting DLL file and have any recipients place it in their Personal Plugins folder? I've tried a couple of different versions so far and it seems to work fine but it's important that I be sure of this.</p><p>Thanks!</p><p>Ben</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '12, 08:37</strong></p><img src="https://secure.gravatar.com/avatar/64351fbd3990575fed5ca68934252c1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bblack&#39;s gravatar image" /><p><span>bblack</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bblack has no accepted answers">0%</span></p></div></div><div id="comments-container-12706" class="comments-container"></div><div id="comment-tools-12706" class="comment-tools"></div><div class="clear"></div><div id="comment-12706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12780"></span>

<div id="answer-container-12780" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12780-score" class="post-score" title="current number of votes">1</div><span id="post-12780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bblack has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>AFIAK the plugin must be compiled with the same compiler version as wireshark.</p><blockquote><p><code>http://ask.wireshark.org/questions/12153/couldnt-load-modulespecified-module-cannot-be-found</code></p></blockquote><p>Besides that, there should be not much you need to consider, as everything else (VC++ distributable, etc.) should be handled by wireshark. As soon as Wireshark runs on a windows version, and you compiled your plugin with the same compiler, your plugin should work on that platform as well.</p><p>HOWEVER: I'm not sure if there is a difference in the way how 32/64 bit builds of wireshark load plugins. So you might have to provide both a 32 and a 64 bit version of your plugin (just guessing!!!).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-12780" class="comments-container"><span id="12785"></span><div id="comment-12785" class="comment"><div id="post-12785-score" class="comment-score"></div><div class="comment-text"><p>As Kurt says, the plugin DLL must be compiled with the same version of Visual Studio as Wireshark, the actual dependency is the C run-time library used by both items.</p><p>Wireshark and the DLL must use the same number of bits, a 32 bit Wireshark cannot load a 64 bit DLL and vice versa.</p><p>Unfortunately the plugin interface isn't guaranteed to remain compatible, so you may have to provide different DLL's for different versions of Wireshark. The easy way around this is to submit your plugin to the project and have it included in every copy of Wireshark with no further effort.</p></div><div id="comment-12785-info" class="comment-info"><span class="comment-age">(16 Jul '12, 14:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-12780" class="comment-tools"></div><div class="clear"></div><div id="comment-12780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

