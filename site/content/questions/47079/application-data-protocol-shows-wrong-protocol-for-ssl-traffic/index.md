+++
type = "question"
title = "Application Data Protocol shows wrong protocol for SSL traffic"
description = '''When playing around with the RSA key listing under Edit -&amp;gt; Preferences -&amp;gt; Protocols -&amp;gt; SSL I set spdy as the protocol for 443 traffic. Now Wireshark things spdy is the Application Data Protocol for all 443 traffic. The only work-around is to have a fake key configured in the RSA key listing...'''
date = "2015-10-29T16:11:00Z"
lastmod = "2015-10-30T15:22:00Z"
weight = 47079
keywords = [ "ssl", "configuration" ]
aliases = [ "/questions/47079" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Application Data Protocol shows wrong protocol for SSL traffic](/questions/47079/application-data-protocol-shows-wrong-protocol-for-ssl-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47079-score" class="post-score" title="current number of votes">1</div><span id="post-47079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When playing around with the RSA key listing under Edit -&gt; Preferences -&gt; Protocols -&gt; SSL I set spdy as the protocol for 443 traffic.</p><p>Now Wireshark things spdy is the Application Data Protocol for all 443 traffic. The only work-around is to have a fake key configured in the RSA key listing for 0.0.0.0 and 443 that lists the protocol as HTTP. But when I remove it Wireshark goes right back to thinking HTTPS traffic should be spdy traffic.</p><p>I have removed and re-installed Wireshark, deleted all references of Wireshark from the registry and this setting is still buried somewhere. I also tried just removing spdy support.</p><p>Any idea where the option to set what protocol is hosted under SSL for a specific port so I can get back to the default?</p><p><img src="https://lh3.googleusercontent.com/-g9U_qO0uuyw/VjKkqTCJFFI/AAAAAAAAI7Q/ipI45mU-fUs/s1152-Ic42/wireshark_wrong_application_data_protocol.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '15, 16:11</strong></p><img src="https://secure.gravatar.com/avatar/75179ddfe0ef46b3af253be18392807b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Drone637&#39;s gravatar image" /><p><span>Drone637</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Drone637 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-47079" class="comments-container"></div><div id="comment-tools-47079" class="comment-tools"></div><div class="clear"></div><div id="comment-47079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47082"></span>

<div id="answer-container-47082" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47082-score" class="post-score" title="current number of votes">1</div><span id="post-47082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Drone637 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are experiencing <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10984">bug 10984</a>. This bug is fixed in Wireshark 2.0 and will also become part of 1.12.9. As a workaround for this bug, you can modify the HTTP preferences, for example by adding additional SSL/TLS ports as described by mrEEde. If you don't know what to add, duplicating a port number is sufficient (like <code>443,443</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '15, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-47082" class="comments-container"><span id="47099"></span><div id="comment-47099" class="comment"><div id="post-47099-score" class="comment-score"></div><div class="comment-text"><p>This resolved the issue. I added a second 443 and it is now resolving as expected.</p></div><div id="comment-47099-info" class="comment-info"><span class="comment-age">(30 Oct '15, 15:22)</span> <span class="comment-user userinfo">Drone637</span></div></div></div><div id="comment-tools-47082" class="comment-tools"></div><div class="clear"></div><div id="comment-47082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47081"></span>

<div id="answer-container-47081" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47081-score" class="post-score" title="current number of votes">1</div><span id="post-47081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So you want a certain port decoded as SSL?<br />
I add the port to the http.ssl.port range Edit-Preferences-Protocols-HTTP <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-Wireshark:_Preferences_-_Profile:_bootcamp_2015.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '15, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-47081" class="comments-container"></div><div id="comment-tools-47081" class="comment-tools"></div><div class="clear"></div><div id="comment-47081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

