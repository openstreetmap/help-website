+++
type = "question"
title = "Use capture filter on tshark when reading a file"
description = '''I need to filter a big pcap, I can use display filter, but it&#x27;s typically slower than capture filter. However I got the following message: tshark -r tmp1.pcap -f &quot;tcp port 80&quot; tshark: Only read filters, not capture filters, can be specified when reading a capture file.  When how can I use capture fi...'''
date = "2015-04-29T12:35:00Z"
lastmod = "2015-04-29T23:40:00Z"
weight = 41951
keywords = [ "tshark" ]
aliases = [ "/questions/41951" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use capture filter on tshark when reading a file](/questions/41951/use-capture-filter-on-tshark-when-reading-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41951-score" class="post-score" title="current number of votes">0</div><span id="post-41951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to filter a big pcap, I can use display filter, but it's typically slower than capture filter. However I got the following message:</p><pre><code>tshark -r tmp1.pcap -f &quot;tcp port 80&quot;
tshark: Only read filters, not capture filters, can be specified when reading a capture file.</code></pre><p>When how can I use capture filter for tshark to read from a file.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-41951" class="comments-container"></div><div id="comment-tools-41951" class="comment-tools"></div><div class="clear"></div><div id="comment-41951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41953"></span>

<div id="answer-container-41953" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41953-score" class="post-score" title="current number of votes">1</div><span id="post-41953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using a capture filter while reading is not an option in tshark. You could use tcpdump or windump to do that for you:</p><pre><code>tcpdump -r infile.pcap -w outfile.pcap &quot;tcp port 80&quot;</code></pre><p>or</p><pre><code>windump -r infile.pcap -w outfile.pcap &quot;tcp port 80&quot;</code></pre><p>This will work quicker than tshark and has less memory consumption, so you can process larger files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '15, 13:05</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-41953" class="comments-container"><span id="41958"></span><div id="comment-41958" class="comment"><div id="post-41958-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@SYN-bit</span>. If I do <code>tcpdump -r infile.pcap  "tcp port 80"</code> to output things to screen (so I can pipe it to another program to process), it's incredibly slow: 6MB pcap infile.pcap will take minutes. Not sure why.</p></div><div id="comment-41958-info" class="comment-info"><span class="comment-age">(29 Apr '15, 21:40)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="41959"></span><div id="comment-41959" class="comment"><div id="post-41959-score" class="comment-score"></div><div class="comment-text"><p>Have you tried to use option "-n" do disable name resolution? Normally DNS lookups slow things down.</p></div><div id="comment-41959-info" class="comment-info"><span class="comment-age">(29 Apr '15, 22:58)</span> <span class="comment-user userinfo">Uli</span></div></div><span id="41960"></span><div id="comment-41960" class="comment"><div id="post-41960-score" class="comment-score"></div><div class="comment-text"><p>With newer versions of tshark you might try</p><pre><code>tcpdump -r infile.pcap -w - &quot;tcp port 80&quot; | tshark -r -</code></pre><p>That might have the same problem, though, as TShark would <em>also</em> try DNS lookups, but might do them differently. You could pass tshark the <code>-n</code> flag to get <em>it</em> not to do DNS lookups in that case.</p></div><div id="comment-41960-info" class="comment-info"><span class="comment-age">(29 Apr '15, 23:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-41953" class="comment-tools"></div><div class="clear"></div><div id="comment-41953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

