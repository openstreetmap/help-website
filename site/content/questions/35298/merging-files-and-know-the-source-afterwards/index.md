+++
type = "question"
title = "Merging files and know the source afterwards"
description = '''Hi, when merging two files (especially in chrononlogical order) it somethimes is nessecary to know from which file the corresponding line came. Is there any possibility to get that information in the columns? There&#x27;s a &quot;file&quot; custom field, but it displays nothing. thanks &amp;amp; best regards, Björn'''
date = "2014-08-07T06:09:00Z"
lastmod = "2014-08-07T06:32:00Z"
weight = 35298
keywords = [ "merge", "pcap" ]
aliases = [ "/questions/35298" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Merging files and know the source afterwards](/questions/35298/merging-files-and-know-the-source-afterwards)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35298-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, when merging two files (especially in chrononlogical order) it somethimes is nessecary to know from which file the corresponding line came. Is there any possibility to get that information in the columns? There's a "file" custom field, but it displays nothing.</p><p>thanks &amp; best regards, Björn</p></div><div id="question-tags" class="tags-container tags">merge pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '14, 06:09</strong></p><img src="https://secure.gravatar.com/avatar/9a0ce3cb9c1e19b4dc8ec97a8b4b7dfd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="McSlow&#39;s gravatar image" /><p>McSlow<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="McSlow has no accepted answers">0%</span></p></div></div><div id="comments-container-35298" class="comments-container"></div><div id="comment-tools-35298" class="comment-tools"></div><div class="clear"></div><div id="comment-35298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35300"></span>

<div id="answer-container-35300" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35300-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The latest builds of mergecap usually write the originating files into the PCAPng file header comment field, so you can see it by looking at Statistics -&gt; Summary.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '14, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35300" class="comments-container"><span id="35306"></span><div id="comment-35306" class="comment"><div id="post-35306-score" class="comment-score"></div><div class="comment-text"><p>yes, but I'd need it for every packet, so that I can see which packet has been captured from which file or point after merging. Perhaps there's another approach to simultaneoulsy capture at several points in your network and put this in one timeline without getting confused :)</p><p>Current scenario was not too uncommon: (Multiple-)Server-Client connection, some "stuff" inbetween, some cross-connections between servers. Captured at all ends with tcpdump and merged all files in wireshark. Of course you will see a lot of packets twice or even n-times, recorded at src- and destination, but sometimes it's a mess to find out which end you're currently watching... :)</p></div><div id="comment-35306-info" class="comment-info"><span class="comment-age">(07 Aug '14, 07:46)</span> McSlow</div></div><span id="35307"></span><div id="comment-35307" class="comment"><div id="post-35307-score" class="comment-score"></div><div class="comment-text"><p>You could try to do that with TraceWrangler. It allows creating PCAPng file with one dedicated interface entry per source interface, so you should end up with a file where each packet is assigned it's own interface. Then you could add a column showing interface IDs and you're there.</p><p>TraceWrangler is available at <a href="http://www.tracewrangler.com">http://www.tracewrangler.com</a></p><p>I have to admit that I didn't test the merge features as much as I should, but time is short and I wanted to release the version for Sharkfest :-)</p></div><div id="comment-35307-info" class="comment-info"><span class="comment-age">(07 Aug '14, 07:49)</span> Jasper ♦♦</div></div></div><div id="comment-tools-35300" class="comment-tools"></div><div class="clear"></div><div id="comment-35300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

