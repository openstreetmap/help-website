+++
type = "question"
title = "starting capture from the command line with a display filter active"
description = '''I have tried using the -R option but it seems it is only for reading previously captured files? Is there anyway of doing this please. I have just downloaded latest stable version 1.6.0 and rebuilt on centos 5.5. e.g.  wireshark -i bond0 -R tcp.port==8600 -k and whatever else options etc I found a fa...'''
date = "2011-07-18T07:36:00Z"
lastmod = "2011-07-18T10:47:00Z"
weight = 5102
keywords = [ "display-filter" ]
aliases = [ "/questions/5102" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [starting capture from the command line with a display filter active](/questions/5102/starting-capture-from-the-command-line-with-a-display-filter-active)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5102-score" class="post-score" title="current number of votes">0</div><span id="post-5102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried using the -R option but it seems it is only for reading previously captured files? Is there anyway of doing this please. I have just downloaded latest stable version 1.6.0 and rebuilt on centos 5.5.</p><p>e.g. wireshark -i bond0 -R tcp.port==8600 -k and whatever else options etc</p><p>I found a faq with someone offering a solution (which was admitted that it did not work) with hope someone would answer.</p><p>any ideas most greatful</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '11, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/d64d9a4ffe16338d4c65598b82424d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spotthemaniac&#39;s gravatar image" /><p><span>spotthemaniac</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spotthemaniac has no accepted answers">0%</span></p></div></div><div id="comments-container-5102" class="comments-container"></div><div id="comment-tools-5102" class="comment-tools"></div><div class="clear"></div><div id="comment-5102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5103"></span>

<div id="answer-container-5103" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5103-score" class="post-score" title="current number of votes">0</div><span id="post-5103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To confirm, the <a href="http://www.wireshark.org/docs/man-pages/wireshark.html#read">man-page</a> for <code>wireshark</code> suggests that <code>-R</code> is only for reading capture files.</p><blockquote><p><strong>-R {read (display) filter}</strong></p><p>When reading a capture file specified with the -r flag, causes the specified filter (which uses the syntax of display filters, rather than that of capture filters) to be applied to all packets read from the capture file; packets not matching the filter are discarded.</p></blockquote><p><strong>EDIT:</strong> If you're building Wireshark, you might as well add code to allow setting the display filter for live captures. See <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.6/gtk/funnel_stat.c?revision=37984&amp;view=markup#l463">funnel_set_filter</a> and <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.6/gtk/funnel_stat.c?revision=37984&amp;view=markup#l467">funnel_apply_filter</a> for examples of how to set a display filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '11, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jul '11, 09:06</strong> </span></p></div></div><div id="comments-container-5103" class="comments-container"><span id="5105"></span><div id="comment-5105" class="comment"><div id="post-5105-score" class="comment-score"></div><div class="comment-text"><p>yes thanks i understand that, I need to run some repetitive tests and would like a one shell command to run wireshark and then look at the captures. Typing in the display filter every time justs adds nause and the possibility of error.</p></div><div id="comment-5105-info" class="comment-info"><span class="comment-age">(18 Jul '11, 08:06)</span> <span class="comment-user userinfo">spotthemaniac</span></div></div><span id="5108"></span><div id="comment-5108" class="comment"><div id="post-5108-score" class="comment-score"></div><div class="comment-text"><p>You can also save the Display Filters:<br />
Wireshark User's Guide: <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDefineFilterSection.html">6.6. Defining and saving filters</a><br />
<br />
Or you can edit the dfilters file:<br />
C:\Documents and Settings\USER\Application Data\Wireshark<br />
Add your filter to the file.<br />
Make sure you end with an empty line, otherwise you won't see your filter.<br />
</p><pre><code>&quot;No ARP and no DNS&quot; not arp and !(udp.port == 53)
&quot;your filter&quot; your filter</code></pre></div><div id="comment-5108-info" class="comment-info"><span class="comment-age">(18 Jul '11, 10:47)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-5103" class="comment-tools"></div><div class="clear"></div><div id="comment-5103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

