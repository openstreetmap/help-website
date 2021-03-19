+++
type = "question"
title = "Active Directory does not allow changing of interface card"
description = '''Hello all, I&#x27;m running the latest version of Wireshark as part of the Cisco curriculum. All of our machines are on Windows 7 Enterprise with all the latest updates and service packs and Windows Server 2008 R2. When the students try to change the interface card, there is nothing listed in the box. I ...'''
date = "2012-10-10T04:51:00Z"
lastmod = "2012-10-13T01:39:00Z"
weight = 14879
keywords = [ "active", "directory" ]
aliases = [ "/questions/14879" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Active Directory does not allow changing of interface card](/questions/14879/active-directory-does-not-allow-changing-of-interface-card)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14879-score" class="post-score" title="current number of votes">0</div><span id="post-14879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all, I'm running the latest version of Wireshark as part of the Cisco curriculum. All of our machines are on Windows 7 Enterprise with all the latest updates and service packs and Windows Server 2008 R2. When the students try to change the interface card, there is nothing listed in the box. I logged in with my ID to the domain figuring it was a rights issue, but I can't see it either and I have administrator rights to the machine if not the domain,but my account gets the same error. The only machine in the lab that is working is the instructor machine, which is connected to a test domain setup to a Cisco demo server. I'm pretty positive it a setting in Active Directory, but which one? Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-active" rel="tag" title="see questions tagged &#39;active&#39;">active</span> <span class="post-tag tag-link-directory" rel="tag" title="see questions tagged &#39;directory&#39;">directory</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '12, 04:51</strong></p><img src="https://secure.gravatar.com/avatar/f8ce9aa334eacda7e886940176bd3bb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Swendsen&#39;s gravatar image" /><p><span>John Swendsen</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Swendsen has no accepted answers">0%</span></p></div></div><div id="comments-container-14879" class="comments-container"><span id="14880"></span><div id="comment-14880" class="comment"><div id="post-14880-score" class="comment-score"></div><div class="comment-text"><p>What are you trying to change? This doesn't sound like a Wireshark question, more a Windows one.</p></div><div id="comment-14880-info" class="comment-info"><span class="comment-age">(10 Oct '12, 04:56)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="14881"></span><div id="comment-14881" class="comment"><div id="post-14881-score" class="comment-score"></div><div class="comment-text"><blockquote><p>When the students try to change the interface card, there is nothing listed in the box.</p></blockquote><p>what does that mean? Where do you change the interface card?<br />
Which "box" do you mean?</p><p>Can you post a screenshot? That would make troubleshooting a lot easier...</p></div><div id="comment-14881-info" class="comment-info"><span class="comment-age">(10 Oct '12, 05:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14893"></span><div id="comment-14893" class="comment"><div id="post-14893-score" class="comment-score"></div><div class="comment-text"><p>I open up Wireshark, go to Capture, Interfaces, and instead of seeing a list of the adapters, I get this error. "There are no interfaces on which a capture can be done."</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark.JPG" alt="alt text" /></p></div><div id="comment-14893-info" class="comment-info"><span class="comment-age">(10 Oct '12, 06:48)</span> <span class="comment-user userinfo">John Swendsen</span></div></div><span id="14920"></span><div id="comment-14920" class="comment"><div id="post-14920-score" class="comment-score"></div><div class="comment-text"><p>Logged in with my account and generated the same error, applied your command and it changed the configuration, so I rebooted and logged in as one of the students and it seems to work. I notified the class instructor and I'm going to have him check and make sure it does what it needs him to do, but looks like you solved it. Thanks.</p></div><div id="comment-14920-info" class="comment-info"><span class="comment-age">(11 Oct '12, 05:07)</span> <span class="comment-user userinfo">John Swendsen</span></div></div><span id="14922"></span><div id="comment-14922" class="comment"><div id="post-14922-score" class="comment-score"></div><div class="comment-text"><p>Good! If you think it is the correct answer, you can mark is as such (check mark).</p></div><div id="comment-14922-info" class="comment-info"><span class="comment-age">(11 Oct '12, 05:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-14879" class="comment-tools"></div><div class="clear"></div><div id="comment-14879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14895"></span>

<div id="answer-container-14895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14895-score" class="post-score" title="current number of votes">1</div><span id="post-14895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I open up Wireshark, go to Capture, Interfaces, and instead of seeing a list of the adapters, I get this error. "There are no interfaces on which a capture can be done."</p></blockquote><p>O.K. sounds like a priviledge problem while accessing the NPF driver. Did you select the option <strong>'start winpcap service "NPF" at startup'</strong> while you installed Winpcap?</p><p>If no: please re-install WinPcap and select that option.<br />
If yes: check if the NPF service is running. In a DOS box: sc qc npf</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '12, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div></div><div id="comments-container-14895" class="comments-container"><span id="14900"></span><div id="comment-14900" class="comment"><div id="post-14900-score" class="comment-score"></div><div class="comment-text"><p>Ran the command and got this. All the machines should have the same settings as they were ghosted from the same master image, but I can't tell if one of the instructors changed the settings on the machine not on the AD Domain.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/NPF.jpg" alt="alt text" /></p></div><div id="comment-14900-info" class="comment-info"><span class="comment-age">(10 Oct '12, 10:44)</span> <span class="comment-user userinfo">John Swendsen</span></div></div><span id="14902"></span><div id="comment-14902" class="comment"><div id="post-14902-score" class="comment-score"></div><div class="comment-text"><p>If you change the START_TYPE from <strong>DEMAND_START</strong> to <strong>AUTO_START</strong> your problem should be gone.</p><blockquote><p><code>sc config npf start= auto</code></p></blockquote></div><div id="comment-14902-info" class="comment-info"><span class="comment-age">(10 Oct '12, 11:30)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14962"></span><div id="comment-14962" class="comment"><div id="post-14962-score" class="comment-score"></div><div class="comment-text"><p>Thanks, spoke with the CISCO instructor and says it's working fine now. AD seems to block the on demand start for the students.</p></div><div id="comment-14962-info" class="comment-info"><span class="comment-age">(12 Oct '12, 06:09)</span> <span class="comment-user userinfo">John Swendsen</span></div></div><span id="14983"></span><div id="comment-14983" class="comment"><div id="post-14983-score" class="comment-score"></div><div class="comment-text"><p>good. If you like, you can accept may answer by clicking on the check mark next to the answer.</p><blockquote><p><code>http://ask.wireshark.org/faq/</code></p></blockquote></div><div id="comment-14983-info" class="comment-info"><span class="comment-age">(13 Oct '12, 01:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-14895" class="comment-tools"></div><div class="clear"></div><div id="comment-14895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

