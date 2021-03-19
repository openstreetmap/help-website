+++
type = "question"
title = "Analyze per IP"
description = '''I&#x27;m desperately trying to determine which clients (IP) are causing a large amount of lag to my server. I have been able to manually scan packet data with IP filters to determine which ones have a large bad packets / total packet ratio, but this is a very labor intensive process. Is there a way to di...'''
date = "2011-09-17T02:32:00Z"
lastmod = "2011-09-17T03:32:00Z"
weight = 6430
keywords = [ "ip", "bad", "packets" ]
aliases = [ "/questions/6430" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Analyze per IP](/questions/6430/analyze-per-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6430-score" class="post-score" title="current number of votes">0</div><span id="post-6430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm desperately trying to determine which clients (IP) are causing a large amount of lag to my server. I have been able to manually scan packet data with IP filters to determine which ones have a large bad packets / total packet ratio, but this is a very labor intensive process. Is there a way to display all clients simultaneously and their "bad" packets / their total packets ratio? Thanks in advance!</p><p>Michael</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-bad" rel="tag" title="see questions tagged &#39;bad&#39;">bad</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '11, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/c2c32e56d8b7214b314e6a8fc85113b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikebriggs2k&#39;s gravatar image" /><p><span>mikebriggs2k</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikebriggs2k has no accepted answers">0%</span></p></div></div><div id="comments-container-6430" class="comments-container"></div><div id="comment-tools-6430" class="comment-tools"></div><div class="clear"></div><div id="comment-6430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6432"></span>

<div id="answer-container-6432" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6432-score" class="post-score" title="current number of votes">2</div><span id="post-6432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what "you" mean by bad packets, but I assume you are able to create a display filter that will match only the bad packets. In that case, there are two ways of doing this.</p><h2 id="in-wireshark">In Wireshark:</h2><ul><li>Use the display filter for "bad" packets</li><li>Go to "Statistics -&gt; Endpoints"</li><li>Click on the IP TAB</li><li>Use "copy" to copy the data in CSV format to clipboard</li><li>Import the data in a tool of choice</li><li>Now enable the "Limit to display filter" checkmark</li><li>Again use copy to export the data</li><li>Use your tool of choice to match the IP addresses in both outputs</li></ul><h2 id="in-tshark">In tshark:</h2><p>The steps are basically the same, but now use the following to commands to create the output:</p><ul><li><code>tshark -r &lt;file&gt; -qz conv,ip</code></li><li><code>tshark -r &lt;file&gt; -qz conv,ip&lt;bad-packet-filter&gt;</code></li></ul><p>This assumes the destination address is always the server-ip as tshark will create conversation overviews, not endpoint overviews.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '11, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6432" class="comments-container"></div><div id="comment-tools-6432" class="comment-tools"></div><div class="clear"></div><div id="comment-6432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

