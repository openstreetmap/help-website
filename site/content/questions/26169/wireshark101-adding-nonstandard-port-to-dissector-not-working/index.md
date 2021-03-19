+++
type = "question"
title = "Wireshark101:  Adding nonstandard port to dissector not working?"
description = '''I am going through the &quot;Wireshark101&quot; book and Lab 5 has the reader add port 81 to the list of ports to be dissected as HTTP (under &quot;Preferences, Protocols, HTTP&quot;). I added port 81 to the list of ports to be dissected as HTTP but nothing has changed in the screen output. The sample file is &quot;http-non...'''
date = "2013-10-18T08:30:00Z"
lastmod = "2013-10-18T11:25:00Z"
weight = 26169
keywords = [ "dissector", "nonstandard", "wireshark101" ]
aliases = [ "/questions/26169" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark101: Adding nonstandard port to dissector not working?](/questions/26169/wireshark101-adding-nonstandard-port-to-dissector-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26169-score" class="post-score" title="current number of votes">0</div><span id="post-26169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am going through the "Wireshark101" book and Lab 5 has the reader add port 81 to the list of ports to be dissected as HTTP (under "Preferences, Protocols, HTTP"). I added port 81 to the list of ports to be dissected as HTTP but nothing has changed in the screen output. The sample file is "http-nonstandard101.pcapng", which has an HTTP session over port 81. But after adding port 81 to the list of HTTP ports Wireshark still dissects port 81 as "hosts2-ns". I've tried 3 different versions of Wireshark all with the same result. Is there something I am missing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-nonstandard" rel="tag" title="see questions tagged &#39;nonstandard&#39;">nonstandard</span> <span class="post-tag tag-link-wireshark101" rel="tag" title="see questions tagged &#39;wireshark101&#39;">wireshark101</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/e248dde28140d0bf47253000215d5257?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc%20Ferreira&#39;s gravatar image" /><p><span>Marc Ferreira</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc Ferreira has no accepted answers">0%</span></p></div></div><div id="comments-container-26169" class="comments-container"></div><div id="comment-tools-26169" class="comment-tools"></div><div class="clear"></div><div id="comment-26169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26172"></span>

<div id="answer-container-26172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26172-score" class="post-score" title="current number of votes">0</div><span id="post-26172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds to me like Wireshark has other settings forcing it to decode the port as something else. I don't know why port 81 is called "hosts2-ns" - this isn't something that comes from the services file, maybe you set it yourself at some point? The name also sounds more like a host name, not a port name.</p><p>You might want to check if you force any kind of decoding: go to "Analyze - Decode As" (with a trace being loaded, otherwise it is greyed out) and use the "Clear" button to reset the decodings. You can verify that there is no decode forcing by using the "Show Current" button.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26172" class="comments-container"><span id="26183"></span><div id="comment-26183" class="comment"><div id="post-26183-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. I didn't set any decoding manually but I did open this screen and tried telling it to decode destination port 81 as HTTP and that still made no difference. Then I hit "Clear" and verified in the "Show Current" screen that it did clear. I found "hosts2-ns" listed as one possible user of port 81 on speedguide.net but yes it is unassigned by IANA. Any other ideas as to why this function would not be working according to "the book"?</p></div><div id="comment-26183-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:17)</span> <span class="comment-user userinfo">Marc Ferreira</span></div></div></div><div id="comment-tools-26172" class="comment-tools"></div><div class="clear"></div><div id="comment-26172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26182"></span>

<div id="answer-container-26182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26182-score" class="post-score" title="current number of votes">0</div><span id="post-26182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But after adding port 81 to the list of HTTP ports Wireshark still <strong>dissects port 81 as "hosts2-ns"</strong>.</p></blockquote><p>Apparently this is mentioned in the book.</p><blockquote><p><a href="http://www.wiresharkbook.com/101_samplepages/9781893939721-page60.pdf">http://www.wiresharkbook.com/101_samplepages/9781893939721-page60.pdf</a></p></blockquote><p><strong>However</strong>: There is no 'hosts2-ns' definition in the Wireshark services file, at least not since 1.6 (I did not check earlier versions). As the screenshot in the book shows 'hosts2-ns' as well, the author either used an older version of Wireshark or its own services file.</p><p>Anyway, if you add the port to the HTTP preferences, Wireshark <strong>will</strong> dissect port 81 as HTTP <strong>unless</strong> the HTTP dissector is disabled (Analyze -&gt; Enabled Protocols -&gt; HTTP)</p><blockquote><p>Edit -&gt; Preferences -&gt; Protocols -&gt;HTTP -&gt; TCP Ports</p></blockquote><p>Click on <strong>Apply</strong> and <strong>OK</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Oct '13, 11:27</strong> </span></p></div></div><div id="comments-container-26182" class="comments-container"><span id="26184"></span><div id="comment-26184" class="comment"><div id="post-26184-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. Yes I'm following the book and added 81 to the list of ports under Edit-&gt;Preferences-&gt;Protocols-&gt;HTTP-&gt;TCP Ports but it had no effect. I'm using 1.10.2 32-bit, I've tried the 64-bit version (first), and 1.8 as well.</p></div><div id="comment-26184-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:21)</span> <span class="comment-user userinfo">Marc Ferreira</span></div></div><span id="26187"></span><div id="comment-26187" class="comment"><div id="post-26187-score" class="comment-score"></div><div class="comment-text"><p>what is your OS?</p></div><div id="comment-26187-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:26)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26192"></span><div id="comment-26192" class="comment"><div id="post-26192-score" class="comment-score"></div><div class="comment-text"><p>Windows 7 Enterprise SP1.</p></div><div id="comment-26192-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:59)</span> <span class="comment-user userinfo">Marc Ferreira</span></div></div><span id="26193"></span><div id="comment-26193" class="comment"><div id="post-26193-score" class="comment-score"></div><div class="comment-text"><p>Did you close and re-open Wireshark (should <strong>not</strong> be necessary, but ...)?</p></div><div id="comment-26193-info" class="comment-info"><span class="comment-age">(18 Oct '13, 11:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26196"></span><div id="comment-26196" class="comment"><div id="post-26196-score" class="comment-score"></div><div class="comment-text"><p>Yes I tried re-loading the file, then closing and re-starting Wireshark. Port 81 still shows in the list of HTTP ports but the "Protocol" column still says TCP and the Destination Port is still interpreted as "hosts2-ns".</p></div><div id="comment-26196-info" class="comment-info"><span class="comment-age">(18 Oct '13, 11:10)</span> <span class="comment-user userinfo">Marc Ferreira</span></div></div><span id="26198"></span><div id="comment-26198" class="comment not_top_scorer"><div id="post-26198-score" class="comment-score"></div><div class="comment-text"><p>And you did <strong>not</strong> disable the HTTP dissector, right?</p><blockquote><p>Analyze -&gt; Enabled Protocols -&gt; HTTP</p></blockquote></div><div id="comment-26198-info" class="comment-info"><span class="comment-age">(18 Oct '13, 11:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26182" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-26182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

