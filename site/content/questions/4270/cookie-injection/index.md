+++
type = "question"
title = "cookie injection"
description = '''hi everyone. i&#x27;m writing a thesis on Facebook Connect implementation and on its vulnerability issues. Since its for educational purpose,it&#x27;s important for me to simulate a side jacking attack. i&#x27;ve used this configuration: one vbox guest machine (WinXP) acting as client and one vbox host machine (op...'''
date = "2011-05-28T10:06:00Z"
lastmod = "2011-05-28T10:06:00Z"
weight = 4270
keywords = [ "sniffing", "cookies", "session", "security" ]
aliases = [ "/questions/4270" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cookie injection](/questions/4270/cookie-injection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4270-score" class="post-score" title="current number of votes">0</div><span id="post-4270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi everyone. i'm writing a thesis on Facebook Connect implementation and on its vulnerability issues.</p><p>Since its for educational purpose,it's important for me to simulate a side jacking attack. i've used this configuration: one vbox guest machine (WinXP) acting as client and one vbox host machine (openSuse) acting as connection gateway (on wich Wireshark is sniffing packets).</p><p><img src="http://i.imgur.com/yKyuS.jpg" alt="alt text" /></p><ul><li>on the guest machine, after having flushed cookies and browser history, i have shared a youtube video on my fb profile through fb connect, while on host i've recorded network traffic. after that, i just closed the browser (not logged out), moved to host, filtered traffing for packets that contains http cookies related to user session.</li><li>After that, i've tried, on host, to share a YT video on FB using these captured cookies. for that purpose i've used Cookie Manager+ ff extension. anyway, this trick doesn't work and my credential (even not my name, but my password yes) are still needed. i'm sure that i can use cookies usefully, but i don't know how practically. I'd like to know from you which cookies have to be injected and also whic other part of the request (e.g. querystring) have to be inserted, so that this attack is effective? i've tried other tools (<a href="http://codebutler.github.com/firesheep/">Firesheep</a> ,<a href="https://github.com/diogomonica/py-cookieJsInjection">py-cookieJsInjection</a>, <a href="http://hamster.erratasec.com/help/index.html">Hamster and Ferret</a>) that help to make straightforward this process, but none of these helped.</li></ul><p>thanks Luke</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-cookies" rel="tag" title="see questions tagged &#39;cookies&#39;">cookies</span> <span class="post-tag tag-link-session" rel="tag" title="see questions tagged &#39;session&#39;">session</span> <span class="post-tag tag-link-security" rel="tag" title="see questions tagged &#39;security&#39;">security</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '11, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/63aff4ae9b0fd0c6c53a613e12a44784?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lordluke80&#39;s gravatar image" /><p><span>lordluke80</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lordluke80 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-4270" class="comments-container"></div><div id="comment-tools-4270" class="comment-tools"></div><div class="clear"></div><div id="comment-4270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

