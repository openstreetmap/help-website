+++
type = "question"
title = "What is going on here! Wireshark capture analysis."
description = '''Just started Wireshark and loving it so far, slowly working my way through the documentation and getting the hang of it, however, I was wondering if a guru could give me a bit of advice to what is going on in these two instances. Firstly, 192.168.1.3 is appearing a lot, what is it? I don&#x27;t believe I...'''
date = "2016-08-08T07:11:00Z"
lastmod = "2016-08-08T08:23:00Z"
weight = 54662
keywords = [ "capture", "analysis", "wireshark" ]
aliases = [ "/questions/54662" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is going on here! Wireshark capture analysis.](/questions/54662/what-is-going-on-here-wireshark-capture-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54662-score" class="post-score" title="current number of votes">0</div><span id="post-54662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just started Wireshark and loving it so far, slowly working my way through the documentation and getting the hang of it, however, I was wondering if a guru could give me a bit of advice to what is going on in these two instances.</p><p>Firstly, 192.168.1.3 is appearing a lot, what is it? I don't believe I have a .3 full stop, somebodies Laptop or something maybe?</p><pre><code>192.168.1.254   192.168.1.255   NBNS    92  Name query NB HOME&lt;1d&gt;
192.168.1.3 224.0.0.1   IGMPv3  60  Membership Query, general
192.168.1.254   224.0.0.1   IGMPv3  60  Membership Query, general
192.168.1.254   192.168.1.255   BROWSER 271 Host Announcement BTHUB3, Workstation, Server, Print Queue Server, Xenix Server, NT Workstation, NT Server, Potential Browser, DFS server
192.168.1.3 224.0.0.1   IGMPv3  60  Membership Query, general
192.168.1.254   224.0.0.1   IGMPv3  60  Membership Query, general
192.168.1.3 224.0.0.1   IGMPv3  60  Membership Query, general
192.168.1.254   192.168.1.255   NBNS    92  Name query NB HOME&lt;1d&gt;
Sagemcom_c1:bc:c3   Broadcast   ARP 60  Who has 192.168.1.254? Tell 192.168.1.3
192.168.1.254   224.0.0.1   IGMPv3  60  Membership Query, general
192.168.1.3 224.0.0.1   IGMPv3  60  Membership Query, general
192.168.1.3 192.168.1.255   BROWSER 271 Local Master Announcement BTHUB3, Workstation, Server, Print Queue Server, Xenix Server, NT Workstation, NT Server, Master Browser, DFS server
192.168.1.3 192.168.1.255   BROWSER 249 Domain/Workgroup Announcement HOME, NT Workstation, Domain Enum
192.168.1.3 224.0.0.1   IGMPv3  60  Membership Query, general
192.168.1.254   192.168.1.255   NBNS    92  Name query NB HOME&lt;1d&gt;</code></pre><p>and secondly this below as I am struggling to work out what 192.168.1.71 actually is on my network either ha :-(</p><pre><code>192.168.1.71    192.168.1.255   NBNS    110 Registration NB &lt;01&gt;
192.168.1.71    192.168.1.255   NBNS    110 Registration NB UOD&lt;00&gt;
192.168.1.71    192.168.1.255   NBNS    92  Name query NB ISATAP&lt;00&gt;
192.168.1.71    255.255.255.255 DHCP    342 DHCP Inform   - Transaction ID 0x2de5bfde
192.168.1.71    192.168.1.255   NBNS    92  Name query NB UOD&lt;1c&gt;
192.168.1.71    192.168.1.255   NBNS    92  Name query NB ISATAP&lt;00&gt;
192.168.1.71    192.168.1.255   NBNS    92  Name query NB UOD&lt;1c&gt;
192.168.1.71    192.168.1.255   BROWSER 220 Request Announcement OLGA-HP
192.168.1.71    192.168.1.255   BROWSER 243 Host Announcement OLGA-HP, Workstation, Server, Print Queue Server, NT Workstation, Potential Browser
192.168.1.71    255.255.255.255 DHCP    342 DHCP Inform   - Transaction ID 0x2de5bfde
192.168.1.71    192.168.1.255   NBNS    92  Name query NB ISATAP.HOME&lt;00&gt;
192.168.1.71    192.168.1.255   NBNS    92  Name query NB UOD&lt;1c&gt;
192.168.1.71    192.168.1.255   NBNS    92  Name query NB ISATAP.HOME&lt;00&gt;
192.168.1.71    192.168.1.255   BROWSER 232 Browser Election Request
192.168.1.71    192.168.1.255   NBNS    92  Name query NB ISATAP.HOME&lt;00&gt;
192.168.1.71    192.168.1.255   NBNS    92  Name query NB ISATAP.HOME&lt;00&gt;
192.168.1.71    192.168.1.255   NBNS    110 Registration NB &lt;01&gt;&lt;02&gt;__MSBROWSE__&lt;02&gt;&lt;01&gt;
192.168.1.71    192.168.1.255   NBNS    110 Registration NB &lt;01&gt;&lt;02&gt;__MSBROWSE__&lt;02&gt;&lt;01&gt;
192.168.1.71    192.168.1.255   NBNS    110 Registration NB &lt;01&gt;&lt;02&gt;__MSBROWSE__&lt;02&gt;&lt;01&gt;
192.168.1.71    192.168.1.255   BROWSER 220 Request Announcement OLGA-HP
Print Queue Server, NT Workstation, Potential Browser, Master Browser
192.168.1.71    192.168.1.255   BROWSER 250 Domain/Workgroup Announcement UOD, NT Workstation, Domain Enum
192.168.1.71    192.168.1.255   BROWSER 243 Local Master Announcement OLGA-HP, Workstation, Server, 
192.168.1.71    255.255.255.255 UDP 82  49156 → 1947  Len=40
192.168.1.71    255.255.255.255 UDP 82  49156 → 1947  Len=40</code></pre><p>Any help would greatly appreciated.</p><p>Kind Regards,</p><p>Hit.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '16, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/f75e163546c5d80a69bd587eb5232bf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hitmanshark&#39;s gravatar image" /><p><span>hitmanshark</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hitmanshark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '16, 07:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-54662" class="comments-container"></div><div id="comment-tools-54662" class="comment-tools"></div><div class="clear"></div><div id="comment-54662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54664"></span>

<div id="answer-container-54664" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54664-score" class="post-score" title="current number of votes">0</div><span id="post-54664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The ARP request from .3 in this line <code>Sagemcom_c1:bc:c3   Broadcast   ARP 60  Who has 192.168.1.254? Tell 192.168.1.3</code> gives a little clue in the MAC address belongs to <a href="https://en.wikipedia.org/wiki/SAGEMCOM">SAGEMCOM</a> who make broadband and energy products.</p><p>Similarly, if you inspect the MAC address for .71 that might give you a clue. As you have posted text excerpts rather than the actual capture file we can't help you any further with that. The capture file allows us to see all the contents of the traffic which helps a lot when investigating issues.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '16, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-54664" class="comments-container"><span id="54665"></span><div id="comment-54665" class="comment"><div id="post-54665-score" class="comment-score"></div><div class="comment-text"><p>Hello Sir,</p><p>Thank you very much for your help.</p><p>Sagemcom, Sky Routers. Which I have one currently at 192.168.1.254, Sagemcom_57:f2:f0.</p><pre><code>Sagemcom_c1:bc:c8   Broadcast   ARP 60  Who has 192.168.1.254? Tell 192.168.1.3</code></pre><p>So from this, can I deduce there has been another potentional Sky Sagemcom router connected?</p><p>Regarding the .71 connection, just looking at the capture now, it relates to a MAC: IntelCor_b3:5c:f2, which I am assuming is just a NIC?</p><p>Looking at what .71 is doing, is there anyway I can deduce what exactly? As I don't see this anywhere on any other machine connected?</p><p>Much appreciated.</p><p>Kind Regards,</p><p>Hit.</p></div><div id="comment-54665-info" class="comment-info"><span class="comment-age">(08 Aug '16, 08:14)</span> <span class="comment-user userinfo">hitmanshark</span></div></div><span id="54666"></span><div id="comment-54666" class="comment"><div id="post-54666-score" class="comment-score"></div><div class="comment-text"><p>There are a couple more lines from .3 indicating it's likely to be a BT Hub making Windows filesharing announcements in the workgroup "HOME":</p><pre><code>192.168.1.3 192.168.1.255   BROWSER 271 Local Master Announcement BTHUB3, Workstation, Server, Print Queue Server, Xenix Server, NT Workstation, NT Server, Master Browser, DFS server
192.168.1.3 192.168.1.255   BROWSER 249 Domain/Workgroup Announcement HOME, NT Workstation, Domain Enum</code></pre><p>As for .71, it's also making windows filesharing announcements giving it's name as OLGA-HP in workgroup "UOD":</p><pre><code>192.168.1.71    192.168.1.255   BROWSER 243 Host Announcement OLGA-HP, Workstation, Server, Print Queue Server, NT Workstation, Potential Browser
192.168.1.71    192.168.1.255   BROWSER 250 Domain/Workgroup Announcement UOD, NT Workstation, Domain Enum</code></pre></div><div id="comment-54666-info" class="comment-info"><span class="comment-age">(08 Aug '16, 08:23)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-54664" class="comment-tools"></div><div class="clear"></div><div id="comment-54664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

