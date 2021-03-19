+++
type = "question"
title = "Understanding IP.ID"
description = '''Can someone please explain or point me to the proper documentation that explains what the IP.ID field tells me and how to properly interpret it? I have done some searching and have been unable to find a clear definition. Thanks. '''
date = "2014-07-09T14:12:00Z"
lastmod = "2014-07-09T14:27:00Z"
weight = 34527
keywords = [ "ip.id" ]
aliases = [ "/questions/34527" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding IP.ID](/questions/34527/understanding-ipid)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34527-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone please explain or point me to the proper documentation that explains what the IP.ID field tells me and how to properly interpret it? I have done some searching and have been unable to find a clear definition. Thanks.</p></div><div id="question-tags" class="tags-container tags">ip.id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '14, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/14ab2e3eff1a124c3013b263d1424c0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="madcap&#39;s gravatar image" /><p>madcap<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="madcap has no accepted answers">0%</span></p></div></div><div id="comments-container-34527" class="comments-container"></div><div id="comment-tools-34527" class="comment-tools"></div><div class="clear"></div><div id="comment-34527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34530"></span>

<div id="answer-container-34530" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34530-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The following RFC explains it pretty much in detail</p><blockquote><p><a href="http://tools.ietf.org/html/rfc6864">http://tools.ietf.org/html/rfc6864</a></p></blockquote><p>The short story: One purpose (probably the most important one) of the IP ID field is to enable systems to distinguish IP fragments and to do de-fragmentation or reassembly.</p><p>For a troubleshooter the IP ID field is interesting as well. If you see duplicate IP IDs in a capture file, it's usually a sign for a switching/routing loop somewhere, given the capture setup is O.K. and does not create duplicate frames itself (like mirroring the wrong ports on a switch).</p><p>Furthermore, if you capture at two different places between client and server you can use the IP ID field to figure out if some frames got lost on the way, given there is no network devices on the path that does IP ID rewriting (for security reasons, or as a result of some NAT operation). You do that by comparing the (sorted) list of the IP IDs of both capture files.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '14, 14:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34530" class="comments-container"><span id="34531"></span><div id="comment-34531" class="comment"><div id="post-34531-score" class="comment-score">1</div><div class="comment-text"><p>One other use-case for the IP ID field is actually vendor detection.</p><p>For example, in mobile wireless networks when looking at dynamic "GTP" tunnel setup and teardown exchanges between operators, one major vendor uses all zeros for the IP ID fields and another follows a specific sequence for that field. Since different vendors have different default settings, timer values, and standards complacency levels, you can actually use the IP ID field from an unknown router and make a really good guess on what optional fields or procedures that router will understand, how quickly it will retransmit something, when it considers a procedure to have implicitely failed, etc., all based on the IP ID field.</p></div><div id="comment-34531-info" class="comment-info"><span class="comment-age">(09 Jul '14, 18:41)</span> Quadratic</div></div><span id="34536"></span><div id="comment-34536" class="comment"><div id="post-34536-score" class="comment-score">1</div><div class="comment-text"><p>There's more:</p><ul><li>you can detect how many devices are behind a NAT router if the router does not sanitize IP IDs</li><li>sometimes it is possible to perform some attacks by watching IP IDs increase in a certain pattern</li><li>forget IP ID as a duplicate detection mechanism as soon as you're seeing IPv6. There's no IP ID unless fragmentation headers are present.</li><li>some OSes set IP ID to random values or 0 unless its a fragment</li></ul></div><div id="comment-34536-info" class="comment-info"><span class="comment-age">(09 Jul '14, 23:50)</span> Jasper ♦♦</div></div><span id="34538"></span><div id="comment-34538" class="comment"><div id="post-34538-score" class="comment-score"></div><div class="comment-text"><p>@Quadratic: Interesting aspect. Is that some kind of 'convention' of those vendors or just a matter of fact that's being used by the carriers to do what you are describing?</p></div><div id="comment-34538-info" class="comment-info"><span class="comment-age">(10 Jul '14, 01:03)</span> Kurt Knochner ♦</div></div><span id="34539"></span><div id="comment-34539" class="comment"><div id="post-34539-score" class="comment-score"></div><div class="comment-text"><ul><li>IP ID increase pattern can also help to fingerprint an OS</li></ul></div><div id="comment-34539-info" class="comment-info"><span class="comment-age">(10 Jul '14, 01:04)</span> Kurt Knochner ♦</div></div><span id="34588"></span><div id="comment-34588" class="comment"><div id="post-34588-score" class="comment-score"></div><div class="comment-text"><p>Well, I guess you could say that vendor detection in mobile/telecom is really just OS detection, and the IP ID traits probably just come form different people having different takes on the RFC.</p><p>In oldschool telecom vendors have very monolithic systems, often developing their own protocol stacks and running them on proprietary hardware. Since a couple of the top vendors just happen to have developed fairly unique IP ID field characteristics, the result is that you can very often eye-ball the IP ID field of a GTP signaling stream and figure the vendor out. Figuring out the vendor effectively figures out the OS, and from that you have all the known limitations, features and default settings of that OS to go on.</p><p>I wouldn't say it's <em>that</em> useful, but it can make educated guesses a bit more educated.</p><p>For example, let's say that I knew the Cisco ASR 5K platform had a unique IP ID signature, and that Cisco was unique among "SGSN" vendors for not properly supporting a given data barring parameter (eg: it translates the data barring parameter into an error code to the mobile phone that knocks it off the network until a reboot, where all other vendors support the parameter and give the mobile phone a cleaner backoff time). Now, if I am thinking about using that barring parameter for my subscriber database (my "HLR"), it's useful to know how many of my subscribers are registering on Cisco ASR 5K's all around the world to gauge what that impact or trade-off would be, but there's no Vendor ID concept in SS7/MAP messages that I'm getting from those SGSNs, nor is there any in GTP setup messaging, nor is it practical to rely on cold calls to all the operators or rely on old records.</p><p>The solution? - Look for the IP ID field in GTP setup requests coming from other operators, and measure how many subscribers register how often on SGSNs with that ID signature. From that, you have an educated guess on what the impact would be if you decided you needed to start using that parameter.</p><p>That's a fictitious example, but that's the concept.</p></div><div id="comment-34588-info" class="comment-info"><span class="comment-age">(10 Jul '14, 15:21)</span> Quadratic</div></div></div><div id="comment-tools-34530" class="comment-tools"></div><div class="clear"></div><div id="comment-34530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

