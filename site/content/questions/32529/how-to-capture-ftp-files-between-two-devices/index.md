+++
type = "question"
title = "how to capture FTP files between two devices?"
description = '''hi, I want to capture FTP Files with Wireshark. I send data between a FTP-Server (PLC) and a FTP-Client (IPC, with Windows Embedded Compact). My PC, the PLC and the IPC are in the same Network, connected with a switch. How can i capture the FTP traffic between the server and the Client? best regards...'''
date = "2014-05-05T04:53:00Z"
lastmod = "2014-05-12T13:22:00Z"
weight = 32529
keywords = [ "ftp" ]
aliases = [ "/questions/32529" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture FTP files between two devices?](/questions/32529/how-to-capture-ftp-files-between-two-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32529-score" class="post-score" title="current number of votes">0</div><span id="post-32529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I want to capture FTP Files with Wireshark. I send data between a FTP-Server (PLC) and a FTP-Client (IPC, with Windows Embedded Compact). My PC, the PLC and the IPC are in the same Network, connected with a switch. How can i capture the FTP traffic between the server and the Client?</p><p>best regards</p><p>Frank</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '14, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/0055d73655c835efd5b1cd9e069b832f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fr_Bier&#39;s gravatar image" /><p><span>Fr_Bier</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fr_Bier has no accepted answers">0%</span></p></div></div><div id="comments-container-32529" class="comments-container"><span id="32535"></span><div id="comment-32535" class="comment"><div id="post-32535-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the fast answers. I will try to get a HUB or managed switch and catch the files! :-)</p></div><div id="comment-32535-info" class="comment-info"><span class="comment-age">(05 May '14, 05:43)</span> <span class="comment-user userinfo">Fr_Bier</span></div></div></div><div id="comment-tools-32529" class="comment-tools"></div><div class="clear"></div><div id="comment-32529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="32530"></span>

<div id="answer-container-32530" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32530-score" class="post-score" title="current number of votes">1</div><span id="post-32530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at this Wiki page: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '14, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32530" class="comments-container"><span id="32717"></span><div id="comment-32717" class="comment"><div id="post-32717-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help.</p><p>I used a mirror Port on my Switch, so i can see the TCP data.</p><p>Best gegards Frank</p></div><div id="comment-32717-info" class="comment-info"><span class="comment-age">(11 May '14, 22:39)</span> <span class="comment-user userinfo">Fr_Bier</span></div></div></div><div id="comment-tools-32530" class="comment-tools"></div><div class="clear"></div><div id="comment-32530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32531"></span>

<div id="answer-container-32531" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32531-score" class="post-score" title="current number of votes">1</div><span id="post-32531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>connected with a switch. How can i capture the FTP traffic between the server and the Client?</p></blockquote><p>by capturing on a mirror port of the switch.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch">http://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_monitor_mode_of_the_switch</a></p></blockquote><p>If your switch does not offer a mirror/monitor port, please try anyone of the other methods described in the link above. If none of the options are applicable in your environment, try to install Wireshark on the FTP-Server (provided, it is running an OS that supports Wireshark).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '14, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32531" class="comments-container"><span id="32533"></span><div id="comment-32533" class="comment"><div id="post-32533-score" class="comment-score">1</div><div class="comment-text"><p><span>@Jasper</span> was 3 minutes faster .... ;-)</p></div><div id="comment-32533-info" class="comment-info"><span class="comment-age">(05 May '14, 05:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32531" class="comment-tools"></div><div class="clear"></div><div id="comment-32531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32737"></span>

<div id="answer-container-32737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32737-score" class="post-score" title="current number of votes">0</div><span id="post-32737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you can make a man in the middle attack. Use "netwox 72" to change the arp table in bouth machines. Enable Ip forward in your machine and then just capture with wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 May '14, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/ca20bac738bbb8b012045602a77d7115?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fachav2&#39;s gravatar image" /><p><span>fachav2</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fachav2 has no accepted answers">0%</span></p></div></div><div id="comments-container-32737" class="comments-container"></div><div id="comment-tools-32737" class="comment-tools"></div><div class="clear"></div><div id="comment-32737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

