+++
type = "question"
title = "Wireshark does not see traffic from other devices (VirtualBox)"
description = '''Hello, I feel like i searched the whole internet and found almost no solution. I use Wireshark on Backtrack in VirtualBox on a OSX System.  But wireshark only sees the traffic from the Backtrack distribution. No traffic from the host itself or my mobile phone. When I sniff on the same port (eth1) wi...'''
date = "2013-01-05T13:57:00Z"
lastmod = "2013-02-15T11:07:00Z"
weight = 17476
keywords = [ "osx", "backtrack", "traffic", "virtualbox", "wireshark" ]
aliases = [ "/questions/17476" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not see traffic from other devices (VirtualBox)](/questions/17476/wireshark-does-not-see-traffic-from-other-devices-virtualbox)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17476-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17476-score" class="post-score" title="current number of votes">0</div><span id="post-17476-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I feel like i searched the whole internet and found almost no solution.</p><p>I use Wireshark on Backtrack in VirtualBox on a OSX System. But wireshark only sees the traffic from the Backtrack distribution. No traffic from the host itself or my mobile phone.</p><p>When I sniff on the same port (eth1) with ettercap I see everything I think.</p><p>Virtual Box is configured in Bridge Mode on eth1</p><p>Maybe you guys know something about the problem, I read about something with newer Versions of Virtual Box but it didnt work out for me.</p><p>Thanks for all the tipps!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-backtrack" rel="tag" title="see questions tagged &#39;backtrack&#39;">backtrack</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-virtualbox" rel="tag" title="see questions tagged &#39;virtualbox&#39;">virtualbox</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '13, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/679badf3748310a2500e8450e537273e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brrenni&#39;s gravatar image" /><p><span>brrenni</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brrenni has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Feb '13, 12:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-17476" class="comments-container"></div><div id="comment-tools-17476" class="comment-tools"></div><div class="clear"></div><div id="comment-17476-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18662"></span>

<div id="answer-container-18662" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18662-score" class="post-score" title="current number of votes">0</div><span id="post-18662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So, I am not the only one!</p><p>I am running Wireshark in a Virtualbox Windows 7 setup (both host and client). Wireshark on the host side has no trouble seeing GOOSE packets coming through from the tester but from the client side, it only reports SSDP packets - no GOOSE.</p><p>My network knowledge is limited to know how to Bridge the packets over to the virtual NIC.</p><p>All I had to do was to change the NIC from NAT to Bridged Adapter and Wireshark works on the client side as well. Great!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '13, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/4025240b8c0475c260d9cb7529e827c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ecs1749&#39;s gravatar image" /><p><span>ecs1749</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ecs1749 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Feb '13, 16:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18662" class="comments-container"></div><div id="comment-tools-18662" class="comment-tools"></div><div class="clear"></div><div id="comment-18662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

