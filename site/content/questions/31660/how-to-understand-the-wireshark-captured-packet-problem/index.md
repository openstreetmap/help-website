+++
type = "question"
title = "How to understand the wireshark captured packet problem?"
description = '''I have a linux-based Firewall/Router (IPtables) in my network. When I change Default gateway of client to the Firewall, I can ping, traceroute, telnet google.com 80 ... but can&#x27;t browse via Browsers (IE, Chrome, FireFox without any proxy config). How can I analyse my tcp packet and understand the pr...'''
date = "2014-04-08T23:58:00Z"
lastmod = "2014-04-09T14:10:00Z"
weight = 31660
keywords = [ "tcp", "packet" ]
aliases = [ "/questions/31660" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to understand the wireshark captured packet problem?](/questions/31660/how-to-understand-the-wireshark-captured-packet-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31660-score" class="post-score" title="current number of votes">0</div><span id="post-31660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a linux-based Firewall/Router (IPtables) in my network. When I change Default gateway of client to the Firewall, I can ping, traceroute, telnet google.com 80 ... but can't browse via Browsers (IE, Chrome, FireFox without any proxy config). How can I analyse my tcp packet and understand the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '14, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/fbfa051911bebbbd854365f89611e645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="q12345&#39;s gravatar image" /><p><span>q12345</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="q12345 has no accepted answers">0%</span></p></div></div><div id="comments-container-31660" class="comments-container"></div><div id="comment-tools-31660" class="comment-tools"></div><div class="clear"></div><div id="comment-31660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31689"></span>

<div id="answer-container-31689" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31689-score" class="post-score" title="current number of votes">0</div><span id="post-31689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but can't browse via Browsers (IE, Chrome, FireFox without any proxy config)</p></blockquote><p>Maybe you just believe there is no proxy config, while there is one. What do you get if you run the following command on the client</p><blockquote><p>telnet wpad 80<br />
</p></blockquote><p>or</p><blockquote><p>telnet wpad.your-internal-domain 80</p></blockquote><p>Do you get a connection?</p><p>If so, please uncheck the following option in your browser and try again:</p><p>Firefox: Disable the option "Autodetect Proxy for this network" and select the option "no proxy".</p><p>Please read about Web Proxy Auto-Discovery Protocol (WPAD): <a href="http://en.wikipedia.org/wiki/Web_Proxy_Autodiscovery_Protocol">http://en.wikipedia.org/wiki/Web_Proxy_Autodiscovery_Protocol</a></p><p>If <code>wpad</code> isn't an issue in your environment, please post a sample capture file somewhere (google drive, dropbox, cloudshark.org) and post the link here.</p><p>Furthermore check the firewall logs ;-))</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '14, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-31689" class="comments-container"></div><div id="comment-tools-31689" class="comment-tools"></div><div class="clear"></div><div id="comment-31689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

