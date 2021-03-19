+++
type = "question"
title = "Adobe Creative Cloud Error"
description = '''Hello, there is a error 201 with adobe creative cloud that we keep getting at my company. It is a small install file that connects to an adobe server and tries to download the main files. I will attach a screenshot so you can see what is happening while it tries to download the file. I also selected...'''
date = "2016-11-07T07:10:00Z"
lastmod = "2016-11-07T07:10:00Z"
weight = 57052
keywords = [ "suite", "adobe", "cloud", "creative" ]
aliases = [ "/questions/57052" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adobe Creative Cloud Error](/questions/57052/adobe-creative-cloud-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57052-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, there is a error 201 with adobe creative cloud that we keep getting at my company. It is a small install file that connects to an adobe server and tries to download the main files. I will attach a screenshot so you can see what is happening while it tries to download the file. I also selected the line that I feel may be related to the issue. Please keep in mind that our network firewall should be open to everything that is reasonable.<img src="https://osqa-ask.wireshark.org/upfiles/Capture_VEkboIg.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">suite adobe cloud creative</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '16, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/293fc83f97e05f8437ac0da1473e82ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flentini&#39;s gravatar image" /><p>flentini<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flentini has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57052" class="comments-container"><span id="57090"></span><div id="comment-57090" class="comment"><div id="post-57090-score" class="comment-score"></div><div class="comment-text"><p>Making assessments from a screen shot is difficult, so this may be off, but the TCP resets suggest that the firewall or proxy is trying to stop this from happening.</p></div><div id="comment-57090-info" class="comment-info"><span class="comment-age">(07 Nov '16, 13:14)</span> Jaap ♦</div></div><span id="57092"></span><div id="comment-57092" class="comment"><div id="post-57092-score" class="comment-score"></div><div class="comment-text"><p>Am I correct in my assumption that for the rcp recets under the info column that it is saying that port 80 on adobes end is trying to communicate back to us on port 129x?</p></div><div id="comment-57092-info" class="comment-info"><span class="comment-age">(07 Nov '16, 13:33)</span> flentini</div></div><span id="57095"></span><div id="comment-57095" class="comment"><div id="post-57095-score" class="comment-score"></div><div class="comment-text"><p>Frames 606 and 608 belong to one TCP session (client:1291 -&gt; server:80), frame 607 belongs to another one (client:1292 -&gt; server:80).</p><p>A RST packet just says that its sender terminates an existing TCP session in emergency mode. It is not an attempt to establish a new one nor to modify the existing one and continue it.</p></div><div id="comment-57095-info" class="comment-info"><span class="comment-age">(07 Nov '16, 13:41)</span> sindy</div></div><span id="57098"></span><div id="comment-57098" class="comment"><div id="post-57098-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy that was usefull information. Could anyone tell me what frame 613 means? I am learning as I go here.</p></div><div id="comment-57098-info" class="comment-info"><span class="comment-age">(07 Nov '16, 13:52)</span> flentini</div></div><span id="57103"></span><div id="comment-57103" class="comment"><div id="post-57103-score" class="comment-score"></div><div class="comment-text"><p>Frame 613 is most likely an ACK packet which has no payload in it but the ACK sequence number matches the one already sent in frame 612 (that's the meaning of <code>612 #1</code>), which is quite a weird behaviour of the server (or firewall, or load balancer, ... which tamper with the TCP session as it passes through them).</p><p>But that's really at the limit of screenshot "analysis", so I'd recommend you to follow @Jaap's soft hint and publish the capture file if you intend to continue asking.</p><p>To publish a capture file, you have to upload it to Cloudshark or to any plain file sharing service (Dropbox, Goggle Drive, ...) and edit your Question with a login-free link to it.</p></div><div id="comment-57103-info" class="comment-info"><span class="comment-age">(07 Nov '16, 14:06)</span> sindy</div></div></div><div id="comment-tools-57052" class="comment-tools"></div><div class="clear"></div><div id="comment-57052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

