+++
type = "question"
title = "How to capture traffic from YouTube"
description = '''How do I capture packets sent only to YouTube and received only from YouTube? I want to check how YouTube streams its video, especially the live ones, so I want to capture only send&#x27;s and receive&#x27;s from YouTube. How do I do that?'''
date = "2011-08-09T12:50:00Z"
lastmod = "2011-08-18T14:42:00Z"
weight = 5597
keywords = [ "capture-filter" ]
aliases = [ "/questions/5597" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture traffic from YouTube](/questions/5597/how-to-capture-traffic-from-youtube)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5597-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I capture packets sent only to YouTube and received only from YouTube? I want to check how YouTube streams its video, especially the live ones, so I want to capture only send's and receive's from YouTube. How do I do that?</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '11, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/d9e68683423689115ca75c2944f6195b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Giu&#39;s gravatar image" /><p>Giu<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Giu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '11, 23:32</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5597" class="comments-container"></div><div id="comment-tools-5597" class="comment-tools"></div><div class="clear"></div><div id="comment-5597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5748"></span>

<div id="answer-container-5748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5748-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to see only the traffic related to you tube, you just need to apply an ip filter</p><pre><code>ip.src ==  74.125.232.232</code></pre><p>But if you want something more accurate you might want to include some of this other filters</p><pre><code>           udp.port==554 
           rtsp</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '11, 14:42</strong></p><img src="https://secure.gravatar.com/avatar/251b4a8e3088f26eeadd3550e205818d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sfrj&#39;s gravatar image" /><p>sfrj<br />
<span class="score" title="74 reputation points">74</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sfrj has no accepted answers">0%</span></p></div></div><div id="comments-container-5748" class="comments-container"><span id="5753"></span><div id="comment-5753" class="comment"><div id="post-5753-score" class="comment-score"></div><div class="comment-text"><p>That won't mean he only captures packets to or from YouTube; it captures all packets and then filters them out later.</p><p>Unfortunately, it's <em>really</em> hard to have a capture filter for YouTube - I just played a video, and it was sent over HTTP from a host named "o-o.preferred.nuq04s10.v2.lscache2.c.youtube.com", so it's probably very hard to predict what host will send the video. I'd say "capture without a filter and look for YouTube traffic".</p></div><div id="comment-5753-info" class="comment-info"><span class="comment-age">(18 Aug '11, 18:08)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5748" class="comment-tools"></div><div class="clear"></div><div id="comment-5748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

