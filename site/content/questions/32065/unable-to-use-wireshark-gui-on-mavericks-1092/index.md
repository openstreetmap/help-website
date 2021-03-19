+++
type = "question"
title = "Unable to use Wireshark GUI on Mavericks 10.9.2"
description = '''Hello, I have a MacBook Pro running OSX 10.9.2 and Wireshark 1.10.6 with XQuartz 2.7.5. If I launch Wireshark directly, it cannot see any of my network interfaces. If I launch XQuartz first and then launch Wireshark from the commandline, it still cannot see any of my network interfaces. And when I l...'''
date = "2014-04-22T10:53:00Z"
lastmod = "2014-04-23T00:12:00Z"
weight = 32065
keywords = [ "osx", "gui", "sudo", "mavericks" ]
aliases = [ "/questions/32065" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to use Wireshark GUI on Mavericks 10.9.2](/questions/32065/unable-to-use-wireshark-gui-on-mavericks-1092)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32065-score" class="post-score" title="current number of votes">0</div><span id="post-32065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a MacBook Pro running OSX 10.9.2 and Wireshark 1.10.6 with XQuartz 2.7.5. If I launch Wireshark directly, it cannot see any of my network interfaces. If I launch XQuartz first and then launch Wireshark from the commandline, it still cannot see any of my network interfaces. And when I launch XQuartz first, and then launch Wireshark with the sudo command, WIreshark can see my network interfaces just fine, however, the Wireshark GUI is completely unusable. Nothing works at all. No menus can be clicked and it is essentially completely dead.</p><p>Ideally I'd like to use Wireshark so that it can read traffic off of my network interfaces. Is this possible with Mavericks? If so, what must be done so that I can launch Wireshark, see all of my network interfaces, and then actually use the Wireshark GUI as it was intended to be used?</p><p>Any feedback would be most appreciated.</p><p>Thanks,</p><p>Wulf</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-sudo" rel="tag" title="see questions tagged &#39;sudo&#39;">sudo</span> <span class="post-tag tag-link-mavericks" rel="tag" title="see questions tagged &#39;mavericks&#39;">mavericks</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '14, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/a61955860fbe8ac5172cd1c39bd2d4ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vulfie&#39;s gravatar image" /><p><span>vulfie</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vulfie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Apr '14, 10:57</strong> </span></p></div></div><div id="comments-container-32065" class="comments-container"></div><div id="comment-tools-32065" class="comment-tools"></div><div class="clear"></div><div id="comment-32065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32071"></span>

<div id="answer-container-32071" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32071-score" class="post-score" title="current number of votes">1</div><span id="post-32071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Wulf, When you download the package from wireshark and open it there is a "Read me first.rtf" which explains the steps that the installation process will follow. Two of them are:</p><ul><li><p>/Library/StartupItems/ChmodBPF. A script which adjusts permissions on the system's packet capture devices (/dev/bpf*) when the system starts up.</p></li><li><p>Additionally a group named access_bpf is created. The user who opened the package is added to the group.</p></li></ul><p>Is your username part of access_bpf group? You can check this by giving the id command in you terminal. Also check your /dev/bpf* which should be root:access_bpf.</p><p>If you check online you will see that there's an update on wireshark to 1.10.7. <a href="https://www.wireshark.org/download.html">https://www.wireshark.org/download.html</a></p><p>BTW, I'm using development version 1.113 and it work very well with QT (without Xquartz)</p><p>Hopes this helps. Let us know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '14, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/57dca282828fcb7b6086c0a77af93ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Edmond&#39;s gravatar image" /><p><span>Edmond</span><br />
<span class="score" title="181 reputation points">181</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Edmond has 2 accepted answers">33%</span></p></div></div><div id="comments-container-32071" class="comments-container"><span id="32073"></span><div id="comment-32073" class="comment"><div id="post-32073-score" class="comment-score"></div><div class="comment-text"><p>Hi Edmond,</p><p>Eureka! I downloaded 1.10.7 as suggested and it worked like a champ! Wow, I need to start paying attention to those ReadMe files again!</p><p>Thanks so much for the help! I am now unblocked!</p><p>Very cordially,</p><p>Wulf</p></div><div id="comment-32073-info" class="comment-info"><span class="comment-age">(22 Apr '14, 17:43)</span> <span class="comment-user userinfo">vulfie</span></div></div><span id="32084"></span><div id="comment-32084" class="comment"><div id="post-32084-score" class="comment-score"></div><div class="comment-text"><p>Hi Wulf, accept my answer as the resolution to your question if it solved your problem.</p><p>Regarding the update of your wireshark, the reason that i put it last was because it was meant for you to try last :). Troubleshooting is alway the 1st step of solving a problem.</p></div><div id="comment-32084-info" class="comment-info"><span class="comment-age">(23 Apr '14, 00:12)</span> <span class="comment-user userinfo">Edmond</span></div></div></div><div id="comment-tools-32071" class="comment-tools"></div><div class="clear"></div><div id="comment-32071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

