+++
type = "question"
title = "How do you cross compile wireshark using MontaVista&#x27;s tools?"
description = '''I&#x27;m wanting to compile wireshark so I can use it on an ARM platform. I keep getting a configuration error &quot;Function &#x27;socket&#x27; not found.&quot; I can do a ./configure with no options just fine and make and make install. But when I run the following command, it gives me that error: CC=/opt/mv_pro_5.0.0/mont...'''
date = "2013-09-05T12:27:00Z"
lastmod = "2014-01-22T05:42:00Z"
weight = 24394
keywords = [ "cross-compile", "arm" ]
aliases = [ "/questions/24394" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do you cross compile wireshark using MontaVista's tools?](/questions/24394/how-do-you-cross-compile-wireshark-using-montavistas-tools)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24394-score" class="post-score" title="current number of votes">0</div><span id="post-24394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wanting to compile wireshark so I can use it on an ARM platform. I keep getting a configuration error "Function 'socket' not found."</p><p>I can do a ./configure with no options just fine and make and make install. But when I run the following command, it gives me that error:</p><pre><code>CC=/opt/mv_pro_5.0.0/montavista/pro/devkit/arm/v5t_le/bin/arm_v5t_le-gcc ./configure --host=armv5tl-montavista-linux-gnueabi --prefix=/home/user/workdir</code></pre><p>Help would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cross-compile" rel="tag" title="see questions tagged &#39;cross-compile&#39;">cross-compile</span> <span class="post-tag tag-link-arm" rel="tag" title="see questions tagged &#39;arm&#39;">arm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '13, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/13a19952b4ec0e8e429a29bb12078783?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sariibunbun&#39;s gravatar image" /><p><span>sariibunbun</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sariibunbun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jan '14, 19:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-24394" class="comments-container"><span id="24400"></span><div id="comment-24400" class="comment"><div id="post-24400-score" class="comment-score"></div><div class="comment-text"><p>What does the config.out file say? (You probably won't be able to paste its entire contents as an answer to the question, so you might have to upload it to a site such as <a href="http://pastebin.com">pastebin</a> and post a link here.)</p></div><div id="comment-24400-info" class="comment-info"><span class="comment-age">(05 Sep '13, 17:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="24424"></span><div id="comment-24424" class="comment"><div id="post-24424-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy,</p><p>Did you mean config.log? I have that, but not the config.out. I uploaded it to pastebin like you suggested. <a href="http://pastebin.com/YupRftDp">config.log</a></p><p>Some errors caught my eye as I've been skimming through the log to try to figure this out on my own:</p><p>/opt/mv_pro_5.0.0/montavista/pro/devkit/arm/v5t_le/bin/../lib/gcc/armv5tl-montavista-linux-gnueabi/4.2.0/../../../../armv5tl-montavista-linux-gnueabi/bin/ld: cannot find -lnl-route-3</p><p>I'm not sure if this is what is causing it to fail or if it's something else. I do know I have those libraries, but I'm unsure if it's just looking in the wrong spot? I'm also unsure how to change it to look in the right spot either(I'm a little new to this, so please bare with me).</p><p>Thanks again!</p><p><em>this is the third time trying to reply to you-it keeps getting blocked my Akismet</em></p></div><div id="comment-24424-info" class="comment-info"><span class="comment-age">(06 Sep '13, 06:07)</span> <span class="comment-user userinfo">sariibunbun</span></div></div></div><div id="comment-tools-24394" class="comment-tools"></div><div class="clear"></div><div id="comment-24394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24437"></span>

<div id="answer-container-24437" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24437-score" class="post-score" title="current number of votes">4</div><span id="post-24437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sariibunbun has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's configure script has some places where it needs to be fixed in order to support cross-compilation. We'd have to look more at the config.log file (yes, I meant config.log, not config.out) to see all the places where it's failing; the best thing to do here is probably to file a bug on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>, and attach config.log to the bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '13, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24437" class="comments-container"><span id="24522"></span><div id="comment-24522" class="comment"><div id="post-24522-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick response, Guy! I will add the bug :)</p></div><div id="comment-24522-info" class="comment-info"><span class="comment-age">(10 Sep '13, 05:39)</span> <span class="comment-user userinfo">sariibunbun</span></div></div><span id="29076"></span><div id="comment-29076" class="comment"><div id="post-29076-score" class="comment-score"></div><div class="comment-text"><p>I'm having this problem too... Was the bug filed? Was it fixed?</p></div><div id="comment-29076-info" class="comment-info"><span class="comment-age">(21 Jan '14, 17:46)</span> <span class="comment-user userinfo">Andrew Knutsen</span></div></div><span id="29091"></span><div id="comment-29091" class="comment"><div id="post-29091-score" class="comment-score"></div><div class="comment-text"><p>I never entered the bug unfortunately. Work got crazy hectic and I found a way to fix some issues without having to compile Wireshark. Pretty sure I lost all my info for this as well...my apologies!</p></div><div id="comment-29091-info" class="comment-info"><span class="comment-age">(22 Jan '14, 05:42)</span> <span class="comment-user userinfo">sariibunbun</span></div></div></div><div id="comment-tools-24437" class="comment-tools"></div><div class="clear"></div><div id="comment-24437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

