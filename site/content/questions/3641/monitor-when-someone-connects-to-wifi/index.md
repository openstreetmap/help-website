+++
type = "question"
title = "Monitor when someone connects to wifi"
description = '''Is there any way to monitor when someone else connects to my wifi? My wifi is OK, but sometimes it dips drastically. I only notice this after the fact. I would like to know exactly when someone is connecting. I only know about the &quot;arp -a&quot; command. Thanks for any help. Kenneth'''
date = "2011-04-20T11:03:00Z"
lastmod = "2011-04-20T11:08:00Z"
weight = 3641
keywords = [ "wifi" ]
aliases = [ "/questions/3641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor when someone connects to wifi](/questions/3641/monitor-when-someone-connects-to-wifi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3641-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any way to monitor when someone else connects to my wifi? My wifi is OK, but sometimes it dips drastically. I only notice this after the fact. I would like to know exactly when someone is connecting. I only know about the "arp -a" command.</p><p>Thanks for any help.</p><p>Kenneth</p></div><div id="question-tags" class="tags-container tags">wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '11, 11:03</strong></p><img src="https://secure.gravatar.com/avatar/96f7c51993c68391c0929d0f35f464d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KSK&#39;s gravatar image" /><p>KSK<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KSK has no accepted answers">0%</span></p></div></div><div id="comments-container-3641" class="comments-container"><span id="3830"></span><div id="comment-3830" class="comment"><div id="post-3830-score" class="comment-score">2</div><div class="comment-text"><p>You <em><strong>really</strong></em> should <a href="http://blog.secure-my-wireless.com/2008/03/how-to-secure-wifi-router-for-best.html">secure your router</a> instead of searching for a WiFi thief.</p></div><div id="comment-3830-info" class="comment-info"><span class="comment-age">(29 Apr '11, 18:07)</span> helloworld</div></div><span id="3844"></span><div id="comment-3844" class="comment"><div id="post-3844-score" class="comment-score"></div><div class="comment-text"><p>@helloworld<br />
</p><p>Thanks for your reply.</p></div><div id="comment-3844-info" class="comment-info"><span class="comment-age">(30 Apr '11, 11:22)</span> KSK</div></div><span id="3845"></span><div id="comment-3845" class="comment"><div id="post-3845-score" class="comment-score"></div><div class="comment-text"><p>PS: I'll read the content in your link, too. Sounds pretty simple from what I've read so far.</p></div><div id="comment-3845-info" class="comment-info"><span class="comment-age">(30 Apr '11, 11:23)</span> KSK</div></div></div><div id="comment-tools-3641" class="comment-tools"></div><div class="clear"></div><div id="comment-3641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3642"></span>

<div id="answer-container-3642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3642-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>arp -a doesn't exactly help you with this kind of topic. You might use Wireshark and capture on a supported wireless adapter on the same channel your wifi is using (supported means that you'll have to use Airpcap adapters if you're running Windows). Then look for association requests with successful association responses - if you find any, you have evidence of someone connecting to your access point.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-3642" class="comments-container"></div><div id="comment-tools-3642" class="comment-tools"></div><div class="clear"></div><div id="comment-3642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

