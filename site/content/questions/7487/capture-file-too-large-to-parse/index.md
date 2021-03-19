+++
type = "question"
title = "capture file too large to parse"
description = '''Is there a way to take a already captured file (like 150mb) and turn it into several smaller files that are easier to manage?'''
date = "2011-11-17T08:48:00Z"
lastmod = "2011-11-17T09:23:00Z"
weight = 7487
keywords = [ "parse", "filesize" ]
aliases = [ "/questions/7487" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture file too large to parse](/questions/7487/capture-file-too-large-to-parse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7487-score" class="post-score" title="current number of votes">0</div><span id="post-7487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to take a already captured file (like 150mb) and turn it into several smaller files that are easier to manage?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-parse" rel="tag" title="see questions tagged &#39;parse&#39;">parse</span> <span class="post-tag tag-link-filesize" rel="tag" title="see questions tagged &#39;filesize&#39;">filesize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '11, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/3ed3b96557b3ec59937517f029add00d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gtefft&#39;s gravatar image" /><p><span>gtefft</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gtefft has no accepted answers">0%</span></p></div></div><div id="comments-container-7487" class="comments-container"></div><div id="comment-tools-7487" class="comment-tools"></div><div class="clear"></div><div id="comment-7487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7488"></span>

<div id="answer-container-7488" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7488-score" class="post-score" title="current number of votes">4</div><span id="post-7488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can slice it into smaller files using <strong>editcap -c 100000 &lt;infile.pcap&gt; &lt;outfile.pcap&gt;</strong>, which will slice the infile.pcap in multiple files with 100,000 frames each (or any other number you put in there). editcap is installed together with the wireshark executable.</p><p>As long as you can load the file into Wireshark you might also save partial files using the "save as" option, and use the "Packet Range" pane to set the boundaries, for example a range like "1-100000", followed by "100001-200000", etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '11, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Nov '11, 08:54</strong> </span></p></div></div><div id="comments-container-7488" class="comments-container"><span id="7490"></span><div id="comment-7490" class="comment"><div id="post-7490-score" class="comment-score"></div><div class="comment-text"><p>thanks so much</p></div><div id="comment-7490-info" class="comment-info"><span class="comment-age">(17 Nov '11, 09:23)</span> <span class="comment-user userinfo">gtefft</span></div></div></div><div id="comment-tools-7488" class="comment-tools"></div><div class="clear"></div><div id="comment-7488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

