+++
type = "question"
title = "How to make &quot;Hide this stream&quot; hide this and previously hidden streams"
description = '''The new interface has a different behaviour for hiding/filtering tcp streams and for my usage, it&#x27;s a lot less useful. Si I&#x27;m looking to see if I can configure the new interface to &quot;do the right thing&quot;. My scenario:  We have a client-server set up where the client will send a series of http requests...'''
date = "2015-12-08T12:07:00Z"
lastmod = "2015-12-08T12:07:00Z"
weight = 48363
keywords = [ "follow.tcp.stream", "hide", "display-filter" ]
aliases = [ "/questions/48363" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to make "Hide this stream" hide this and previously hidden streams](/questions/48363/how-to-make-hide-this-stream-hide-this-and-previously-hidden-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48363-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The new interface has a different behaviour for hiding/filtering tcp streams and for my usage, it's a lot less useful. Si I'm looking to see if I can configure the new interface to "do the right thing".</p><p>My scenario: We have a client-server set up where the client will send a series of http requests, and get responses. A session consists of multiple http request/responses, and there may be several sessions.</p><p>When I'm using wireshark, I look at one request/response pair (or maybe several, if persistent connections happen). Once I'm done with that, I want to hide it and move on to the next.</p><p>Old interface had "filter out this stream". New one has "hide this stream". But the old one kept hiding previous streams I'd also filtered out, the new one just hides the current one, and any previous ones I'd hidden now reappear.</p><p>Which is a pain, since they're "in the past", and I don't want to see them again. I want to move on to the next request/response.</p><p>Can I configure "Hide this stream" to still hide previously hidden streams? Shouldn't this be the default anyway? Is it ever useful just to hide one stream at a time?</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream hide display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Dec '15, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/8d1dc85bd2d8ed3a2074b9728fbdaa55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="The%20Archetypal%20Paul&#39;s gravatar image" /><p>The Archetyp...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="The Archetypal Paul has no accepted answers">0%</span></p></div></div><div id="comments-container-48363" class="comments-container"></div><div id="comment-tools-48363" class="comment-tools"></div><div class="clear"></div><div id="comment-48363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

