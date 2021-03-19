+++
type = "question"
title = "Keylogger outbound traffic"
description = '''I suspect a keylogger on a client&#x27;s PC, but cannot isolate it. My fear is that this keylogger transmits data outbound to an indeterminate location. So I am seeking a tool which may allow me to look at any outbound activity, and then isolate destinations and take it from there. Time is of the essence...'''
date = "2011-01-29T12:34:00Z"
lastmod = "2016-04-03T07:43:00Z"
weight = 2011
keywords = [ "outbound", "transmits", "keylogger" ]
aliases = [ "/questions/2011" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Keylogger outbound traffic](/questions/2011/keylogger-outbound-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2011-score" class="post-score" title="current number of votes">0</div><span id="post-2011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I suspect a keylogger on a client's PC, but cannot isolate it. My fear is that this keylogger transmits data outbound to an indeterminate location.</p><p>So I am seeking a tool which may allow me to look at any outbound activity, and then isolate destinations and take it from there.</p><p>Time is of the essence, so I only have a limited time to familiarize myself with a tool.</p><p>Will Wireshark address my needs? Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-outbound" rel="tag" title="see questions tagged &#39;outbound&#39;">outbound</span> <span class="post-tag tag-link-transmits" rel="tag" title="see questions tagged &#39;transmits&#39;">transmits</span> <span class="post-tag tag-link-keylogger" rel="tag" title="see questions tagged &#39;keylogger&#39;">keylogger</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '11, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/1809a081485259754df7ff06eef0e122?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lastditch&#39;s gravatar image" /><p><span>lastditch</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lastditch has no accepted answers">0%</span></p></div></div><div id="comments-container-2011" class="comments-container"></div><div id="comment-tools-2011" class="comment-tools"></div><div class="clear"></div><div id="comment-2011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="2016"></span>

<div id="answer-container-2016" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2016-score" class="post-score" title="current number of votes">1</div><span id="post-2016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, Wireshark can help but depending on the usage pattern of the PC it can be difficult to determine which traffic is harmless and which is malicious.</p><p>This is what I would do if I suspect a keylogger transmitting data:</p><ol><li>If you can, put Wireshark on a 2nd PC and use a Hub/SPAN Port to capture the suspicious PC's data. If you can't you might have to go with installing Wirehark on the actual client's PC which has some drawbacks but sometimes can't be helped.</li><li>Start the client's PC and let Wireshark capture the data coming and going to it's network card</li><li>Close as much programs that use the network as you can, so make sure that there is as little valid network traffic created as possible</li><li>Open a text editor and start typing. Now if there's a keylogger it should at some point start to send out the captured data. You should see that as communications coming from the PC that have no other reason to be there. You can filter on that by using something like "ip.src==X.X.X.X" where X.X.X.X is the PC's IP address. This way you see everything that goes out. If there is something that you have no explanation for you can filter on this communication bidirectionaly, for example by using the "Follow TCP stream" filter (if it is in fact a TCP session). Then you need to determine what is happening and if this is in fact a keylogger.</li><li>You may have to monitor the PC for a while because not all keyloggers send their data out right away. If you have a Wireshark on a 2nd PC you can try to shut down the suspicious PC and see if there is a transmission right before the keylogger is terminated.</li></ol><p>BTW, if you suspect a keylogger you should also check the PC for physical dongles - nobody checks the back of the PC for PS/2 or USB keyloggers in hardware unless it's a notebook ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '11, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2016" class="comments-container"></div><div id="comment-tools-2016" class="comment-tools"></div><div class="clear"></div><div id="comment-2016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2014"></span>

<div id="answer-container-2014" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2014-score" class="post-score" title="current number of votes">0</div><span id="post-2014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, it may. You'll have to be prepared to chew on some raw data packets, the keylogger most likely tries to conceal its communications. Still Wireshark should show them, and allows some higher level view on the connections. Take a stroll through the <a href="http://www.wireshark.org/docs/wsug_html_chunked/">User's Guide</a> to get an idea what's possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '11, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2014" class="comments-container"></div><div id="comment-tools-2014" class="comment-tools"></div><div class="clear"></div><div id="comment-2014-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51381"></span>

<div id="answer-container-51381" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51381-score" class="post-score" title="current number of votes">0</div><span id="post-51381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What's type of protocol that keylog using to tranfer file outbound my PC? I used wireshark but couldn't find smtp or ftp protocol :(</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '16, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/99e958fccb851d94253e7653f709498f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tr%E1%BA%A7n%20Th%C3%A0nh%20%C4%90%E1%BB%A9c&#39;s gravatar image" /><p><span>Trần Thành Đức</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trần Thành Đức has no accepted answers">0%</span></p></div></div><div id="comments-container-51381" class="comments-container"><span id="51382"></span><div id="comment-51382" class="comment"><div id="post-51382-score" class="comment-score"></div><div class="comment-text"><p>It is not a Wireshark question so I won't ask you to convert your "Answer" into a Question (which would be the right thing to do if it wasn't totally off-topic). As it is, the right thing according to site policy is to remove your non-Answer.</p><p>To the subject: if you would be creating a keylogger yourself, would you like it to be easily noticeable? That's the reason why any keylogger is not likely to use smtp or ftp but rather some encrypted proprietary protocol using tcp (or even udp) as transport layer.</p></div><div id="comment-51382-info" class="comment-info"><span class="comment-age">(03 Apr '16, 07:43)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-51381" class="comment-tools"></div><div class="clear"></div><div id="comment-51381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

