+++
type = "question"
title = "Show visited http address and &quot;who&quot; (ip address) who requested given url"
description = '''Hello, I have tried following: Statistics -&amp;gt; HTTP -&amp;gt; Load Distribution, setting the filter &quot;tcp.port == 80&quot;, then I get in the dialog that pops up HTTP urls that were/are called in the network (promiscuous mode is of course on). I see when someone on the network calls address by name, but I ca...'''
date = "2015-09-27T12:34:00Z"
lastmod = "2015-09-27T23:47:00Z"
weight = 46199
keywords = [ "url", "filtering", "http" ]
aliases = [ "/questions/46199" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Show visited http address and "who" (ip address) who requested given url](/questions/46199/show-visited-http-address-and-who-ip-address-who-requested-given-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46199-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have tried following: Statistics -&gt; HTTP -&gt; Load Distribution, setting the filter "tcp.port == 80", then I get in the dialog that pops up HTTP urls that were/are called in the network (promiscuous mode is of course on).</p><p>I see when someone on the network calls address by name, but I can not differentiate who called the address.</p><p>Is there any easy way how to filter out traffic on the network in form of table, which could possibly look like this?</p><p>| Time | Domain/url address visited | IP of who visited the address |</p><p>Thanks in advance for any help provided!</p></div><div id="question-tags" class="tags-container tags">url filtering http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '15, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/6a64cda56727bab4fa53ba7ea0a8fac0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddaniel&#39;s gravatar image" /><p>ddaniel<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddaniel has no accepted answers">0%</span></p></div></div><div id="comments-container-46199" class="comments-container"></div><div id="comment-tools-46199" class="comment-tools"></div><div class="clear"></div><div id="comment-46199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46207"></span>

<div id="answer-container-46207" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46207-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark for that:</p><blockquote><p>tshark -nr http.pcap -T fields -e frame.time -e http.request.full_uri -e ip.src -E separator=;</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '15, 23:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46207" class="comments-container"><span id="46211"></span><div id="comment-46211" class="comment"><div id="post-46211-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply but - is this tshark version specific? It tells me that "Separator" can not be used with option=value pair. Can you provide me with further assistance please?</p></div><div id="comment-46211-info" class="comment-info"><span class="comment-age">(28 Sep '15, 01:24)</span> ddaniel</div></div></div><div id="comment-tools-46207" class="comment-tools"></div><div class="clear"></div><div id="comment-46207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

