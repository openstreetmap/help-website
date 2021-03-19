+++
type = "question"
title = "Wireshark without root - Can&#x27;t restart anymore"
description = '''I run a remote server that requires wireshark for debugging purposes and I wanted to have a php script start/stop wireshark at a users request. Using &quot;wireshark&quot; as a normal user did not open it as I had to have root privilege and every time I ran it using &quot;sudo wireshark&quot;, I got an LUA error about ...'''
date = "2015-07-16T12:44:00Z"
lastmod = "2015-07-17T13:21:00Z"
weight = 44218
keywords = [ "boot-process", "root", "restart", "wireshark" ]
aliases = [ "/questions/44218" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark without root - Can't restart anymore](/questions/44218/wireshark-without-root-cant-restart-anymore)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44218-score" class="post-score" title="current number of votes">0</div><span id="post-44218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I run a remote server that requires wireshark for debugging purposes and I wanted to have a php script start/stop wireshark at a users request. Using "wireshark" as a normal user did not open it as I had to have root privilege and every time I ran it using "sudo wireshark", I got an LUA error about permissions so I was looking for a solution that allowed me to run wireshark without root and came across a blog: <a href="https://blog.wireshark.org/2010/02/running-wireshark-as-you/">https://blog.wireshark.org/2010/02/running-wireshark-as-you/</a></p><pre><code> $ sudo -s
 # groupadd -g wireshark
 # usermod -a -G wireshark admin
 # chmod 750 /usr/bin/dumpcap
 # setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap</code></pre><p>I reset the server after entering the code above and while that did get wireshark to open how I wanted, now I am having issues when restarting the server. I have tried all possible ways to restart the system and each one ends with the server just shutting off instead of rebooting. This is the only system change that happened during this boot cycle so I am assuming this code screwed something up. Is there anyway to reverse the code listed above?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-boot-process" rel="tag" title="see questions tagged &#39;boot-process&#39;">boot-process</span> <span class="post-tag tag-link-root" rel="tag" title="see questions tagged &#39;root&#39;">root</span> <span class="post-tag tag-link-restart" rel="tag" title="see questions tagged &#39;restart&#39;">restart</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '15, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/b31f8a25e65b77f3925b1fa825dbe336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dirtyrobinson&#39;s gravatar image" /><p><span>dirtyrobinson</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dirtyrobinson has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jul '15, 10:58</strong> </span></p></div></div><div id="comments-container-44218" class="comments-container"></div><div id="comment-tools-44218" class="comment-tools"></div><div class="clear"></div><div id="comment-44218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44258"></span>

<div id="answer-container-44258" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44258-score" class="post-score" title="current number of votes">0</div><span id="post-44258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I run a <strong>headless</strong> remote server that requires wireshark for debugging purposes and I wanted to have a php script start/stop wireshark at a users request.</p></blockquote><p>Wait a moment: Are you trying to start the <strong>GUI</strong> version of Wireshark on a system <strong>without display</strong> through a php script on a web server? If so, that's not going to work very well, no matter what your admin privileges are.</p><p>If it's correct what I assume, you should use dumpcap and/or tshark instead of Wireshark.</p><p>If I got it wrong, please add more details to your problem description and what you want to achieve.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '15, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jul '15, 11:01</strong> </span></p></div></div><div id="comments-container-44258" class="comments-container"><span id="44261"></span><div id="comment-44261" class="comment"><div id="post-44261-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I typed headless initially and changed it to remote, I didn't realize it wasn't deleted, so I would be starting the GUI version. The server holds files for a mobile application that communicates with databases. I hop on and run wireshark when something requires debugging, since I'm not always in a position to start it, I just wanted to have the user push a button to start wireshark themselves so I can come back and look at the logs.</p><p>Regardless, I couldn't find any information on what is causing this issue so I just uninstalled everything related to wireshark. After uninstalling, the server was back to normal so I entered the same command. Once again when I tell my server to reboot, it shuts off and doesn't power back up until I manually turn it on.<br />
</p><p>I replicated the issue a few times and have decided to just abandon the project altogether. I am so perplexed as to why it's caused the issue so I will instead set it up manually like I have been.</p><p>The server is running Debian Wheezy Linux 3.8.13.30. I'm think I'm gonna post this issue to some linux forums. Thanks Kurt.</p></div><div id="comment-44261-info" class="comment-info"><span class="comment-age">(17 Jul '15, 11:20)</span> <span class="comment-user userinfo">dirtyrobinson</span></div></div><span id="44262"></span><div id="comment-44262" class="comment"><div id="post-44262-score" class="comment-score"></div><div class="comment-text"><p>So, your real problem is that your Linux server does not reboot any longer? If so, I don't think this community will be able to help you. That problem is certainly not related to the Wireshark installation or the commands your ran.</p></div><div id="comment-44262-info" class="comment-info"><span class="comment-age">(17 Jul '15, 11:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="44268"></span><div id="comment-44268" class="comment"><div id="post-44268-score" class="comment-score"></div><div class="comment-text"><p>Yea, I thought at first it was because of wireshark but after replicating it and looking at similar reboot issues I agree that its a linux issue. Thanks again!</p></div><div id="comment-44268-info" class="comment-info"><span class="comment-age">(17 Jul '15, 13:21)</span> <span class="comment-user userinfo">dirtyrobinson</span></div></div></div><div id="comment-tools-44258" class="comment-tools"></div><div class="clear"></div><div id="comment-44258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

