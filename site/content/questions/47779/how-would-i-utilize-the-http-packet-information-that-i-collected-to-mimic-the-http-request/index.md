+++
type = "question"
title = "How would I utilize the http packet information that I collected to mimic the http request?"
description = '''Hello I am new to wireshark and the whole concept of protocols in general, so my question may be really dumb. I have a web game that I am playing right now. I was monitoring the wireshark to at least have good idea of what kind of http packet (package?) the app is sending to server in order to proce...'''
date = "2015-11-19T16:55:00Z"
lastmod = "2015-11-20T03:57:00Z"
weight = 47779
keywords = [ "http", "request", "packet" ]
aliases = [ "/questions/47779" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How would I utilize the http packet information that I collected to mimic the http request?](/questions/47779/how-would-i-utilize-the-http-packet-information-that-i-collected-to-mimic-the-http-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47779-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I am new to wireshark and the whole concept of protocols in general, so my question may be really dumb.</p><p>I have a web game that I am playing right now. I was monitoring the wireshark to at least have good idea of what kind of http packet (package?) the app is sending to server in order to process my request (by eliminating all other browser process from my computer). This request takes about 10 clicks in game to get to which is really tedious in my opinion. Now if I could mimic this request some how directly, my mission is accomplished.</p><p>First of all, is there way to perform such a task? Can I make a html button or wpf control and attach some sort of code to just send this packet?</p><p>How do I analyze the package so I would know where in the package is about my information and how would I know where my package is going?</p><p>How would I send a http request to the location (server) I observed from above?</p><p>Any advice are appreciated.</p><p>Thank you very much in advanced.</p><p>P.S My deep apology if this question is posted twice. When I signed up for this Q&amp;A forum, my previous submission was gone in void.</p></div><div id="question-tags" class="tags-container tags">http request packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '15, 16:55</strong></p><img src="https://secure.gravatar.com/avatar/b7f59522a0315acf3bd63a1fbb300f63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="publicats&#39;s gravatar image" /><p>publicats<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="publicats has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Nov '15, 16:56</p></div></div><div id="comments-container-47779" class="comments-container"></div><div id="comment-tools-47779" class="comment-tools"></div><div class="clear"></div><div id="comment-47779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47785"></span>

<div id="answer-container-47785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47785-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>First of all, is there way to perform such a task?</p></blockquote><p>Yes it might be possible, but it's very complex and requires a lot of basic protocol knowledge (TCP, HTTP) AND a lot of knowledge about the protocol used by the game on top of HTTP.</p><p>As you said, you're new to 'the whole concept of protocols in general', I don't see a realistic chance for you to finish such a complex task. It would be a lot of work even for the best Wireshark experts.</p><p>What you are looking for is actually a game cheating bot/tool. So, I suggest to ask your question in a game related forum (there are tons of cheater forums out there). They will be able to help you much more than the Wireshark community.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '15, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47785" class="comments-container"><span id="47796"></span><div id="comment-47796" class="comment"><div id="post-47796-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt! Thanks for the reply.</p><p>Sounds like it is a difficult problem and I like that challenge! Rather than relying on other people, I would like to challenge myself and see if I could fix it, so next time similar but different problem appears I do not have to surf internet for countless hours to search for answer. Would you be able to guide me to where I would be able to start reading about this?</p><p>Thank you!</p></div><div id="comment-47796-info" class="comment-info"><span class="comment-age">(20 Nov '15, 08:58)</span> publicats</div></div><span id="47797"></span><div id="comment-47797" class="comment"><div id="post-47797-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Would you be able to guide me to where I would be able to start reading about this?</p></blockquote><p>I'm afraid, but I'm pretty sure, that I don't know anything about the protocol your game is using. And without that knwoledge, it's virtually impossible to accomplish the task.</p></div><div id="comment-47797-info" class="comment-info"><span class="comment-age">(20 Nov '15, 09:03)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47785" class="comment-tools"></div><div class="clear"></div><div id="comment-47785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

