+++
type = "question"
title = "Gather hosts information"
description = '''Hi all, I am trying to gather hosts information by using Tshark under Linux. My linux distro (Kali) is under VirtualBox, my computer is running Windows 7. By reading wireshark book (second edition) I&#x27;ve found this command: tshark -i 1 -qz hosts &amp;gt; hostsinfo.txt to export host information to a file...'''
date = "2014-04-22T05:08:00Z"
lastmod = "2014-04-22T08:23:00Z"
weight = 32050
keywords = [ "tshark" ]
aliases = [ "/questions/32050" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Gather hosts information](/questions/32050/gather-hosts-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32050-score" class="post-score" title="current number of votes">0</div><span id="post-32050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am trying to gather hosts information by using Tshark under Linux. My linux distro (Kali) is under VirtualBox, my computer is running Windows 7.</p><p>By reading wireshark book (second edition) I've found this command: <code>tshark -i 1 -qz hosts &gt; hostsinfo.txt</code> to export host information to a file called hostsinfo.txt. Unfortunately, it doesn't work.</p><p>After waiting a couples of minutes, hostsinfos.txt file is totally empty.</p><p>Any idea?</p><p>Thanks in adavance for your help.</p><p>Olivier</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '14, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/6e268eb7decc1adca019b6394269348f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olivier&#39;s gravatar image" /><p><span>Olivier</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olivier has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Apr '14, 05:10</strong> </span></p></div></div><div id="comments-container-32050" class="comments-container"></div><div id="comment-tools-32050" class="comment-tools"></div><div class="clear"></div><div id="comment-32050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32052"></span>

<div id="answer-container-32052" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32052-score" class="post-score" title="current number of votes">0</div><span id="post-32052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tshark -i 1</p></blockquote><p>well, interface 1 is probably lo0 (the loopback interface) in your VM.</p><p>Please run tshark with the <strong>name of the interface</strong> (eth0,eth1, etc.) you want to capture on</p><blockquote><p>thsark -i eth0 ....</p></blockquote><p>or figure out the interface number with dumpcap</p><blockquote><p>dumpcap -D -M</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '14, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32052" class="comments-container"><span id="32053"></span><div id="comment-32053" class="comment"><div id="post-32053-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your feedback.</p><p>no I also used tshark -i eth0.</p><p>my first network interface is well eth0.</p><pre><code>[email protected]:~# tshark -D</code></pre><ol><li>eth0</li><li>nflog</li><li>any</li><li><p>lo (Loopback)</p><p>dumpcap -D -M provides the same information</p></li></ol><p>Regards,</p><p>Olivier</p></div><div id="comment-32053-info" class="comment-info"><span class="comment-age">(22 Apr '14, 05:53)</span> <span class="comment-user userinfo">Olivier</span></div></div><span id="32054"></span><div id="comment-32054" class="comment"><div id="post-32054-score" class="comment-score"></div><div class="comment-text"><p>O.K. so, eth0 is indeed interface number 1.</p><p>So, what do you see, if you run the following command</p><blockquote><p>tshark -i eth0</p></blockquote></div><div id="comment-32054-info" class="comment-info"><span class="comment-age">(22 Apr '14, 06:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32056"></span><div id="comment-32056" class="comment"><div id="post-32056-score" class="comment-score"></div><div class="comment-text"><p>If I enter tshark -i eth0, I can see traffic (gateway, etc....) . So that's why I am so amazed. My VM is setup in bridged adapter.</p><p>Do you think I should wait for a very long time to be able to gather hosts?</p><p>Can an IPS prevent gathering hosts info?</p></div><div id="comment-32056-info" class="comment-info"><span class="comment-age">(22 Apr '14, 06:59)</span> <span class="comment-user userinfo">Olivier</span></div></div><span id="32058"></span><div id="comment-32058" class="comment"><div id="post-32058-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Do you think I should wait for a very long time to be able to gather hosts?</p></blockquote><p>No, it works within a few seconds on my Ubuntu test system.</p><p>Please run the following command for a few seconds in one window</p><blockquote><p>tshark -i 1 -qz hosts</p></blockquote><p>Then in a second window ping some servers on the internet (www.google.com, ask.wireshark.org, etc.).</p><p>After that, stop tshark with CTRL-C and post <strong>all</strong> messages printed by tshark here.</p><p>BTW: Are you able to do DNS resolving in your VM?</p></div><div id="comment-32058-info" class="comment-info"><span class="comment-age">(22 Apr '14, 07:36)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32059"></span><div id="comment-32059" class="comment"><div id="post-32059-score" class="comment-score"></div><div class="comment-text"><p>Kurt, I did what you said</p><pre><code>tshark -i 1 -qz hosts
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on &#39;eth0&#39;
503 ^C
# TShark hosts output
#
# Host data gathered from /tmp/wireshark_pcapng_eth0_20140422164754_ISPcbO

162.159.241.165             ask.wireshark.org
162.159.242.165             ask.wireshark.org
173.194.41.160              google.com
173.194.41.167              google.com
173.194.41.165              google.com
173.194.41.174              google.com
173.194.41.166              google.com
173.194.41.168              google.com
173.194.41.161              google.com
173.194.41.169              google.com
173.194.41.164              google.com
173.194.41.163              google.com
173.194.41.162              google.com
64.4.11.37              microsoft.com
65.55.58.201                microsoft.com</code></pre><p>I didn't configure DNS resolving in my VM. I am using demo.local domain.</p></div><div id="comment-32059-info" class="comment-info"><span class="comment-age">(22 Apr '14, 07:52)</span> <span class="comment-user userinfo">Olivier</span></div></div><span id="32062"></span><div id="comment-32062" class="comment not_top_scorer"><div id="post-32062-score" class="comment-score"></div><div class="comment-text"><p>Well, tshark prints the hosts output, as you can see.</p><p>So, what exactly does not work?</p><blockquote><p>After waiting a couples of minutes, hostsinfos.txt file is totally empty.</p></blockquote><p>Did you check the file content while tshark was running?</p><p>If so, you'll have to end tshark to get the results, either on the console or in the file!</p></div><div id="comment-32062-info" class="comment-info"><span class="comment-age">(22 Apr '14, 08:23)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32052" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-32052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

