+++
type = "question"
title = "Internet Protocol Version 4, Src: Dst: question"
description = '''Internet Protocol Version 4, Src: 10.1.73.73 (10.1.73.73), Dst: 10.1.10.71 (10.1.10.71) This is what I&#x27;m seeing. The problem is that these are 2 diffrent networks and i don&#x27;t have any rules set up for them to see each other on my firewall, so i&#x27;m wondering how i can find that out. Thanks'''
date = "2016-01-13T07:29:00Z"
lastmod = "2016-01-13T08:11:00Z"
weight = 49172
keywords = [ "protocol", "interet" ]
aliases = [ "/questions/49172" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Internet Protocol Version 4, Src: Dst: question](/questions/49172/internet-protocol-version-4-src-dst-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49172-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Internet Protocol Version 4, Src: 10.1.73.73 (10.1.73.73), Dst: 10.1.10.71 (10.1.10.71)</p><p>This is what I'm seeing. The problem is that these are 2 diffrent networks and i don't have any rules set up for them to see each other on my firewall, so i'm wondering how i can find that out.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">protocol interet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '16, 07:29</strong></p><img src="https://secure.gravatar.com/avatar/139c12c9dbf49deae2cbd6872627c917?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kobe%20310&#39;s gravatar image" /><p>kobe 310<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kobe 310 has no accepted answers">0%</span></p></div></div><div id="comments-container-49172" class="comments-container"></div><div id="comment-tools-49172" class="comment-tools"></div><div class="clear"></div><div id="comment-49172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49174"></span>

<div id="answer-container-49174" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49174-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Too little information given, but if you look just at a single packet, you can merely see that the src machine has sent such packet and sent it to the dst. This does not imply that this packet has ever made it to the destination machine. Can you be more specific about what really bothers you and why?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '16, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-49174" class="comments-container"><span id="49179"></span><div id="comment-49179" class="comment"><div id="post-49179-score" class="comment-score"></div><div class="comment-text"><p>i guess what i'm asking is, since wireshark showed it, it must be, and how would 73.73 even know that 10.71 was a destination , they are on 2 separate networks, and shouldn't be able to see each other at all.</p><p>this is going through a cisco asa firewall, with these 2 on seperate interfaces within the asa,which i just learned how to set up, so i guess i would just like to know how they know about each other, when i would think it would be impossible.</p><p>It doesn't bother me, just trying to figure out how to use wireshark, new to this, but not good at reading and understanding, hands on is best for me.</p><p>Thanks</p></div><div id="comment-49179-info" class="comment-info"><span class="comment-age">(13 Jan '16, 09:52)</span> kobe 310</div></div><span id="49180"></span><div id="comment-49180" class="comment"><div id="post-49180-score" class="comment-score"></div><div class="comment-text"><p>It seems to me that Wireshark is not the main subject here :-)</p><p>An application which sends a packet to some destination IP may have learned about the very existence of that IP by several means:</p><ul><li><p>it could have been manually (statically) configured to use it</p></li><li><p>it could have received it as an answer to a DNS query, like "which IP address represents hostname my.forged-domain.org?"</p></li><li><p>it could have received that IP inside a message of some other protocol (e.g., a Voice over IP control protocol like SIP may indicate a destination for an audio or video stream which may be a totally different machine than the one sending the SIP message)</p></li></ul><p>In all the above cases (and maybe some others too, these are typical representatives):</p><ul><li><p>the machine sending the packet didn't need to be in contact with the destination of the packet previously,</p></li><li><p>the source of the information about existence of the dst IP has no knowledge that there is some packet filtering device between the src IP and the dst IP.</p></li></ul><p>Or, from the perspective of verification of your ASA configuration: if you can see, at the machine at which you capture, that packets have arrived to it <em>from</em> an IP for which it should not be accessible, then your ASA (or a firewall in general) is not configured properly. If you only can see packets with src IP of the machine at which you capture, and only their dst IPs belong to machines which should not be accessible to it, it is not an indication of an issue of ASA configuration.</p></div><div id="comment-49180-info" class="comment-info"><span class="comment-age">(13 Jan '16, 10:34)</span> sindy</div></div><span id="49187"></span><div id="comment-49187" class="comment"><div id="post-49187-score" class="comment-score"></div><div class="comment-text"><p>Awesome, thanks alot for going into detail!!!! ASA definitely configured right, cisco tech support helped me set up.</p><p>would it be possible to trace and track what is causing that, i love challenges.</p></div><div id="comment-49187-info" class="comment-info"><span class="comment-age">(13 Jan '16, 12:39)</span> kobe 310</div></div><span id="49188"></span><div id="comment-49188" class="comment"><div id="post-49188-score" class="comment-score"></div><div class="comment-text"><p>Sure, that is what Wireshark has been made for. But it is much easier if you have a look at some network protocols' theory first, or, if tutorials make you sick, at least get acquainted with the network traffic by observing regular behaviour, like e.g. opening a not-yet-visited web page, which should first cause a DNS query to the site name, and then a http GET request to (one of) the IP address(es) which the response to that DNS query has indicated (or about a hundred occurrences of that scenario if by chance that site is full of advertisements from different sources).</p></div><div id="comment-49188-info" class="comment-info"><span class="comment-age">(13 Jan '16, 12:52)</span> sindy</div></div><span id="49215"></span><div id="comment-49215" class="comment"><div id="post-49215-score" class="comment-score"></div><div class="comment-text"><p>OK, Thanks for your help!!!</p></div><div id="comment-49215-info" class="comment-info"><span class="comment-age">(14 Jan '16, 05:54)</span> kobe 310</div></div></div><div id="comment-tools-49174" class="comment-tools"></div><div class="clear"></div><div id="comment-49174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

