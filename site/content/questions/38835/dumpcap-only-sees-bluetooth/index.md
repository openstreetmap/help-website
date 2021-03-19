+++
type = "question"
title = "Dumpcap only sees bluetooth?"
description = '''I have some troubles getting dumpcap to see all the available capturing interface. I added myself to the wireshark group, but dumpcap really only sees bluetooth interface and nothing else. antony@medina:~$ dumpcap -D 1. bluetooth0 antony@medina:~$ dumpcap -L Capturing on &#x27;bluetooth0&#x27; Data link types...'''
date = "2014-12-31T14:12:00Z"
lastmod = "2016-11-16T09:23:00Z"
weight = 38835
keywords = [ "ubuntu" ]
aliases = [ "/questions/38835" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Dumpcap only sees bluetooth?](/questions/38835/dumpcap-only-sees-bluetooth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38835-score" class="post-score" title="current number of votes">0</div><span id="post-38835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some troubles getting dumpcap to see all the available capturing interface. I added myself to the wireshark group, but dumpcap really only sees bluetooth interface and nothing else.</p><pre><code>[email protected]:~$ dumpcap -D
1. bluetooth0
[email protected]:~$ dumpcap -L
Capturing on &#39;bluetooth0&#39;
Data link types of interface bluetooth0 (use option -y to set):
  BLUETOOTH_HCI_H4_WITH_PHDR (Bluetooth HCI UART transport layer plus pseudo-header)
[email protected]:~$ ls -la /usr/bin/dumpcap 
-rwxr-x--- 1 root wireshark 77080 Mar 11  2014 /usr/bin/dumpcap
[email protected]:~$ groups antony
antony : antony adm cdrom sudo dip plugdev lpadmin sambashare chrome-remote-desktop wireshark

[email protected]:~$ sudo dumpcap -D
[sudo] password for antony: 
1. eth0
2. zt0
3. bluetooth0
4. nflog
5. nfqueue
6. vmnet1
7. vmnet8
8. any
9. lo (Loopback)</code></pre><p>As you can see, if I sudo dumpcap, I can see all the interfaces. Thus, clearly, wireshark group has no access to interfaces like <code>eth0</code> But really not sure how to fix it.</p><p>Running Ubuntu 14.04.1</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '14, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/9a81c141683a3e7b41f894b361d7089e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="antony&#39;s gravatar image" /><p><span>antony</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="antony has no accepted answers">0%</span></p></div></div><div id="comments-container-38835" class="comments-container"><span id="57395"></span><div id="comment-57395" class="comment"><div id="post-57395-score" class="comment-score"></div><div class="comment-text"><p>I have exactly the same problem.</p><pre><code>[email protected] ~ $ dumpcap -D
1. bluetooth0
[email protected] ~ $ dumpcap -L
Capturing on &#39;bluetooth0&#39;
Data link types of interface bluetooth0 (use option -y to set):
  BLUETOOTH_HCI_H4_WITH_PHDR (Bluetooth HCI UART transport layer plus pseudo-header)
[email protected] ~ $ ls -la /usr/bin/dumpcap
-rwxr-xr-x 1 root wireshark 77080 Mar 11  2014 /usr/bin/dumpcap
[email protected] ~ $ groups allenb
allenb : allenb root sudo smbusers wireshark
[email protected] ~ $ sudo dumpcap -D
[sudo] password for allenb: 
1. eth0
2. wlan0
3. bluetooth0
4. nflog
5. nfqueue
6. any
7. lo (Loopback)
[email protected] ~ $</code></pre><p>I have restarted the computer several times without any success.</p><p>Any suggestions?</p><p>Thank you Allen</p></div><div id="comment-57395-info" class="comment-info"><span class="comment-age">(15 Nov '16, 10:43)</span> <span class="comment-user userinfo">Allen</span></div></div><span id="57397"></span><div id="comment-57397" class="comment"><div id="post-57397-score" class="comment-score"></div><div class="comment-text"><p>I suggest you read the answers to the question and try doing what they say.</p></div><div id="comment-57397-info" class="comment-info"><span class="comment-age">(15 Nov '16, 12:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-38835" class="comment-tools"></div><div class="clear"></div><div id="comment-38835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="38836"></span>

<div id="answer-container-38836" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38836-score" class="post-score" title="current number of votes">1</div><span id="post-38836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="antony has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you done <code>sudo dpkg-reconfigure wireshark-common</code>? If not, do so, and then try it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '14, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-38836" class="comments-container"><span id="38846"></span><div id="comment-38846" class="comment"><div id="post-38846-score" class="comment-score"></div><div class="comment-text"><p>I actually did issue <code>sudo dpkg-reconfigure wireshark-common</code> and rebooted, noticed that it wasn't working..so that's why I went through all that troubles in the original post. But I just did the same command again and rebooted... it works this time. I still can't explain why. I checked ~/.bash_history to confirm that I did indeed issue such command in the past too..</p></div><div id="comment-38846-info" class="comment-info"><span class="comment-age">(01 Jan '15, 16:18)</span> <span class="comment-user userinfo">antony</span></div></div></div><div id="comment-tools-38836" class="comment-tools"></div><div class="clear"></div><div id="comment-38836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38845"></span>

<div id="answer-container-38845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38845-score" class="post-score" title="current number of votes">0</div><span id="post-38845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you logged off then on again? I believe group permissions are only updated on logon.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '15, 14:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38845" class="comments-container"><span id="38847"></span><div id="comment-38847" class="comment"><div id="post-38847-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>, please see my comment to Guy Harris. I am a little dumbfounded that dumpcap did not work at all, after I issued the <code>sudo dpkg-reconfigure wireshark-common</code> first time...and now many reboots later... and issued the same command once more.. viola. it works.</p></div><div id="comment-38847-info" class="comment-info"><span class="comment-age">(01 Jan '15, 16:20)</span> <span class="comment-user userinfo">antony</span></div></div></div><div id="comment-tools-38845" class="comment-tools"></div><div class="clear"></div><div id="comment-38845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57421"></span>

<div id="answer-container-57421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57421-score" class="post-score" title="current number of votes">0</div><span id="post-57421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Finally fixed it. The mistake I made was not making the wireshark group a SYSTEM group. I back tracked and removed everything and started again and it's now working.</p><p>For user guy's benefit, I had done exactly what you had said. There wasn't a bloody thing to indicate that the group wireshark had to be a system group.</p><p>Anyway, all's well and thank you to those who helped.</p><p>Allen</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '16, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/7d297f9abce800e6c7094abf70744bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Allen&#39;s gravatar image" /><p><span>Allen</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Allen has no accepted answers">0%</span></p></div></div><div id="comments-container-57421" class="comments-container"></div><div id="comment-tools-57421" class="comment-tools"></div><div class="clear"></div><div id="comment-57421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

