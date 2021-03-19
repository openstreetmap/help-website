+++
type = "question"
title = "DNS queries number is not the same all the time"
description = '''Hi,  I&#x27;m analyzing a website for a school project (dns queries especially) and I was wondering why the number of dns queries constant ? I&#x27;m aware that there are some fluctuations because of the advertising websites but when I refresh the page without using the cache (Ctrl+Shift+R) I&#x27;ve got like 70 q...'''
date = "2014-12-06T12:48:00Z"
lastmod = "2014-12-08T05:01:00Z"
weight = 38399
keywords = [ "query", "dns", "dnsquery" ]
aliases = [ "/questions/38399" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [DNS queries number is not the same all the time](/questions/38399/dns-queries-number-is-not-the-same-all-the-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38399-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm analyzing a website for a school project (dns queries especially) and I was wondering why the number of dns queries constant ? I'm aware that there are some fluctuations because of the advertising websites but when I refresh the page without using the cache (Ctrl+Shift+R) I've got like 70 queries but when I clear my history, I'm having 140 queries. Also these numbers change when I use a different browser.</p><p>Someone to help ? Thanks ! :)</p></div><div id="question-tags" class="tags-container tags">query dns dnsquery</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '14, 12:48</strong></p><img src="https://secure.gravatar.com/avatar/76e44f4e20950e6d6c7bee6556a597fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomatediabolik&#39;s gravatar image" /><p>tomatediabolik<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomatediabolik has no accepted answers">0%</span></p></div></div><div id="comments-container-38399" class="comments-container"></div><div id="comment-tools-38399" class="comment-tools"></div><div class="clear"></div><div id="comment-38399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38429"></span>

<div id="answer-container-38429" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38429-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Both your OS and your browser do DNS caching to speed up your browsing experience, hence you won't see the same amount of DNS queries if you access the same site several times. If you want to get the same amount of DNS queries (more or less), please clear all DNS caches on the client.</p><ul><li>clear the browser history</li><li>clear the OS dns cache (on Windows: ipconfig /flushdns)</li><li>restart the browser</li><li>start Wirshark</li><li>access the site</li></ul><p>Now you should see the same DNS queries every time (more or less), <strong>unless</strong> the site places different ads on their page every now and then. Then you will get different DNS queries for those embedded ads (different target servers).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '14, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38429" class="comments-container"></div><div id="comment-tools-38429" class="comment-tools"></div><div class="clear"></div><div id="comment-38429-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

