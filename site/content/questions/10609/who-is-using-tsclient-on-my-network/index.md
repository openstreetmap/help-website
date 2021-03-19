+++
type = "question"
title = "Who is using &quot;tsclient&quot; on my network?"
description = '''Hello, I respectfully ask if someone can assist me in sniffing out who is &quot;tsclient&quot; on my network.'''
date = "2012-05-02T10:31:00Z"
lastmod = "2012-05-07T12:59:00Z"
weight = 10609
keywords = [ "tsclient" ]
aliases = [ "/questions/10609" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Who is using "tsclient" on my network?](/questions/10609/who-is-using-tsclient-on-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10609-score" class="post-score" title="current number of votes">0</div><span id="post-10609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I respectfully ask if someone can assist me in sniffing out who is "tsclient" on my network.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tsclient" rel="tag" title="see questions tagged &#39;tsclient&#39;">tsclient</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '12, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/d055fba27abd7f4ac2f11207162e3758?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="crobinso777&#39;s gravatar image" /><p><span>crobinso777</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="crobinso777 has no accepted answers">0%</span></p></div></div><div id="comments-container-10609" class="comments-container"><span id="10610"></span><div id="comment-10610" class="comment"><div id="post-10610-score" class="comment-score"></div><div class="comment-text"><p>where did you find that string. Please provide as much information as possible.</p><p>BTW: if you are talking about the linux "Terminal Server Client [tsclient]", there is no chance to detect that with wireshark, as tsclient is just a GUI wrapper for rdesktop and other remote access tools.</p></div><div id="comment-10610-info" class="comment-info"><span class="comment-age">(02 May '12, 10:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10614"></span><div id="comment-10614" class="comment"><div id="post-10614-score" class="comment-score"></div><div class="comment-text"><p>thanks for your reply!!! not sure what it is linux. just see it on the network on and off. Currently, it's back on the network. Can't ping it, can't remote to it, can't resolve an ip from it....</p></div><div id="comment-10614-info" class="comment-info"><span class="comment-age">(02 May '12, 13:24)</span> <span class="comment-user userinfo">crobinso777</span></div></div><span id="10621"></span><div id="comment-10621" class="comment"><div id="post-10621-score" class="comment-score"></div><div class="comment-text"><p>where do you see it on the network? Where do you see that string?</p></div><div id="comment-10621-info" class="comment-info"><span class="comment-age">(02 May '12, 23:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10634"></span><div id="comment-10634" class="comment"><div id="post-10634-score" class="comment-score"></div><div class="comment-text"><p>Hello Kurt. actually it is not a string. From a Windows 7 PC, i open up Windows Explorer and browse the "Network" folder. Within that folder I see all of the computers, servers and print devices on my network. I also see "tsclient" in the listing as though it was a computer on my network. However, I cannot ping it, i cannot remote to it, i cannot do anything to it. It's there sometimes and then it is not there. So my goal is to utilize a tool such as Wireshark to help me with monitoring this estranged "tsclient".</p></div><div id="comment-10634-info" class="comment-info"><span class="comment-age">(03 May '12, 06:42)</span> <span class="comment-user userinfo">crobinso777</span></div></div></div><div id="comment-tools-10609" class="comment-tools"></div><div class="clear"></div><div id="comment-10609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10637"></span>

<div id="answer-container-10637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10637-score" class="post-score" title="current number of votes">0</div><span id="post-10637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>&gt;&gt; From a Windows 7 PC, i open up Windows Explorer and browse the "Network" folder</p><p>O.K. that's the important information. Indeed, it could be a system on your network. You can't ping it because name resolution might not work for that machine (DNS and/or Netbios), or it simply does not answer.</p><p>If you see that name again, run Wireshark without any capture filter for a few minutes. Then browse the network again. Stop wireshark and try to find that name in the capture file. I'm not sure if you will find anything, as that depends on your networks structure (Domain: yes/no, Windows 2008 Server: yes/no, etc.). In parallel run these commands in a DOS box:</p><p>nbtstat -n<br />
nbtstat -r<br />
arp -a<br />
ipconfig /displaydns<br />
</p><p>If you can't interpret all that information yourself, do what you can and come back with that information.</p><p>Any further ideas?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '12, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-10637" class="comments-container"><span id="10642"></span><div id="comment-10642" class="comment"><div id="post-10642-score" class="comment-score"></div><div class="comment-text"><p>Great help, Kurt!!! I was able to do "process of elimination" and found the culprit; a Windows Vista machine doing remote sessions. i found this forum session to be very helpful! i am still going to setup a capture to learn more about packet types associated with remote desktop. Thanks again for being responsive, Kurt!! Chris R.</p></div><div id="comment-10642-info" class="comment-info"><span class="comment-age">(03 May '12, 08:45)</span> <span class="comment-user userinfo">crobinso777</span></div></div><span id="10643"></span><div id="comment-10643" class="comment"><div id="post-10643-score" class="comment-score"></div><div class="comment-text"><p>I'm glad I was able to help.</p><p>Could you please comment how you actually found the problem?</p><p>Thank you!</p><p>Regards<br />
Kurt</p></div><div id="comment-10643-info" class="comment-info"><span class="comment-age">(03 May '12, 09:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="10744"></span><div id="comment-10744" class="comment"><div id="post-10744-score" class="comment-score"></div><div class="comment-text"><p>Well Kurt, all i can say is what I mentioned before regarding seeing tsclient in the network directory from time to time. I began to get a little suspicious in that i could not identify this device on the network and wanted to see what kind of traffic was going to/from this device. At the same time i googled the problem and some of the responses mentioned "Vist Machine". I only have one on the network so I turned the machine off and noticed "tsclient" went away. Turned it back on and there it was again. Strange, but that's what i did. CR</p></div><div id="comment-10744-info" class="comment-info"><span class="comment-age">(07 May '12, 12:59)</span> <span class="comment-user userinfo">crobinso777</span></div></div></div><div id="comment-tools-10637" class="comment-tools"></div><div class="clear"></div><div id="comment-10637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

