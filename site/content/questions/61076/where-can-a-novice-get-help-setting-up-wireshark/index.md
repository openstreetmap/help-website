+++
type = "question"
title = "Where can a novice get help setting up Wireshark?"
description = '''I want to use Wireshark to keep an eye on my family&#x27;s activity while at home; phone calls, text messages, websites, etc. I&#x27;ve installed Wireshark, but have no idea how to set it up. When I open the program it looks like Latin to me. Where can I get help to setup up the program for my simple purpose?...'''
date = "2017-04-27T07:52:00Z"
lastmod = "2017-04-28T11:17:00Z"
weight = 61076
keywords = [ "home", "setup", "newbie", "wireshark" ]
aliases = [ "/questions/61076" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where can a novice get help setting up Wireshark?](/questions/61076/where-can-a-novice-get-help-setting-up-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61076-score" class="post-score" title="current number of votes">0</div><span id="post-61076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use Wireshark to keep an eye on my family's activity while at home; phone calls, text messages, websites, etc. I've installed Wireshark, but have no idea how to set it up. When I open the program it looks like Latin to me. Where can I get help to setup up the program for my simple purpose? I've tried to read the User's Guide and other guides on the internet, but I can't understand any of them. Please please help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-home" rel="tag" title="see questions tagged &#39;home&#39;">home</span> <span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '17, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/ee8fecfd1d195fdc5fe200dfe9b4b5f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BWnBama&#39;s gravatar image" /><p><span>BWnBama</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BWnBama has no accepted answers">0%</span></p></div></div><div id="comments-container-61076" class="comments-container"></div><div id="comment-tools-61076" class="comment-tools"></div><div class="clear"></div><div id="comment-61076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61108"></span>

<div id="answer-container-61108" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61108-score" class="post-score" title="current number of votes">1</div><span id="post-61108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would attempt to build trust through communication. Gathering intelligence this way probably won't help them trust you any more than you trust them.</p><p>However, if Wireshark is still the route you'd like to take, I would probably "<a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Capture using a machine-in-the-middle</a>" and place the machine between your router and your cable modem, DSL modem, etc. If your modem and router are an integrated box, you can't do this--you might have to go with "Capture using a MITM (Man-In-The-Middle) software".</p><p>This won't capture phone calls and text messages. While you can use other software along with Wireshark to do that, I won't give you instructions on that because intercepting mobile-phone communication without permission is illegal (unless you work for the NSA, I guess).</p><p>Regarding the guides looking like Latin: This is because those guides are meant for super-users, software engineers, network technicians etc. If you'd like to learn the background knowledge you need for understanding the guides:</p><ol><li>Read some books computer networking</li><li>Set up a Linux PC to experiment with. Read some books on Linux and POSIX operating systems</li><li>Read some more books on TCP/IP and HTTP specifically</li></ol><p>This is what I did. It took me several years.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '17, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/2e9c62b124fec3ee23c99d84d58ca5bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="watkipet&#39;s gravatar image" /><p><span>watkipet</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="watkipet has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Apr '17, 11:20</strong> </span></p></div></div><div id="comments-container-61108" class="comments-container"></div><div id="comment-tools-61108" class="comment-tools"></div><div class="clear"></div><div id="comment-61108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

