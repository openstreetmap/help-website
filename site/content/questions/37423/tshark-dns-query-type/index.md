+++
type = "question"
title = "TShark DNS Query Type"
description = '''Is there a way to use TShark to extract TCP/UDP DNS queries and end up with a list of the original query and query type in letter format? Right now my command looks like this: tshark -n -r capture.pcap -T fields -e dns.qry.name -e dns.qry.type -Y &#x27;( udp.port==53 || tcp.port==53 ) &amp;amp;&amp;amp; dns.flag...'''
date = "2014-10-28T19:43:00Z"
lastmod = "2014-10-29T07:26:00Z"
weight = 37423
keywords = [ "query", "type", "tshark", "dns" ]
aliases = [ "/questions/37423" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TShark DNS Query Type](/questions/37423/tshark-dns-query-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37423-score" class="post-score" title="current number of votes">0</div><span id="post-37423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to use TShark to extract TCP/UDP DNS queries and end up with a list of the original query and query type in letter format?</p><p>Right now my command looks like this:</p><p>tshark -n -r capture.pcap -T fields -e dns.qry.name -e dns.qry.type -Y '( udp.port==53 || tcp.port==53 ) &amp;&amp; dns.flags.response==0'</p><p>What it generates is a file of query names with a tab and then a number of the query type. I then have to cat the file and SED looking for a combination of a &lt;tab&gt; plus the query type number to replace it with a &lt;tab&gt; and the right letter query - i.e., A is 1, CNAME is 5, AAAA is 2, etc.</p><p>My goal is to come up with a list of domains I can replay against a DNS server using queryperf or dig.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '14, 19:43</strong></p><img src="https://secure.gravatar.com/avatar/6c53519eeea2cfa4117e24e24d0b547c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JerimiahF&#39;s gravatar image" /><p><span>JerimiahF</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JerimiahF has no accepted answers">0%</span></p></div></div><div id="comments-container-37423" class="comments-container"></div><div id="comment-tools-37423" class="comment-tools"></div><div class="clear"></div><div id="comment-37423-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37430"></span>

<div id="answer-container-37430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37430-score" class="post-score" title="current number of votes">0</div><span id="post-37430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My goal is to come up with a list of domains</p></blockquote><p>Then you could try this:</p><blockquote><p>tshark -nr capture.pcap -V -Y "dns" | grep "Name:" | awk '{print $2}' | sort -u</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '14, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Oct '14, 05:02</strong> </span></p></div></div><div id="comments-container-37430" class="comments-container"><span id="37434"></span><div id="comment-37434" class="comment"><div id="post-37434-score" class="comment-score"></div><div class="comment-text"><p>Kurt - thanks for answering.<br />
</p><p>The challenge I have though is that besides the DNS name, I also need the type of record asked for either with a TAB or space between it so the list would look like this:</p><p>www.apple.com A</p><p>Queryperf (the faster and preferred tool) needs both pieces in order to do the query and ensure its asking the same request as the capture did.</p></div><div id="comment-37434-info" class="comment-info"><span class="comment-age">(29 Oct '14, 05:37)</span> <span class="comment-user userinfo">JerimiahF</span></div></div><span id="37435"></span><div id="comment-37435" class="comment"><div id="post-37435-score" class="comment-score">1</div><div class="comment-text"><p>O.K. then try this:</p><blockquote><p>tshark.exe -nr c:\temp\dns.pcap -V | grep ": type" | awk '{print $1 $3}'</p></blockquote><p>Please add some 'sed magic' to remove the : and ,. I leave that up to you ;-)</p></div><div id="comment-37435-info" class="comment-info"><span class="comment-age">(29 Oct '14, 05:47)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="37440"></span><div id="comment-37440" class="comment"><div id="post-37440-score" class="comment-score"></div><div class="comment-text"><p>Wow - simple yet VERY effective. This is perfect! Thanks Kurt!!!</p><p>Difference of before/after is now a 150MB capture with ~240k of queries - now processes in about 1/3 the time and thus is far less complex of the SED hell I was going thru before with some massive -V dumps to parse thru.</p></div><div id="comment-37440-info" class="comment-info"><span class="comment-age">(29 Oct '14, 07:26)</span> <span class="comment-user userinfo">JerimiahF</span></div></div></div><div id="comment-tools-37430" class="comment-tools"></div><div class="clear"></div><div id="comment-37430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

