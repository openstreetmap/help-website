+++
type = "question"
title = "looking for a computer sending out spam how do I find it using wireshark?"
description = '''I am looking for a computer sending email, I have an IP of the source, I am trying to locate the machine. It is internal on our domain, we are using NAT. The emails are getting blocked, I am just trying to the computer, any ideas. All the posts I read, is to use wireshark. I have version 1.6.7 Thank...'''
date = "2012-06-15T07:56:00Z"
lastmod = "2012-06-15T10:40:00Z"
weight = 11941
keywords = [ "capture", "trace" ]
aliases = [ "/questions/11941" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [looking for a computer sending out spam how do I find it using wireshark?](/questions/11941/looking-for-a-computer-sending-out-spam-how-do-i-find-it-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11941-score" class="post-score" title="current number of votes">0</div><span id="post-11941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a computer sending email, I have an IP of the source, I am trying to locate the machine. It is internal on our domain, we are using NAT. The emails are getting blocked, I am just trying to the computer, any ideas. All the posts I read, is to use wireshark. I have version 1.6.7</p><p>Thank you</p><p>coz</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '12, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/1c3e1b9048c9fc881f6351d1f79e907f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Coz&#39;s gravatar image" /><p><span>Coz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Coz has no accepted answers">0%</span></p></div></div><div id="comments-container-11941" class="comments-container"></div><div id="comment-tools-11941" class="comment-tools"></div><div class="clear"></div><div id="comment-11941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11942"></span>

<div id="answer-container-11942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11942-score" class="post-score" title="current number of votes">0</div><span id="post-11942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>if you have the IP address of the machine, you don't necessarily need wireshark. There are several options:</p><p>If it's a windows machine:</p><ul><li>run this command on a computer that is a member of the domain: <strong><code>nbtstat -a x.x.x.x</code></strong>. Maybe you can spot the computername or even a logged on user in the output (depends on some settings in the domain)</li><li>Mount the C drive of that machine and check the local copy of the domain profiles to figure out who is working on that computer: <strong><code>net use * \\x.x.x.x\c$</code></strong>. The domain admin account will give you access to that share.</li></ul><p>If it's not a windows machine, or nbtstat did not help:</p><ul><li>ping it from a computer in the same network: <strong><code>ping x.x.x.x</code></strong><br />
</li><li>get the mac address: <strong><code>arp -a | find "x.x.x.x"</code></strong></li><li>Go to your network admin and ask him to give you the port on the switch where that MAC address is connected to.</li><li>Follow the cable to the machine</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '12, 08:12</strong> </span></p></div></div><div id="comments-container-11942" class="comments-container"><span id="11943"></span><div id="comment-11943" class="comment"><div id="post-11943-score" class="comment-score"></div><div class="comment-text"><p>Great Information but:</p><p>I have an IP of the source of the email, it's external (112.xxx.xxx.xxx). But I do not have the internal machine, which are (10.xxx.xxx.xxx). The emails are going through email server, but they are being blocked at the gateway. Like I said I have the source IP, someone might be telneting or remoting with the source IP. I am trying to locate machine that is being used on our network.</p><p>Thank you,</p><p>Coz</p></div><div id="comment-11943-info" class="comment-info"><span class="comment-age">(15 Jun '12, 08:11)</span> <span class="comment-user userinfo">Coz</span></div></div><span id="11947"></span><div id="comment-11947" class="comment"><div id="post-11947-score" class="comment-score"></div><div class="comment-text"><p>BTW: If you add a comment to my answer it will be easier to follow the conversation.</p><p>O.K. I thought the IP is on your LAN as you said: "it is internal on our domain".</p><p>Anyway, in that case you need Wireshark.</p><ul><li>Run wireshark on a mirror port of your internal mail server. See here how to do that: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></li><li>Run Wireshark with this capture filter "port 25" (see wiki, if you don't know how to do it)</li><li>Sniff until you think there is enough data (some minutes, maybe hours)</li><li>Analyze the data by looking for some string pattern you know to be in the spam mail. Use this display filter: <strong><code>tcp contains "string in spam mail"</code></strong></li><li>As soon as you find a match, look at the source IP address in Wireshark. It it's not the mail server, it's the IP address of the spammer.</li></ul><p>CONSTRAINT: if the spammer sends mail through MAPI (exchange), you need a different capture filter. Try SMTP (port 25) first and see what you find.</p></div><div id="comment-11947-info" class="comment-info"><span class="comment-age">(15 Jun '12, 08:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11966"></span><div id="comment-11966" class="comment"><div id="post-11966-score" class="comment-score"></div><div class="comment-text"><p>thanks,</p><p>I will try that. Also sorry about the confusion on the post</p><p>Coz</p></div><div id="comment-11966-info" class="comment-info"><span class="comment-age">(15 Jun '12, 09:41)</span> <span class="comment-user userinfo">Coz</span></div></div></div><div id="comment-tools-11942" class="comment-tools"></div><div class="clear"></div><div id="comment-11942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11970"></span>

<div id="answer-container-11970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11970-score" class="post-score" title="current number of votes">0</div><span id="post-11970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><em>If</em> whatever machine is doing the NAT keeps a record of the internal-IP+port-to-external-IP+port mappings it has in effect at particular times, and you know what time the spam was sent, you could try using that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 10:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-11970" class="comments-container"></div><div id="comment-tools-11970" class="comment-tools"></div><div class="clear"></div><div id="comment-11970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

