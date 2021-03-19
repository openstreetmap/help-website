+++
type = "question"
title = "Read &quot;WhatsApp&quot; messages over wlan"
description = '''How can I follow messages sent over a mobile phone with WhatsApp Messenger in a local wlan?'''
date = "2012-01-22T01:39:00Z"
lastmod = "2012-05-23T01:19:00Z"
weight = 8539
keywords = [ "filter", "whatsapp", "wlan" ]
aliases = [ "/questions/8539" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Read "WhatsApp" messages over wlan](/questions/8539/read-whatsapp-messages-over-wlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8539-score" class="post-score" title="current number of votes">0</div><span id="post-8539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I follow messages sent over a mobile phone with <a href="http://www.whatsapp.com/">WhatsApp Messenger</a> in a local wlan?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-whatsapp" rel="tag" title="see questions tagged &#39;whatsapp&#39;">whatsapp</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '12, 01:39</strong></p><img src="https://secure.gravatar.com/avatar/82430c9aeb3635c636e17c88c535774a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anon&#39;s gravatar image" /><p><span>Anon</span><br />
<span class="score" title="84 reputation points">84</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anon has one accepted answer">16%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '12, 07:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-8539" class="comments-container"></div><div id="comment-tools-8539" class="comment-tools"></div><div class="clear"></div><div id="comment-8539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9746"></span>

<div id="answer-container-9746" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9746-score" class="post-score" title="current number of votes">0</div><span id="post-9746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is even an easier way to follow the conversations, if you use only the filter expression <strong>ssl contains F8:03:83:BD:AD</strong> you get the same result.</p><p>The structure of WhatsApp-messages looks like this:</p><h3 id="incoming-whatsappmessage">Incoming WhatsAppMessage</h3><p>00:[LENGTH]:{ #Header# F8:[LENGTH]:{ #CallingNumber# 5D:38:FA: FC:[LENGTH]:{ASCII}: #UserID# 8A:43: FC:[LENGTH]:{ASCII}: #MessageID# A2:1B:9D: FC:[LENGTH]:{ASCII}: } #Content# F8:[LENGTH]:{ #Name# F8:[LENGTH]:{ 65:BD:AE:61: FC:[LENGTH]:{ASCII}: } #Seperator ???# F8:[LENGTH]:{ 83:BD:AD: } #MessageText# F8:[LENGTH]:{ 16: FC:[LENGTH]:{ASCII}:<br />
} #Date (optional)# F8:[LENGTH]:{ 25:BD:AB:38:8A:92: FC:[LENGTH]:{ ASCII: ### YYYY-MM-DD "T": ASCII: ### HH:MM:SS }<br />
5A:66: } #Date (optional)# F8:[LENGTH]:{ BA:BD:4E:92: FC:[LENGTH]:{ ASCII: ### YYYYMMDD "T": ASCII: ### HH:MM:SS }<br />
} } }</p><h3 id="outgoing-whatsappmessage">Outgoing WhatsAppMessage</h3><p>00:[LENGTH]:{ #Header# F8:[LENGTH]:{ #CallingNumber# 5D:A2:1B:A0:FA: FC:[LENGTH]:{ASCII}: #UserID# 8A:43: FC:[LENGTH]:{ASCII}: } #Content# F8:[LENGTH]:{ #MessageText# F8:[LENGTH]:{ 16: FC:[LENGTH]:{ASCII}:<br />
} #Seperator ???# F8:[LENGTH]:{ 83:BD:AD: } #EndOfMessage ???# F8:[LENGTH]:{ BA:BD:4F: F8:[LENGTH]:{ F8:[LENGTH]:{ 8C } }<br />
} } }</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '12, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/82430c9aeb3635c636e17c88c535774a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anon&#39;s gravatar image" /><p><span>Anon</span><br />
<span class="score" title="84 reputation points">84</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anon has one accepted answer">16%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Mar '12, 05:00</strong> </span></p></div></div><div id="comments-container-9746" class="comments-container"><span id="11245"></span><div id="comment-11245" class="comment"><div id="post-11245-score" class="comment-score"></div><div class="comment-text"><p>Hello, above filter isn't working. Maybe due to my Wireshark configuration. I'm using a Mac (OS 10.7.3) in a wireless network (Netgear WNR2000 (WPA2)). Any suggestions on tutorials setting up Wireshark and configuring right filters for Whatsapp reading? Thanks, Stan</p></div><div id="comment-11245-info" class="comment-info"><span class="comment-age">(23 May '12, 01:19)</span> <span class="comment-user userinfo">jojo</span></div></div></div><div id="comment-tools-9746" class="comment-tools"></div><div class="clear"></div><div id="comment-9746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8540"></span>

<div id="answer-container-8540" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8540-score" class="post-score" title="current number of votes">-2</div><span id="post-8540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use the filter expression: --- (ssl contains f8:08:5d:a2 and ssl contains f8:02:16:fc) or (ssl contains f8:0a:5d and ssl contains bd:ae:61:fc) --- and you get only the relevant packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '12, 01:41</strong></p><img src="https://secure.gravatar.com/avatar/82430c9aeb3635c636e17c88c535774a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anon&#39;s gravatar image" /><p><span>Anon</span><br />
<span class="score" title="84 reputation points">84</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anon has one accepted answer">16%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '12, 01:41</strong> </span></p></div></div><div id="comments-container-8540" class="comments-container"></div><div id="comment-tools-8540" class="comment-tools"></div><div class="clear"></div><div id="comment-8540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

