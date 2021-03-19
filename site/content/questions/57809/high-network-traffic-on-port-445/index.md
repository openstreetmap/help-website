+++
type = "question"
title = "High network traffic on port 445"
description = '''Hi, I have a network performance issue and a quick wireshark capture shows a high traffic between my client and the NAS. This doesn&#x27;t occur frequently but it seems to have disrupt the office network.  Based on the capture below which lasted 10 mins, how can i go deeper into the each packets to see i...'''
date = "2016-12-03T00:33:00Z"
lastmod = "2016-12-06T11:45:00Z"
weight = 57809
keywords = [ "nas" ]
aliases = [ "/questions/57809" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [High network traffic on port 445](/questions/57809/high-network-traffic-on-port-445)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57809-score" class="post-score" title="current number of votes">0</div><span id="post-57809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a network performance issue and a quick wireshark capture shows a high traffic between my client and the NAS. This doesn't occur frequently but it seems to have disrupt the office network.</p><p>Based on the capture below which lasted 10 mins, how can i go deeper into the each packets to see if there was a bottleneck in bandwidth or was there any other possibilities that might have slow down the network?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Conversations_1.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Conversations_2.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nas" rel="tag" title="see questions tagged &#39;nas&#39;">nas</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '16, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/149d6f8eb0595bad31c406551c9654a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doran_lum&#39;s gravatar image" /><p><span>doran_lum</span><br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doran_lum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57809" class="comments-container"><span id="57812"></span><div id="comment-57812" class="comment"><div id="post-57812-score" class="comment-score"></div><div class="comment-text"><p>Easily said in your case you can use tcptrace or the smb request stats.</p><p>An other way could be that you share us a at a public accessible place like dropbox, google drive or cloudshark.</p></div><div id="comment-57812-info" class="comment-info"><span class="comment-age">(03 Dec '16, 02:18)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="57861"></span><div id="comment-57861" class="comment"><div id="post-57861-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I was looking at this link to see if it's link to a DOS attack using this vulnerability.</p><p><a href="https://www.symantec.com/security_response/vulnerability.jsp?bid=33121">https://www.symantec.com/security_response/vulnerability.jsp?bid=33121</a></p><p>pcap file: <a href="https://drive.google.com/open?id=0B6Euh1o48D7ESkpOSUVnSEo4YzQ">https://drive.google.com/open?id=0B6Euh1o48D7ESkpOSUVnSEo4YzQ</a></p></div><div id="comment-57861-info" class="comment-info"><span class="comment-age">(05 Dec '16, 04:29)</span> <span class="comment-user userinfo">doran_lum</span></div></div></div><div id="comment-tools-57809" class="comment-tools"></div><div class="clear"></div><div id="comment-57809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57870"></span>

<div id="answer-container-57870" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57870-score" class="post-score" title="current number of votes">2</div><span id="post-57870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="doran_lum has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For me the traffic on port 445 looks good. It is normal SMB (Windows network file sharing and can be used for NAS) and it seems that someone downloads a vmplayer.exe. So everything looks calm on this port to me.</p><p>But there is a lot of traffic on Port 9001. Port 9001 can be used for Sharepoint authoring or for TOR-Browsing. There is huge traffic to the internet (5.135.184.158) on that port, this could slow down your network, FW or WAN interface. The traffic comes from 192.168.70.8 on Port 53947</p><p>You can see that stas under: Statitstics -&gt; Conversations - TCP And then you can sort by each column you want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '16, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '16, 00:51</strong> </span></p></div></div><div id="comments-container-57870" class="comments-container"><span id="57897"></span><div id="comment-57897" class="comment"><div id="post-57897-score" class="comment-score"></div><div class="comment-text"><p>Thanks, how did you find out that someone was downliading the vmplayer ? I was trying to search on wireshark and networkminer but can't seem to find it.</p><p>Anyway a vmplayer.exe file would be less than 100MB, so it's unlikely it can slow down the network.</p><p>Yes for the port 9001, i show it as second highest byte under Conversations.</p></div><div id="comment-57897-info" class="comment-info"><span class="comment-age">(06 Dec '16, 05:39)</span> <span class="comment-user userinfo">doran_lum</span></div></div><span id="57898"></span><div id="comment-57898" class="comment"><div id="post-57898-score" class="comment-score"></div><div class="comment-text"><p>Sorry I found it out by filtering smb.cmd==46</p><p>I also can see .m4v files being play. May I ask how do I tell if the movie file i being download or being stream from the NAS ?</p></div><div id="comment-57898-info" class="comment-info"><span class="comment-age">(06 Dec '16, 05:52)</span> <span class="comment-user userinfo">doran_lum</span></div></div><span id="57900"></span><div id="comment-57900" class="comment"><div id="post-57900-score" class="comment-score"></div><div class="comment-text"><p>Please try this displayfilter:</p><pre><code>((smb.cmd == 0xa2) &amp;&amp; (smb.nt_status == 0x00000000) &amp;&amp; !(smb.fid.opened_in)) &amp;&amp; !(smb.file == &quot;&quot;)</code></pre><p>And there we find the evidence that Port 9001 is TOR</p></div><div id="comment-57900-info" class="comment-info"><span class="comment-age">(06 Dec '16, 06:26)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="57908"></span><div id="comment-57908" class="comment"><div id="post-57908-score" class="comment-score"></div><div class="comment-text"><p>Well, you have to enable TCP Reassembly. Right click TCP header in Packet Detail. Select Protocol preferences. Enable TCP reassembly.</p><p>Then select a SMB packet. And then choose the export SMB objects dialog. Now you get all the transfered objects.</p></div><div id="comment-57908-info" class="comment-info"><span class="comment-age">(06 Dec '16, 11:45)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-57870" class="comment-tools"></div><div class="clear"></div><div id="comment-57870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

