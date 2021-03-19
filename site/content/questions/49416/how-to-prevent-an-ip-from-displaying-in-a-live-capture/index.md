+++
type = "question"
title = "How to prevent an IP from displaying in a live capture?"
description = '''Hi, everytime I hit &quot;start a new live capture&quot; a set of new Ips will pop up. Whenever I press ignore on the IPS I do not want to show up ever again, they still show up whenever I do another live capture... How do I prevent this from happening? Say I want 192.168.1.215 and 239.255.255.250 to not show...'''
date = "2016-01-20T15:03:00Z"
lastmod = "2016-01-21T22:53:00Z"
weight = 49416
keywords = [ "blacklist", "ignore" ]
aliases = [ "/questions/49416" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to prevent an IP from displaying in a live capture?](/questions/49416/how-to-prevent-an-ip-from-displaying-in-a-live-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49416-score" class="post-score" title="current number of votes">0</div><span id="post-49416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, everytime I hit "start a new live capture" a set of new Ips will pop up. Whenever I press ignore on the IPS I do not want to show up ever again, they still show up whenever I do another live capture... How do I prevent this from happening?</p><p>Say I want 192.168.1.215 and 239.255.255.250 to not show up again, what do I do?</p><p>Also, is it possible to copy Ip addresses found in live captures to your clipboard? So you dont have to type them out?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-blacklist" rel="tag" title="see questions tagged &#39;blacklist&#39;">blacklist</span> <span class="post-tag tag-link-ignore" rel="tag" title="see questions tagged &#39;ignore&#39;">ignore</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '16, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/085299273416958d9fa522275f25dc45?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="julian4445&#39;s gravatar image" /><p><span>julian4445</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="julian4445 has no accepted answers">0%</span></p></div></div><div id="comments-container-49416" class="comments-container"></div><div id="comment-tools-49416" class="comment-tools"></div><div class="clear"></div><div id="comment-49416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49417"></span>

<div id="answer-container-49417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49417-score" class="post-score" title="current number of votes">0</div><span id="post-49417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can apply a display filter like <code>!(ip.addr == ip.add.re.ss1) and !(ip.addr == ip.add.re.ss2)</code> during live capture.</p><p>You can build the display filter expression step-by-step by right-clicking on a line representing a packet field (like source IP address) in the packet dissection pane and choose <code>Apply as Filter -&gt; ... and not Selected</code> from the context menu. To do so conveniently when a capture is running, it is better to switch off the automatic scrolling of the packet list before doing it.</p><p>You <em>cannot</em> build display filter expressions which use pseudo-fields (such as <code>ip.addr</code> which represents <code>ip.src</code> and <code>ip.dst</code> simultaneously) this way (i.e. <code>Apply as Filter -&gt;</code>) because they are not available as lines in the packet dissection, but you may use e.g. <code>ip.dst</code> to get the address to the filter expression and then manually change <code>ip.dst</code> to <code>ip.addr</code>.</p><p>You can save named (labelled) pre-defined display filters for single-click application in future: at the rightmost end of the line which contains the display filter form field, there is a "+" button. When you press it, another form line is inserted between the original one and the packet list pane, where the filter expression is pre-filled with a copy of the currently used one, and it is enough to fill in the "label" form field and press OK. The additional line disappears and a button with the label you've just filled in is added to the right from the "+" button. Pressing one of these "label" buttons applies the corresponding filter. There is also another button, <code>Filter Expression Preferences</code>, on that additional line, which is a shortcut to the preferences dialog, where you can enable/disable, add and delete your single-click display filters. Only the enabled ones are available as buttons next to the "+".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '16, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jan '16, 16:10</strong> </span></p></div></div><div id="comments-container-49417" class="comments-container"><span id="49442"></span><div id="comment-49442" class="comment"><div id="post-49442-score" class="comment-score"></div><div class="comment-text"><p>You're of great help, thank you! Whenever I click apply as filter and then "not selected" and I try to do it to another source IP Address, it gets rid of the current filter. How do I prevent that from happening?</p></div><div id="comment-49442-info" class="comment-info"><span class="comment-age">(21 Jan '16, 20:55)</span> <span class="comment-user userinfo">julian4445</span></div></div><span id="49444"></span><div id="comment-49444" class="comment"><div id="post-49444-score" class="comment-score"></div><div class="comment-text"><p>Click on "Apply as Filter" and then "...and not Selected."</p><p>"Selected" or "Not Selected" will replace the current display filter. Any of the choices beginning with "..." will add to the current display filter.</p></div><div id="comment-49444-info" class="comment-info"><span class="comment-age">(21 Jan '16, 22:53)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div></div><div id="comment-tools-49417" class="comment-tools"></div><div class="clear"></div><div id="comment-49417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

