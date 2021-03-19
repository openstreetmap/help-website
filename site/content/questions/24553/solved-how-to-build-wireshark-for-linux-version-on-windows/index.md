+++
type = "question"
title = "[SOLVED] How to build &quot;Wireshark for Linux version&quot; on Windows"
description = '''Hi all, I&#x27;m trying to build Wireshark on Windows Enviroment. I have already finished the Wireshark Windows version by using nmake and now I&#x27;m going to build Linux version. I have some questions to ask:   Can I build the Wireshark for Linux version on Windows OS? because I don&#x27;t have server installed...'''
date = "2013-09-11T02:54:00Z"
lastmod = "2013-09-18T03:54:00Z"
weight = 24553
keywords = [ "build", "linux" ]
aliases = [ "/questions/24553" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[SOLVED\] How to build "Wireshark for Linux version" on Windows](/questions/24553/solved-how-to-build-wireshark-for-linux-version-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24553-score" class="post-score" title="current number of votes">0</div><span id="post-24553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm trying to build Wireshark on Windows Enviroment. I have already finished the Wireshark Windows version by using nmake and now I'm going to build Linux version. I have some questions to ask:</p><ol><li><p>Can I build the Wireshark for Linux version on Windows OS? because I don't have server installed Linux right now and one more reason is that my PC already had installed build environment which is quite complicated to prepare.</p></li><li><p>On Windows, if I install Ubuntu to run those commands below, is it possible to have the build for Linux version?</p></li></ol><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_7.PNG" alt="alt text" /></p><p>So, experts, please help if you have any idea or experience on that? Thank you so much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '13, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Sep '13, 02:55</strong> </span></p></div></div><div id="comments-container-24553" class="comments-container"><span id="24901"></span><div id="comment-24901" class="comment"><div id="post-24901-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@hoangsonk49</span> There's no need to edit your question title to add "[SOLVED]". Accepting the appropriate answer by clicking the checkmark does that and indicates to other users that there is a good answer to the question.</p></div><div id="comment-24901-info" class="comment-info"><span class="comment-age">(18 Sep '13, 03:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="24903"></span><div id="comment-24903" class="comment"><div id="post-24903-score" class="comment-score"></div><div class="comment-text"><p><span>@Grahamb</span>, thanks for your suggestion, I will do it that way :-)</p></div><div id="comment-24903-info" class="comment-info"><span class="comment-age">(18 Sep '13, 03:54)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div></div><div id="comment-tools-24553" class="comment-tools"></div><div class="clear"></div><div id="comment-24553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24555"></span>

<div id="answer-container-24555" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24555-score" class="post-score" title="current number of votes">2</div><span id="post-24555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't build a version for Linux on a Windows host OS. None of the correct toolchain, headers and libraries are available. You can install a version of Linux in a VM on your windows host and use that to build the Linux version, but it will use a separate copy of the sources and be built as per the developers guide for a Linux host.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '13, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24555" class="comments-container"><span id="24559"></span><div id="comment-24559" class="comment"><div id="post-24559-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb, so does this mean it is impossible to build version for Linux with Ubuntu installed on my Destop? I must install on a server or in a VM, am I right?</p></div><div id="comment-24559-info" class="comment-info"><span class="comment-age">(11 Sep '13, 04:11)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="24561"></span><div id="comment-24561" class="comment"><div id="post-24561-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure i understand "Linux installed on my desktop" If you have Linux installed then in effect it's a Linux dektop and you can build Wireshark following the instructions for a linux system I guess</p></div><div id="comment-24561-info" class="comment-info"><span class="comment-age">(11 Sep '13, 04:14)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="24563"></span><div id="comment-24563" class="comment"><div id="post-24563-score" class="comment-score"></div><div class="comment-text"><p><span>@hoangsonk49</span></p><p>I didn't mention installing Linux as a boot option as I'd thought that sort of thing had died out.</p><p>Did you install Ubuntu using the Windows installer? If so you now have a dual boot computer with both Windows and Ubuntu. Just boot in to Ubuntu and follow the dev guide for building on Linux.</p></div><div id="comment-24563-info" class="comment-info"><span class="comment-age">(11 Sep '13, 04:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="24567"></span><div id="comment-24567" class="comment"><div id="post-24567-score" class="comment-score"></div><div class="comment-text"><p>Yes, I 've just installed Ubuntu as a boot option and I'm going to try. Hope it could be done in this way. Thank you so much, grahamb:)</p></div><div id="comment-24567-info" class="comment-info"><span class="comment-age">(11 Sep '13, 05:30)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div></div><div id="comment-tools-24555" class="comment-tools"></div><div class="clear"></div><div id="comment-24555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

