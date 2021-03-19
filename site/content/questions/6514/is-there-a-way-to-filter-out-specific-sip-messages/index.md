+++
type = "question"
title = "Is there a way to filter out specific SIP messages?"
description = '''I&#x27;m monitoring a Cisco CUCM for troubleshooting purposes. All I care about are call setup messages. The REGISTER and OPTIONS messages are cluttering up the display, and I was wondering if I could filter those out?'''
date = "2011-09-23T08:47:00Z"
lastmod = "2012-09-26T15:50:00Z"
weight = 6514
keywords = [ "filter", "sip", "options", "register" ]
aliases = [ "/questions/6514" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to filter out specific SIP messages?](/questions/6514/is-there-a-way-to-filter-out-specific-sip-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6514-score" class="post-score" title="current number of votes">1</div><span id="post-6514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm monitoring a Cisco CUCM for troubleshooting purposes. All I care about are call setup messages.</p><p>The REGISTER and OPTIONS messages are cluttering up the display, and I was wondering if I could filter those out?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-options" rel="tag" title="see questions tagged &#39;options&#39;">options</span> <span class="post-tag tag-link-register" rel="tag" title="see questions tagged &#39;register&#39;">register</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '11, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/a4dce96f216fca0f0685324914fa1b31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cisco%20TelePresence%20Guy&#39;s gravatar image" /><p><span>Cisco TelePr...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cisco TelePresence Guy has no accepted answers">0%</span></p></div></div><div id="comments-container-6514" class="comments-container"></div><div id="comment-tools-6514" class="comment-tools"></div><div class="clear"></div><div id="comment-6514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6524"></span>

<div id="answer-container-6524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6524-score" class="post-score" title="current number of votes">2</div><span id="post-6524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Apply display filter <code>sip.Method == "INVITE"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '11, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6524" class="comments-container"><span id="6529"></span><div id="comment-6529" class="comment"><div id="post-6529-score" class="comment-score"></div><div class="comment-text"><p>OK, so if all I want to see are the INVITEs and the dialog that comes after them, I would use:</p><p>sip.Method != "REGISTER" or sip.Method != "OPTIONS"</p></div><div id="comment-6529-info" class="comment-info"><span class="comment-age">(23 Sep '11, 13:19)</span> <span class="comment-user userinfo">Cisco TelePr...</span></div></div><span id="6531"></span><div id="comment-6531" class="comment"><div id="post-6531-score" class="comment-score">1</div><div class="comment-text"><p>@Cisco, I don't know much about SIP, but I think you meant:</p><pre><code>(sip.Method != &quot;REGISTER&quot;) &amp;&amp; (sip.Method != &quot;OPTIONS&quot;)</code></pre></div><div id="comment-6531-info" class="comment-info"><span class="comment-age">(23 Sep '11, 13:48)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="6532"></span><div id="comment-6532" class="comment"><div id="post-6532-score" class="comment-score">2</div><div class="comment-text"><p>If you want to see them use:<br />
(sip.Method == "REGISTER") || (sip.Method == "OPTIONS")<br />
If you want to hide them use:<br />
!(sip.Method == "REGISTER") &amp;&amp; !(sip.Method == "OPTIONS")</p></div><div id="comment-6532-info" class="comment-info"><span class="comment-age">(23 Sep '11, 14:32)</span> <span class="comment-user userinfo">joke</span></div></div><span id="6533"></span><div id="comment-6533" class="comment"><div id="post-6533-score" class="comment-score"></div><div class="comment-text"><p>Yes, I think the last comment is the syntax of what I was looking for. Thanks!</p></div><div id="comment-6533-info" class="comment-info"><span class="comment-age">(23 Sep '11, 14:37)</span> <span class="comment-user userinfo">Cisco TelePr...</span></div></div><span id="14564"></span><div id="comment-14564" class="comment"><div id="post-14564-score" class="comment-score"></div><div class="comment-text"><p>above ones are not filtering all OPTIONS and 200 OK response to OPTIONS message.</p><p>But below one is working for that.</p><p>sip &amp;&amp; !(sip.CSeq.method == "OPTIONS")</p></div><div id="comment-14564-info" class="comment-info"><span class="comment-age">(26 Sep '12, 15:50)</span> <span class="comment-user userinfo">optionsboy</span></div></div></div><div id="comment-tools-6524" class="comment-tools"></div><div class="clear"></div><div id="comment-6524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

