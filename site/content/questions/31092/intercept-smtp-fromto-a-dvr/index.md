+++
type = "question"
title = "Intercept SMTP from/to a DVR"
description = '''I have a CCTV DVR that sends alert messages via SMTP. According to my router logs the ISP&#x27;s email is replying with an error message and I need to read this to understand what&#x27;s going wrong. I&#x27;m trying to read the reply with Wireshark on another PC on the same network but after reading FAQs and stumb...'''
date = "2014-03-23T05:23:00Z"
lastmod = "2014-03-24T15:20:00Z"
weight = 31092
keywords = [ "smtp" ]
aliases = [ "/questions/31092" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Intercept SMTP from/to a DVR](/questions/31092/intercept-smtp-fromto-a-dvr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31092-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31092-score" class="post-score" title="current number of votes">0</div><span id="post-31092-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a CCTV DVR that sends alert messages via SMTP. According to my router logs the ISP's email is replying with an error message and I need to read this to understand what's going wrong. I'm trying to read the reply with Wireshark on another PC on the same network but after reading FAQs and stumbling around for some time I have got nowhere. Could someone help please?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smtp" rel="tag" title="see questions tagged &#39;smtp&#39;">smtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '14, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/2a9cee485aefa70b64c986650dfc09d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roger99&#39;s gravatar image" /><p><span>Roger99</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roger99 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Mar '14, 07:23</strong> </span></p></div></div><div id="comments-container-31092" class="comments-container"><span id="31096"></span><div id="comment-31096" class="comment"><div id="post-31096-score" class="comment-score"></div><div class="comment-text"><p>Do you want to know how to capture the traffic or do you need help with the file analysis?</p></div><div id="comment-31096-info" class="comment-info"><span class="comment-age">(23 Mar '14, 09:01)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="31102"></span><div id="comment-31102" class="comment"><div id="post-31102-score" class="comment-score"></div><div class="comment-text"><p>Roland - sorry I missed your comment. It's the capture that beats me. I have the PC and the DVR going into the same cable router but don't understand which method I should be using.</p></div><div id="comment-31102-info" class="comment-info"><span class="comment-age">(23 Mar '14, 15:26)</span> <span class="comment-user userinfo">Roger99</span></div></div><span id="31132"></span><div id="comment-31132" class="comment"><div id="post-31132-score" class="comment-score"></div><div class="comment-text"><p>Kurt was quicker. Use the port mirroring feature of the Draytek.</p></div><div id="comment-31132-info" class="comment-info"><span class="comment-age">(24 Mar '14, 13:21)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="31133"></span><div id="comment-31133" class="comment"><div id="post-31133-score" class="comment-score"></div><div class="comment-text"><p>Thanks Roland. I'll take it from there.</p></div><div id="comment-31133-info" class="comment-info"><span class="comment-age">(24 Mar '14, 14:32)</span> <span class="comment-user userinfo">Roger99</span></div></div></div><div id="comment-tools-31092" class="comment-tools"></div><div class="clear"></div><div id="comment-31092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31100"></span>

<div id="answer-container-31100" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31100-score" class="post-score" title="current number of votes">0</div><span id="post-31100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please read the wiki to learn how to capture Ethernet traffic</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '14, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31100" class="comments-container"><span id="31103"></span><div id="comment-31103" class="comment"><div id="post-31103-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. I did go through that FAQ several times before posting, but could not work out which of the methods I should be using. Guess this is going to be beyond my limited knowledge.</p></div><div id="comment-31103-info" class="comment-info"><span class="comment-age">(23 Mar '14, 15:27)</span> <span class="comment-user userinfo">Roger99</span></div></div><span id="31120"></span><div id="comment-31120" class="comment"><div id="post-31120-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but could not work out which of the methods I should be using.</p></blockquote><p>well, that depends on you enviroment. If you have a switch with mirror port then use that, but I guess that's not very common in a private environment.</p><p>So, please add some details how you connected your DVR to the network (switch: yes/no) and to the ISP router. What kind of router is that?</p><p>Depending on that information I can suggest one or another method.</p></div><div id="comment-31120-info" class="comment-info"><span class="comment-age">(24 Mar '14, 08:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31123"></span><div id="comment-31123" class="comment"><div id="post-31123-score" class="comment-score"></div><div class="comment-text"><p>I have a Draytek Vigor 2860 router. The DVR and PC are both connected by cable to the router and both have fixed IP addresses on the local network. The router's syslog show me that the DVR is talking to the ISP email server, but the DVR then says 'email failed'. I need to see what the DVR is actually sending to the email server, and the server's reply.</p></div><div id="comment-31123-info" class="comment-info"><span class="comment-age">(24 Mar '14, 09:16)</span> <span class="comment-user userinfo">Roger99</span></div></div><span id="31124"></span><div id="comment-31124" class="comment"><div id="post-31124-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The DVR and PC are both connected by cable to the router</p></blockquote><p>well, then either use a hub (hard to find these days) to connect the DVR and the PC to the router, or a small/cheap switch with port mirroring feature</p><blockquote><p><a href="http://ask.wireshark.org/questions/13892/port-mirror-switch">http://ask.wireshark.org/questions/13892/port-mirror-switch</a><br />
</p></blockquote><p>or use the built-in packet capture feature of the Draytek</p><blockquote><p><a href="http://www.draytek.com/index.php?option=com_k2&amp;view=item&amp;id=2069&amp;Itemid=296&amp;lang=en">http://www.draytek.com/index.php?option=com_k2&amp;view=item&amp;id=2069&amp;Itemid=296&amp;lang=en</a></p></blockquote><p>Please ask Draytek support how that works!</p></div><div id="comment-31124-info" class="comment-info"><span class="comment-age">(24 Mar '14, 09:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31129"></span><div id="comment-31129" class="comment"><div id="post-31129-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt. That's very helpful. I'll look into those alternatives.</p></div><div id="comment-31129-info" class="comment-info"><span class="comment-age">(24 Mar '14, 11:50)</span> <span class="comment-user userinfo">Roger99</span></div></div><span id="31135"></span><div id="comment-31135" class="comment not_top_scorer"><div id="post-31135-score" class="comment-score"></div><div class="comment-text"><p>The built-in capture method of the Draytek is probably the easiest one.</p></div><div id="comment-31135-info" class="comment-info"><span class="comment-age">(24 Mar '14, 15:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31100" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-31100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

