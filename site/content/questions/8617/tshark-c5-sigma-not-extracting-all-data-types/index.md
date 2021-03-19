+++
type = "question"
title = "[closed] TShark C5 Sigma not extracting all data types"
description = '''Hi, I am trying to extract the data out of a number of PCAP files in to a MySQL database using C5 SIGMA. I have managed to get it to create a range of tables such as frame/IP/TCP/UDP but it only creates some of the tables relating to the propriety datatypes that are decoded in wireshark using a plug...'''
date = "2012-01-26T00:23:00Z"
lastmod = "2015-04-13T07:20:00Z"
weight = 8617
keywords = [ "wireshark", "sigma", "tshark", "c5", "sql" ]
aliases = [ "/questions/8617" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] TShark C5 Sigma not extracting all data types](/questions/8617/tshark-c5-sigma-not-extracting-all-data-types)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8617-score" class="post-score" title="current number of votes">0</div><span id="post-8617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to extract the data out of a number of PCAP files in to a MySQL database using C5 SIGMA. I have managed to get it to create a range of tables such as frame/IP/TCP/UDP but it only creates some of the tables relating to the propriety datatypes that are decoded in wireshark using a plugin. C5 SIGMA uses TShark so it should decode anything that wireshark itself can decode and create the necessary tables in MySQL, a separate table for each layer in wireshark..</p><p>I was wondering whether anyone has had experience in C5 SIGMA and who can give me some advice as to how I can fault find this issue</p><p><strong>Additional</strong> After looking further into this it seems that the extraction from PCAPs to XML is capturing all the PCAP data correctly, the issue is that C5 SIGMA is not then transferring all this data in the XML files and creating the necessary MySQL tables. I am not sure how to log what is going on. Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-sigma" rel="tag" title="see questions tagged &#39;sigma&#39;">sigma</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-c5" rel="tag" title="see questions tagged &#39;c5&#39;">c5</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '12, 00:23</strong></p><img src="https://secure.gravatar.com/avatar/9ccdf645a58ff89056dec0273965243f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Degsy&#39;s gravatar image" /><p><span>Degsy</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Degsy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>13 Apr '15, 07:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-8617" class="comments-container"><span id="41399"></span><div id="comment-41399" class="comment"><div id="post-41399-score" class="comment-score"></div><div class="comment-text"><p>hi degsy, could you send me some cmd code used for creating database using C5sigma.exe</p><p>i could not able to connect with my database</p><p>please its an urgent need</p></div><div id="comment-41399-info" class="comment-info"><span class="comment-age">(12 Apr '15, 23:52)</span> <span class="comment-user userinfo">Nikhil Rajen...</span></div></div><span id="41402"></span><div id="comment-41402" class="comment"><div id="post-41402-score" class="comment-score"></div><div class="comment-text"><p><span>@nikhil rajendran</span></p><p>I think Degsy is long gone, last seen on the site in May 2012.</p></div><div id="comment-41402-info" class="comment-info"><span class="comment-age">(13 Apr '15, 03:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41403"></span><div id="comment-41403" class="comment"><div id="post-41403-score" class="comment-score"></div><div class="comment-text"><p>Dear Grahamb can you help me in solving the problem</p></div><div id="comment-41403-info" class="comment-info"><span class="comment-age">(13 Apr '15, 06:52)</span> <span class="comment-user userinfo">Nikhil Rajen...</span></div></div><span id="41404"></span><div id="comment-41404" class="comment"><div id="post-41404-score" class="comment-score"></div><div class="comment-text"><p>C5 Sigma not connecting to your db is not a Wireshark issue, you'll have to look for C5 Sigma support at whatever support offerings they have.</p></div><div id="comment-41404-info" class="comment-info"><span class="comment-age">(13 Apr '15, 07:01)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="41405"></span><div id="comment-41405" class="comment"><div id="post-41405-score" class="comment-score"></div><div class="comment-text"><p>how to use the c5sigma</p><p>i have following doubts</p><pre><code>   **do we have to create a database ourself and create tables with different columns and names**

   **do we need to save pcap file as input **

   **is it possible to use xammp for creating a mysql server as localhost**</code></pre></div><div id="comment-41405-info" class="comment-info"><span class="comment-age">(13 Apr '15, 07:01)</span> <span class="comment-user userinfo">Nikhil Rajen...</span></div></div><span id="41407"></span><div id="comment-41407" class="comment not_top_scorer"><div id="post-41407-score" class="comment-score"></div><div class="comment-text"><p>You questions (that you keep posting as "answers") are all related to C5 Sigma, not Wireshark (or tshark even). As can be seen by the tumble-weeds blowing around this question since it was originally asked, it doesn't seem likely that anyone here has had any experience of C5 Sigma.</p><p>Please use whatever support facilities they provide to resolve your issue.</p></div><div id="comment-41407-info" class="comment-info"><span class="comment-age">(13 Apr '15, 07:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-8617" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-8617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 13 Apr '15, 07:21

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8795"></span>

<div id="answer-container-8795" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8795-score" class="post-score" title="current number of votes">0</div><span id="post-8795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Degsy,<br />
Can you please post some of the PDML that you're having problems with and confirm whether you're using any data filters (i.e. "-pre" or "-fil" command line options) that might be preventing tables from being created. Are you receiving any error messages in the trace (which you should be able to pipe from stdout/stderr to a file)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '12, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/db75d16ea52fabd951df9ec659b9e5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valve&#39;s gravatar image" /><p><span>valve</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valve has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-8795" class="comments-container"></div><div id="comment-tools-8795" class="comment-tools"></div><div class="clear"></div><div id="comment-8795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

