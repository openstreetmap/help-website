+++
type = "question"
title = "capturing POP3"
description = '''Hello! I am relatively new to wireshark, and I want to capture POP3 protocol. I am using ethernet, wireshark, and gmail or hotmail, however. The thing is I have tried many times to do that and there is no POP SMTP or IMAP filters to be shown in wireshark, when I type them in filter bar at the top, a...'''
date = "2017-05-22T12:23:00Z"
lastmod = "2017-05-22T12:25:00Z"
weight = 61548
keywords = [ "pop3", "filter", "protocol", "capture", "wireshark" ]
aliases = [ "/questions/61548" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capturing POP3](/questions/61548/capturing-pop3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61548-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I am relatively new to wireshark, and I want to capture POP3 protocol. I am using ethernet, wireshark, and gmail or hotmail, however. The thing is I have tried many times to do that and there is no POP SMTP or IMAP filters to be shown in wireshark, when I type them in filter bar at the top, all I get is empty window. How can I manage to show those packets over the network??? Is there some security which I need to deactivate or something else???</p></div><div id="question-tags" class="tags-container tags">pop3 filter protocol capture wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '17, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/8f7157c31c43a9a2d9275cfd576badff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joy%20Boy&#39;s gravatar image" /><p>Joy Boy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joy Boy has no accepted answers">0%</span></p></div></div><div id="comments-container-61548" class="comments-container"></div><div id="comment-tools-61548" class="comment-tools"></div><div class="clear"></div><div id="comment-61548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61549"></span>

<div id="answer-container-61549" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61549-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I assume you're accessing those mail servers via web browser? Or do you use a Mail client like Thunderbird? If you're using a web browser you wont see POP, SMTP or IMAP because it all is done over HTTPS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '17, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61549" class="comments-container"><span id="61550"></span><div id="comment-61550" class="comment"><div id="post-61550-score" class="comment-score"></div><div class="comment-text"><p>I have tried using thunderbird with my gmail account, and it still does not work, I have enabled untrusted apps in gmail, and all protocols are enabled in wireshark</p></div><div id="comment-61550-info" class="comment-info"><span class="comment-age">(22 May '17, 12:28)</span> Joy Boy</div></div><span id="61551"></span><div id="comment-61551" class="comment"><div id="post-61551-score" class="comment-score"></div><div class="comment-text"><p>or I am using it the wrong way also I am running all with administrator permisssion</p></div><div id="comment-61551-info" class="comment-info"><span class="comment-age">(22 May '17, 12:29)</span> Joy Boy</div></div><span id="61552"></span><div id="comment-61552" class="comment"><div id="post-61552-score" class="comment-score"></div><div class="comment-text"><p>but I did send mail over thunderbird, and the opened it via Firefox, could I possibly send mail over my phone and then open it via thunderbird, would it then work??</p></div><div id="comment-61552-info" class="comment-info"><span class="comment-age">(22 May '17, 12:30)</span> Joy Boy</div></div><span id="61553"></span><div id="comment-61553" class="comment"><div id="post-61553-score" class="comment-score"></div><div class="comment-text"><p>Check ports that are used, maybe POP also uses the encrypted protocol versions. Running as admin isn't required by the way.</p><p>You can check if you have unencrypted POP3, IMAP and SMTP traffic by filtering for</p><pre><code>tcp.port==25 or tcp.port==110 or tcp.port==143</code></pre><p>If no packets are left, your mail program doesn't use the non encrypted ports. In that case check for encrypted ports:</p><pre><code>tcp.port==465 or tcp.port==587 or tcp.port==993 or tcp.port==995</code></pre><p>If those show packets, your communication is using the encrypted ports and you won't be able to read clear text.</p></div><div id="comment-61553-info" class="comment-info"><span class="comment-age">(22 May '17, 12:53)</span> Jasper ♦♦</div></div><span id="61554"></span><div id="comment-61554" class="comment"><div id="post-61554-score" class="comment-score"></div><div class="comment-text"><p>I will post here, because now i have an image. Finally the tcp.port==995 managed to show some results. Now, is there anything useful which Ii can extract from this data. Clear text is not that much important, but the need for at least small portion of text is required...</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_yLz2bhj.PNG" width="640" /></p></div><div id="comment-61554-info" class="comment-info"><span class="comment-age">(22 May '17, 13:26)</span> Joy Boy</div></div><span id="61555"></span><div id="comment-61555" class="comment not_top_scorer"><div id="post-61555-score" class="comment-score"></div><div class="comment-text"><p>tcp.port==995 is what finally showed some results, as in the image posted below</p></div><div id="comment-61555-info" class="comment-info"><span class="comment-age">(22 May '17, 13:26)</span> Joy Boy</div></div><span id="61556"></span><div id="comment-61556" class="comment not_top_scorer"><div id="post-61556-score" class="comment-score"></div><div class="comment-text"><p>does the image need to be bigger...</p></div><div id="comment-61556-info" class="comment-info"><span class="comment-age">(22 May '17, 13:27)</span> Joy Boy</div></div><span id="61557"></span><div id="comment-61557" class="comment not_top_scorer"><div id="post-61557-score" class="comment-score"></div><div class="comment-text"><p>Thank You for the help!</p></div><div id="comment-61557-info" class="comment-info"><span class="comment-age">(22 May '17, 13:27)</span> Joy Boy</div></div><span id="61559"></span><div id="comment-61559" class="comment not_top_scorer"><div id="post-61559-score" class="comment-score"></div><div class="comment-text"><p>As you can see your communication is encrypted (TLS v1.2), so no clear text of any email. You'll need to find a mail server that still does unencrypted POP3, but for that you'll probably have to run your own server. All the big commercial ones are probably not offering that anymore.</p></div><div id="comment-61559-info" class="comment-info"><span class="comment-age">(22 May '17, 13:28)</span> Jasper ♦♦</div></div><span id="61564"></span><div id="comment-61564" class="comment not_top_scorer"><div id="post-61564-score" class="comment-score"></div><div class="comment-text"><p>Oh, well that puts some new implications on the process. But, sure, it would be good to check possibility of running personal version of some server. Thank You!!!</p></div><div id="comment-61564-info" class="comment-info"><span class="comment-age">(22 May '17, 15:41)</span> Joy Boy</div></div></div><div id="comment-tools-61549" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-61549-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

