+++
type = "question"
title = "Latency issue.  Capture included."
description = '''Hello. I&#x27;m hoping someone could help me. I am having latency issues with my network with 60 users. We have a call center that relies on constant connection to the Cloud, but it&#x27;s being crippled because of a latency issue. Our internet provider Comcast has come out to examine the hardware and the lin...'''
date = "2017-05-01T15:23:00Z"
lastmod = "2017-05-02T17:51:00Z"
weight = 61144
keywords = [ "latency", "comcast", "capture" ]
aliases = [ "/questions/61144" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Latency issue. Capture included.](/questions/61144/latency-issue-capture-included)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61144-score" class="post-score" title="current number of votes">0</div><span id="post-61144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I'm hoping someone could help me. I am having latency issues with my network with 60 users. We have a call center that relies on constant connection to the Cloud, but it's being crippled because of a latency issue. Our internet provider Comcast has come out to examine the hardware and the lines to determine that there were no issues with Comcast.<br />
I've been studying my Wireshark capture results but I am pretty new to the software and I'm having a hard time processing the data.<br />
Any help would be appreciated. Thank you!</p><p><a href="https://www.dropbox.com/s/ejgz2bs4mz9qw2k/MC%20Cap.pcapng?dl=0">https://www.dropbox.com/s/ejgz2bs4mz9qw2k/MC%20Cap.pcapng?dl=0</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-comcast" rel="tag" title="see questions tagged &#39;comcast&#39;">comcast</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '17, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/16f182fc31e5d55c31911fe3c3ad2b89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rummy&#39;s gravatar image" /><p><span>rummy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rummy has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-61144" class="comments-container"><span id="61146"></span><div id="comment-61146" class="comment"><div id="post-61146-score" class="comment-score">1</div><div class="comment-text"><p>Could you please be more specific regarding the problem description. What kind of connection is affected, what are the IPs involved, what does the problem look like exactly?</p><p>Your capture contains lots of protocols, and the capture PC wasn't fast enough to grab it all correctly, so it's hard enough as it is...</p></div><div id="comment-61146-info" class="comment-info"><span class="comment-age">(01 May '17, 15:42)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="61147"></span><div id="comment-61147" class="comment"><div id="post-61147-score" class="comment-score">1</div><div class="comment-text"><p>Can you say what specific application is experiencing a slowdown, and do you know what specific network connections it uses (ie: what IP to what IP, what protocol)?</p><p>It doesn't look like you have an <em>overall</em> Internet latency issue, since if you look for example at your largest TCP sessions (eg: "tcp.stream eq 12" as a display filter, to look at that Google session), the longest TCP-level response times from Google are received by the client in 242ms (as an overall high in the whole trace).</p><p>In general, there are a lot of different applications in that trace so it's hard to say what the problem is without knowing what particular application is having a problem. Is this one of the SSL sessions?</p></div><div id="comment-61147-info" class="comment-info"><span class="comment-age">(01 May '17, 15:45)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="61157"></span><div id="comment-61157" class="comment"><div id="post-61157-score" class="comment-score"></div><div class="comment-text"><p>Good morning. Thanks for your replies. Where we're most effected is our call center. Our call center uses software called Incontact to handle in coming phone calls. We started experiencing lag in performing actions such as picking up a call, putting someone on hold, or transferring. Comcast technician came out and told us that there is something on our network that is causing latency, and I"m trying to find out if it is the incontact software that is causing it.</p><p>I was told these are the servers that Incontact uses.</p><pre><code>DAL: 216.20.235.240/28 dalsip.incontact.com dalsec.incontact.com
LAX: 216.20.237.240/28 laxsip.incontact.com laxsec.incontact.com
MUN: 216.20.255.0/28 munsip.incontact.eu munsec.incontact.eu
FRA: 216.20.254.0/28 frasip.incontact.eu frasec.incontact.eu
HKO: 205.252.219.240/28 hkosip.incontact.com hkosec.incontact.com

216.20.240.1
216.20.242.1
216.20.230.211
205.252.219.20
216.20.255.2
216.20.254.2</code></pre><p>Thank you.</p></div><div id="comment-61157-info" class="comment-info"><span class="comment-age">(02 May '17, 06:30)</span> <span class="comment-user userinfo">rummy</span></div></div><span id="61176"></span><div id="comment-61176" class="comment"><div id="post-61176-score" class="comment-score"></div><div class="comment-text"><p>If you go to Statistics &gt; Conversations &gt; IPv4, you can see that none of those IP addresses or ranges appear in your packet capture. The closest range to any of the above would be 216.58.212.0/24.</p><p>Do you know what application/protocol this voice service uses? Is it possible to get a packet capture of just a client, just when it is trying to use the service and failing?</p><p>To troubleshoot this, you need to have some understanding of how this application uses the network to provide the service. I went to the inContact website but they only seem to provide high-level descriptions for the networking aspect of this cloud service. Basically, you need to know how it's supposed to work before we can say why it isn't.</p></div><div id="comment-61176-info" class="comment-info"><span class="comment-age">(02 May '17, 17:51)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-61144" class="comment-tools"></div><div class="clear"></div><div id="comment-61144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

